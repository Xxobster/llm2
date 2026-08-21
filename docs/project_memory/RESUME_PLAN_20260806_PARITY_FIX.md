# Resume plan — CAUS-STRUCT-001 remediation

**Paused:** 2026-08-06 (user reboot). Nothing is mid-flight; no live host was changed.
**Authorised by user:** stop the fleet, then deploy the fix and retrain (option 1A);
next focus is retraining and re-freezing the packs (option 2A).
**Background jobs running at pause:** none. Warehouse rebuild completed
(`ok=48`, the 92 failures are macro/FX symbols with no candles at those timeframes).

Full findings: `LIVE_BT_SIGNAL_PARITY_REPORT_20260806.md`.
Standing decisions: `DECISIONS.md` D-052, D-053, D-054.

---

## State at pause

Done and on disk:

* `indicators/compute.py` — retracement published at the successor leg (CAUS-STRUCT-001),
  regression bound in `packages/indicators/tests/test_structure_causality.py`.
* Research warehouse rebuilt with the causal feature; prefix-invariance 10/10 on
  BTC/ETH/SOL against a full-recompute control.
* `llm2/data/loader.py` — `last` + `last_price` loaded as one gap-free series.
* `llm2/live/multitrade.py` — shared `slot_release_ts_ms`.
* `llm2/live/micro_runner.py` — candle-derived clarity history; retrace zero-fill removed.
* `llm2/experiments/eth_multitrade_nested.py` — exit-aware slots, `size_mult`.
* Leakage registry marked `REMEDIATED_RETRAIN_REQUIRED`.
* Tests: LLM2 394 passed / 1 skipped; indicators 8 passed.

Not done:

* Trading hosts still run the pre-fix indicator and pre-fix runner.
* Fleet is **still live on models trained against the leaked column**.
* Packs not retrained.
* Leakage engine still blind to warehouse-backed builders.

---

## Order of work on resume

### 1. Stop the fleet (authorised, but decide the position handling first)

Stopping a runner does **not** close positions. Exchange-side take-profit and stop
orders survive, but max-hold exits and protection re-attachment stop happening, so an
open book can sit past its intended hold. Decide per unit before issuing the stop:

* flatten open positions reduce-only, then stop the service (clean, realises now), or
* let existing take-profit/stop orders resolve, stop only the entry side.

Hosts: `94.156.189.76` (ln1, units `llm2-structure*`) and `185.203.119.52`
(Xxobster3 / Xxobster9 / Xxobster11).
Read exposure first with `scripts/_vps_fleet_open_orders_audit.py`.

### 2. Deploy the corrected engines

* `C:\projects\botsgeneral\packages\indicators` → `/opt/botsgeneral/packages/indicators`
  on both hosts.
* `llm2/data/loader.py`, `llm2/live/micro_runner.py`, `llm2/live/multitrade.py`,
  `llm2/experiments/eth_multitrade_nested.py`.
* `scripts/_vps_refresh_all_structure_binance.py` (already rewritten: full history,
  units discovered from `/opt`) — replaces the copy that has been failing hourly with
  `structure_history_too_short` because it requested 1,500 bars against a 5,000-bar guard.
* Also bring ln1 up to the fail-closed decide guard (`STRUCTURE_NOT_READY`) and the
  O(n) `build_legs`; both are on 185 only.

Then rebuild every pack slice from full history and confirm
`llm2-structure-refresh.service` is green — it has never once succeeded on ln1.

### 3. Close the leakage blind spot

The engine only re-calls `build_features(ohlcv)`; `structure_v1` reads a pre-computed
warehouse and joins it, so truncation and future-mutation changed nothing and both
hard checks passed trivially. Fixes, in `C:\projects\botsgeneral\packages\leakage`:

1. **Builder-responsiveness probe** — shock the bars a column depends on; if the column
   does not move, the builder is reading a cache. HARD finding
   `EXTERNAL_CACHE_SUSPECTED`, never a silent PASS. This alone would have caught it.
2. **Warehouse-aware guard builder** for `structure_v1` that recomputes the indicator
   into a temp store at each cutoff, as
   `scripts/test_indicator_recompute_prefix_invariance.py` does.
3. Bind as conformance id `CAUS-WAREHOUSE-001`; a missing binding fails the build.

### 4. Retrain and re-freeze (option 2A)

Fresh pre-registration first — hypothesis, candidate space, folds, seed, gates, all
hashed before any out-of-sample is viewed. The corrected feature is materially
different (ETH 2026-08-06 01:00: +0.073 leaked → −0.758 causal), so nothing from the
old search carries over and no prior number may be quoted.

Re-run outer-fold validation from scratch. Quote nothing until
`scripts/audit_live_bt_signal_parity.py` shows Layer A `n_bars_pred_differ = 0` on
forward bars produced after the deploy.

### 5. Only then consider re-enabling live

Historical evidence alone earns at most `SHADOW_READY`. Re-deployment needs fresh
forward shadow reconciliation and a new authorisation.

---

## Quick verification commands

```powershell
cd d:\projects\LLM2
python -m pytest tests/ -q
cd C:\projects\botsgeneral\packages\indicators; python -m pytest tests/ -q

# causality probe (expects "identical at cutoff: N/N" and control "0/N differ")
cd d:\projects\LLM2
python scripts/test_indicator_recompute_prefix_invariance.py ETHUSDT 10

# three-layer live-vs-backtest audit
python scripts/audit_live_bt_signal_parity.py
```
