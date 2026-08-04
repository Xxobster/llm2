# LLM2 Current State

Updated: 2026-08-04

## Status

`LIVE_STOP / RESEARCH_ONLY` for scale. Micro-live: Xxobster7 single-book fleet
(BTC/ETH/SOL) + Xxobster8 ETH **multitrade v1** (certificates expire 2026-08-17).

## ABC family (2026-08-03) — D-030 / D-031

**Continuation (“A≈C” / equal-leg / 0.618 / 1.618 continues):** CLOSED on BTCUSDT 1h/4h
unless a separate lockbox prereg says otherwise. Train report:
`artifacts/reports/abc_factor/abc_factor_BTCUSDT_20260803T124220Z.md`.

**Bounce against BC:** family status **UNDERPOWERED_HOLD**
(`artifacts/reports/abc_bounce/abc_bounce_001_family_status.json`). First lockbox open:
`abc_bounce_BTCUSDT_20260803T130016Z` — 46 trades (<50); bounce PF 0.54 vs control 0.59.
Second one-shot refused until the same parameter digest projects ≥50 sequential trades.
Do not widen tolerance. Decision **D-031**.

**Causal-wave extrema arm:** `abc_wave_extrema_BTCUSDT_20260803T125911Z` — **0** FDR
survivors on 1h/4h train. Labels `abc_wave|*`; diagnostic only.

**Policy enforced:** continuation CLOSED; refuse wavetheory BT (D-026); warehouse legs
required; lockbox opens need frozen exits + matched control; video extractions are not
evidence (`ABC_RULES_TESTED.md`). Hunt continues **outside** ABC (`structure_v1`, TE falsify).

**Transfer-entropy falsify (outside ABC):** `te_falsify_BTCUSDT_1h.json` — 0/31 pairs
survive all three controls; nonlinear cross-asset direction not promoted.

**structure_v1 — fold V2 settled + micro-live on ln1 (user-authorized 2026-08-03):**
- Settle: **SHADOW_READY_CANDIDATE**, pooled Profit Factor ≈ **1.865**, tier 3; PBO UNAVAILABLE.
- Frozen pack: `artifacts/live_packs/structure_v1_lgbm` (model + 35 Bybit risk tiers + feature slice).
- Certificate: `AUTHORIZED` → `94.156.189.76` / `Xxobster7`, expires 2026-08-17 (MICRO only).
- VPS live fleet on Xxobster7 (user-authorized 2026-08-04), three **separate** services:
  - `llm2-structure-micro` BTCUSDT 1h fwd_return
  - `llm2-structure-eth` ETHUSDT 1h direction
  - `llm2-structure-sol` SOLUSDT 1h direction
  Each: MIN_EXCHANGE, SL-derived **18×**, hedge mode, max one book per symbol.
- **ETH multitrade on Xxobster8 (user-authorized 2026-08-04):** distinct from
  single-book ETH. **Active:** `eth_multitrade_v1_1` — mean_strength, fib_ext=1.618
  (book3+ TP 2.618%), hold_addon=12, **K=7**/side. Service
  `llm2-structure-eth-multitrade-v1_1`. Prior `eth_multitrade_v1` (K=6) pack+unit
  retained stopped for rollback. Map: `artifacts/live_packs/VERSIONS.md`. MICRO only.
- Live leverage is SL-derived with security margin (D-001): `floor(1/(sl+0.5%+0.2%))*0.5`
  → **18×** for SL 2% (ceiling 37). Runner calls Bybit `set-leverage` + hedge mode on LIVE
  start and before every entry; pack leverage mismatch fails closed.
- Direction packs use gate ±0.10 (research parity), not the fee hurdle.
- Structure / signal candles: **Binance USD-M** (research parity) → pack slice; orders /
  mark / TP-SL remain **Bybit**. Env `LLM2_STRUCTURE_SOURCE=binance`. Collector discovers
  Binance 1h/4h/1w for BTC/ETH/SOL; on-decide + `:55` refresh recompute structure from
  Binance shared candles (REST fallback).
