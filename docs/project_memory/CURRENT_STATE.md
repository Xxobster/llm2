# LLM2 Current State

Updated: 2026-08-21

## 2026-08-21 — ln1 live-vs-BT re-check (no new fills)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. **Promoted: none.**

live-network-1 units left running (`active`, collector `active`, 1-minute rows still 0). Overnight: Solana +20 / Ether +19 decides, all `FLAT`. No new ENTER, no `pivot_fills`. Audit `price_type=last` only. 15-minute Virtual Private Server vs warehouse match_rate 1.0 through 2026-08-21 02:45 UTC. live-network-2 four pivot units also flat, zero fills. Did not retune the pack. Did not loosen live-data-001. Report: `artifacts/reports/audit_llm2_pivot_live_vs_bt_latest.md`.

## 2026-08-20 — ln1 pivot fill ledger + live-vs-BT re-audit

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. **Promoted: none.**

User authorized live-network-1 restart of `llm2-pivot-sol-geo-p75-w4` and `llm2-pivot-eth-p75-ctrl-atr-w4` only. Deployed `pivot_fills` + 2-second fill poll (`FILL_POLL_SEC=2`). Start `2026-08-20T21:04:07Z`, both `active`, `NRestarts=0`. No take-profit / stop / work / hold retune. live-data-001 left fail-closed.

Collector still has **zero** 1-minute rows. Research 1-minute Last+Mark is local warehouse only (`source=binance` / `binance_mark`). After three 15-minute closes (21:15 / 21:30 / 21:45 UTC) both arms `FLAT` / `below_thr` with `LIVE-DATA-001=PASS`. Re-audit: `artifacts/reports/audit_llm2_pivot_live_vs_bt_latest.md`.

## 2026-08-21 — ETH+SOL 15m 0.5%/0.5% pivot LIVE on ln2 / Xxobster9

**Authorization:** user named host `212.73.150.178` and account `Xxobster9`, exits 0.5%/0.5%.

New units `llm2-pivot-eth-p50-tp05-sl05` and `llm2-pivot-sol-p50-tp05-sl05` (do not overwrite Xxobster8 1%/1%). Same parent models/gates; `tp_pct=sl_pct=0.005`; leverage from stop = 41x. Certificates: `configs/live/pivot_*_p50_tp05_sl05_w4_xxobster9_ln2_certificate.yaml` (expire 2026-09-04). **Research readiness remains `LIVE_STOP / RESEARCH_ONLY`** (~80% same-15-minute exits); this is operational authorization only. Xxobster8 1%/1% units on the same host were left running.

## 2026-08-21 — ETH+SOL 15m 1%/1% pivot LIVE on ln2 / Xxobster8

**Authorization:** user named host `212.73.150.178` and account `Xxobster8`.

Units `llm2-pivot-eth-p75-ctrl-atr-w4` and `llm2-pivot-sol-geo-p75-w4` are **active** (`NRestarts=0`), `--live-orders`, same frozen packs as Xxobster7. First decides: both `FLAT` / `below_thr` with `LIVE-DATA-001=PASS`. Collector on ln2 now also fetches Binance ETH/SOL 15m (3000 bars). Certificates: `configs/live/pivot_*_xxobster8_ln2_certificate.yaml` (expire 2026-09-04). Xxobster7 / 94.156.189.76 units were not changed.

## 2026-08-19 — Autonomous confluence hunt 002 (done)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. **Promoted: none.** Not live.

Preregister: `configs/preregister/confluence_autonomous_hunt_002.yaml`  
Full table: `artifacts/reports/confluence/autonomous_hunt_002_latest.md`  
Diagnostic flags only: `artifacts/reports/confluence/autonomous_hunt_002_survivors.md`

Watchdog clean exit 0 after **1,092 / 1,092** arms (722 RAN, 370 too few). Rank window: chronological test before lockbox. Do not retune on this peek.

0.5%/0.5% brackets stay invalid (entry-bar exit ~80%) **after 1-minute touch resolution** (100% of those exits were `resolved_by_touch`, ambiguous rate 0). The stop is inside the 15-minute candle, not an Open-High-Low-Close guess. Hunt 002 already used 1-minute touch for ETH/BTC 15m and all 1h; SOL 15m had been 5-minute — now `touch_timeframe` maps 15m/1h/4h → 1m. SOL 1%/1% control unchanged on 1-minute re-score (PF 1.67, entry-bar 32%). Honest 15m 1%/1% controls: ETH PF 1.55 n=384; SOL PF 1.67 n=385; BTC PF 1.02 n=28 (thin). 67 arms beat the same-bracket control at n>=50 and entry-bar <=35%; many of those beat a *losing* 2%/1% book. Stronger-looking flags (still not promote): ETH RSI-cross-up filter 1.5%/1%; SOL failed-swing-low filter 1%/1%; SOL pulse-extend filter 2%/1%; BTC structure-break standalone. No outer settle. Do not add events.

## 2026-08-19 — Confluence future-event pack 001 (research)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Not live. **Promoted: none.**

Preregister: `configs/preregister/confluence_event_pack_001.yaml`  
Oracle diagnostic: `artifacts/reports/confluence/event_importance_001_latest.json`  
Predicted heads: `artifacts/reports/confluence/event_pack_train_001_latest.json`

Hypothesis: predict a closed pack of *future events* (RSI cross, MACD histogram flip, failed swing, …), not reconstructed indicator levels. Leakage on known-now features: PASS (ETH/SOL/BTC).

Phase 2 oracle (true future bit AND current pivot control — **never a live edge**):
- Reversal events beat continuation on this list. Pulse-extend / structure-break-hold were too sparse to AND with the control.
- SOL `atr_clip_w5`: **no survivors**.
- ETH `q50_w4` / BTC `p80_w4`: several reversal events cleared inner intent-expectancy + FDR + entry-bar ≤35%. Those Profit Factors are oracle peeks.

Phase 3 predicted `P(event)` heads, same-side AND at π*≈0.5375, test window only:
- ETH long-pack AND control: 12 trades, PF 1.83 vs control-test PF 1.55 — **too few trades, no promote**.
- ETH short-pack and both BTC packs: **TOO_FEW**.
- Strict AND of several heads is too sparse once the oracle bit is replaced by a model.

Do not add more indicators. Next bounded step (if any): one-head predicted filter on the existing control (not a full AND pack), still RESEARCH_ONLY.

