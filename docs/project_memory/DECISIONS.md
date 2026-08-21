# LLM2 Decisions

Standing decisions. Each one is here because reversing it silently would invalidate
results, so a reversal needs an explicit, dated entry rather than a code change.

---

## D-061 — ETH K5 TP1/BE/TP2 fixed-hold arm fails; do not promote

**Date:** 2026-08-15 · **Status:** ACTIVE · **Evidence:**
`configs/preregister/structure_v1_eth_k5_tp1_be_tp2_hold24_001.yaml`,
`artifacts/reports/structure_v1_eth_k5_tp1_be_tp2_hold24_001_latest.json`

One frozen outer-transfer arm retained the ETH K5 median-strength, K=5 and
double-within-three-hours entry geometry, while changing exits to: 50% TP1 at
1%, break-even after TP1, 50% TP2 at 2%, and fixed hold 24 from entry.

| Arm | Stitched E[r] | PF | Trades | Decision |
|---|---:|---:|---:|---|
| Control, TP1% / SL2% / hold12 | -0.1879% | 0.7145 | 6,384 | baseline |
| TP1/BE/TP2 / fixed hold24 | -0.1807% | 0.7514 | 3,881 | **FAIL** |

The candidate improves the negative control slightly but remains negative and
fails the pre-frozen PF >= 1.20 requirement. It is not a live candidate.

The hold is an explicit approximation: it starts at original entry, including
after TP1. tradesim currently cannot reset/extend residual hold from TP1. The
required botsgeneral-only engine work is recorded in
`docs/project_memory/BOTSGENERAL_POST_TP1_HOLD_PROMPT.md`; do not build a
second simulator in LLM2.

## D-060 — Direction nest-filter trading branch CLOSED (forecast skill ≠ trade)

**Date:** 2026-08-08 · **Status:** ACTIVE · **Evidence:**
`artifacts/reports/structure_v1_next_retrace_forecast_001_latest.json`,
`artifacts/reports/structure_v1_forecast_filter_on_direction_001_latest.json`,
`artifacts/reports/post_caus_parent_pf_inventory_001.json`,
`configs/preregister/structure_v1_forecast_filter_on_direction_001.yaml`,
`llm2/research/forecast_filter_seal.py`

Post-CAUS nested program:

| Generation | Forecast skill | Trading Profit Factor (PF) |
|---|---|---|
| `structure_v1_next_retrace_forecast_001` Stage-1 | PASS (Spearman IC ≈ 0.67–0.69) | Stage-2 naive every-leg **FAIL** PF ≈ 0.70–0.74 |
| `structure_v1_forecast_filter_on_direction_001` | next_retrace / next_vol skill reconfirmed | Control + filters **FAIL** mean_fold PF ≈ 0.64–0.79 |

Therefore:

* **Close** the dense `structure_v1` **direction@1h nest-filter trading claim**.
  Status of gen `structure_v1_forecast_filter_on_direction_001` =
  `CLOSED_TRADING_FAIL`.
* **Freeze** nest thresholds (no outer-OOS retune): deep_retrace_thresh=0.5,
  retrace_score_min=0.05, vol_skip_percentile=75, tp=1%, sl=2%, hold=6,
  min_edge=0.1, filter arm set = {control, next_retrace_agree_skip,
  next_vol_skip_p75}. Exact list in `FROZEN_NEST_THRESHOLDS`.
* High next_retrace Information Coefficient (IC) is a **state forecast**, not a
  mandate to trade direction and not live authorization.
* Do not improve by multi-arm grids or multi-task selection on outer PF.
* Post-CAUS parent inventory: **no** hunt row with pooled PF ≥ 1.0 on
  `structure_v1` / `structure_v1_no_retrace` direction or fwd_return @ 1h
  (`caus_retrain_001`, `causal_drop_retrace_001`). **Do not nest** filters on
  these parents. Prefer shifting trading research off this family.
* Optional single-arm continuation (not auto-run, not a reopening of the nest):
  `structure_v1_sparse_leg_vol_skip_001` — sparse leg-confirm impulse + next_vol
  p75 skip only. One fail closes it without threshold hunting.
* Re-run of closed nest script requires
  `LLM2_ALLOW_CLOSED_NEST_FILTER_RERUN=1` and
  `--i-accept-closed-trading-fail-rerun` (diagnostics with frozen constants only).

## D-058 — Orange / oracle_leaky is contamination forensics only (no PnL track)

**Date:** 2026-08-08 · **Status:** ACTIVE · **Evidence:**
`artifacts/reports/leaky_proxy_asof_max_001/leaky_proxy_asof_max_001_latest.json`,
`artifacts/reports/oracle_pred_residual_forensics_001/`,
`llm2/research/orange_track_seal.py`,
`configs/preregister/structure_v1_causal_drop_retrace_001.yaml`

Best *causal* reconstruction of the look-ahead orange series (`oracle_leaky` /
pre-CAUS-STRUCT-001 `last_retrace_pct`) tops out near outer MAE ≈ 0.38 and
correlation ≈ 0.79 (HistGradientBoosting + as-of running retrace). Trade retest on
`pred_leaky` loses money while `oracle_leaky` profits — the residual is future-swing
information, not a deployable edge. Therefore:

* Stop optimizing orange for profit and loss (P&L). Sealed scripts refuse unless
  `LLM2_ALLOW_ORANGE_FORENSICS=1` and `--i-accept-contamination-forensics`.
* Never freeze live packs on `pred_leaky` or `oracle_leaky`.
* HistGradientBoosting + `run_retrace_expand_max` is a leg-state **diagnostic**, not
  a substitute for cyan publish or a model feature path to promote.
* Research budget goes to post-CAUS **causal** alphas: true-cyan warehouse publish and
  `structure_v1_no_retrace` (generation `structure_v1_causal_drop_retrace_001`), not
  perfect-orange imitation.
* Residual histogram / Finplot of `oracle − pred` is optional forensics only.

## D-060 — Causal running-retrace is a separate alpha prereg (not orange MAE)

**Date:** 2026-08-08 · **Status:** ACTIVE · **Code:**
`llm2/features/run_retrace_v1.py`,
`configs/preregister/structure_v1_run_retrace_alpha_001.yaml`,
`scripts/run_structure_v1_run_retrace_alpha_001.py`

The ~0.79 correlation HistGradientBoosting reconstruction of orange remains
**diagnostics only**. Tradable use of retrace-like information must target the
**causal** running depth (`run_retrace*`, space `structure_v1_run_retrace`) under
a fresh pre-registration. Forbidden still: mean absolute error (MAE) → 0 on
`oracle_leaky`, packs with `pred_leaky` / `oracle_leaky`, promoting residual plots.

## D-059 — structure_v1_causal_drop_retrace_001: no edge without last_retrace*

**Date:** 2026-08-08 · **Status:** ACTIVE · **Evidence:**
`artifacts/reports/structure_v1_causal_drop_retrace_001_latest.json`,
`configs/preregister/structure_v1_causal_drop_retrace_001.yaml`

Fresh nested hunt on causal `structure_v1_no_retrace` (BTCUSDT/ETHUSDT/SOLUSDT ×
fwd_return/direction) failed V2.1 on every combo (pooled Profit Factor ≈
0.77–0.86, negative daily mark-to-market Sharpe, zero positive bootstrap fraction).
Leakage and four-proof gates passed. Maximum readiness remains
`LIVE_STOP / RESEARCH_ONLY`. Do not open multitrade/k5 overlays on this parent.
Do not re-search the same space without a new, pre-registered hypothesis change.

## D-057 — FOUR_PROOF_GATE_V1 before train / freeze / live authorize

**Date:** 2026-08-06 · **Status:** ACTIVE · **Code:** `llm2/evidence/four_proof.py`

A green shared leakage report alone is illegal evidence for warehouse-backed spaces.
Before train, pack freeze, or live certificate authorization, all four proofs must pass
and their SHA-256 hashes must be stored on the pack / certificate:

1. builder_responsiveness (CAUS-WAREHOUSE-001)
2. recompute_prefix (decisive leakage battery on the warehouse-recompute builder)
3. no_live_feature_fill (no NaN→0 on the live path)
4. layer_a_pred_identity (research join vs recompute path agree on tip)

`register_freeze` and `refuse_vps_deploy_without_live_certificate` fail closed without
these hashes. Live↔backtest prediction mismatch is a hard stop.

## D-055 — CAUS-WAREHOUSE-001: leakage engine must catch cache builders

**Date:** 2026-08-06 · **Status:** ACTIVE · **Evidence:**
`packages/leakage/tests/test_builder_responsiveness.py`,
`tests/test_caus_warehouse_001.py`,
`llm2/features/structure_recompute.py`

The shared leakage engine now hard-fails when a tip shape-shock does not move
feature outputs (`EXTERNAL_CACHE_SUSPECTED` / `BUILDER_RESPONSIVENESS`). Warehouse-
backed spaces must recompute indicators into a temporary store inside the audit
builder; joining a calendar-keyed database alone is forbidden as an audit path.
A missing `pytest.mark.conformance("CAUS-WAREHOUSE-001")` binding fails the build.

## D-056 — structure_v1_caus_retrain_001: no edge after causal fix

**Date:** 2026-08-06 · **Status:** ACTIVE · **Evidence:**
`artifacts/reports/structure_v1_caus_retrain_001_latest.json`,
`configs/preregister/structure_v1_caus_retrain_001.yaml`