- ETH/SOL full-gate settles (fold V2): all 4 combos **overall PASS**, tier 3;
  report `artifacts/reports/structure_v1_eth_sol_settle_20260803T161346Z.json`.
  **Quotable promotion proxies (stitched outer OOS):** ETH 1h direction pooled PF ≈
  **1.768**, SOL 1h direction ≈ **1.858**, ETH fwd_return ≈ **1.733**, SOL fwd_return ≈
  **1.471**. PBO UNAVAILABLE.
- **Lockbox opened / contaminated (D-035):** May-2026→≈2026-08-02 Finplot on frozen
  ETH/SOL direction packs — `structure_v1_lockbox_eth_sol.json`. Lockbox PF≈2.5 is
  **not** a promotion gate. Do not retune on that window.
- LINK/VET/ADA direction lockbox Finplot opened (contaminated): structure_v1_lockbox_link_vet_ada.json; metrics canvas + structure_v1_link_vet_ada_metrics.json. Quote settle PF not lockbox.
- **ETH concurrent fib v2_ext (corrected TP + unlimited K, 2026-08-04):** book 3+ TP =
  `usual_TP + fib*(usual_TP−entry)` → offsets 1.233%…**2.618%** (fib≤1.618), not +23–62%.
  258 arms incl. K unlimited. Best PnL `none|fib1.618|hold18|unlimited` ≈179 USDT PF≈2.58
  peak concurrent 18. Best PF among heavy arms `none|fib0.377|hold18|unlimited` PF≈2.95.
  Report `structure_v1_eth_concurrent_fib_ext_latest.json`. Lockbox contaminated.
- **ETH concurrent hedge×3 reproducibility (2026-08-04):** screenshots PF≈2.44 are
  mechanically identical on re-sim; stitched outer-OOS hedge×3 PF≈**2.21** (6/6 positive
  folds, bootstrap pos-exp 100%). Official single-book settle remains PF≈**1.77**.
  Lockbox still contaminated (+0.22 PF optimism). Report
  `structure_v1_eth_concurrent_reproducibility.json`. Concurrency not live-authorized.
- **Touch TF:** 1h decisions now resolve same-bar order on **1m** (was 5m). Cause of prior
  “317 incomplete touch coverage” warning: 5m warehouse for expansion symbols stalled at
  ~2026-07-16 while 1h/1m continued. `load_ohlcv` also picks the densest of `last`/
  `last_price`. Re-sim lockbox with 1m → ~0–1 incomplete bars (trailing forming hour trimmed).
- Expansion settle (fold V2, research-only): report
  `structure_v1_expansion_settle_20260803T181235Z.json` — **13/13 overall PASS**, tier 3.
  Quotable pooled Profit Factors (outer OOS, not lockbox): VET direction ≈ **1.921**,
  XRP direction ≈ **1.711**, BNB direction ≈ **1.567**, LINK direction ≈ **1.953** (best),
  ADA ≈1.915, DOT ≈1.840, AVAX ≈1.799, XLM ≈1.691, DOGE ≈1.606, TRX ≈1.538;
  VET fwd ≈1.689, BNB fwd ≈1.650, XRP fwd ≈1.313. PBO UNAVAILABLE. Min-exchange equity
  caveat applies. Leakage recheck 26/26 PASS
  (`structure_v1_leakage_recheck_20260803T175941Z.json`). Proxy hunt
  `structure_v1_expansion_hunt_20260803T181203Z.json` is screen-only. `load_ohlcv` pins
  single `price_type` (`last_price` preferred). **No new VPS deploy** without pack +
  certificate + explicit auth per symbol.
- Smooth min-size equity is **not** a tradable edge. Scale not authorized. ABC bounce HOLD.

## WAVE001 mining (in progress)

Registered candidate space: `configs/preregister/wave001_candidate_space.yaml`.
Families: amplitude events, structure-break (B/C), wave panel, causal metrics/triggers,
shape k-NN motifs. Stage-1 only — contaminates the training window; no trading claim.

**Correctness fixes landed:** fold-fitted period API (`fit_period_in_window`);
`analytic_wave` hard-blocked from mining modules; lead null is now max-over-lags
(`circular_shift_max_lag_null`, D-027). Prior lead p-values are INVALIDATED.

**Warehouse leakage audit:** 8 PASS, 0 FAIL, 1 BLOCKER (`cryptodb/market.sqlite` timing
semantics — D-028). `market_ohlcv`, `indicators` (confirmation-time re-verified; swing
kind=`high`/`low`), `binance_funding`, and shared leakage on `build_causal_metrics` are
clean.