## 2026-08-19 — Pivot live max_hold=6 + ETH tip identity

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`.

- Live `pivot_runner` now market-flattens at pack `max_hold_bars=6` (same deadline as tradesim: fill-bar open + 6 × 15m). Deployed and restarted `llm2-pivot-sol-geo-p75-w4` and `llm2-pivot-eth-p75-ctrl-atr-w4` on `94.156.189.76` (`pivot_runner start` 2026-08-19T03:23:16Z, both active).
- Decide payloads now persist `feature_snapshot` + `n_prefix_bars` for Layer A replay.
- ETH “2 flips” (15 Aug 08:30 / 12:45) were a **local comparison artifact** (thin ETH CSV). On the VPS pack + 3000-bar prefix + live `tip_ohlc`: **2/2 and 8/8 ENTER bound identity**.
- Other live hosts already flatten on max hold: `tsm_chandelier` (36 × 1h), `tsm_vpa` (pack 20), `xgb` (`step_maybe_time_exit`). Structure `micro_runner` already had it; those units stay `LIVE_STOP`.
- Isolated “hold longer than 6 on the frozen TP1/SL1 arms” was **not** a completed hunt. Closest stack test (work+hold 4/6/8/10 on TP2/SL1) got worse as hold grew. Live was wired to the **frozen pack** value 6, not a new hold search.

## 2026-08-14 — LIVE-DATA-001 tip freshness + DATA_UNSAFE

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Code landed; VPS collector/bot restart **not** done in this step (needs explicit deploy auth).

- Shared gate: `live_candles.freshness` (`LIVE-DATA-001`) — Binance server time vs local last closed tip; codes PASS / CANDLE_STALE / CANDLE_AHEAD / CLOCK_SKEW / CANDLE_MISSING / COLLECTOR_ERROR.
- Shared flag: `meta` key `data_unsafe:{exchange}:{symbol}:{timeframe}` in `shared_candles.db` (+ fleet `binance:COLLECTOR:1m`).
- Collector (`botsgeneral.collect`): on tip-poll / per-pair failure writes DATA_UNSAFE; successful poll clears COLLECTOR flag and re-checks tip.
- Pivot runner + micro runner: refuse **new entries** when unsafe; cancel resting entry LIMIT; **keep** protective TP/SL.
- Probe: `python scripts/ops_live_data_001_probe.py --demo-cases` (also live `--symbol …`).
- Tests: `live_candles/tests/test_live_data_001.py`, `tests/test_live_data_001.py` (6 passed).

## 2026-08-15 — LIVE-DATA-001 deployed on Xxobster7

**Authorization:** user explicitly authorized VPS sync/restart/verification.

- Deployed `live_candles.freshness`, collector, pivot runner, micro runner and
  `botsgeneral` sitrep to `94.156.189.76`; restarted collector first, then
  `llm2-pivot-sol-geo-p75-w4` and `llm2-pivot-eth-p75-ctrl-atr-w4`.
- First probe exposed stale 15m data because the collector blocked in an
  unlimited thin-history 1m bootstrap. Fixed collector policy: continuous
  collector refreshes closed tips and defers full-history backfill to a finite
  watchdog-supervised job. This is a safety fix, not a strategy change.
- Post-fix probes: ETHUSDT and SOLUSDT 15m `LIVE-DATA-001=PASS`; clock skew
  ~133–158ms; no `DATA_UNSAFE` flags; both pivot units and collector active,
  `NRestarts=0`.
- `botsgeneral sitrep` now prints `LIVE-DATA-001 DATA_UNSAFE` (currently PASS).
- Fail-closed was observed before recovery: no new pivot entries while stale;
  once the tip caught up, the runner made a normal `FLAT` decision with
  `live_data_001.allow_new_entries=true`.
- Other running external traders remain `xgb` (screen), `tsm-vpa`, and
  `tsm-chandelier`; their code is outside this repository and requires a
  separate source-level parity audit before claiming they implement
  `LIVE-DATA-001`.

## 2026-08-14 — Fleet 005: confirm / confidence size / from→to

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Not live. **Promoted: none.**

Preregister: `configs/preregister/pivot_confirm_fromto_005.yaml`  
Report: `artifacts/reports/pivot_forecast/fleet_005_latest.json` (stamp `20260814T022921Z`)

Headline vs each book’s control (rank by intent expectancy; entry-bar exit rate cap 35%):
- **Confirm then enter / confirm add-on (K=1..3):** all hurt intent expectancy on ETH/SOL/BTC. Reject.
- **Confidence sizing:** ETH linear tiny lift only (exp_i 0.01517→0.01565); not enough to promote. BTC tertile look nicer on PnL but does not clear size-normalized gate + fleet policy. Reject as fleet change.
- **From→to abs(predicted level) as TP:** high PF but **entry-bar exit rate** 55% ETH / 39% BTC — blocked (stop inside single-bar noise).
- **Predicted next opposite pivot as TP:** weak (near PF≈1). Reject.
- **Oracle next opposite pivot:** strong upper bound (ETH PF~4.1, SOL~11.7, BTC~11.6) but **uses future labels — never promote**.
- **Label `confirm_bars` 3/4/5** (right_bars=3): identical ETH control metrics / level P90 — no lift.

Fleet unchanged: ETH `q50_w4` (+ soft-VSA quality), SOL `atr_clip_w5`, BTC `p80_w4` (+ 1h tp15/sl15 research sibling).

## 2026-08-13 — Fleet 004: ETH dual + BTC 1h entry-bar attack

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Not live.

Preregister: `configs/preregister/pivot_fleet_004_eth_dual_btc1h.yaml`  
Report: `artifacts/reports/pivot_forecast/fleet_004_latest.json`

Fleet:
- **ETH volume** `q50_w4` (812 tr, PF 1.62) + **quality** `q50_softvsa_w4` (587 tr, PF 1.78, intent-exp↑)
- **SOL** `atr_clip_w5` held (ebr 41%; no 1h)
- **BTC 15m** `p80_w4` kept
- **BTC 1h**: widening SL fixes entry-bar. Among ebr≤25%: prefer `tp15/sl15` (ebr 22.7%, exp_i 0.025); lowest ebr is `tp2/sl2` (13.6%). Baseline tp1/sl1 still ebr 48% — rejected.

## 2026-08-13 — Pivot fleet improve 003 (no Finplot)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Not live.

Preregister: `configs/preregister/pivot_fleet_improve_003.yaml`  
Report: `artifacts/reports/pivot_forecast/fleet_improve_003_latest.json`

Frozen research fleet:
- ETH `q50_w4` (volume) / **quality sibling** `q50_softvsa_w4` (intent-exp↑, pnl↓)
- SOL `atr_clip_w5` (keep; 1h atr_clip blocked — entry-bar ~80%)
- BTC `p80_w4` (keep; mid-density p76–p79 no lift; 1h blocked entry-bar >35%)

## 2026-08-12 — Pivot exec improve 002 (+ BTC)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`.

Preregister: `configs/preregister/pivot_exec_improve_002.yaml`  
Report: `artifacts/reports/pivot_forecast/exec_improve_002_latest.json`

Recommended trio (intent-exp / volume-aware):
- **BTC** `ctrl_ret_w4` — placement/pull/w5 all **hurt**; PF ~1.02 only
- **ETH** `level_q50_w4` — promote (812 tr, pnl↑)
- **SOL** `level_atr_clip_w5` — promote (859 tr, pnl ~29)

BTC rescue 002b (`btc_rescue_002b_latest.json`):
- **p80 gate** promote (234 tr, PF 1.24, pnl 8.7 vs ctrl 4.8) — best dense BTC lift
- π\*+band still sparse (n=20, PF 3.08) diagnostic only
- soft VSA / tp2sl1 / mid-band: reject

## 2026-08-12 — Pivot exec improve (`pivot_exec_improve_001`)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`.

Preregister: `configs/preregister/pivot_exec_improve_001.yaml`  
Report: `artifacts/reports/pivot_forecast/exec_improve_latest.json`

- Default pair unchanged: ETH P75 ATR **w4**, SOL TP1/SL1 P75 **w4**
- SOL **w5** frozen sibling — promote OK on intent expectancy (tiny lift)
- Time-head adaptive cancel **dropped**; adverse-path cancel **did not** beat w4
- Calibration-first (isotonic vs Platt by inner ECE): all folds kept **isotonic**
- Promising placement siblings (intent-exp + more fills/PnL, PF not collapsed):
  - ETH **level_q50_w4** (812 tr, pnl 40.9 vs ctrl 39.8)
  - SOL **level_atr_clip_w4** (790 tr, pnl 29.0 vs ctrl 24.4)
- Mid ATR band ranks #1 on intent expectancy but **cuts** trade count — quality arm, not volume

## 2026-08-13 — Structure fleet LIVE_STOP cleanup on 94.x

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY` for structure_v1 (CAUS-STRUCT-001 void).

Done on `94.156.189.76`:
- `bots_registry.yaml`: removed host bot tag `llm2`; `bots.llm2` → `status=LIVE_STOP`,
  `enabled=false`, `account=[]` (Xxobster6/7/8/10 no longer labeled live structure).
- Live host bots now: `llm2_pivot_*` (Xxobster7), `xgb` (Xxobster2), `tsm_vpa`
  (Xxobster5), `tsm_chandelier` (Xxobster6).
- All `llm2-structure*` systemd units **masked** + refresh timer disabled.
- Bybit audit Xxobster8/10/6/7: **no open positions / orders / stop / TP-SL**.
- Chandelier kept **systemd-only** (one process per symbol).

Evidence: `artifacts/reports/structure_live_stop_cleanup_latest.json`.

## 2026-08-12 — Pivot tip packs frozen; LIVE orders NOT enabled

User authorized real-USDT micro-live on `94.156.189.76` / Xxobster7 for:
- SOLUSDT `geo_tp1_sl1_p75_w4` (lev **29**)
- ETHUSDT `p75_ctrl_atr_w4` (lev **29**)

**Done:** tip packs frozen under `artifacts/live_packs/pivot_*`;
`llm2/live/pivot_runner.py` tip decide smoke OK (SHADOW).

**Not done (blocker):** certificates with four-proof, TP/SL-after-fill polish,
systemd deploy, bots registry, live↔BT parity job. **No orders placed.**
Max readiness still `LIVE_STOP / RESEARCH_ONLY` until those close.

## 2026-08-10 — Pivot multi-head rare settle (time + level heads)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`.

Clarification: prior **0.815 was PR-AUC**, not precision; baserate was already ~0.785
on a dense label. New rare settings (short horizon + high ATR) drop frac_any to
~0.15–0.26. LGBM lifts PR-AUC ≈ +0.10–0.13 vs baserate but outer ECE is often
poor (uncalibrated) — no promotion.