Fresh nested hunt on the causal warehouse (BTC/ETH/SOL × fwd_return/direction)
failed V2.1 gates on every combo (pooled Profit Factor ≈ 0.75–0.81, Sharpe negative,
zero positive-expectancy bootstrap fraction). Maximum earned readiness remains
`LIVE_STOP / RESEARCH_ONLY`. Do not redeploy LIVE structure_v1 packs from this
generation. Multitrade / k5 overlays inherit the failed parent and stay stopped.

## D-052 — CAUS-STRUCT-001: leg retracement publishes at the successor leg

**Date:** 2026-08-06 · **Status:** ACTIVE · **Evidence:**
`docs/project_memory/LIVE_BT_SIGNAL_PARITY_REPORT_20260806.md`,
`packages/indicators/tests/test_structure_causality.py`,
`scripts/test_indicator_recompute_prefix_invariance.py`

A leg's `retrace_pct` is measured against the end of the **next** opposite leg, so it
is published at that successor leg's known time, never at the leg's own confirmation.
Publishing earlier put post-T prices into bar T and made live (which sees `NaN` there)
structurally unable to reproduce research: predictions differed on 84–100% of live
decision bars and the side flipped on about half.

Consequences that must not be quietly undone:

* Every published structure column must stay prefix-invariant; a missing test binding
  fails the build like a failing test.
* Live must never substitute a value for a missing feature that research drops. The
  retrace zero-fill in `micro_runner` is removed permanently.
* All `structure_v1` models trained before this date consumed the leaked column.
  Their readiness, backtests and charts are void; retraining under a fresh
  pre-registration is required before any number is quoted again.

## D-053 — `last` and `last_price` are one series, never a choice

**Date:** 2026-08-06 · **Status:** ACTIVE · **Evidence:**
`tests/test_ohlcv_price_type_resolve.py`,
`tests/test_live_bt_signal_parity_guards.py`

`price_type` is not part of the `market_ohlcv` primary key, so the two labels are
disjoint slices of the same last-trade series. Loading must take both. Pinning one
label served ETHUSDT 1h as 8,844 bars with a 49,807-bar hole. Mark prices are still
never mixed into a last-trade load.

## D-054 — one shared slot-release rule for concurrent books

**Date:** 2026-08-06 · **Status:** ACTIVE · **Evidence:**
`llm2/live/multitrade.py::slot_release_ts_ms`,
`tests/test_live_bt_signal_parity_guards.py`

A book stops occupying a slot when its take-profit or stop fills, not at max-hold.
Research and live use the same function, so a `cap_reached` skip means the same thing
on both sides. The clarity strength history is likewise derived from candles, so it
does not depend on how long the bot process has been running.

## D-051 — ETH K5 size_scale ref=0.30: hold as potential live upgrade

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`configs/preregister/structure_v1_eth_k5_size_scale_ref_thresholds_001.yaml`,
`scripts/settle_eth_k5_size_scale_ref_thresholds_001.py`,
`artifacts/reports/structure_v1_eth_k5_size_scale_ref_thresholds_001_latest.json`,
`artifacts/reports/structure_v1_eth_k5_size_scale_ref_0_30_display_001_latest.json`,
`scripts/plot_eth_k5_size_scale_ref_0_30.py`,
`llm2/live/multitrade.py` (`scale_size_mult_by_abs_mean`),
`llm2/signals/cluster_concurrency.py` (`size_scale_by_abs_mean`)

**Rules:**
1. **Hold only.** User keeps size-scale **ref=0.30** as a **potential upgrade**
   if (and only if) the **current live** ETH K5 path proves profitable under the
   existing pack sizing (time-double / no strength size-scale). Research only until
   then; max readiness `RESEARCH_ONLY`.
2. **Not live now.** Do **not** freeze, certify, VPS-deploy, or change live
   `size_mult` to strength-scale without a **new** single-arm generation + pack
   + certificate + **explicit user authorization** after live profitability is
   established. Multi-threshold table remains MEASURE_DIAGNOSTIC — not a menu.
3. **Frozen research formula** (if later promoted as that generation):
   `size_mult = time_mult × clip(|pred_mean| / 0.30, 1.0, 2.0)` with
   `time_mult = 2` if same-side entry within 3h else 1; base geometry =
   ETH K5 double-within-3h + median clarity + min_edge 0.10.
4. **Do not promote ref=0.15** (or other refs picked from the multi-ref table).
   Prefer mild refs (≥ ~0.30) so the 2× strength cap is rare (~6% at 0.30 vs
   ~72% at 0.15). E[r] / WR match control; capital and fees rise — treat as risk
   scale, not new alpha.
5. Gate checklist before any future freeze: live profitability evidence for the
   base K5 unit; single-arm re-settlement at ref=0.30 only; margin/liquidation
   under the sizing mode live will use; code path parity
   (`size_scale_by_abs_mean` on research + live); no multi-arm outer pick.

---

## D-050 — ETH 15m wall_clock p75 shipped to Xxobster11 / 185.203.119.52

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1/`,
`configs/live/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1_certificate.yaml`,
`scripts/authorize_eth_15m_multitrade_wall_clock_p75_v1_live.py`,
`scripts/deploy_eth_15m_multitrade_wall_clock_p75_v1.ps1`,
`scripts/_vps_register_llm2_units_185.py`

**Rules:**
1. User authorized pack `eth_15m_multitrade_wall_clock_p75_v1` on **Xxobster11**
   / **185.203.119.52** as unit
   `llm2-structure-eth-15m-multitrade-wall-clock-p75-v1` (registry name
   `llm2_structure_eth_15m_multitrade_wall_clock_p75`).
2. Decision TF=15m; touch=1m; HTF structure refresh must include **1h+4h**
   (not 1w). Live skip-tip must require HTF series depth.
3. Candles = botsgeneral shared collector (Binance signal); execution Bybit;
   MIN_EXCHANGE only; cert expires 2026-08-19 unless renewed.
4. On 185, `bots_registry` fleet lists the three llm2 units explicitly
   (Xxobster3 / 9 / 11); do not use catch-all `llm2` on this host.
5. Does **not** authorize capital scale-up or promoting the nested TP∝|mean| arm.
6. Live must fail-closed on incomplete structure: after refresh, require deep
   decision+HTF series, decision-bar tip, and HTF tips covering the completed
   join; on failure log `STRUCTURE_NOT_READY`, skip decide, leave
   `last_processed` unchanged (retry bar). Redeploy `micro_runner` to 185 when
   authorized so bring-up tip-drift cannot recur.

---

## D-049 — ETH 15m wall_clock p75 + TP∝|mean| nested PASS (research)

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`configs/preregister/structure_v1_eth_15m_wall_clock_p75_tp_scale_absmean_001.yaml`,
`scripts/settle_eth_15m_wall_clock_p75_tp_scale_absmean_001.py`,
`artifacts/reports/structure_v1_eth_15m_wall_clock_p75_tp_scale_absmean_001_latest.json`,
`llm2/live/multitrade.py` (`scale_tp_by_abs_mean`),
`llm2/experiments/eth_multitrade_nested.py` (tp_scale on book TP)

**Rules:**
1. Nested only on frozen ETH 15m **wall_clock_q75**. No 1h grid reopen;
   no reopening 15m geometry arms in this generation.
2. Formula (after book TP including fib books):
   `TP = book_tp × min(2, max(1, |pred_mean| / 0.5))`.
3. Outer stitch: candidate E[r] ≈ **1.078%** PF ≈ **6.64** mean TP ≈ **2.23%**
   vs control E[r] ≈ **1.040%** PF ≈ **6.49**; n≈13502; no liq. **PASS**.
4. Max readiness `RESEARCH_ONLY`. Live FORBIDDEN without new pack+cert+auth.

---

## D-048 — BTC 15m Phase 2: same geometry; wall_clock p75 wins

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`scripts/build_btc_15m_structure_and_audit.py`,
`artifacts/reports/structure_v1_btc_15m_warehouse_audit_latest.json`,
`configs/preregister/structure_v1_btc_15m_multitrade_geometry_001.yaml`,
`scripts/settle_btc_15m_multitrade_geometry_001.py`,
`artifacts/reports/structure_v1_btc_15m_multitrade_geometry_001_latest.json`

**Rules:**
1. BTC is a **separate generation** from ETH 15m (D-047). ETH OOS must not
   choose the BTC arm.
2. Knobs match ETH a priori (wall-clock q50/q75 + bar-count q75). Touch=1m.
3. BTC warehouse + leakage `structure_v1` @ 15m must PASS before settle.
4. Outer stitch: best = **wall_clock_q75** E[r] ≈ **0.796%** PF ≈ **5.28**
   vs q50 E[r] ≈ **0.557%**; bar-count E[r] ≈ **0.426%** loses primary.
   Criteria **PASSED**. Max readiness `RESEARCH_ONLY`. Live FORBIDDEN.
5. Do not reopen 1h clarity×hold×TP after this OOS.

---

## D-047 — ETH 15m multitrade wall-clock p75 beats median; bar-count loses on E[r]

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`scripts/build_eth_15m_structure_and_audit.py`,
`artifacts/reports/structure_v1_eth_15m_warehouse_audit_latest.json`,
`configs/preregister/structure_v1_eth_15m_multitrade_geometry_001.yaml`,
`scripts/settle_eth_15m_multitrade_geometry_001.py`,
`artifacts/reports/structure_v1_eth_15m_multitrade_geometry_001_latest.json`,
`llm2/experiments/eth_multitrade_nested.py` (timeframe/label_horizon overrides),
`artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1/`,
`scripts/freeze_eth_15m_multitrade_wall_clock_p75_v1.py`,
`scripts/plot_eth_15m_wall_clock_q75_last3m_clean.py`

**Rules:**
1. ETHUSDT **15m** structure warehouse is built with botsgeneral
   `indicators.update_series` before any 15m train; leakage
   `structure_v1` @ 15m must PASS.
2. Decision TF = 15m; touch TF = **1m** (per `touch_timeframe`).
3. Frozen multi-arm (all listed before OOS): wall-clock q50 / wall-clock q75 /
   bar-count q75. Multitrade K=7, fib 1.618, TP1%/SL2%, clarity_scope=all.
4. Wall-clock mapping: base_hold=24, hold_addon=48, mean_lookback=672,
   label_horizon=24. Bar-count keeps 6/12/168/6.
5. Outer stitch: best = **wall_clock_q75** E[r] ≈ **1.040%** PF ≈ **6.49**
   vs wall_clock_q50 E[r] ≈ **0.809%** PF ≈ **3.73**. Bar-count q75 E[r] ≈
   **0.633%** PF ≈ **8.79** — loses primary. Criteria **PASSED**.
   Max readiness `RESEARCH_ONLY`. Live FORBIDDEN without new pack+cert+auth.
6. Research pack `eth_15m_multitrade_wall_clock_p75_v1` is hashable
   `FROZEN_RESEARCH_ONLY` (retrained 15m model). Not live.
7. Display Finplot last-3m uses only pre-lockbox `[2026-02-01, 2026-05-01)`;
   not a promotion gate (`DISPLAY_ONLY_CLEAN_OOS_SLICE`).
8. BTC Phase 2 is a **new** prereg (D-048), not this generation.
9. Do not reopen 1h clarity×hold×TP grids after this OOS.

---

## D-046 — ETH multitrade p75 shipped to Xxobster9 / 185.203.119.52

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`artifacts/live_packs/structure_v1_ethusdt_multitrade_p75_v1/`,
`configs/live/structure_v1_ethusdt_multitrade_p75_v1_certificate.yaml`,
`scripts/authorize_eth_multitrade_p75_v1_live.py`,
`scripts/deploy_eth_multitrade_p75_v1.sh`,
`scripts/_vps_register_eth_multitrade_p75_xxobster9.py`,
`artifacts/reports/structure_v1_eth_multitrade_strength_p75_001_latest.json`

**Rules:**
1. User authorized pack `eth_multitrade_p75_v1` (v1.2 geometry +
   `strength_quantile=0.75`) on **Xxobster9** / **185.203.119.52** as unit
   `llm2-structure-eth-multitrade-p75-v1` (registry bot name
   `llm2_structure_eth_multitrade_p75`). Xxobster8 on 94 stays **median**
   multitrade v1.2.
2. Candles = botsgeneral collector `shared_candles.db` (Binance signal);
   execution Bybit; MIN_EXCHANGE only; cert expires 2026-08-19 unless renewed.
3. Does **not** authorize capital scale-up or replacing v1.2 on Xxobster8.

---

## D-045 — ETH K5 p75 shipped to Xxobster3/185; nested TP∝|mean| PASS (research)

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1/`,
`configs/live/structure_v1_ethusdt_k5_double3h_p75_v1_certificate.yaml`,
`scripts/authorize_eth_k5_double3h_p75_v1_live.py`,
`scripts/deploy_eth_k5_double3h_p75_v1.ps1`,
`scripts/_vps_register_eth_k5_p75_xxobster3.py`,
`configs/preregister/structure_v1_eth_k5_p75_tp_scale_absmean_001.yaml`,
`scripts/settle_eth_k5_p75_tp_scale_absmean_001.py`,
`artifacts/reports/structure_v1_eth_k5_p75_tp_scale_absmean_001_latest.json`,
`llm2/live/multitrade.py` (`scale_tp_by_abs_mean`),
`tests/test_tp_scale_by_abs_mean.py`