**wavetheory private backtest:** VOID (D-026). Rebuild only via confirmed-swing warehouse
+ tradesim.

**Authoritative stage-1 scan (post D-027, expanded external panel):**
`artifacts/reports/wave001/wave001_BTCUSDT_1h_20260803T121754Z.md` — **6/614** survive
q≤0.05 across 27 external panel members (lab crypto + 1h price-like macros + funding).
Same-series Tier B / own volume excluded from the lead panel (D-029). Survivors are
**magnitude** arms and benchmarks (`trailing_move_control`, `atr_surge_*`,
`amp_surge_95|magnitude`) plus one wrong-sign structure break
(`retest_down|coil` → negative forward return). Amplitude does **not** beat the
trailing-move control. Wave-panel leads and shape k-NN: **zero** FDR survivors under
`null=max_over_lags`. **Stage 2 through tradesim is not warranted.**

`cryptodb` excluded (D-028). Prior single-lag panel leads remain INVALIDATED.

**Non-directional go/no-go:** **WITHDRAWN.** The prior NO-GO was produced by a Stage-B
gate that could not return True for any input (D-013). The question is unanswered, not
answered negatively.

**Prior research record:** all 148 generations / 603 trials predating 2026-08-03 are
**GATE_VOID** and are not quotable as evidence in either direction.

**Vol-as-filter:** methodology results only, not strategy candidates. Those numbers came
from the proxy and tradesim paths rather than the Stage-B gate, so they stand as written,
but they were never edge candidates.

**Engine conformance:** GREEN. tradesim 1.0.0, fixture pack `9a037b290c8a`, registry digest
`f9e9c06aa562`, 62 of 62 required identifiers satisfied, none unsatisfied. The earlier
VALD-002 / VALD-005 blocker is cleared. One caveat: `engine_commit` reports
`UNKNOWN_DIRTY`, so the stamp pins a fixture hash but not a botsgeneral commit.

## Closed 2026-08-03

Three questions answered, all negative, all with the control arm that makes the answer
mean something.

**Pulse continuation — CLOSED (D-021).** The only diagnostic survivor with an effect size
above the round trip. Pooled profit factor 1.067 against a 1.20 gate, two of five folds
negative. The volatility-matched random-entry control returned 1.049, so the pulse
contributed 0.018 of profit factor: the 87 bps was the return to being long BTCUSDT for four
days in a volatile regime. Funding, charged at actual settlements, cost 4.59 against 5.06 in
fees and moved profit factor from 1.118 to 1.067.

**Cross-asset wave lead — ARTEFACT, then negative (D-020).** "ETHUSDT leads BTCUSDT by 4
bars, r = 0.48, 24 of 24 surviving FDR" was entirely band-pass group delay; a BTCUSDT series
was shown leading *itself* by 4 bars. Through one common filter, 24 of 26 pairs place their
maximum at lag 0. The markets co-move; none leads.

**Dollar/commodity complex — CLOSED (D-019).** One factor explains 46 percent of the
13-series block, so the separate tests were mostly redundancy. Collapsed and asked once: -0.009
correlation with BTCUSDT forward return at 1h, +0.010 at 4h, R-squared 0.009 percent. No more
external series.

## Market strength as a wave — answered

Yes, weakly, and only in the form you cannot trade. BTCUSDT 1h carries a 15.3-bar spectral
peak at 1.69x an AR(1) null (p = 0.005), which is significant but shallow.

The number that settles it is **0.58**: the correlation between the zero-phase wave and the
one-sided wave computed without future data. Two thirds of the variance of the pretty wave
is hindsight. `llm2/diagnostics/wave.py` therefore returns both and never mixes them; the
chart at `artifacts/reports/diagnostics/wave_BTCUSDT_1h.png` draws them together so the gap
is visible — the non-causal wave turns at the exact high and low, the causal one turns late.

Across 28 series the fitted period ranges from 2.0 to 19.7 bars with peaks of 1.2x to 2.3x.
Highly correlated crypto assets pick unrelated periods (BTCUSDT 15.3, ETHUSDT 7.1, SOLUSDT
2.7), which is itself evidence the peaks are noise rather than a shared market rhythm: a
genuine cycle would be shared by assets that co-move at 0.84.