Time-to-pivot and level-return heads: LGBM correlations weak on outer OOS under
current feature pack. Report:
`artifacts/reports/pivot_forecast/multihead_rare_latest.json`
Script: `scripts/run_pivot_multihead_rare.py`

## 2026-08-10 — Pivot train matrix (Binance-only numerical models)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. No live orders. No chat-LLM core.

Run: `python scripts/run_pivot_train_matrix.py`  
Report: `artifacts/reports/pivot_forecast/train_matrix_latest.json`

Outer walk-forward (fold V2, end before lockbox 2026-05-01). Target = first fractal
pivot class {none, high, low} within horizon. Feature packs and LGBM/HistGB/MLP
variants compared to baserate.

Headline (outer pooled PR-AUC of "any pivot" in horizon): BTC 5m lgbm_m ≈ 0.815
(vs baserate ≈ 0.785); 15m/1h lifts smaller but models beat baserate on Brier.
Logistic initially failed on sklearn API (`multi_class` removed) — fixed after run.

## 2026-08-10 — Pivot MTF forecast system (additive, research-only) phases 1–6 starter

**Maximum earned readiness:** `LIVE_STOP / RESEARCH_ONLY`. No live orders.

| Item | Location / status |
|---|---|
| Architecture + leakage map | `docs/project_memory/PIVOT_MTF_FORECAST_ARCHITECTURE.md` |
| Coverage audit (JSON) | `artifacts/reports/pivot_forecast/data_coverage_latest.json` |
| Preregister | `configs/preregister/pivot_mtf_forecast_001.yaml` (OPEN) |
| Config | `configs/pivot_forecasting.yaml` |
| Package | `llm2/pivot/` (schema, fractal labels, resampler) |
| Pivot DB | `D:\projectsdata\pivot\pivot_research.sqlite` |
| Tests | `tests/test_pivot_labels.py` — 7 passed |

**Coverage facts (audited market_ohlcv):** Binance last 1m/5m/15m/1h/4h/1d OK for BTC/ETH/SOL;
Bybit OHLCV **MISSING**; 5m tip lag vs some 1h tips (~2026-07-11 vs Aug). Do not manufacture 5m from 15m/1h.

**Next:** cross-TF matcher, family B DC labels, causal feature pipeline, base-rate + logistic + LightGBM ladder with nested walk-forward (no NN until GBT baselines).

## 2026-08-08 — D-060: direction nest-filter trading CLOSED; no post-CAUS parent PF≥1

**Maximum earned readiness:** `LIVE_STOP / RESEARCH_ONLY`.

| Generation | Status |
|---|---|
| `structure_v1_next_retrace_forecast_001` | Stage-1 forecast skill **PASS** (IC ≈ 0.67–0.69); Stage-2 naive trade **FAIL** (PF ≈ 0.70–0.74) |
| `structure_v1_forecast_filter_on_direction_001` | Nest on tp1/sl2/hold6 direction: control + filters **FAIL** mean_fold PF ≈ 0.64–0.79 → **`CLOSED_TRADING_FAIL`** |
| Threshold freeze | `llm2.research.forecast_filter_seal.FROZEN_NEST_THRESHOLDS` — no outer retune |
| Parent inventory | `artifacts/reports/post_caus_parent_pf_inventory_001.json` — **answer NO** (max pooled hunt PF still &lt; 1) |
| Optional one-shot (not auto-run) | `configs/preregister/structure_v1_sparse_leg_vol_skip_001.yaml` sparse impulse + next_vol p75 skip only |

**Trading research:** prefer **leaving** `structure_v1` **direction@1h** (and nesting
on those failed parents). next_retrace remains a **state forecast**, not a live gate.
Do not re-open multi-arm filter hunts on viewed outer OOS.

## 2026-08-08 — D-058: orange track sealed; causal alpha redirect

**Maximum earned readiness:** `LIVE_STOP / RESEARCH_ONLY`.

Best causal proxy of look-ahead orange (`oracle_leaky`): outer mean absolute error
(MAE) ≈ 0.38, correlation ≈ 0.79 (HistGradientBoosting + as-of running retrace).
Not solvable to perfect orange under no-leakage. Trade on `pred_leaky` still fails;
`oracle_leaky` P&L is contamination look-ahead. **Stop optimizing orange for P&L.**

| Track | Status |
|---|---|
| `oracle_leaky` / `pred_leaky` hunt + pack freeze | **SEALED** (forensics only; `llm2.research.orange_track_seal`) |
| Residual oracle − pred histogram / Finplot | Done: outer residual MAE ≈ 0.381 matches proxy report (`artifacts/reports/oracle_pred_residual_forensics_001/`) |
| Causal clean space `structure_v1_no_retrace` | Hunt `structure_v1_causal_drop_retrace_001` **all 6 combos FAIL** V2.1 (PF ≈ 0.77–0.86) — report `artifacts/reports/structure_v1_causal_drop_retrace_001_latest.json` |
| Pre-fix structure packs / pre-2026-08-06 OOS | Still void |

**Next research (not orange):** leave structure_v1 single-book as abandoned family
candidate space, or open a **new** prereg only if the hypothesis changes (other
feature spaces / labels / horizons) — never re-rank these FAILS.

## 2026-08-06 — FOUR_PROOF_GATE_V1 + expanded leakage battery enforced

Shared `leakage` now hard-fails on: builder-responsiveness, prefix, future-mutation,
streaming/batch tip, forward-shift/near-label, and skipped decisive checks.
LLM2 requires `llm2.evidence.four_proof` (responsiveness + recompute_prefix +
no_live_fill + layer_a identity) before train/freeze; `register_freeze` and live
certificates refuse without `four_proof_hashes`. Structure columns have explicit
knowable-when rules in `indicators.publication_rules`. Pred mismatch = hard stop.

## 2026-08-06 — Fleet flattened; causal retrain FAIL; LIVE stays stopped

**Exposure:** Both hosts flattened (cancel orphans + reduce-only close). All
`llm2-structure*` units stopped/disabled. `bots` `since_date` / llm2 overrides set to
**2026-08-06**. Shutdown-flatten hook added to `micro_runner` (SIGTERM closes positions).

**Leakage engine (before retrain):** builder-responsiveness probe
(`EXTERNAL_CACHE_SUSPECTED`, conformance `CAUS-WAREHOUSE-001`) + warehouse-recompute
guard builder for `structure_v1`. Deployed to `/opt/botsgeneral/packages/{indicators,leakage}`
and LLM2 trees on ln1 + ln3. Units not restarted.

**Fresh hypothesis `structure_v1_caus_retrain_001`:** leakage gates PASS on BTC/ETH/SOL;
all six nested hunts **FAIL** V2.1 (PF 0.75–0.81). Report:
`artifacts/reports/structure_v1_caus_retrain_001_latest.json`.
**Max readiness: `LIVE_STOP / RESEARCH_ONLY`.** Do not restart LIVE on these packs.

## 2026-08-06 — CAUS-STRUCT-001: look-ahead in `last_retrace_pct` (fleet-wide invalidation)

Investigating why live and backtest trades differ found that the two sides were not
even scoring the same number: locally recomputed `pred_mean` differed from live on
84–100% of decision bars, flipping the side on roughly half.

Cause: a leg's Fibonacci retracement is measured against the END of the **next**
opposite leg, but `indicators/compute.py` published it at the leg's own confirmation
time. Research therefore scored bar T with post-T prices (look-ahead), while live saw
`NaN` and zero-filled it (a value training had dropped). Fixed by publishing at the
successor leg's known time; prefix-invariance now 10/10 on BTC/ETH/SOL with a
full-recompute control, bound by
`packages/indicators/tests/test_structure_causality.py`.

Also fixed: `last`/`last_price` are disjoint slices of one series (price_type is not
in the primary key), so `load_ohlcv` had been serving ETHUSDT 1h with a 49,807-bar
hole; concurrent-book slots now release on take-profit/stop in research as they do
live; clarity history is candle-derived instead of uptime-dependent; `size_mult` is
emitted by the research gate; the live retrace zero-fill is removed (fail closed).

**Consequence:** every `structure_v1` pack was trained on the leaked column. All
inherited readiness, backtests and live-vs-backtest charts predating 2026-08-06 are
void. Registry: `artifacts/sqlite/leakage_registry.json` →
`REMEDIATED_RETRAIN_REQUIRED`. Full write-up:
`docs/project_memory/LIVE_BT_SIGNAL_PARITY_REPORT_20260806.md`.

**Not yet deployed:** trading hosts still run the pre-fix indicator. `ln1`'s
`llm2-structure-refresh.service` has additionally been failing every hour
(`limit=1500` below the 5,000-bar guard) and its target list omits the k5 units.