**Rules:**
1. User authorized **p75 fixed-TP** pack `eth_k5_double3h_p75_v1` on
   **Xxobster3** / **185.203.119.52** as isolated unit
   `llm2-structure-eth-k5-double3h-p75-v1` (registry name
   `llm2_structure_eth_k5_double3h_p75`). Xxobster6 on 94.156.189.76 stays
   **median** `eth_k5_double3h_v1`.
2. Certificate + pack_hash must match after registry writes (authorize seals
   fingerprint **after** `register_freeze` / `register_live`).
3. Live uses botsgeneral tradesim under `/opt/botsgeneral/packages/tradesim`
   (`TRADESIM_REQUIRE_UNDER` pinned). Signal candles = **Binance**.
4. Bybit API IP whitelist for Xxobster3 includes `185.203.119.52` (confirmed
   2026-08-05: `MODE_SET`/`LEVERAGE_SET` retCode=0). Do not leave the unit in a
   restart crash-loop if unmatched IP returns.
5. Nested transfer **p75 + TP proportional to |pred_mean|** PASSED vs p75 fixed
   TP control: E[r] ≈ **0.703%** vs **0.643%**; PF ≈ **7.45** vs **7.04**;
   mean TP ≈ **1.07%**; n≈5994; no liq. Frozen formula
   `TP = 0.01 × min(2, max(1, |pred_mean| / 0.5))`. Evidence
   `OUTER_TRANSFER_COMPARE`. **Not live** without new pack + cert + auth.
6. Do **not** reopen clarity×hold×TP after this OOS. Remaining TP ideas
   (vol-scale, discrete strength buckets, structure impulse, multi-TP/BE,
   hold-after-TP1) are train-window / new-prereg TODO only.
7. Does not authorize scaling capital or promoting the TP-scale arm by default.

---

