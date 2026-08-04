# LLM2 Decisions

Standing decisions. Each one is here because reversing it silently would invalidate
results, so a reversal needs an explicit, dated entry rather than a code change.

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