Command: `python -m llm2.cli wave --symbols ... --plot`.

## Blocker resolved 2026-08-03

`audit_predictability` probed with a constant predictor scoring exactly 0 against a
`> 1e-6` pass threshold, and graded it in-sample. It capped every trial at tier 0 and
blocked every tradesim escalation in the 108-combo and 162-combo sweeps. Replaced with a
permutation test over real learners with a chronological split and out-of-sample scoring;
draw counts derived from alpha; underpowered configurations report `underpowered` rather
than a false negative. Release gate `require_predictability_gate_discriminates` fails the
build if known signal does not pass or pure noise does pass.

## Market-structure warehouse integrated 2026-08-03 (`indicators.sqlite`)

`D:\projectsdata\indicators\indicators.sqlite` — 179 series at 15m/1h/4h/1w, confirmed
swings, HH/HL/LH/LL labels, impulse/correction legs, Fibonacci retracement and extension
grids, distance to prior confirmed support and resistance. Single parameterisation
`swing_left=2, swing_right=2`. 38 symbols carry 1h and 4h structure.

**Causality: PASS, verified not assumed.** Swing structure is the highest-risk indicator
family for look-ahead, because a pivot only becomes a pivot once `swing_right` further bars
print. This warehouse stores `pivot_ts_ms` separately from `confirm_ts_ms` and `bar_features`
cites only already-confirmed structure. Measured over 60,466 BTCUSDT 1h bars: 0 swing highs
cited before confirmation, 0 swing lows, 0 support/resistance levels, 0 crossed
support/resistance pairs, 0 Fibonacci anchors that are not real confirmed swing prices,
0 structure labels disagreeing with the last event at or before the bar. Bound in
`tests/test_structure_causality.py` for BTCUSDT 1h/4h and ETHUSDT 1h.

`ts_ms` is bar **open**, same convention as `market_ohlcv`; the row describes state at that
bar's close and is knowable at `ts_ms + tf`. Same-timeframe use needs no shift;
cross-timeframe use goes through completion-aware alignment.

**Third look-ahead defect, found and fixed in this work:** `TF_MS` had no `1w` entry, and
`align_multi_timeframe` fell back to one hour. That declared a weekly bar complete one hour
after it opened, exposing 6 days 23 hours of the future in every weekly context column — and
the shared leakage audit still reported PASS, for the same reason it could not catch
`macro_v1`: truncating the bar frame does not truncate the database. `TF_MS["1w"]` added and
the silent fallback replaced with a hard `KeyError`; a guessing default in a completion-time
lookup is a leak generator. Bound in `test_every_warehouse_timeframe_has_a_known_bar_length`
and two alignment tests.

**`structure_bias` is unusable and is not used.** It reads +1 on 93.7% of BTCUSDT 1h bars,
98.1% of ETHUSDT, 99.2% of XAUUSD. A confluence table built on it puts nearly everything in
one cell — the first run populated 2 of 8 states, one holding 98% of the data. The Dow
reading of the label (HH/HL up, LH/LL down) splits within a point of 50/50 on every series
checked and is used instead, as `struct_dir`. Bound in
`test_label_derived_direction_is_balanced_where_structure_bias_is_not`.

New: `llm2/data/indicators.py` (causal reader), `llm2/features/structure_v1.py` (48 columns,
scale-free only, leakage audit PASS), `llm2/diagnostics/marketstructure.py`.

### Structure diagnostics result: comprehensively negative

BTCUSDT 1h (620 tests, 28 survivors) and 4h (601 tests, 16 survivors). Of the four structure
families, **0 of 70 effects survive FDR at either timeframe**.

- **Structure labels do not predict direction** (0/24). Higher high over 24 bars: −6.8 bps
  excess, p = 0.36. Lower high: +6.0 bps. Point estimates are marginally the *wrong* way for
  the folk claim, and neither is distinguishable from zero.
