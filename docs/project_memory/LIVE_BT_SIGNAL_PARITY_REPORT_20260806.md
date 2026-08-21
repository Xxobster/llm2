# Live vs backtest signal parity — full investigation

**Date:** 2026-08-06
**Question asked:** why are live trades and backtest trades not the same, and what makes them the same?
**Maximum earned readiness after this work:** `LIVE_STOP / RESEARCH_ONLY`.
**Evidence class:** PARITY_AUDIT + CAUSALITY_AUDIT. Promotes nothing.
**Principal blocker:** every deployed `structure_v1` model was trained on a
look-ahead feature. The parity defect is fixed in code, but the models are invalid
until retrained, and the fix is not yet on the trading hosts.

---

## 1. Headline

The predictions themselves disagreed, not just the trade selection. Across all seven
live units, the locally recomputed `pred_mean` differed from the live `pred_mean` on
84–100% of decision bars, and the **trade side flipped on roughly half of them**
(BTC single-book: 33 of 46 bars). No gate, cost or execution setting can be blamed
for that: the two sides were scoring different inputs.

One feature caused it. `last_retrace_pct` — the depth of the last Fibonacci
retracement — was **published before it was knowable**. It is therefore both

* a **look-ahead leak in research** (the backtest scored bar T with a number derived
  from prices after T), and
* a **guaranteed live/backtest mismatch** (live could only ever see "not yet known"
  there and substituted zero).

Four further defects, each real but an order of magnitude smaller, are listed in
section 4. All are fixed.

---

## 2. How the cause was isolated

The audit splits divergence into three independent layers so a difference is
attributed rather than guessed (`scripts/audit_live_bt_signal_parity.py`):

| Layer | Question | Method |
|---|---|---|
| A Prediction | do live and research score the same number on the same bar? | replay every ledger decision bar against a local recompute |
| B Gate | given identical predictions, do they select the same trades? | replay the live gate over the live prediction series under four state models |
| C Execution | same size, take-profit, hold? | compare ledger order fields against research signal fields |

Layer A failed first and hardest, so it was chased before anything else.

**Bar-by-bar, ETH k5 unit** (`scripts/_diff_live_local_preds.py`): the last six bars
matched to the last decimal, everything before diverged. That pattern — the present
agrees, the past does not — is the signature of a value that gets rewritten once
later candles arrive.

Two candidate explanations had to be separated:

1. the feature builder is not prefix-invariant (future rewrites the past), or
2. the two sides simply used different amounts of history.

`scripts/test_indicator_recompute_prefix_invariance.py` settles it by recomputing the
indicator at successive cutoffs and comparing each cutoff bar against a **full
recompute produced by the same code from the same candles** (the negative control).
With that control in place exactly one column moved:

```
cutoff (was tip)        live-style    research       diff   rewritten_columns
2026-08-05 14:00:00        0.52004    -0.28776    0.80781   ['last_retrace_pct']
2026-08-05 15:00:00       -0.55151     0.48877   -1.04028   ['last_retrace_pct']
...
identical at cutoff: 6/12
```

A single column swung the direction score by up to **1.04** on a scale of roughly
[-1, 1].

---

## 3. Root cause CAUS-STRUCT-001

In `C:\projects\botsgeneral\packages\indicators`:

* `structure.py::build_legs` computes a leg's `retrace_pct` from `raw[i + 1]` — the
  end of the **next** opposite leg. By construction it cannot be known until that
  next leg confirms.
* `compute.py` then published it with the as-of index built from
  `known_ts[i] = max(confirm(start_swing_i), confirm(end_swing_i))`, i.e. the moment
  the leg **itself** confirms — strictly earlier than the moment its retracement
  becomes measurable.

Consequences:

* **Research/backtest** saw the finished retracement at bar T, using prices from
  after T. Look-ahead.
* **Live** at bar T was always on the newest leg, which has no successor, so the
  value was `NaN`. `micro_runner` then **zero-filled** it. Training had *dropped*
  those rows, so live was feeding the model a value research never scored.

So the two sides were not merely inconsistent — each was wrong in its own direction.

### Fix

`compute.py` now publishes the retracement (and its fib label) at the **successor
leg's** known time:

```python
if len(legs_o) >= 2:
    retr_known = known_ts[1:]
    idx_r = np.searchsorted(retr_known, ts_ms, side="right") - 1
    last_retrace[ok_r] = retr[:-1][idx_r[ok_r]]
```

Bar T now carries the last **completed** retracement, which live and research both
compute identically.

### Verification

`identical at cutoff` after the fix, comparing a truncated live-style recompute
against the full-history research build:

| Symbol | Before | After | Shipped warehouse vs recompute |
|---|---|---|---|
| ETHUSDT | 6/12 | **10/10** | 0/10 differ |
| BTCUSDT | — | **10/10** | 0/10 differ |
| SOLUSDT | — | **10/10** | 0/10 differ |

The chain *shipped warehouse = full recompute = truncated live-style recompute* is
now closed for all three fleet symbols.

Regression: `packages/indicators/tests/test_structure_causality.py` asserts
prefix-invariance over every published column, so this cannot silently return.

---

## 4. Secondary defects, all fixed

### DATA-CANDLE-001 — half of ETH's history was invisible to research

`price_type` is **not** part of the `market_ohlcv` primary key
`(source, symbol, timeframe, ts_ms)`, so `last` and `last_price` are disjoint slices
of one series, split wherever the downloader changed its label. `load_ohlcv` pinned a
single label, which meant research loaded ETHUSDT 1h as **8,844 bars containing one
49,807-bar hole** covering 2020-01 to 2025-09, while the indicator warehouse and the
live bot both used the complete 58,651-bar series.