## Status

`LIVE_STOP / RESEARCH_ONLY` for scale. Micro-live: Xxobster7 single-book fleet
(BTC/ETH/SOL) + Xxobster8 ETH **multitrade v1.2** (certificates expire 2026-08-17)
+ Xxobster6 ETH **k5_double3h_v1** (median strength) + Xxobster10 BTC/SOL K5 double
+ **Xxobster3** ETH **k5_double3h_p75_v1** on `185.203.119.52` (LIVE unit up;
  IP whitelist confirmed 2026-08-05 — `MODE_SET`/`LEVERAGE_SET` OK)
+ **Xxobster9** ETH **multitrade_p75_v1** on `185.203.119.52` (LIVE unit up 2026-08-05;
  `MODE_SET`/`LEVERAGE_SET` OK; `bots` name `llm2_structure_eth_multitrade_p75`)
+ **Xxobster11** ETH **15m wall_clock_p75** on `185.203.119.52` (LIVE unit up
  2026-08-05; `bots` name `llm2_structure_eth_15m_multitrade_wall_clock_p75`).
  Bring-up bars 14:00–14:45 UTC had live↔warehouse `pred_mean` tip-drift (decide
  ran while structure slice was incomplete; later full rebuild matched research).
  **Fail-closed gate redeployed 2026-08-05 (code-only):** `STRUCTURE_NOT_READY`
  refuse decide; shared tip must cover latest closed bar; REST tip merges onto
  shared history (no 20k wipe); refuse `structure_history_regression`. Full slice
  restored (15m n≈234544). Contaminated bring-up / 20k-refresh bars remain
  non-identity evidence.   Post-restore decides: **15:45**, **16:00**, **16:15 UTC** all
  `ops_fleet_live_signal_parity` **PASS** (exact `pred_mean`, side match).
  Soft pack-vs-research was tip-lag noise on 16:00; at 16:15 after research
  `update_series`: **0 column mismatches**, soft=[].
  **16:30 UTC:** log `need=15m skipped=1h,4h` (selective HTF skip works);
  refresh was ~386s. **VPS profile (2026-08-05):** compute 96% / upsert 3.6%;
  bottleneck `build_legs` O(n²) ~536s on ~65k swings. Fixed in botsgeneral
  `indicators.structure.build_legs` to O(n) prefix bias — re-profile `build_legs`
  ~2.4s, full compute+upsert ~30s class. Deployed to `/opt/botsgeneral/...` on
  185; tip-append deferred (full recompute now cheap enough). Hourly boundary
  still needs `1h` (`need_hour_open → ('15m','1h')`). Fleet signal parity
  `--bar-ts-ms 1785947400000` after research `update_series`: **PASS**
  (exact pred, soft=[]).

### Live↔warehouse/signal parity on 185 (2026-08-06)

Scripts: `run_fleet_live_warehouse_parity.py`, `ops_fleet_live_signal_parity.py`.
Tip **signal identity PASS** for all three units after research tip refresh:
15m wall_clock (02:15), ETH k5 p75 + multitrade p75 (01:00). Fixed OHLCV loader
to prefer freshest `last`/`last_price` tip (stale dense `last_price` had blocked
1h recompute). Multi-bar warehouse windows may still report `PARTIAL_TIP_DRIFT`
on older decisions; tip match + `snap=1.0` are the identity signal.

### `bots` on 185 (2026-08-05)

Fleet registry lists the three llm2 units explicitly (catch-all `llm2` removed on
185). `report.yaml` accounts: Xxobster3 / Xxobster9 / Xxobster11. `bots` shows
all three running bots and all three account PnL rows.

### ETH 15m multitrade geometry transfer (2026-08-05) — D-047

**Max readiness:** `RESEARCH_ONLY` / `OUTER_TRANSFER_COMPARE`. Live deploy
**FORBIDDEN**. Touch = **1m**.

**Warehouse:** built ETHUSDT **15m** `bar_features` via botsgeneral
`indicators.update_series` (n≈234551, swings≈64882); tip-refreshed 1h/4h.
Leakage audit `structure_v1` @ 15m: **PASS** (49 cols, LEAKAGE_POTENTIAL=0).
Report: `structure_v1_eth_15m_warehouse_audit_latest.json`.

| Arm | Geometry | q | E[r] | PF | WR | n | Result |
|-----|----------|---|------|-----|-----|---|--------|
| wall_clock_q50 | hold 24/48, lookback 672, label 24 | 0.5 | 0.809% | 3.73 | 72.4% | 21747 | control |
| **wall_clock_q75** | same wall-clock | **0.75** | **1.040%** | **6.49** | — | 13508 | **BEST** |
| bar_count_q75 | hold 6/12, lookback 168, label 6 | 0.75 | 0.633% | 8.79 | — | 26357 | higher PF, lower E[r] |

- p75 beats median on wall-clock (primary E[r]).
- Bar-count does **not** beat wall-clock p75 on E[r] (PF higher — denser short holds).
- Success criteria **PASSED** (best E[r]>0, PF≥1.20, no liq).
- Sharpe fold-mean is diagnostic only (not headline daily MTM wallet Sharpe);
  MIN_EXCHANGE dust caveat on dollar PnL.
- Report: `structure_v1_eth_15m_multitrade_geometry_001_latest.json`
- Prereg: `configs/preregister/structure_v1_eth_15m_multitrade_geometry_001.yaml`
- **Do not** reopen 1h clarity×hold×TP.

**Frozen RESEARCH_ONLY pack (D-047 winner):**
`artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1/`
(`eth_15m_multitrade_wall_clock_p75_v1`, hash
`03beafc58556db9adc4937d00eb43829cb5fb04d4284eaab1dbe66dd6de795fc`).
Retrained 15m model (not 1h). Live deploy **FORBIDDEN**.

**Clean last-3m Finplot (display only):** window `[2026-02-01, 2026-05-01)`
pre-lockbox OOS — n=880, E[r]=1.143%, PF=6.34, WR=82.3%, no liq.
Evidence `DISPLAY_ONLY_CLEAN_OOS_SLICE`. Metrics:
`structure_v1_eth_15m_wall_clock_q75_last3m_clean/metrics_latest.json`.
Calendar May–Aug 2026 lockbox **not** used.

### ETH 15m wall_clock p75 + TP∝|mean| nested (2026-08-05) — D-049

**Max readiness:** `RESEARCH_ONLY` / `OUTER_TRANSFER_COMPARE`. Live **FORBIDDEN**.

Control = wall_clock_q75 fixed book TP. Candidate =
`TP = book_tp × min(2, max(1, |pred_mean|/0.5))`.

| Arm | E[r] | PF | mean TP | n | Result |
|-----|------|-----|---------|---|--------|
| control fixed TP | 1.040% | 6.49 | — | 13508 | baseline |
| **TP∝\|mean\|** | **1.078%** | **6.64** | **2.23%** | 13502 | **PASS** |

- Criteria **PASSED** (beats control E[r], PF≥1.20, no liq).
- Report: `structure_v1_eth_15m_wall_clock_p75_tp_scale_absmean_001_latest.json`
- Prereg: `configs/preregister/structure_v1_eth_15m_wall_clock_p75_tp_scale_absmean_001.yaml`
- No 1h grid reopen; not live without new pack+cert+auth.

### BTC 15m Phase 2 same geometry (2026-08-05) — D-048

**Max readiness:** `RESEARCH_ONLY` / `OUTER_TRANSFER_COMPARE`. Live **FORBIDDEN**.
Separate generation (ETH OOS does not select BTC arm).

**Warehouse:** BTCUSDT 15m n≈242192, swings≈67158; leakage **PASS**.
Report: `structure_v1_btc_15m_warehouse_audit_latest.json`.

| Arm | E[r] | PF | WR | n | Result |
|-----|------|-----|-----|---|--------|
| wall_clock_q50 | 0.557% | 2.99 | 66.8% | 22742 | control |
| **wall_clock_q75** | **0.796%** | **5.28** | **76.0%** | 14139 | **BEST** |
| bar_count_q75 | 0.426% | 6.17 | 73.0% | 25776 | loses on E[r] |

- Same ranking pattern as ETH: wall-clock p75 wins primary E[r]; bar-count denser but worse E[r].
- Success criteria **PASSED**.
- Report: `structure_v1_btc_15m_multitrade_geometry_001_latest.json`
- Prereg: `configs/preregister/structure_v1_btc_15m_multitrade_geometry_001.yaml`

### ETH live pred_mean vs recompute (2026-08-05)