- **Fibonacci ratios carry nothing beyond an arbitrary fraction of the same range** (0/22).
  Each real ratio was paired with non-Fibonacci placebos (0.150, 0.310, 0.440, 0.550, 0.690,
  0.870) drawn from the same confirmed anchors, same bars, same volatility-scaled proximity
  band. Mean |excess|, 1h/24-bar: Fibonacci 2.89 bps, placebo 3.76 bps — the placebo arm is
  *larger*. Separation (real − placebo): −0.12 and −0.88 bps at 1h, +0.002 and +0.16 bps at
  4h. At 4h the largest placebo effect (14.8 bps) exceeds the largest Fibonacci one (11.1).
- **Confirmed support and resistance do not produce bounces** (0/8). Near support, 24 bars:
  −2.0 bps, wrong sign for the claim, p = 0.70.
- **Cross-asset structural confluence is absent** (0/16 at each timeframe, all 16 joint
  states populated after the `struct_dir` fix). The user's literal case,
  `BTCUSDT+ | DXY− | XAUUSD+ | ETHUSDT+`, is −18.4 bps over 24 bars, p = 0.067, q = 0.744 —
  and negative, i.e. the opposite of the folk claim, before any cost.

The structure warehouse is now available to the hunt as `structure_v1`; what is closed is
the descriptive claim that these objects predict direction on their own.

## Second leakage defect found and fixed 2026-08-03: `macro_v1` look-ahead

`market_ohlcv.ts_ms` is bar **open** time, so a bar stamped `T` on timeframe `tf` is only
knowable at `T + tf`. `macro_v1` did `reindex(decision_index, method="ffill").shift(1)` on
daily macro series, which assigned a daily bar's **close** to every hour of that same day.
Measured directly: at 01:00 UTC on 2024-06-05 the feature carried DXY = 104.241, the close
of the whole of 2024-06-05 — 23 hours of look-ahead, on all six macro symbols, on every
intraday timeframe.

The shared `leakage` prefix-invariance guard cannot catch this. It truncates the crypto
OHLCV handed to the builder, but the macro series is loaded from the database *inside* the
builder, so truncation never reaches it. Bound instead to a direct integration test in
`tests/test_macro_causality.py`.

Replaced by `llm2/data/macro.py`: every series indexed by its completion instant plus an
explicit per-source publication lag, as-of joined rather than forward-filled, with an
`age_sec` column so staleness is visible rather than implicit. Vendor is pinned per symbol
(`EURUSD`, `XAUUSD`, `WTI` and others exist under two sources and were previously selected
without one). `is_complete` is recomputed rather than trusted: the current day's daily bar
is flagged complete while still in progress.

Warehouse coverage went from 20 series to 31 registered externals plus funding.
`binance_funding.sqlite` is now wired in (7,527 BTCUSDT settlements from 2019-09-10,
14.5% negative), carried as a stationary level rather than a differenced price.

## Diagnostics pass 1: BTCUSDT 1h and 4h (2026-08-03)

Runs `diag_BTCUSDT_1h_20260803T083613Z` (58,231 bars) and
`diag_BTCUSDT_4h_20260803T083839Z` (14,557 bars). Training window only, ends 2026-05-01.
Every family is false-discovery-rate corrected; cross-asset nulls are circular-shift, which
preserves each series' own persistence while destroying alignment.

| Family | 1h tests | 1h survive | 4h survive | Reading |
| --- | ---: | ---: | ---: | --- |
| lead_lag (cross-asset, tradeable) | 228 | **0** | 0 | No external series linearly leads BTC |
| contemporaneous (context only) | 76 | 0 | 0 | Max \|r\| 0.26 (AUDUSD), not tradeable |
| transfer_entropy | 19 | 11 | **0** | Tiny and does not appear at 4h — see below |
| seasonality | 45 | **0** | 0 | No session, hour, weekday or funding-hour effect |
| confluence (DXY × XAUUSD states) | 4 | 0 | 0 | Joint trend states carry nothing |
| pre_event displacement | 19 | **0** | 0 | Nothing moves before a BTC pulse |
| post_pulse | 6 | 3 | 0 | Up-pulse continuation, see below |
| volatility_clustering | 8 | 6 | 6 | Overwhelming, as expected |
| autocorrelation | 54 | 15 | 8 | Real but \|r\| ≤ 0.029 |
| cycles | 6 | 1 | 1 | Weak spectral peak, 15.3 bars at 1h |
| regime | 10 | 3 | — | Momentum sign flips across regimes |