Fixed in `llm2/data/loader.py`: the last-trade labels are loaded as one series (mark
prices are still never mixed in). Every fleet series is now gap-free:

```
ETHUSDT 1h n=58651 missing_bars=0     BTCUSDT 1h n=60549 missing_bars=0
SOLUSDT 1h n=51631 missing_bars=0
```

### GATE-SLOT-001 — the backtest held book slots that live had already released

The research pre-pass kept a concurrent book occupying a slot until `max_hold`, while
live frees it the moment the exchange reports the take-profit or stop filled. The
backtest therefore skipped `cap_reached` entries that live took. `slot_release_ts_ms`
in `llm2/live/multitrade.py` is now the single shared rule, wired into
`build_multitrade_signals` via `occupancy_bars`.

### GATE-CLARITY-001 — the clarity quantile depended on bot uptime

Live accumulated the `|pred_mean|` histogram in SQLite from process start, so every
restart, redeploy or missed bar produced a different median gate than research, which
seeds from the preceding window. `decide_once` now derives the history from candles
(prior bars with a side that cleared the edge), making it a pure function of data.
The persisted value remains only as a fallback.

### GATE-SIZE-001 — the doubling rule existed only in live

`size_double_within_bars` produced 2× venue-minimum orders live and 1× in the
backtest. `build_multitrade_signals` now emits `size_mult` in `Signal.meta` using the
same window rule.

### Live zero-fill removed

`micro_runner` no longer substitutes zero for a missing retrace. Research drops such
rows, so live must refuse the bar. Post-fix NaN rate on the last 3,000 bars of
BTC/ETH/SOL is **0.00%**, so this is a fail-closed guard, not a throttle.

---

## 5. Operational defects on the trading host (`vps-LIVENET`, ln1)

Found while verifying, not yet changed on the host:

1. **`llm2-structure-refresh.service` has failed on every run.** It calls
   `refresh_symbol(..., limit=1500)`, below the `MIN_STRUCTURE_HISTORY_BARS` guard
   (5,000 on 1h, 2,000 on 4h), so it exits `structure_history_too_short` hourly and
   has never updated a pack slice. The bots' in-process refresh masked it.
2. **The refresh target list had drifted** — the three k5 units were absent entirely.
3. **ln1 is behind on code.** `STRUCTURE_NOT_READY` (fail-closed decide) is absent,
   `llm2/data/loader.py` dates from 2026-08-04, and
   `indicators/structure.py` from 2026-08-03 (missing the O(n) `build_legs`). These
   landed on 185 only.

A corrected `scripts/_vps_refresh_all_structure_binance.py` (full history, units
discovered from `/opt`) is prepared locally but **not deployed** — deployment needs
explicit authorization.

---

## 6. What this means for existing results

Per the stop-before-optimize rule, all of the following are invalidated:

* Every `structure_v1` model in `artifacts/live_packs/` was trained on
  `last_retrace_pct` in its leaked form. Their scores are not evidence of edge.
* Every backtest, hunt, walk-forward and live-vs-backtest chart produced before
  today used the leaked column and the gap-holed ETH series.
* Inherited readiness for all affected packs is void. `last_retrace_pct`,
  `last_retrace_pct_4h` and `last_retrace_pct_1w` are recorded in
  `artifacts/sqlite/leakage_registry.json` as `REMEDIATED_RETRAIN_REQUIRED`.

The corrected feature is materially different: on ETH 2026-08-06 01:00 the score
moves from +0.073 (leaked) to −0.758 (causal). Running the existing models against
the corrected feature is out-of-distribution and must not be treated as a strategy.

## 7. Required order of work

1. Deploy the fixed `indicators` package to both trading hosts, plus the repaired
   refresh script and unit list. *(needs authorization)*
2. Rebuild every pack slice from full history and confirm the hourly timer is green.
3. Retrain and re-freeze the packs on the corrected feature set, under a fresh
   pre-registration.
4. Re-run outer-fold validation from scratch; quote no prior number.
5. Re-run `scripts/audit_live_bt_signal_parity.py` on forward bars only and require
   Layer A `n_bars_pred_differ = 0` before any readiness claim.

## 8. Files changed

| File | Change |
|---|---|
| `botsgeneral/packages/indicators/src/indicators/compute.py` | CAUS-STRUCT-001 causal retrace publication |
| `botsgeneral/packages/indicators/tests/test_structure_causality.py` | new prefix-invariance regression |
| `llm2/data/loader.py` | last-trade labels loaded as one gap-free series |
| `llm2/live/multitrade.py` | shared `slot_release_ts_ms` |
| `llm2/live/micro_runner.py` | candle-derived clarity history; zero-fill removed |
| `llm2/experiments/eth_multitrade_nested.py` | exit-aware slots, `size_mult` |
| `llm2/diagnostics/structurebreak.py` | `merge_asof` dtype normalisation (pre-existing failure) |
| `scripts/audit_live_bt_signal_parity.py` | new three-layer parity audit |
| `scripts/test_indicator_recompute_prefix_invariance.py` | new causality probe with control |
| `scripts/rebuild_structure_warehouse_causal.py` | warehouse rebuild |
| `scripts/register_structure_retrace_leak.py` | leakage registry entry |
| `scripts/_vps_refresh_all_structure_binance.py` | full-history refresh, unit discovery (undeployed) |
| `tests/test_live_bt_signal_parity_guards.py` | new guards for the four gate/data defects |
| `tests/test_ohlcv_price_type_resolve.py` | updated to union semantics |
| `tests/test_structure_refresh_history.py` | de-pinned assertion built on leaked numbers |

Test state: LLM2 394 passed / 1 skipped; indicators 8 passed.