**Max earned readiness:** `LIVE_STOP / RESEARCH_ONLY`
**Evidence class:** `LIVE_PRED_DIVERGENCE_DIAGNOSTIC`
**Principal blocker:** Live structure refresh used `limit=800` and
`upsert_bundle` wipe/rebuild — truncated swings ≠ research warehouse.

First live bar 2026-08-03 16:00 UTC: ledger `pred_mean=+0.456` / long;
warehouse recompute `−0.310` / short (same model SHA `7e826c63…`).
Truncated-800 reproduction → `+0.40` (same sign as live; residual ~0.05 from
shared-candle tip vs warehouse last_price). No decide-time feature snapshot
existed (now added). `full` vs `recent_only` on the same warehouse still matches.

**Fix (local):** `ensure_live_structure_parity` — sync research warehouse when
available, else `refresh_symbol(limit=None)`; hard-refuse `limit<5000` 1h;
persist `feature_snapshot` in decisions. Contract:
`llm2/live/feature_parity_contract.py`.

**Deployed 2026-08-05 (authorized):** ln1 (**94.x**) + ln3 (**185.203.119.52**)
structure live units corrected and restarted. All active packs: parity code +
depth gate + binance 1h `n_bars≥50k`. Inactive ln1 multitrade v1/v1_1 also
refreshed. Live decide Open-High-Low-Close-Volume tip widened to 2000 bars.
Evidence: `fleet_parity_audit_ln1.json`, `fleet_parity_audit_ln3_185.json`,
`live_bt_calc_gap_risks_20260805.json`.

**Remaining exact-signal risk:** live structure/vol still come from
`shared_candles.db`, while backtest reads research `market_ohlcv` +
`indicators.sqlite`. Full-history removes the 800-bar bug; byte-identical
signals need the same candle/indicator bytes (warehouse sync = gold path).

**Backtest does NOT use truncated 800-bar refresh.** Hunt/backtest reads the
full-history research `indicators.sqlite`. Live was the divergent path.

### Live↔research candle/indicator/signal identity (2026-08-05)

**Max earned readiness:** `LIVE_STOP / RESEARCH_ONLY`
**Evidence class:** `OPS_LIVE_RESEARCH_PARITY_GATE`
**Principal blocker:** none on ETH 12:00 UTC bar after bake + heal.

- botsgeneral collector baked onto `market_data.fetch_binance` Last (schema 6).
- Research `indicators update-all` for BTC/ETH/SOL 1h/4h/1w from `market_ohlcv`.
- Fleet pack structure refreshed from shared; concurrent refresh had wiped ETH 1h
  briefly — restored.
- **Catch-up bug fixed** in `micro_runner`: restart no longer sleeps past closed bars;
  processes chronological unprocessed bars. Deployed ln1 + ln3.
- Ops gate (single unit deep): `scripts/ops_live_research_parity_gate.py`
- **Fleet Live Signal Parity** (all ln1 + ln3 bots, last closed 1h `pred_mean`):
  `scripts/ops_fleet_live_signal_parity.py` →
  `artifacts/reports/ops_fleet_live_signal_parity_latest.json`
- ETH 12:00 UTC live vs warehouse: candles tip OK; pack indicators identical
  (`close=1875.22`); `pred_mean` exact match (−0.26046579158340305); side −1;
  `feature_snapshot` 0 mismatches. Report:
  `artifacts/reports/ops_live_research_parity_gate_latest.json`.

### Fleet Live Signal Parity (standard anytime gate)

**Name:** Fleet Live Signal Parity  
**Evidence class:** `OPS_FLEET_LIVE_SIGNAL_PARITY`  
**Max earned readiness:** none (ops diagnostic; does not promote readiness).  
**What it checks:** every active structure unit on **ln1 (94.x)** and **ln3 (185.x)** —
live ledger `pred_mean` + side vs local warehouse recompute with the matching frozen
pack under `artifacts/live_packs/`. Soft-flags pack tip vs research `bar_features`
mismatches unless `--strict-indicators`.

```text
python scripts/ops_fleet_live_signal_parity.py
python scripts/ops_fleet_live_signal_parity.py --host ln1
python scripts/ops_fleet_live_signal_parity.py --require-target-bar
python scripts/ops_fleet_live_signal_parity.py --list-fleet
```

Reports: `artifacts/reports/ops_fleet_live_signal_parity_latest.json`  
Registry of units/packs is in the script (`FLEET_REGISTRY`).  
Related: single-unit deep gate `ops_live_research_parity_gate.py`; 1m tip-only
`run_1m_indicator_parity_bot.py`.

### ETH K5 size-scale ref / min_edge metrics table (diagnostic)

**Evidence class:** `MEASURE_DIAGNOSTIC` — multi-threshold outer stitch; **not** for
promotion (do not pick a ref after peeping).
**Script:** `scripts/settle_eth_k5_size_scale_ref_thresholds_001.py`  
**Prereg:** `configs/preregister/structure_v1_eth_k5_size_scale_ref_thresholds_001.yaml`  
**Reports:**  
`artifacts/reports/structure_v1_eth_k5_size_scale_ref_thresholds_001_latest.json`,  
`…_TABLE.md`, `…_all_cells.csv`  
**Frequency companion:**  
`structure_v1_eth_k5_pred_mean_strength_met_freq_001_latest.json`  
(`scripts/report_eth_k5_pred_mean_strength_met_freq.py`)

Keeps full PF / WR / trades / E[r] next to any size or take-profit scale design.

### ETH K5 size_scale ref=0.30 — potential upgrade (D-051)

**Status:** **HOLD** as research potential upgrade — **not live**.  
**Gate:** only reconsider after the **current live** ETH K5 path shows sustained
profitability; then new single-arm freeze + cert + explicit auth (D-051).  
**Formula:** `size_mult = time_mult × clip(|pred_mean|/0.30, 1, 2)` on K5
double-within-3h + median clarity.  
**Stitch (pre-lockbox):** n=10818, net_pnl≈2902 vs control≈2394, PF≈4.61 vs 4.11,
WR/E[r] same as control; ~72% size-lift / ~6% at 2× cap; 0 liq.  
**Metrics + Finplot:** `scripts/plot_eth_k5_size_scale_ref_0_30.py` →  
`artifacts/reports/structure_v1_eth_k5_size_scale_ref_0_30_display_001_latest.json`  
**Forbidden now:** live pack change, ref=0.15, or multi-threshold peep promotion.

### 1m indicator parity testbot (diagnostic only)

**Max earned readiness:** none (does **not** promote fleet readiness).
**Evidence class:** `INDICATOR_PARITY_1M_DIAGNOSTIC`
**Scope:** closed Binance USD-M **Last** 1m tip → live-path structure slice vs
local research structure DBs; tip `bar_features` + tip-50 close hash. No train,
no orders, not a 1h SHADOW/micro-live gate.

**Operational rules:**
- Use the 1m bot **only** for indicator / candle tip identity.
- Keep the production 1h fleet under `ops_live_research_parity_gate.py` for
  pack structure, `pred_mean`, and side / decision checks.
- After any warehouse or collector heal (schema bump, bake, tip-fix), re-run
  `run_1m_indicator_parity_bot.py --once` **before** debugging live structure
  packs on the research host.

- Library: `llm2/live/indicator_parity_1m.py` (min structure history 20k 1m bars;
  refuses short truncate).
- Runner: `scripts/run_1m_indicator_parity_bot.py`
- Ledger: `artifacts/indicator_parity_1m/parity.sqlite`
- Research indicators DB: `D:\projectsdata\indicators\indicators_1m_parity.sqlite`

```text
python scripts/run_1m_indicator_parity_bot.py --once --symbol ETHUSDT
python scripts/run_1m_indicator_parity_bot.py --loop --symbol ETHUSDT
```

1h fleet ops gate remains `scripts/ops_live_research_parity_gate.py`.

### ETH single-book max-hold gap (2026-08-05)

**Finding:** Xxobster7 ETH Buy had correct Full Take Profit / Stop Loss
(MarkPrice; ~+1% / −2%) but never exited via max-hold because single-book did not
track `open_books` or run `_expired_books` (multitrade-only). Mark had not reached TP.
**Fix (local, not yet deployed):** single-book inserts `open_books`, syncs orphans,
runs max-hold close; Full trading-stop + fail-closed flatten; `_bybit_retcode` treats
integer `0` as success (avoid `x or -1`). Fleet stop-order coverage on ln1 audit: all
open sizes covered (Partial empties position TP/SL fields by design).
**Blocker:** VPS deploy/restart of `llm2-structure-eth` (+ other single-book units)
needs explicit user authorization — overdue books will max-hold-close on next bar.