**The cross-asset question is answered negatively for linear lead-lag.** Zero of 228
tradeable lead-lag pairings survive at either timeframe, across 31 external series, four
predictor windows and three horizons. The strongest was XAGUSD 24-bar → 24-bar at r = −0.046
(raw p = 0.0014, q = 0.155). Contemporaneous correlations reach 0.26 and are worthless.

**Transfer entropy at 1h is not 11 discoveries.** The 11 survivors are the dollar,
metals and energy complex with an effective independent count of 5.09 out of 10 (WTI/BRENT
correlate 0.91, XAUUSD/XAGUSD 0.70, EURUSD/USDCHF −0.67). Effect size is ~0.0025 nats
against a target entropy of ln(4) = 1.386, i.e. **0.18% of the target's uncertainty**. A
time-of-day confound was tested and rejected (clock controls p = 0.72 and 0.28; pure noise
p = 0.74), so the effect appears real but is far below any cost hurdle and absent at 4h.

**Seasonality is a clean negative.** The London/New York/Tokyo session question is answered:
nothing survives. Strongest was hour 16 UTC at q = 0.058.

**The "market strength as a wave" question has a weak yes.** The global spectral peak beats
an AR(1)-matched null at both timeframes (1h q = 0.005, peak 15.3 bars; 4h q = 0.015, peak
13.1 bars ≈ 2.2 days), but the peak is only 1.7× the null level.

Two hypotheses preregistered: `diag001_pulse_continuation` (up-pulse continuation,
+87 bps over 96 bars, q = 0.0004, but only 185 events and absent at 4h) and
`diag002_regime_conditional_momentum` (sign flip, +0.043 in low volatility versus −0.046 in
a downtrend, both at q = 0.038). Both carry an explicit note that the training window is now
contaminated for them.

## Standing policy (locked)

| Rule | Enforcement |
| --- | --- |
| Vol-filter percentile frozen at 75 | `FROZEN_VOL_FILTER_PERCENTILE`; `validate_vol_filter_prereg` |
| Do not hunt other percentiles after OOS | `volfilter_001` / `_002` status `FROZEN` |
| Magnitude never emits trade side | `predictions_to_signals(..., target_family="magnitude")` raises |
| High vol → skip-more, never leverage-more | prereg `action_forbidden` |
| Beats control but PF&lt;1 | methodology win, not deployable edge |
| Readiness | `RESEARCH_ONLY` only |
| ABC continuation (A≈C / 0.618 / 1.618) | CLOSED on BTCUSDT 1h/4h unless lockbox prereg |
| abc_bounce_family | UNDERPOWERED_HOLD — no retune; reopen only at ≥50 projected trades |
| Lockbox open | `require_lockbox_prereg_frozen` (exits + matched control) |
| ABC geometry | warehouse `indicators.legs` / `structure_v1` only; no wavetheory private BT |
| Video ABC rules | inventory in `ABC_RULES_TESTED.md` only — not evidence |
| V2.1 stress/MDD/margin | bound in hunt tradesim path (`llm2/gates/evidence.py`) |
| PBO | fold-aligned matrix only; unavailable ≠ PASS; truncated stitches refused |
| Proxy Tier ≥ 2 | screen signal only — full-gate settle required before readiness |

## Vol-filter evidence (BTCUSDT 1h)

| Gen | Entry rule | Proxy filtered PF | Proxy control PF | Verdict |
| --- | --- | --- | --- | --- |
| volfilter_001 | momentum_24 | 0.914 | 0.864 | filter beats control; both lose; tradesim same story (~0.89 vs ~0.82) |
| volfilter_002 | meanrev_24 | 0.755 | 0.825 | filter **fails** vs control; no tradesim |

Interpretation: the same skip helps momentum and hurts mean-reversion → usefulness
is **entry-rule-specific**, not a universal noise gate. Do not expand the filter
grid; further work needs a new preregistered entry hypothesis, not a new percentile.

## Conformance

`tradesim @ 3e7eb30 | 62/62 GREEN` when tree clean.

## Tests

Policy + invariant suite green (`test_vol_filter_policy`, constant-predictor gate).