## D-044 — Selective data program: p75 multitrade + weak-short-book1 PASS; OI/news fail

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1/`,
`scripts/freeze_eth_k5_double3h_p75_v1.py`,
`configs/preregister/structure_v1_eth_multitrade_strength_p75_001.yaml`,
`scripts/settle_eth_multitrade_strength_p75_001.py`,
`artifacts/reports/structure_v1_eth_multitrade_strength_p75_001_latest.json`,
`configs/preregister/structure_v1_eth_multitrade_skip_weak_short_book1_001.yaml`,
`scripts/settle_eth_multitrade_skip_weak_short_book1_001.py`,
`artifacts/reports/structure_v1_eth_multitrade_skip_weak_short_book1_001_latest.json`,
`llm2/features/oi_v1.py`, `llm2/features/news_v1.py`,
`configs/preregister/structure_v1_selective_data_feature_compare_001.yaml`,
`scripts/settle_structure_selective_data_feature_compare_001.py`,
`artifacts/reports/structure_v1_selective_data_feature_compare_001_latest.json`,
`tests/test_oi_news_causality.py`

**Rules:**
1. **max readiness remains `RESEARCH_ONLY` / `LIVE_STOP` for scale.** Overlays
   that beat median live geometry on outer stitch do **not** auto-deploy.
2. **ETH K5 p75** `eth_k5_double3h_p75_v1` (strength_q=0.75) from D-041; live on
   Xxobster3/185 authorized under **D-045** (IP whitelist still required).
   Live Xxobster6 stays median `eth_k5_double3h_v1`.
3. **ETH multitrade p75 PASSED** outer transfer vs live v1.2 control:
   expectancy_return_units ≈ **0.952%** vs **0.802%**; PF ≈ **6.96** vs **4.26**;
   win rate ≈ **83.6%** vs **75.5%**; n≈6697 vs 12608; no liq. Evidence class
   `OUTER_TRANSFER_COMPARE`. Not live.
4. **Skip mid/low-strength SHORT book1 PASSED** (causal: side + book_idx +
   strength history tercile only, no exit labels): E[r] ≈ **0.826%** vs **0.802%**;
   PF ≈ **4.43** vs **4.26**; ~915 skips. Does not combine with cooloff/EV-π*
   on this OOS. Not live.
5. **structure_oi_v1 FAILED** primary E[r] vs structure_v1 (single-book geometry):
   E[r] 0.223% vs 0.283%; PF 1.74 vs 2.02. Do not promote OI into packs from this
   generation. Negative success stands; no OOS retune of OI transforms.
6. **structure_news_v1 FAILED** (identity with control after fixing all-NaN
   `news_z`); density features alone did not change LightGBM path. Expand labels
   or entity filters only under a **new** prereg — not re-grid on this window.
7. Defer order book (short calendar), cryptodb (D-028), vault `tradeshistory`,
   and Polymarket as promotion evidence for this family.
8. Does not authorize VPS pack swap or certificate extension.

---

## D-043 — ETH K5 EV isotonic + π* gate fails vs control (research only)

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`llm2/decision/calibrate.py`,
`configs/preregister/structure_v1_eth_k5_ev_calibrated_pi_star_001.yaml`,
`scripts/settle_eth_k5_ev_calibrated_pi_star_001.py`,
`artifacts/reports/structure_v1_eth_k5_ev_calibrated_pi_star_001_latest.json`,
`tests/test_calibrate_decision.py`

**Rules:**
1. Live / structure packs remain **LightGBM regressors**, not calibrated long/short
   probability models. Open decision is banded `pred_mean` + execution gates; not
   P(long)/P(short) percent pairs on the micro path.
2. **Train-only isotonic** maps `|score| → P̂(bracket path win)` then requires
   `p_hat ≥ π*` from `CostHurdle` (TP 1% / SL 2% → π* ≈ **0.72**). Labels are
   adverse TP/SL path hits on the train calib slice, not raw direction-match.
3. Outer transfer on `eth_k5_double3h_v1` geometry: control E[r] ≈ **0.5206%**
   PF ≈ **4.11** n≈10818; candidate E[r] ≈ **0.5203%** PF ≈ **4.07** n≈9411
   (π* skipped ~4.2k decision-rows); criteria **FAILED**. Negative result stands.
4. Do not retune π*, calib_frac, or combine with p75 on this OOS after failure.
   Best expectancy arm still the prior **p75 strength** transfer (D-041), not live.
5. Does not authorize live deploy.

---

## D-042 — Fleet streak autopsy; cooloff gate fails primary expectancy (research only)

**Date:** 2026-08-05 · **Status:** ACTIVE · **Evidence:**
`llm2/evidence/streak_autopsy.py`,
`scripts/analyze_fleet_streak_autopsy.py`,
`artifacts/reports/structure_v1_fleet_streak_autopsy_001_latest.json`,
`configs/preregister/structure_v1_eth_multitrade_loss_streak_cooloff_001.yaml`,
`scripts/settle_eth_multitrade_loss_streak_cooloff_001.py`,
`artifacts/reports/structure_v1_eth_multitrade_loss_streak_cooloff_001_latest.json`

**Rules:**
1. Chronological win/loss streaks (by exit time) are **Measure_diagnostic**, not a
   promotion gate. Autopsy hard end is exclusive of the forward lockbox.
2. Large Language Model (LLM) output on dossiers is analyst-only
   (`promotion_blocked`); does not retrain LightGBM or deploy.
3. **Cooloff-after-3-losses** on live eth_multitrade_v1_2 geometry was a frozen
   outer transfer: slightly higher Profit Factor, slightly **lower**
   expectancy_return_units vs control → **failed success criteria**. Negative
   result stands; do not promote cooloff.
4. Do not select cooloff N (or other streak filters) on outer Out-of-Sample (OOS)
   after viewing this fail. Next arm must be a new prereg (e.g. p75 already
   settled separately, or a train-only feature) without multi-arm outer grids.
5. Does not authorize live pack swaps.

---

## D-041 — Pack registry + ETH K5 p75 expectancy transfer (research only)

**Date:** 2026-08-04 · **Status:** ACTIVE · **Evidence:**
`llm2/evidence/pack_registry.py`, `llm2/registry/schema.sql` (`live_pack_versions`),
`artifacts/live_packs/VERSIONS.md`, `scripts/backfill_live_pack_registry.py`,
`configs/preregister/structure_v1_eth_k5_expectancy_strength_p75_001.yaml`,
`scripts/settle_eth_k5_expectancy_strength_p75_001.py`,
`artifacts/reports/structure_v1_eth_k5_expectancy_strength_p75_001_latest.json`

**Rules:**
1. **Pack versions are append-friendly and reopenable.** Every freeze writes
   `pack_meta.json` + a `live_pack_versions` row; `VERSIONS.md` is generated from
   the registry (do not hand-edit as source of truth). `open_pack_run(version_id)`
   / plot `--from-pack` reopens stored `tradesim` run_ids — never label a resim as
   freeze evidence.
2. **strength_quantile** default remains **0.5 (median)** on all live packs.
   `mean_strength_ok(..., strength_quantile=…)` is available for research; live
   geometry unchanged unless a new pack freezes another quantile.
3. **p75 transfer PASS (not live):** candidate `strength_quantile=0.75` on
   eth_k5_double3h geometry beat control on full outer-fold stitch:
   expectancy_return_units ≈0.6432% vs 0.5206%; Profit Factor ≈7.04 vs 4.11;
   fewer trades (≈5996 vs ≈10818); no liquidation. Evidence class
   `OUTER_TRANSFER_COMPARE`. Quote full outer stitch only — not last-30d display.
4. **Does not authorize live pack freeze or Xxobster6 swap.** Promotion needs
   new pack directory + certificate + explicit user auth. Do not combine with
   hold/K/TP grids in the same generation.

---

## D-040 — User authorized live swap: eth_multitrade_v1_2 (clarity_scope=all)

**Date:** 2026-08-04 · **Status:** ACTIVE · **Evidence:**
`artifacts/live_packs/structure_v1_ethusdt_multitrade_v1_2`,
`configs/live/structure_v1_ethusdt_multitrade_v1_2_certificate.yaml`,
`structure_v1_eth_multitrade_primary_clarity_all_001_latest.json`

**Rules:**
1. User explicitly authorized replacing Xxobster8 live multitrade with the
   `clarity_scope=all` candidate (2026-08-04 chat).
2. Active unit: `llm2-structure-eth-multitrade-v1_2` on `94.156.189.76` /
   Xxobster8. Prior `llm2-structure-eth-multitrade-v1_1` stopped, pack retained.
3. Geometry unchanged except clarity scope: K=7, fib 1.618, hold 6/12, TP/SL 1%/2%,
   mean_strength, MIN_EXCHANGE, leverage 18×.
4. Rollback: re-enable `llm2-structure-eth-multitrade-v1_1` (see VERSIONS.md).
5. Does not authorize other pack swaps (clarity hold12 single-book, K changes, etc.).

---

## D-039 — Nested improve path: primary clarity transfer; shorter-hold contaminated

**Date:** 2026-08-04 · **Status:** ACTIVE · **Evidence:**
`configs/preregister/structure_v1_eth_multitrade_primary_clarity_all_001.yaml`,
`configs/preregister/structure_v1_eth_multitrade_shorter_hold_001.yaml`,
`scripts/settle_eth_multitrade_nested_arm.py`,
`artifacts/reports/structure_v1_eth_multitrade_primary_clarity_all_001_latest.json`,
`artifacts/reports/structure_v1_eth_multitrade_shorter_hold_001_latest.json`,
`artifacts/reports/structure_v1_failure_modes_btc_eth_sol_001_latest.json`

**Rules:**
1. Same-side entry bursts (≥3 within 6 hours) going **all-loss** are uncommon
   (~5% of such clusters on ETH multitrade; ≪1% on live single-book). Do not
   design filters as if “everyone wrong together” were the dominant mode.
2. **Primary conviction arm** (`clarity_scope=all` on eth_multitrade_v1_1) is a
   frozen transfer from single-book clarity settle. Outer compare: candidate
   stitched Profit Factor ≈4.26 vs live control ≈3.59; book1 wrong@1h 38% vs 42%.
   Evidence class `OUTER_TRANSFER_COMPARE`. **Not a live pack swap** without new
   pack hash, certificate, and explicit user auth.
3. **Shorter-hold arm** (base 4 / addon 8) is `OUTER_COMPARE_CONTAMINATED`
   (hypothesis from failure_modes peek). Marginal PF lift (~3.63 vs 3.59) — do
   **not** promote from this window; clean retest only after
   `POST_MULTITRADE_FREEZE_START` if still desired.
4. Do not combine (2) and (3) in one generation. Do not cut K from “too many
   signals feel wrong.” Keep multitrade measure Profit Factor separate from
   single-book settle when judging readiness.
5. Wrong-way @ 1 hour remains a noise / explanation metric, not a promotion gate.

---

## D-038 — Forward lockbox sealed against silent Finplot / peeks

**Date:** 2026-08-04 · **Status:** ACTIVE · **Evidence:**
`llm2/evidence/lockbox_guard.py`, `tests/test_lockbox_guard.py`

**Rules:**
1. Any evaluation that uses bars on/after `FORWARD_LOCKBOX_START` (2026-05-01) must
   call `require_lockbox_access` and pass `--i-accept-lockbox-contamination`
   (or `LLM2_I_ACCEPT_LOCKBOX_CONTAMINATION=1` for explicit batch tools).
2. **Finplot / interactive charts** need a second opt-in:
   `--i-accept-finplot-lockbox` (or `LLM2_I_ACCEPT_FINPLOT_LOCKBOX=1`) **and**
   contamination accept. Default is report-only with `TRADESIM_NO_PLOT=1`.
3. Authorized peeks always append `artifacts/evidence/peek_log.jsonl`.
4. Wired scripts include `plot_structure_lockbox.py`, concurrent Finplot scripts,
   multitrade lockbox hunts. Outer-fold settle (end ≤ lockbox start) is not gated.
5. Does not re-seal already-peeked calendars; it prevents **new silent** peeks.

---

## D-037 — Expansion sealed lockbox one-shot (direction packs)

**Date:** 2026-08-04 · **Status:** ACTIVE · **Evidence:**
`configs/preregister/structure_v1_expansion_lockbox_final_001.yaml`,
`scripts/run_expansion_lockbox_once.py`,
`artifacts/reports/structure_v1_expansion_settle_20260803T181235Z.json`

**Rules:**
1. Train / freeze expansion **direction** live packs only on bars strictly before
   `FORWARD_LOCKBOX_START` (2026-05-01); model fit before last outer fold start
   (2025-10-01). Lockbox never used for train or multitrade retune.
2. Candidate space for the *pristine* one-shot is settle-PASS pairs that were never
   Finplot/lockbox-opened for charts: BNB, XRP, DOGE, AVAX, DOT, TRX, XLM (direction).
   ETH/SOL/LINK/VET/ADA/BTC already peeeed — excluded from “pristine” claims.
3. Open is **one frozen single-book arm** only (Take Profit 1%, Stop Loss 2%, hold 6,
   max one book). Multi-arm search (`--grid`, K, fib, switch, clarity hunts) is
   refuse-closed (`refuse_expansion_lockbox_multi_arm`).
4. After open, evidence class for that calendar is
   `LOCKBOX_OPENED_CONTAMINATED` — append peeks. **Quotable promotion** remains
   outer-fold settle pooled Profit Factor only
   (`refuse_promotion_from_expansion_lockbox_pf`).
5. Does **not** authorize live deploy, VPS pack install, or ETH multitrade knob changes
   (still D-036 / certificate + user auth).

---

## D-036 — Multitrade lockbox peeks are diagnostic; clean claims after 2026-08-05

**Date:** 2026-08-04 · **Status:** ACTIVE · **Evidence:**
`artifacts/evidence/peek_log.jsonl`,
`configs/preregister/structure_v1_eth_multitrade_v1_1_post_freeze_001.yaml`,
`llm2/evidence/peek_log.py`, `llm2/research_policy.py`

Extends D-035 for concurrent / multitrade knobs (switch book, addon TP, K, clarity
grids on the forward lockbox).

**Rules:**
1. Calendar **2026-05-01 → 2026-08-04** multitrade/lockbox multi-arm work is
   `LOCKBOX_OPENED_CONTAMINATED_DIAGNOSTIC_ONLY` — not parameter promotion.
2. Quotable historical edge remains **outer-fold settle** (and fold-V2 proxy reports
   already stamped as RESEARCH_ONLY where applicable).
3. **Copying** SQLite / reports does **not** re-seal a peeked window
   (`refuse_copy_as_pristine_holdout`).
4. Every peek must be append-logged via `append_peek` / `scripts/log_research_peek.py`.
5. Locked micro-live arm remains `eth_multitrade_v1_1` (K=7, mean_strength, switch=3,
   TP 2.618%, hold 12). Next **real** multitrade parameter claim: prereg first, then
   evaluate only with `window_start >= 2026-08-05` (`POST_MULTITRADE_FREEZE_START`) or
   on outer folds without lockbox ranking. Live micro is a separate evidence class and
   does not re-seal the lockbox.

---

## D-035 — ETH/SOL structure_v1 direction lockbox opened (contaminated)

**Date:** 2026-08-04 · **Status:** ACTIVE · **Evidence:**
`artifacts/reports/structure_v1_lockbox_eth_sol.json`, Finplot run_ids
`…3984260142` (ETH), `…e575ca73ec` (SOL)

User-requested Finplot of the forward lockbox (2026-05-01 → warehouse end
≈2026-08-02) with frozen ETH/SOL direction live packs. Evidence class is
`LOCKBOX_OPENED_CONTAMINATED`. Lockbox Profit Factor ≈2.5 is a sanity chart only —
**not** a promotion / scale / retune gate. Quote ETH/SOL promotion claims from the
outer-fold settle record
(`artifacts/reports/structure_v1_eth_sol_settle_20260803T161346Z.json`: ETH direction
pooled PF≈1.768, SOL direction≈1.858), not from the peeked lockbox.

Any parameter change (max hold, band, Take Profit / Stop Loss, gate) starts a new
generation; the peeked May→Aug window is reused/contaminated for that idea. Fresh
forward evidence is only bars arriving after this inspection under a new freeze.
Live micro on the Virtual Private Server (VPS) is a separate evidence class and does
not re-seal this lockbox.

---

## D-034 — User-authorized micro-live on ln1 / Xxobster7 (MIN_EXCHANGE)

**Date:** 2026-08-03 · **Status:** ACTIVE · **Config:**
`configs/live/structure_v1_lgbm_certificate.yaml` (AUTHORIZED through 2026-08-17),
`/opt/llm2-structure` on `94.156.189.76`, systemd `llm2-structure-micro.service`

User explicitly authorized host + account for live tests. Frozen pack includes Bybit
risk-limit tiers (35) + LightGBM model + indicators slice. First LIVE order succeeded
(`retCode=0`) after hedge-mode `positionIdx` fix (Buy=1 / Sell=2). Sizing remains
MIN_EXCHANGE only — not SCALE. Feature warehouse must be refreshed for new bars;
service decides on bar close.

---

## D-033 — Outer fold geometry V2 closes Oct-2025→lockbox gap; VPS needs live certificate

**Date:** 2026-08-03 · **Status:** ACTIVE · **Config:**
`configs/preregister/structure_v1_fold_extension_001.yaml`,
`llm2/validation/folds.py` (`OUTER_FOLD_RANGES_V2`),
`configs/live/structure_v1_lgbm_certificate.yaml`,
`llm2/live/certificate.py`

Prior nested OOS ended at 2025-10-01 while research bars ran to 2026-04-30 — Finplot
correctly showed no trades after 2025-09-30 because fold 5 did not exist. V2 adds
`["2025-10-01", FORWARD_LOCKBOX_START)`. Prior V1 settles remain labelled fold-geometry V1.

**VPS / xxobster7:** research settle and Finplot never authorize deploy. Certificate stays
`BLOCKED` until user sets `AUTHORIZED` after a frozen live pack with funding + Mark/tier
parity. `refuse_vps_deploy_without_live_certificate` fails closed.

**Equity caveat:** smooth MIN_EXCHANGE wallet curves are not tradable-edge evidence.

---

## D-032 — V2.1 stress/MDD/margin bound; structure_v1 settle earns SHADOW_READY_CANDIDATE

**Date:** 2026-08-03 · **Status:** ACTIVE · **Code:** `llm2/gates/evidence.py`,
`llm2/hunt/runner.py`, `scripts/settle_structure_tier2.py`

Tradesim hunt path now computes moderate stress (2× slippage), baseline/stress MDD, peak
margin utilisation, and liquidation. Pooled PF uses pooled trade PnL (not mean fold PF).
PBO requires a fold-aligned candidate matrix; truncated independent daily stitches are
refused (they produced a spurious PBO=0). PBO UNAVAILABLE does not auto-block overall PASS.

**structure_v1 BTCUSDT 1h fwd_return** settle: overall PASS, tier 3, pooled PF≈1.84.
Readiness remains `RESEARCH_ONLY` / `LIVE_STOP` until user authorises any shadow/live step.
Proxy Tier≥2 on other combos is SCREEN_CANDIDATE only.

---

## D-031 — ABC bounce lockbox prereg + wave-extrema arm; continuation stays closed

**Date:** 2026-08-03 · **Status:** ACTIVE · **Code / config:**
`configs/preregister/abc_bounce_001.yaml`, `llm2/experiments/abc_bounce.py`,
`llm2/diagnostics/abc_factor.py` (`run_abc_factor_study_wave_extrema`),
`refuse_abc_continuation_without_lockbox_prereg`, `refuse_wavetheory_simulator_for_abc`,
`require_warehouse_legs_for_abc`

**Prereg (frozen before lockbox open):** bounce against BC after warehouse A→B→C with
`f` near {0.618, 1.0, 1.618}, hold 6, stop 0.04, leverage 10, evaluation
`forward_lockbox_once`, volatility-matched control mandatory. Failure closes
`abc_bounce_family` — no post-hoc widening of tolerance/targets/hold.

**Wave-extrema arm:** same factor scan on causal-wave peaks/troughs confirmed one bar after
the turn, labelled `abc_wave|*`. Diagnostic only; not a substitute for warehouse legs.

**Policy:** “A and C similar length” continuation remains CLOSED on BTCUSDT 1h/4h unless a
separate lockbox prereg says otherwise. Never quote ABC numbers from the wavetheory private
simulator (D-026). Prefer warehouse legs ratios over hand-drawn A/B/C.

**Checklist:** keep `ABC_RULES_TESTED.md` as the inventory so video extractions are not
mistaken for evidence.

**Lockbox result (first open):** `abc_bounce_BTCUSDT_20260803T130016Z` —
UNDERPOWERED (46 < 50 trades). Bounce PF 0.54 did not beat control PF 0.59; family not
closed solely because the sample floor was not met. Wave-extrema arm:
`abc_wave_extrema_BTCUSDT_20260803T125911Z` — zero FDR survivors on 1h/4h train.

**Hold enforcement:** `family_status=UNDERPOWERED_HOLD` in
`abc_bounce_001_family_status.json`; `refuse_abc_bounce_reopen_while_underpowered` blocks
a second run until the same **parameter digest** projects ≥50 sequential trades.
`require_lockbox_prereg_frozen` gates any lockbox open on frozen exits + matched control.
`refuse_abc_video_claim_as_evidence` keeps video extractions out of the evidence column.

---

## D-030 — ABC distance-factor similarity: continuation fails; bounce is not a free trade

**Date:** 2026-08-03 · **Status:** ACTIVE · **Evidence:**
`artifacts/reports/abc_factor/abc_factor_BTCUSDT_20260803T124220Z.md`

Theory: three confirmed swings A→B→C, factor `f = |BC|/|AB|`, historically similar `f`
should share forward behaviour. Inventory of prior ABC rules: `ABC_RULES_TESTED.md`.

**Result (BTCUSDT 1h/4h, train before lockbox):** k-NN similarity and linear correlation of
`f` with forward return do **not** survive FDR. Classical factor bins (0.618 / 1.0 / 1.618)
do not outperform placebo bins as unsigned predictors. The FDR survivors are
`bc_continuation|*` arms with **negative** mean signed return: after C confirms, price tends
to move *against* the BC leg (short-horizon bounce), not continue it. That is the opposite
of the “equal legs / golden-ratio extension continues” story.

**Consequence:** do not promote a BC-continuation rule. Do not invert the bounce into a
live rule on this same window (selection). Bounce hypothesis moved to lockbox prereg
`abc_bounce_001` (D-031). Stage 2 from the train scan alone is not warranted.

---

## D-029 — Prefer raw returns when the wave channel disagrees

**Date:** 2026-08-03 · **Status:** ACTIVE · **Code:** `prefer_raw_return_when_disagreement`

A lead that exists only after band-pass filtering and vanishes on unfiltered returns is
the filter talking (D-020 class). When wave and raw-return arms disagree, believe the
returns. Tier B of the wave panel stays a closed five-transform list; do not expand it
after seeing a scan.

**Same-series transforms are not external leads.** RSI / realised vol / signed volume /
run length / ATR-displacement computed from BTCUSDT OHLCV must not enter the external
lead panel against BTCUSDT — they are deterministic functions of the predictand and
manufacture lag artefacts. They remain valid inside own-series metrics (`wavemetrics`,
`waveevent`).

---

## D-028 — `cryptodb/market.sqlite` is not a causal feature source until timing is pinned

**Date:** 2026-08-03 · **Status:** ACTIVE · **Evidence:** `artifacts/reports/wave001/warehouse_leakage_audit.json`

The warehouse stores only a calendar `date` string, blends vendors without a documented
cutover, and has no knowable-at instant. Audit status: BLOCKER. Do not feed same-day
cryptodb values into WAVE001 or any causal feature until per-source day-boundary and
publication lag are recorded.

Research warehouses that **did** pass confirmation-time / integrity checks for WAVE001:
`market_ohlcv.sqlite`, `indicators.sqlite` (kind=`high`/`low`, not `SH`/`SL`),
`binance_funding.sqlite`, plus shared `leakage` prefix-invariance on `build_causal_metrics`.

---

## D-027 — Lead p-values under single-lag-after-selection null are INVALIDATED

**Date:** 2026-08-03 · **Status:** ACTIVE · **Code:** `circular_shift_max_lag_null`

`phase_lead_scan` (and the first WAVE001 panel scan) selected the winning lag by maximising
absolute correlation over up to 48 lags, then tested that winner against a circular-shift
null at the *single* winning lag. That makes every p-value optimistic by roughly the
selection factor. The null must take its own maximum over the same lag range (same pattern
as `dominant_period` across frequency bins).

**Consequence:** every lead p-value computed before this fix is `INVALIDATED` and must be
recomputed before quoting. Re-runs stamp `null=max_over_lags`.

---

## D-026 — The wavetheory private backtest is void; rebuild on warehouse + tradesim

**Date:** 2026-08-03 · **Status:** ACTIVE · **Path:** `C:\projects\wavetheory`

Two independent fatal defects: (1) `fractal_pivots` publishes a pivot at the centre bar
rather than at confirmation (`pivot_wing=5` → five-bar look-ahead into entry/TP/SL);
(2) `simulate_long_trades` skips the entry bar for stop/target checks (EXEC-010 immunity)
and charges a flat 0.05% with no funding, slippage, margin or liquidation.

**Consequence:** no number from that simulator is quotable. The public skeleton of the
method (casser le top / casser le bas) is re-tested in LLM2 via confirmed-swing warehouse
boundaries and tradesim only. A negative result closes the public skeleton, not the paid
formation.

---

## D-025 — Research methodology policies are machine-enforceable

**Date:** 2026-08-03 · **Status:** ACTIVE · **Code:** `llm2/research_policy.py`

Five standing rules are now functions that raise `PolicyError`, not prose:

1. **Placebo arm for every level claim** (round numbers, pivots, VWAP, MAs as support).
2. **Confirmation-time audit for warehouse-backed feature spaces** — a green leakage report
   is insufficient. Bound today: `macro_v1`, `structure_v1`, `crosspair_v1`, `xs_v1`.
   `build_space` calls `require_warehouse_audit_bound` so an unbound warehouse space fails
   before it can produce a number.
3. **Matched control for every event study** (volatility / regime matched, not uniform random).
4. **Estimator self-control** — run the estimator against itself before believing a
   cross-series finding.
5. **Do not invert inspected non-significant structure signs** without a lockbox preregistration.

The autonomy sweep's per-combo `try/except` now calls `is_critical_failure` and **halts**
on parquet / conformance / botsgeneral / gate failures instead of logging and continuing.

---

## D-024 — Do not invert the non-significant structure signs

**Date:** 2026-08-03 · **Status:** ACTIVE · **Evidence:** D-017

Higher highs were mildly negative and lower highs mildly positive on the training window.
Neither survived FDR. Fitting a contrarian rule to that pattern after seeing it is selection
on the same data. `refuse_structure_sign_inversion` blocks it unless a fresh hypothesis has
been preregistered for the forward lockbox.

---

## D-023 — Shared causal warehouse beats per-strategy pivots

**Date:** 2026-08-03 · **Status:** ACTIVE

Swing structure is the most leakage-prone indicator family, but the correct response is
**not** for every strategy to recompute its own pivots. Re-implementing confirmation logic
in each strategy multiplies the chance of an off-by-one, and a private pivot series cannot
be audited once. The warehouse already separates `pivot_ts_ms` from `confirm_ts_ms` and
passes a bar-by-bar confirmation-time audit. Strategies must:

- consume confirmed structure only (never treat `pivot_ts` as knowable at the pivot);
- share one confirmation rule;
- carry a confirmation-time regression test for every warehouse-backed feature space.

Making your own pivots does not reduce leakage if you make the same mistake; it removes the
single place where the mistake can be caught.

---

## D-022 — Transfer-entropy findings require three falsification controls before modelling

**Date:** 2026-08-03 · **Status:** ACTIVE · **Code:** `llm2/diagnostics/te_falsify.py`
**Evidence:** `artifacts/reports/diagnostics/te_falsify_BTCUSDT_1h.json`

Linear correlation found nothing; transfer entropy found something. Before any nonlinear
model is fitted, every TE survivor must pass: (1) block shuffle of the source must *kill*
the finding, (2) volatility standardisation must *preserve* it, (3) sign-only recoding must
*preserve* it.

**Result on BTCUSDT 1h, 31 external series:** 0 of 31 survive all three. Ten had a
significant baseline; nine of those still looked alive after vol-standardisation alone; only
one (EURJPY) was killed by the block shuffle in the right direction; **none** survived
sign-only. Effect sizes are ~0.002 nats. The nonlinear cross-asset direction is closed for
modelling: what TE was measuring was not directional information flow.

---

## D-021 — Pulse continuation is closed; the effect was drift, not response

**Date:** 2026-08-03 · **Status:** ACTIVE · **Evidence:** `diag001_pulse_continuation_BTCUSDT_1h`,
`artifacts/reports/pulse_continuation_result.json`, tradesim 1.0.0 fixtures `9a037b290c8a`,
conformance 62/62

The only diagnostic survivor with an effect size meaningfully above the round trip — 87 bps
of 96-bar forward return after an upward three-sigma pulse against 16 bps of cost — does not
survive execution. Pooled profit factor 1.067 against a 1.20 gate, two of five folds
negative, so the 80 percent positive-fold requirement fails as well.

**The control is the finding.** A volatility-matched random entry, same count, same 96-bar
hold, same costs, returned 1.049. The pulse arm beat it by 0.018 of profit factor on 92
trades against 82. What the diagnostics measured was very largely the return to holding
BTCUSDT long for four days in a volatile regime. The down-pulse arm at 0.779 does not rescue
the asymmetry story: being short a structurally rising asset loses money whether or not a
pulse preceded it.

Charging funding at actual historical settlements moved pooled profit factor from 1.118 to
1.067 — over a four-day hold funding cost 4.59 against 5.06 in fees. It had been silently
absent from the first run.

**Consequence:** the family is closed exactly as the preregistration committed in advance.
Do not tune the sigma threshold, hold length, lookback or stop in response. Any event-study
effect from here on must be reported against a matched-control arm before it is called an
effect; `llm2/experiments/pulse_continuation.py::volatility_matched_control` is the pattern.

---

## D-020 — A cross-asset wave lead must be measured through one common filter

**Date:** 2026-08-03 · **Status:** ACTIVE · **Evidence:** `tests/test_wave.py`

The first cross-asset wave scan reported "ETHUSDT leads BTCUSDT by 4 bars, r = 0.48" with 24
of 24 pairs surviving false-discovery control. All of it was an artefact of the estimator.

A forward-only band-pass has a group delay set by its centre frequency: measured here, 3
bars at a 7.1-bar period and 7 bars at 15.3. Each asset had been filtered at *its own*
fitted period, so BTCUSDT's wave was delayed 4 bars more than ETHUSDT's, and the scan
reported that difference as a lead. The proof is a synthetic control — BTCUSDT filtered at
15.3 against **the same BTCUSDT series** filtered at 7.1 shows an apparent lead of 4 bars at
r = 0.57, and a series cannot lead itself.

Refiltering every series at one common period, 24 of 26 pairs then place their maximum at
lag 0: the markets co-move and none of them leads. This agrees with the raw-return lead-lag
scan, which found zero survivors, and with the fact that ETHUSDT-to-BTCUSDT return lead
correlations run between -0.013 and +0.008 against a contemporaneous +0.84.

**Consequence:** `phase_lead_scan` takes a `common_period` and the price series needed to
refilter, records `filters_matched` and `corr_lag0`, and marks any pair whose best lagged
correlation does not exceed its contemporaneous one as co-moving rather than leading. The
self-control is bound as a regression test. More generally: when a result comes out of a
filter, run the filter against itself before believing it.

---

## D-019 — The dollar/commodity complex is one hypothesis, and it is negative

**Date:** 2026-08-03 · **Status:** ACTIVE · **Evidence:** `llm2/diagnostics/dollarfactor.py`

Thirty-one external series produced zero linear survivors and one correlated factor block.
Testing them separately was never 31 hypotheses: a single principal component explains 46
percent of the variance of the 13-series dollar and commodity block, so most of that
multiplicity budget was spent on redundancy.

Collapsed to one fold-fitted factor and asked once, the answer is negative and clean. The
factor's correlation with BTCUSDT forward returns is -0.009 at 1h over 6 bars (p = 0.16) and
+0.010 at 4h — the sign flips between timeframes, which is what noise looks like. R-squared
is 0.009 percent.

**Consequence:** the dollar/commodity complex is closed as a directional input for crypto.
Do not add further external series; the marginal series is worth less than the multiplicity
penalty it carries. Loadings are fitted inside each training fold, never on full history.

---

## D-018 — A silently-caught dependency error made a sweep report success while doing nothing

**Date:** 2026-08-03 · **Status:** ACTIVE

An Application Control policy on this machine blocked pyarrow's native library. pandas
selects pyarrow before fastparquet and does not fall back when the module imports but is
broken, so `write_fold_parquet` raised on every call. The autonomy sweep caught the
exception per combo, logged a traceback and continued, so a run that appeared healthy
completed 131 combos having produced no research at all — and the failing step was the
physical train/test split, the very thing that guarantees features are computed separately
per split.

Two fixes. `llm2/data/splits.py::parquet_engine` chooses an engine once by attempting a real
round trip, and the sweep calls it before the first combo so a broken environment stops the
run instead of decorating it. Separately, `GATE_REVISION` now prefixes every generation
identifier: the 148 GATE_VOID generations were still marked `completed` in the research
database, so the resume check would have skipped precisely the reopened targets the sweep
existed to re-test.

**Consequence:** any change that invalidates prior results must bump `GATE_REVISION`. A
per-item `try/except` around a step that is required for correctness must re-raise or
pre-flight; logging and continuing turns a hard failure into a false negative.

---

## D-017 — Classical price structure is descriptively closed for BTCUSDT

**Date:** 2026-08-03 · **Status:** ACTIVE · **Evidence:** `diag_BTCUSDT_1h_20260803T090059Z`,
`diag_BTCUSDT_4h_20260803T090220Z`

Four structural claims were measured against the confirmed-swing warehouse, on the training
window only, with overlap-aware standard errors and false-discovery-rate control. **0 of 70
effects survive at either timeframe.** Point estimates are single-digit basis points against
a round-trip cost of 16 bps, and several carry the opposite sign to the claim.

The Fibonacci arm is the one worth keeping as a template. Testing "price near the 0.618 line
bounces" on its own cannot separate the ratio from the mere fact of sitting inside a recent
range, so each real ratio was paired with arbitrary placebo ratios computed from the same
confirmed anchors, on the same bars, through the same code. The Fibonacci arm did not
separate from the placebo arm at either timeframe, and at 1h the placebos were slightly
larger. Whatever weak effect exists near a retracement level belongs to the range, not to
the ratio.

**What this does and does not close.** Closed: these objects as standalone directional
predictors on BTCUSDT 1h/4h. Not closed: their use as *conditioning* or *filtering* inputs
inside a hunt, which is why `structure_v1` is registered rather than frozen out. Any future
claim that a Fibonacci level "works" must carry a placebo arm or it is not evidence.

**Consequence:** `llm2/diagnostics/marketstructure.py`; `structure_v1` available to the hunt
but no structure-only hypothesis may be preregistered without new evidence.

---

## D-016 — A timeframe lookup must never guess a bar length

**Date:** 2026-08-03 · **Status:** ACTIVE

`TF_MS` carried no `1w` entry and `align_multi_timeframe` defaulted to one hour, declaring a
weekly bar complete one hour after its open and exposing 6 days 23 hours of future in every
weekly context column. The shared leakage audit reported PASS throughout, because truncating
the bar frame does not truncate the warehouse the values are read from — the same blind spot
that hid the `macro_v1` defect (D-014).

This is now the third look-ahead defect in this codebase to arrive through a *convenience
default* rather than through wrong logic. Completion-time arithmetic gets no defaults:
`llm2.data.indicators.timeframe_ms` raises on an unknown timeframe.

Prefix-invariance is a real test of the transform layer and a vacuous one for values read
from a database. Warehouse-backed feature spaces need a direct confirmation-time audit bound
as a test; a green leakage report is not evidence for them.

**Consequence:** `llm2/paths.py` `TF_MS["1w"]`; `timeframe_ms`;
`tests/test_structure_causality.py`; note in `llm2/features/guard.py`.

---

## D-015 — Cross-asset linear lead-lag is closed for BTCUSDT; nonlinear residual is below cost

**Date:** 2026-08-03 · **Status:** ACTIVE · **Evidence:** `diag_BTCUSDT_1h_20260803T083613Z`,
`diag_BTCUSDT_4h_20260803T083839Z`

Zero of 228 tradeable lead-lag pairings survive false-discovery-rate control at 1h, and zero
at 4h, across 31 external series (foreign exchange, metals, energy, equity indices, the
yield curve, stablecoin supply, sentiment) times four predictor windows times three
horizons. Contemporaneous correlations reach 0.26 and are explicitly labelled untradeable.
Seasonality (hour, weekday, Tokyo/London/New York sessions, funding hours, turn of month)
is a clean zero. Joint DXY × XAUUSD trend-state confluence is zero. Pre-event displacement
across the panel is zero.

Unlike D-010 this is an earned negative: the machinery is bound to tests that recover
planted one-bar leads out of a 30-series decoy panel and reject unrelated persistent series.

The one non-null cross-asset result, transfer entropy at 1h, is retained as a weak open
question rather than a finding: 0.0025 nats against a target entropy of 1.386 (0.18%),
concentrated in ~5 effectively independent series, absent at 4h.

**Consequence:** do not build further cross-asset *linear* feature spaces for BTCUSDT
without new evidence. Any revisit must be nonlinear, factor-based rather than 30 separate
series, and must clear the cost hurdle in its own preregistration.

---

## D-014 — Warehouse timestamps are bar OPEN time; external series align on completion

**Date:** 2026-08-03 · **Status:** ACTIVE

`market_ohlcv.ts_ms` is the bar's opening instant, so a bar stamped `T` on timeframe `tf`
is knowable only at `T + tf`. `macro_v1` forward-filled daily macro bars across the hours of
their own day, giving the model up to 23 hours of look-ahead on DXY, US10Y, US02Y, VIX, SPX
and FNG. Confirmed directly: at 01:00 on 2024-06-05 it served DXY = 104.241, the close of
all of 2024-06-05.

Rules now in force:

- Every external series is indexed by completion instant (`ts_ms + timeframe`) plus an
  explicit per-source publication lag before any alignment.
- Alignment is as-of (`merge_asof`, backward), never `reindex(method="ffill")`.
- Every lookup pins `(symbol, source, timeframe)`. Selecting on symbol alone silently
  interleaves vendors for `EURUSD`, `XAUUSD`, `USDJPY`, `WTI`, `COPPER` and others.
- `is_complete` is recomputed, not trusted: the in-progress daily bar is flagged complete.
- Aligned series carry an `age_sec` column, because a constant run in a foreign exchange
  series means "closed", not "unchanged".
- Series whose *level* is the signal (yields, VIX, term spread, sentiment, funding rate)
  are marked `stationary_level` and are not log-differenced.

The shared `leakage` prefix-invariance guard structurally cannot catch this class, because
it truncates the OHLCV passed into the builder while the macro series is loaded from the
database inside it. Bound to a direct integration test instead.

**Consequence:** `llm2/data/macro.py`, `llm2/features/macro_v1.py`,
`llm2/diagnostics/crossasset.py`, `tests/test_macro_causality.py`.

---

## D-013 — The Stage-B predictability gate was unconditionally false; 148 generations are GATE_VOID

**Date:** 2026-08-03 · **Status:** ACTIVE · **Retracts:** D-010

`audit_predictability` probed with `HistoricalMeanBaseline`, which ignores `X` and returns
the mean of `y`. Its `r2_like` was therefore `1 - var(y)/var(y)`, i.e. exactly 0 (about
1e-9 after the denominator epsilon), while the pass condition demanded `> 1e-6`. The gate
could not return True for any data, any symbol, any target, any feature space.

That single boolean was the tier ceiling for the entire project. `runner.py` set
`screen_pass = bool(pred_report.passed)`, `_tier_from_gates` returns 0 whenever
`screen_pass` is false, and `autonomy_sweep._should_escalate` refuses to escalate without
it. The screen runs `run_backtest=False`. Consequently **no trial could exceed tier 0 and
the 108-combo and 162-combo sweeps never ran a single tradesim backtest.**

A second defect compounded it: the probe was scored with `model.predict(X)` on the same
`X` it was fitted on, so even a real learner would have been graded in-sample.

Consequences:

- All 148 generations and 603 trials in `artifacts/sqlite/research.sqlite` predating
  2026-08-03 are marked **GATE_VOID**. They are not quotable as negative evidence. They
  do not falsify anything. The question they were meant to answer is simply unanswered.
- The gate is now a permutation test: real learners (ridge with train-fitted
  standardisation, and gradient boosting) fitted on a chronological training slice and
  scored out-of-sample against a training-mean baseline, compared against the same
  pipeline run on surrogate labels. Pass is an add-one empirical p-value at or below
  alpha.
- Draw counts are derived from alpha via `required_surrogates_per_family`. If the draw
  count cannot express alpha the report fails with reason `underpowered` rather than
  reporting a negative, because a structural inability to reject is what caused D-013.
- `require_predictability_gate_discriminates` is a release gate: known signal must pass
  and pure noise must fail. Bound to `tests/test_release_gates.py` and
  `tests/test_predictability_gate.py`.

**Consequence:** `llm2/audit/predictability.py`, `llm2/audit/release_gates.py`,
`llm2/hunt/runner.py`, `scripts/autonomy_sweep.py`.

---

## D-001 — Operational leverage is minimised, not maximised

**Date:** 2026-08-02 · **Status:** ACTIVE · **Supersedes:** the project's opening request
to deploy at "the smallest position value and highest leverage based on TP and SL".

Trading Bot Research Standard v2.1 requires the *lowest* operational leverage that clears
margin once an edge is proven. Leverage is a survival parameter, not a return parameter:
raising it cannot turn a Profit Factor below 1.0 into a profitable system, and it moves
the liquidation price toward the stop, converting a survivable losing streak into an
account-ending one.

Highest-leverage sizing therefore stays out of the code path. If it is still wanted later
it needs a dated override entry below this one, written after an edge exists, not before.

**Consequence:** no sizing code reads a "max leverage" parameter.

---

## D-002 — Non-directional targets are searched first

**Date:** 2026-08-02 · **Status:** ACTIVE

LLM1 spent 24 generations falsifying first-touch direction on BTC, ETH and SOL and found
nothing. Re-searching direction with a new feature set is the same experiment with a new
label on it.

The sweep therefore orders targets `vol_ratio`, `volatility`, `xs_rank`, `quantile`,
`fwd_return`, `direction`. Direction and forward return run last, and only to keep a
negative control in the ledger.

**Consequence:** `scripts/autonomy_sweep.py::TARGETS` ordering is load-bearing.

---

## D-003 — Proxy Profit Factor is a filter, never evidence

**Date:** 2026-08-02 · **Status:** ACTIVE

gen_008 screened at proxy PF 1.13 and came back 0.79 under tradesim. The proxy ignores
fills, fees, funding and the intrabar path, so it is systematically optimistic.

A proxy number may decide whether to spend compute on a tradesim re-run. It may not appear
in any result claim, and it may not by itself raise a tier above 1.

**Consequence:** the sweep escalates at screen tier >= 1 but only alerts on a
tradesim-backed tier >= 2.

---

## D-004 — A target's family decides how it may be scored

**Date:** 2026-08-02 · **Status:** ACTIVE

The first run of the reprioritised sweep reported a Tier-2 candidate at Profit Factor
2988, and a *constant* predictor at PF 2.0, on the `vol_ratio` target. The proxy was
computing `side * y - cost`, which is only a P&L when `y` is a forward return. A
volatility target is positive by construction, so every bar became a winning long.

Targets now carry a family, and the family decides both the deadband and the metric:

| Family | Targets | Side from | Scored on |
| --- | --- | --- | --- |
| return | `fwd_return`, `quantile` | prediction vs cost hurdle | realized forward return |
| directional | `direction` | prediction vs ±0.10 | realized forward return |
| rank | `xs_rank` | prediction vs 0.5 ± 0.05 | realized forward return |
| magnitude | `volatility`, `vol_ratio` | *no side* | forecast skill vs train-mean |

Proxy P&L is always denominated in the realized forward return, whatever the model was
trained to predict. A magnitude target never reaches the signal translator or tradesim,
and is capped at tier 1: a volatility forecast is an input to sizing or regime filtering,
never a standalone strategy.

**Consequence:** `llm2/hunt/runner.py::_TARGET_FAMILY`; regression test in
`tests/test_target_family_routing.py`.

---

## D-005 — A failed surrogate challenge caps the tier at zero

**Date:** 2026-08-02 · **Status:** ACTIVE

Tier was previously computed from the profit gates alone, and the surrogate screen only
controlled the difference between tier 0 and tier 1. A result that the surrogate challenge
could not distinguish from randomised data could therefore still reach tier 2 and
interrupt the operator.

Skill is now measured against the train-mean baseline — unit-free, and valid for targets
that are not centred on zero — and the real fit must beat its own surrogate.

**Consequence:** `_tier_from_gates` returns 0 whenever `screen_pass` is false.

---

## D-007 — Cross-sectional rank uses a relative-value feature space

**Date:** 2026-08-02 · **Status:** ACTIVE

Predicting `xs_rank` from single-symbol open-high-low-close-volume features is a
geometry mismatch. The hunt pairs `xs_rank` with `xs_v1` (panel ranks, z-scores,
relative momentum, breadth) and `crosspair_v1`; `ohlcv_v1` is kept only as a
mismatch control. `xs_v1` passed the shared leakage audit with zero
`LEAKAGE_POTENTIAL` columns.

**Consequence:** `scripts/autonomy_sweep.py::_spaces_for`; `llm2/features/xs_v1.py`.

---

## D-008 — Forecast skill and Profit Factor are separate fields

**Date:** 2026-08-02 · **Status:** ACTIVE

A magnitude target's skill ratio (train-mean Mean Absolute Error / model Mean
Absolute Error) must not be written into `pooled_pf` or graded against the frozen
Profit Factor threshold 1.20. `evaluate_v21_gates` takes `metric_kind` of
`profit_factor` or `forecast_skill` and populates `pooled_skill` for the latter
while leaving `pooled_pf` as `UNKNOWN` / not applicable.

**Consequence:** `llm2/gates/v21.py`; hunt runner; `tests/test_gate_metric_kind.py`.

---

## D-009 — Constant-predictor invariant (release gate)

**Date:** 2026-08-02 · **Status:** ACTIVE

A constant predictor must score at or below 1.0 on every target family. This is the
standing guard against the units-bug class that produced the false Tier-2 at
Profit Factor 2988. It now runs as a fail-closed release gate at the start of every
nested hunt and autonomy sweep.

**Consequence:** `llm2/audit/release_gates.py`; `tests/test_constant_predictor_invariant.py`.

---

## D-011 — Vol-as-filter experiment (bounded); skip-more, never side from vol

**Date:** 2026-08-02 · **Status:** ACTIVE

Decision: run preregistered volatility-as-filter experiments rather than stop all
compute after the non-directional NO-GO. The volatility model may only skip
entries. It must never emit long/short, and high volatility must not increase
leverage or size.

**Consequence:** `llm2/experiments/vol_filter.py`;
`predictions_to_signals(..., target_family="magnitude")` raises.

---

## D-012 — Vol-filter grid frozen; entry rules may change, percentiles may not

**Date:** 2026-08-02 · **Status:** ACTIVE

After out-of-sample inspection of `volfilter_001`, the filter specification is
frozen: name `skip_top_quartile_predicted_vol`, percentile **75**. Code refuses
any other percentile (`FROZEN_VOL_FILTER_PERCENTILE`). Further work may only
preregister a *different entry rule* and re-test the same skip (e.g.
`volfilter_002` mean-reversion).

Beating always-on while both arms have Profit Factor &lt; 1 is a **methodology
win**, not a strategy candidate. Readiness stays `RESEARCH_ONLY`. No Finplot /
live path from vol-filter results alone.

**Consequence:** `validate_vol_filter_prereg`; `volfilter_001.yaml` status
`FROZEN`; `volfilter_002.yaml` for mean-reversion.

---

## D-010 — Non-directional NO-GO; freeze direction and forward return

**Date:** 2026-08-02 · **Status:** RETRACTED 2026-08-03 by D-013

~~The non-directional block (vol_ratio, volatility, xs_rank including matched xs_v1)
finished at max Tier 0 with `predictability_passed=false` across the board. That is
a stronger negative than LLM1's direction-only falsification.~~

**Retracted.** The `predictability_passed=false` this rested on was returned
unconditionally by a broken gate, not measured from the data. The block was never
tested. `fwd_return` and `direction` return to the active candidate space and
`FROZEN_TARGETS` is empty.

The one part that survives: skill above 1 with a failed Stage-B audit still must not
escalate to tradesim — now that a failed audit carries information.

**Consequence:** `scripts/autonomy_sweep.py` `ACTIVE_TARGETS` / `FROZEN_TARGETS`;
go/no-go line in `CURRENT_STATE.md`.

---

## D-006 — Conformance is read from the checker's report, not from process state

**Date:** 2026-08-02 · **Status:** ACTIVE

`llm2/backtest/conformance.py` ran the checker in a subprocess and then read
`tradesim.conformance.stamp.last_stamp()` in the parent. That recorder is process-local,
so the parent always saw `None` and every backtest was treated as unstamped.

The wrapper now reads the checker's `--json` report and replays the stamp into this
process with `record_stamp`, so `assert_quotable` sees the real verdict.

**Consequence:** see also the cross-drive checker fix recorded in `CURRENT_STATE.md`.