### ETH multitrade p75 lockbox Finplot + metrics (2026-08-05) — diagnostic

**Max readiness from this open:** still `MICRO_LIVE_CANDIDATE` from live ship /
`OUTER_TRANSFER_COMPARE` from outer settle — lockbox is **not** a promotion gate.
**Evidence class:** `LOCKBOX_OPENED_CONTAMINATED` (D-036/D-038).

Script: `scripts/plot_eth_multitrade_p75_lockbox.py` (dual accept required).
Report: `artifacts/reports/structure_v1_eth_multitrade_p75_lockbox_latest.json`.

| Window | n trades | PF | E[r] | WR | net PnL (MIN_EXCHANGE) |
|--------|----------|-----|------|-----|-------------------------|
| 2026-05-01 → ~2026-08-05 | 397 | ~11.78 | ~0.985% | ~86.4% | ~73.76 USDT |

Diagnostic only. Do **not** retune knobs or scale capital from these numbers.
Quotable history remains outer settle `structure_v1_eth_multitrade_strength_p75_001`.

### Xxobster9 live vs warehouse parity bundle (2026-08-05)

**Evidence class:** `LIVE_WAREHOUSE_FULL_PARITY_BUNDLE_XXOBSTER9`.
**Max readiness:** still micro-live / research — **not** a retune gate for p75.

Scripts: `run_x9_full_parity_bundle.py`, `compare_x9_snap_vs_pack_indicators.py`,
`compare_x9_snapshot_vs_research_bar_features.py`.
Reports: `x9_live_full_parity_bundle_latest.json`,
`x9_live_snap_vs_pack_indicators_latest.json`,
`x9_snapshot_vs_research_bar_features_latest.json`.

| Check | Result |
|-------|--------|
| Shared candles tip vs research OHLCV tip | **PASS** (same tip_ts + OHLC + tip50 SHA) |
| Pack structure depth | ~58.6k 1h bars (full-history, not 800) |
| `strength_hist` | **n=3 / 168** (warm-up; expected days after deploy) |
| Model from `feature_snapshot` | **3/3 exact** |
| Scored `pred_mean` vs warehouse recompute | **2/3 exact** (11:00, 12:00); **10:00** residual drift ~0.11 after research indicator refresh |
| Side match (scored) | **3/3** |
| Gate skips | 2× `clarity_mean_strength` (weak buffer history) |
| Local research `bar_features` tip | Extended via botsgeneral `update_series` ETH 1h/4h/1w (was lagging 1 bar) |

**Do not** retune strength_quantile from warm-up skips or the single 10:00 residual.

### ETH multitrade p75 live ship (2026-08-05) — D-046

**Max earned readiness (arm):** `MICRO_LIVE_CANDIDATE` (authorized ship of
prior D-044 OUTER_TRANSFER_COMPARE pack). Certificate expires 2026-08-19.
**Pack:** `structure_v1_ethusdt_multitrade_p75_v1` / `eth_multitrade_p75_v1`
hash `1babf3afa0406d96…` · account **Xxobster9** · host **185.203.119.52** ·
service `llm2-structure-eth-multitrade-p75-v1`.
**Geometry:** eth_multitrade_v1_2 (K=7, clarity_scope=all, fib 1.618, hold12)
+ **strength_quantile=0.75**. MIN_EXCHANGE. Signal Binance via botsgeneral
`shared_candles.db` collector; execution Bybit.
Evidence: `structure_v1_eth_multitrade_strength_p75_001` (E[r]≈0.952% vs 0.802% control).
Register: `bots` / `bots discover` include `llm2_structure_eth_multitrade_p75`.

### ETH K5 p75 live ship + nested TP∝|mean| (2026-08-05) — D-045

**Max earned readiness (nested TP arm):** `RESEARCH_ONLY` / `OUTER_TRANSFER_COMPARE`.
**Live p75 unit:** pack + certificate sealed; `bots` / `bots sitrep` show
`llm2_structure_eth_k5_double3h_p75` on Xxobster3; **orders blocked** by
IP whitelist done 2026-08-05 — unit **active**, `MODE_SET`/`LEVERAGE_SET` OK.
Signal source Binance; engine botsgeneral tradesim
(`TRADESIM_REQUIRE_UNDER=/opt/botsgeneral/packages/tradesim`).

| Arm | Control | Candidate | Primary E[r] | PF | Result |
|-----|---------|-----------|--------------|-----|--------|
| p75 ship (live) | median k5 (Xxobster6) | `eth_k5_double3h_p75_v1` @ Xxobster3/185 | prior D-041 0.643% | 7.04 | **AUTHORIZED**; API IP blocker |
| p75 + TP∝\|mean\| | p75 fixed TP 1% | `TP=1%×min(2,max(1,\|mean\|/0.5))` | **0.703% vs 0.643%** | **7.45 vs 7.04** | **PASS** research-only; mean TP≈1.07% |

- Report: `structure_v1_eth_k5_p75_tp_scale_absmean_001_latest.json`
- Prereg: `configs/preregister/structure_v1_eth_k5_p75_tp_scale_absmean_001.yaml`
- Helper: `llm2.live.multitrade.scale_tp_by_abs_mean` (live gate flag off by default)
- **Candles on 185:** exchange=`binance` (correct for signal parity). Collector
  `botsgeneral-collector@185.203.119.52` **active** and fetching. 1h/4h
  open-time lag ~45–50 min mid-hour is **normal** (forming bar). 1w STALE is
  expected until the weekly bar closes. Bybit series in the same DB are stale
  and unused by this pack.
- **Do not** reopen clarity×hold×TP after this OOS; variable TP stays proportional.
- TP-scale arm is **not** live until a new pack hash + certificate + explicit auth.

### ETH K5 TP1 / break-even / TP2 fixed hold-24 (2026-08-15)

**Max earned readiness:** `RESEARCH_ONLY` / `OUTER_TRANSFER_COMPARE`.
No deployment, pack change, or VPS action is authorized.

| Arm | Stitched trades | E[r] | PF | Liquidations | Verdict |
|-----|----------------:|-----:|---:|-------------:|---------|
| Frozen K5 control: TP 1%, SL 2%, hold 12 | 6,384 | -0.1879% | 0.7145 | 0 | baseline fails |
| 50% TP1 1%, BE after TP1, 50% TP2 2%, fixed hold 24 | 3,881 | -0.1807% | 0.7514 | 0 | **FAIL** PF gate; no promotion |

- The candidate marginally improves the negative primary expectancy, but remains
  negative and fails the frozen PF >= 1.20 gate.
- Break-even arms after TP1 and becomes effective on the next decision bar under
  tradesim `EXEC-020`.
- Hold 24 is measured from entry. It is **not** a reset or extension from TP1;
  the engine feature is absent. Handoff prompt:
  `docs/project_memory/BOTSGENERAL_POST_TP1_HOLD_PROMPT.md`.
- Evidence: `artifacts/reports/structure_v1_eth_k5_tp1_be_tp2_hold24_001_latest.json`;
  preregistration: `configs/preregister/structure_v1_eth_k5_tp1_be_tp2_hold24_001.yaml`.

**TODO (train-window / new prereg only — not this OOS):**

1. Vol-scaled TP (average true range / realized vol factor, still capped)
2. Discrete post-p75 strength-rank TP buckets (not continuous chase)
3. Structure-impulse TP extension (separate feature family)
4. Multi-take-profit + break-even after TP1 (tradesim `tp_legs` parity)
5. Hold-extend **only after** TP1 (needs tradesim engine work — frozen hold today)
6. ~~After IP whitelist restart~~ **done** — unit running; watch first LIVE entry

### Selective data program (2026-08-05) — D-044

**Max readiness:** `RESEARCH_ONLY`. Evidence class for overlays:
`OUTER_TRANSFER_COMPARE`. Official settle readiness unchanged
(`SHADOW_READY_CANDIDATE` PF≈1.77–1.87 for base packs). MIN_EXCHANGE dust caveat
applies to all high geometry PF below.

**Phase A — execution overlays (keep hunting here):**

| Arm | Control | Candidate | Primary E[r] | PF | WR | Result |
|-----|---------|-----------|--------------|-----|-----|--------|
| ETH K5 p75 freeze | live median k5 | pack `eth_k5_double3h_p75_v1` | 0.643% vs 0.521% (prior D-041) | 7.04 vs 4.11 | 89% vs — | **FROZEN research pack** |
| ETH multitrade p75 | v1.2 q=0.5 | q=0.75 | **0.952% vs 0.802%** | 6.96 vs 4.26 | 83.6% vs 75.5% | **PASS**, not live |
| Skip weak SHORT book1 | v1.2 | require high tercile \|mean\| on short book1 | **0.826% vs 0.802%** | 4.43 vs 4.26 | 76.2% vs 75.5% | **PASS**, not live |

- Pack: `artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1/`
- Reports: `structure_v1_eth_multitrade_strength_p75_001_latest.json`,
  `structure_v1_eth_multitrade_skip_weak_short_book1_001_latest.json`
- Live deploy still **FORBIDDEN** without certificate + explicit user auth.

**Phase B — new features (valid negatives):**

- Built `oi_v1` / `structure_oi_v1` and `news_v1` / `structure_news_v1` with
  confirmation-time audits (`tests/test_oi_news_causality.py`). Leakage PASS.
- Outer single-book feature compare vs `structure_v1`:
  - **OI FAILED** E[r] (0.223% < 0.283%); PF still ≥1.20 but primary fails.
  - **News FAILED** (no lift; identical stitch to control).
- Report: `structure_v1_selective_data_feature_compare_001_latest.json`.
- Warehouse refresh attempted via `botsgeneral.research_candles` (candles OK;
  funding still ends ~2026-07-24 in local DB — not a blocker for this run).

**Do not:** combine cooloff / EV-π* with p75 on viewed OOS; promote OI/news;
open lockbox for ranking; live-swap without auth.

### ETH K5 EV calibration / π* (2026-08-05) — D-043

- **Transfer:** isotonic hit-cal + `p_hat ≥ π*≈0.72` (CostHurdle TP1/SL2) on live
  K5 double geometry vs median control.
- First buggy run: calibrator did not fit (train/calib split collapsed to 1 row) →
  identity control. Fixed: `train_calib_split` + bracket path win labels.
- **Corrected OOS:** candidate E[r] **0.5203%** vs control **0.5206%**; PF **4.07**
  vs **4.11**; n **9411** vs **10818**; ~4197 π* skips; no liq. **FAILED** primary.
- Report: `structure_v1_eth_k5_ev_calibrated_pi_star_001_latest.json`.
- **Maximize expectancy (return units) still:** p75 strength (K5 + now multitrade
  transfer PASS under D-044), research-only. Cooloff (D-042) and EV-π* (D-043)
  both fail primary E[r].

### Fleet streak autopsy + cooloff transfer (2026-08-05) — D-042

- **Measure (all 22 live_packs, pre-lockbox outer stitch):** generation
  `structure_v1_fleet_streak_autopsy_001`. Reports:
  `artifacts/reports/structure_v1_fleet_streak_autopsy_001_latest.json`,
  trades under `…_trades/`, dossiers under `…_dossiers/`, LLM proposals (offline
  template, `promotion_blocked`) `…_llm_proposals.json`.
- **Pain rank top:** eth_multitrade_v1_1 (max loss streak 17) → v1 → **live v1.2**
  (streak 15) → eth_k5_double3h → btc_k5… Cross-pack: max_hold + wrong-way@1h
  buckets, often mid/low strength on short book1.
- **Nested transfer (gate-first):** cooloff after 3 proxy losses vs live
  `eth_multitrade_v1_2`. Candidate PF **4.31 vs 4.26** control but
  expectancy_return_units **0.797% vs 0.802%** (failed primary criterion);
  830 cooloff skips; no liq. **Not promoted.** Report:
  `structure_v1_eth_multitrade_loss_streak_cooloff_001_latest.json`.
- Negative cooloff stands. Autopsy follow-up **skip weak short book1** (D-044)
  and **multitrade p75** both passed primary E[r] as RESEARCH_ONLY.

### Sizing policy (2026-08-04)

- **Live (all micro bots):** always **MIN_EXCHANGE** — venue minimum qty per symbol
  (double-within-3h multiplies min qty only). `micro_runner` forces min even if a
  pack incorrectly declares equity leverage.
- **Research / display only:** `EQUITY_LEVERAGE_NOTIONAL`
  (`notional = equity × N × leverage`, default N=0.01) in tradesim +
  `llm2/sizing_policy.py` for wallet-linked study (wallet_return vs
  roi_on_invested_notional + peak concurrent margin). Not wired as live size.
- K5 double packs stay `sizing: MIN_EXCHANGE` with min-size equity caveat.
- Display example (research equity mode):  
  `structure_v1_ethusdt_k5_flat_vs_double_last30d_eq10000_lev15_szequity_leverage_N0.01_metrics.json`

### Pack version registry (2026-08-04) — D-041

- SQLite table `live_pack_versions` in `artifacts/sqlite/research.sqlite`
- Writer: `llm2/evidence/pack_registry.py` (`register_freeze`, `register_live`,
  `open_pack_run`, `backfill_all_packs`, `regenerate_versions_md`)
- Human map regenerated from registry: `artifacts/live_packs/VERSIONS.md`
- Reopen without resim: `python scripts/plot_eth_k5_flat_vs_double.py --from-pack eth_k5_double3h_v1`
  or `--run-id …` (labels `REOPEN_ONLY`)

### ETH K5 expectancy strength p75 (2026-08-04) — D-041

- **Outer transfer** on live `eth_k5_double3h_v1` geometry (K=5, hold12, TP1%/SL2%,
  size×2 within 3h, `clarity_scope=all`): control median `strength_quantile=0.5`
  vs candidate **p75** (`strength_quantile=0.75`).
- Full outer stitch (hard end &lt; 2026-05-01, lockbox unused):
  - Control: expectancy_return_units ≈ **0.5206%**, Profit Factor ≈ **4.11**, n≈10818
  - Candidate: expectancy_return_units ≈ **0.6432%** (+0.1225 pp), Profit Factor ≈ **7.04**, n≈5996
  - No liquidations; success criteria **PASSED** (`OUTER_TRANSFER_COMPARE`)
- Report: `artifacts/reports/structure_v1_eth_k5_expectancy_strength_p75_001_latest.json`
- Prereg: `configs/preregister/structure_v1_eth_k5_expectancy_strength_p75_001.yaml`
- **Live deploy FORBIDDEN** until new pack hash + certificate + explicit user auth.
  Xxobster6 remains **median gate** (`eth_k5_double3h_v1`).

### ETH multitrade failure modes + nested improves (2026-08-04) — D-039

- Cluster plain English: same-side ≥3-within-6h **all-loss** clusters ≈**5.2%**
  (ETH multitrade) and **≪1%** on BTC/ETH/SOL live single-book — **not** the
  usual mode. Most bursts are mixed/profitable.
- Cross-pack wrong@1h (live geometry): ETH mt book1 ≈**41.5%** ≈ BTC/ETH/SOL
  single ≈40–42%. Book1 is not uniquely “more wrong” than other symbols; it is
  weak *relative to deeper filtered books* inside multitrade.
  Report: `structure_v1_failure_modes_btc_eth_sol_001_latest.json`.
- **Nested settle A (transfer):** `clarity_scope=all` vs live addon control —
  PF **4.26 vs 3.59**, book1 wrong@1h **38% vs 42%**, no liquidation.
  `OUTER_TRANSFER_COMPARE`. **No live swap** without auth.
  Report: `structure_v1_eth_multitrade_primary_clarity_all_001_latest.json`.
- **Nested settle B (contaminated):** shorter hold 4/8 vs 6/12 — PF **3.63 vs
  3.59** only. Not promotion-eligible from this window.
  Report: `structure_v1_eth_multitrade_shorter_hold_001_latest.json`.
- **Live swapped (user auth 2026-08-04):** Xxobster8 now runs **v1.2**
  `clarity_scope=all` (D-040). v1.1 retained for rollback.

### Clean-data improve (2026-08-04) — OUTER_SETTLE clarity hold12

- **Track 1 complete:** frozen arm `mean_strength|hold12|tp1%|sl2%` full V2.1 outer
  settle (hard end &lt; 2026-05-01, no lockbox). All three live-matching combos **PASS**
  and beat control: BTCUSDT fwd_return PF≈**2.86** (ctrl≈2.03); ETHUSDT direction
  PF≈**3.32** (ctrl≈1.99); SOLUSDT direction PF≈**2.66** (ctrl≈1.94).
  Report: `artifacts/reports/structure_v1_clarity_hold12_outer_settle_001_latest.json`.
  New packs (not live): `structure_v1_{btc,eth,sol}usdt_clarity_hold12_v1`.
  **No VPS swap without certificate + explicit user auth.**
- **Track 2 complete (RESEARCH_ONLY):** BTC/SOL transfer of k1_clarity + k5_double3h
  both beat control; k5 PF≈3.89 (BTC) / 3.36 (SOL). Not a pack freeze.
  Report: `structure_v1_btc_sol_cluster_double_transfer_001_latest.json`.
- **Track 3 deferred:** prereg `structure_v1_target_align_calibration_001` remains
  PREREG_ONLY — Tracks 1–2 already yield pack-eligible single-book improves.

### BTC/SOL K5 double on Xxobster10 (user-authorized 2026-08-04)

- **Not** previously live; deployed as isolated units on **Xxobster10** (shared
  account, different symbols). Track2 RESEARCH_TRANSFER_MICRO (not full V2.1
  hedge settle). MIN_EXCHANGE.
  - `llm2-structure-btc-k5-double3h-v1` — BTCUSDT K5 double3h
  - `llm2-structure-sol-k5-double3h-v1` — SOLUSDT K5 double3h
- Xxobster7 single-book BTC/ETH/SOL left running (separate accounts).
- Multitrade K7 measure (clean outer folds): report
  `structure_v1_eth_multitrade_v1_1_measure_latest.json` (MEASURE_LIVE_GEOMETRY).

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
  single-book ETH. **Active:** `eth_multitrade_v1_2` — mean_strength,
  **clarity_scope=all**, fib_ext=1.618 (book3+ TP 2.618%), hold_addon=12,
  **K=7**/side. Service `llm2-structure-eth-multitrade-v1_2`. Replaces v1.1
  (addon-only clarity); v1.1 + v1 packs retained stopped for rollback.
  Evidence: `structure_v1_eth_multitrade_primary_clarity_all_001`. Map:
  `artifacts/live_packs/VERSIONS.md`. MICRO only.
- **D-036 peek discipline (2026-08-04):** May-2026→2026-08-04 multitrade lockbox grids
  are **diagnostic only**. Quotable historical edge = outer-fold settle. Peek log:
  `artifacts/evidence/peek_log.jsonl` (seed via `python scripts/log_research_peek.py seed`).
  Clean multitrade *parameter* claims only with prereg +
  `POST_MULTITRADE_FREEZE_START=2026-08-05` (or outer folds). Copying DBs does not reset
  contamination. Locked arm stay: `eth_multitrade_v1_1`.
  Prereg: `structure_v1_eth_multitrade_v1_1_post_freeze_001.yaml`.
- **ETH multitrade K=1..36 outer-OOS sweep (2026-08-04):** frozen arm
  `mean_strength|fib1.618|hold12` (live v1.1 knobs), window [2022-01-01, 2026-05-01)
  — lockbox not used. Symmetric K/side (both long and short allowed).
  **Saturation at K≈14** (cap skips → 0); **K=15..36 identical** to K=14. Peak occupancy
  only **12/side** under mean_strength. Best diagnostic PnL/PF at K=14 (PF≈5.31);
  within ~2% best PnL already at **K=10**. Live freeze stays **K=7** until nested
  promotion protocol. MIN_EXCHANGE dust. Report
  `structure_v1_eth_multitrade_k_sweep_001_latest.json`.
  + `artifacts/reports/live_fleet_concordance_latest.json`. Window
  [2022-01-01, 2026-05-01) only — lockbox not used. Signal intent (gated sides):
  Xxobster7 ≥2 bots fire on **~69%** of bars; all three on **~26%**. ETH single vs
  multitrade raw sides **identical**; path: multitrade enters more (stack/clarity).
  Pairwise lifts above independence (clustered hours). Not a promotion gate.
  Gate: `llm2/evidence/lockbox_guard.py` — requires
  `--i-accept-lockbox-contamination`; Finplot also needs
  `--i-accept-finplot-lockbox`. Charts default off (`TRADESIM_NO_PLOT`).
  Scripts: `plot_structure_lockbox`, concurrent finplot plots, fib/switch hunts.
  Prefer outer-fold settle. Peek log still authoritative for contamination status.
- **D-037 expansion sealed lockbox (2026-08-04):** prereg
  `structure_v1_expansion_lockbox_final_001`. Freezes + one-shot single-book done for
  BNB/XRP/DOGE/AVAX/DOT/TRX/XLM (train cut before lockbox; fit before 2025-10-01).
  Multi-arm refuse-closed. After open: **LOCKBOX_OPENED_CONTAMINATED** (diagnostic).
  Quotable promotion = settle outer-OOS PF only. Report
  `structure_v1_expansion_lockbox_final_001_latest.json`. No live deploy.
  Diagnostic lockbox PF (MIN_EXCHANGE dust) vs settle PF:
  BNB 1.95/1.57, XRP 1.87/1.71, DOGE 2.36/1.61, AVAX 2.60/1.80, DOT 2.71/1.84,
  TRX 1.65/1.54, XLM 2.52/1.69 — **XLM entry-bar exits ≈47%** (noise caveat).
  Packs under `artifacts/live_packs/structure_v1_{sym}_direction`.
- **Switch×TP ablation 001 (2026-08-04):** prereg
  `structure_v1_eth_switch_tp_ablation_001`. Contaminated lockbox. Uniform +1%
  control loses badly (PF≈3.07 vs live≈3.96). Wider TP schedule helps; Fibonacci
  label not required. Only gate-pass vs live: same arm with **K=8** (PF≈4.01,
  bal↑). **Not promoted** per D-036 — keep v1.1.
  Report `structure_v1_eth_switch_tp_ablation_001_latest.json`.
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
- **ETH single-book clarity×hold×TP gen-1 (2026-08-04):** preregister
  `structure_v1_eth_singlebook_clarity_hold_tp_001` (SL fixed 2%). Inner-selected
  `mean_strength|hold12|tp1%` on fold-0 train; stitched outer OOS PF≈**3.32** vs
  control `none|hold6|tp1%` PF≈**1.99** (ΔPF≈+1.34; 5072 vs 8657 trades; bootstrap
  pos-exp 100%; no liquidation). Winning arm kept Take Profit at 1% — clarity + hold
  transferred from multitrade; Fibonacci 2.618% TP not selected. Conformance GREEN.
  Evidence class: execution-grid fold-V2 stitch, **RESEARCH_ONLY** — does **not** replace
  official settle PF≈1.77 and does **not** authorize live pack edits. Lockbox not used.
  Report `structure_v1_eth_singlebook_clarity_hold_tp_001_latest.json` + `_REPORT.md`.
  Do not re-search this space after OOS view.
- **Frozen-arm BTC/SOL transfer (2026-08-04):** same arm `mean_strength|hold12|tp1%`
  (no re-rank) vs control on fold V2. Stitched PF: BTC direction **2.94** (ctl 1.90),
  BTC fwd_return **2.86** (ctl 2.03), SOL direction **2.66** (ctl 1.94), SOL fwd_return
  **1.90** (ctl 1.51). Live-matching targets both beat control. Still **RESEARCH_ONLY**;
  not a V2.1 full-gate settle; no Xxobster7 pack swap without explicit auth. Report
  `structure_v1_frozen_arm_btc_sol_transfer_001_latest.json` + `_REPORT.md`.
- **ETH cluster concurrency 2nd/3rd book (2026-08-04):** on frozen
  `mean_strength|hold12|tp1%`, fold V2 stitch. K=1 PF≈**3.21**; K=2 open **3.32**;
  K=3 open **3.53** (best PnL); K=3 cluster≤3h **3.61** (best PF, Δ+0.41 vs K=1);
  K=3 cluster≤6h **3.58**. Yes — a 2nd/3rd book helps; short cluster gate lifts PF
  further while taking fewer add-ons than always-open K=3. RESEARCH_ONLY; stacked
  min-exchange margin not scale evidence. Report
  `structure_v1_eth_cluster_concurrency_001_latest.json` + `_REPORT.md`.
- **ETH concurrency ladder K=1..9 / max 18 total (2026-08-04):** same frozen arm.
  Open ladder PF rises K1 **3.21** → K9 **4.16** (PnL 358→**1809**); diminishing
  after ~K4–5 (K8→K9 only +0.04 PF). K9 cluster≤3h PF **4.24** (fewer trades).
  RESEARCH_ONLY. Report `structure_v1_eth_cluster_concurrency_k9_001_latest.json`.
- **ETH size-double ≤3h + K=3..9 (2026-08-04):** fold V2 only (no lockbox/peek).
  If signal ≤3h after last same-side entry → **2×** min-qty else 1×. Double beats
  flat 1× at **all** K on PF and PnL (7/7); best double K9 PF≈**4.43** PnL≈**3133**
  vs flat K9 PF≈4.16 PnL≈1809. RESEARCH_ONLY. Report
  `structure_v1_eth_cluster_size_double_k3_9_001_latest.json` + `_REPORT.md`.
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
