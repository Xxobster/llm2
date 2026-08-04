# ABC / wave-structure rules — tested vs untested

Updated: 2026-08-03

This is the inventory of A–B–C / impulse–correction / Fibonacci claims that have touched
this stack. **Extraction is not a test.** Only rows with a measured result under
false-discovery-rate control (or an explicit void) count as tested. Use this file as the
checklist so video extractions are never mistaken for evidence.

## Already tested (measured)

| Claim | Where | Result |
|---|---|---|
| Structure label (HH/HL/LH/LL) predicts direction | LLM2 `marketstructure.structure_label_effect` · D-017 | **Negative** — 0/24 survive FDR |
| Impulse continues / correction reverts | same · `leg\|impulse_*` / `leg\|correction_*` | **Negative** |
| Fibonacci retracements are special S/R vs placebo ratios | `fibonacci_placebo_test` · D-017 | **Negative** — 0/22; placebos often larger |
| Confirmed support/resistance produces bounces | `support_resistance_effect` | **Negative** — 0/8 |
| Cross-asset structure confluence | `structure_confluence` | **Negative** — 0/16 |
| Break of swing/channel boundary → continuation (“casser le top/bas”) | WAVE001 `structurebreak` | **Mostly negative**; one FDR survivor has **wrong sign** |
| Pullback 25–78% of impulse then long (wavetheory formalisation) | `wavetheory` `wave_strategy.py` | Reported PF ~0.65–0.75 but **VOID (D-026)** — look-ahead pivots + entry-bar immunity; not quotable. **Never revive for ABC numbers.** |
| A–B / B–C **distance factor** similarity (`\|BC\|/\|AB\|`) on warehouse legs | LLM2 `abc_factor` · D-030 · `abc_factor_BTCUSDT_20260803T124220Z` | **Continuation claim CLOSED** on BTCUSDT 1h/4h train. k-NN / linear factor correlation fail FDR. FDR survivors are *negative* BC-continuation (bounce). |
| **A and C similar length → continuation** | same (equal-leg / factor≈1.0 buckets) · D-030 | **CLOSED** for continuation on BTCUSDT 1h/4h unless a fresh lockbox prereg says otherwise |
| ABC bounce against BC near {0.618, 1.0, 1.618} | `abc_bounce_001` prereg · lockbox once · D-031 · `abc_bounce_BTCUSDT_20260803T130016Z` | **UNDERPOWERED** — 46 trades (<50 floor); bounce PF 0.54 vs vol-matched control PF 0.59. Family not closed on underpowered evidence; do not lower the floor or retune. |
| Same factor scan on **causal-wave extrema** (separate arm) | `abc_wave|*` · `abc_wave_extrema_BTCUSDT_20260803T125911Z` · D-031 | **0/60 (1h) and 0/30 (4h)** FDR survivors. Diagnostic only — does not revive warehouse continuation/bounce claims. |

## Extracted from Wave Trading videos — **not formally tested**

Source: `C:\projects\wavetheory\reports\` (one-off extractions; creator says public material ≈ 30% of method).

| Claim | Notes |
|---|---|
| Corrective wave = ABC or running flat; impulse = 5-wave | Taxonomy only |
| **A and C similar in length**; B retraces prior impulse without exceeding its start | Classical equality — **continuation CLOSED** on warehouse factor scan (D-030); bounce lockbox is a separate claim |
| Running flat: break of top validates; break of bottom invalidates | Partial overlap with structure-break study (negative) |
| Flat / running flat / contracting subtypes | Untested |
| Fib 38.2 / 50 / 61.8 / 78.6 as entry or take-profit | Covered by Fib placebo → negative |
| No indicators for structure; trade the timeframe of the objective; break-even then trail | Process rules, not edge tests |

## Standing policy (machine-enforced)

- Prefer warehouse `indicators.legs` ratios over hand-drawn A/B/C (`require_warehouse_legs_for_abc`).
- Refuse wavetheory private simulator paths for ABC evidence (`refuse_wavetheory_simulator_for_abc`, D-026).
- Refuse ABC continuation promotion without lockbox prereg (`refuse_abc_continuation_without_lockbox_prereg`).
- Bounce family is **UNDERPOWERED_HOLD** — no retune; second one-shot only at ≥50 projected trades (`refuse_abc_bounce_reopen_while_underpowered`).
- Any lockbox open: freeze exits + matched control first (`require_lockbox_prereg_frozen`).
- Video / extraction notes are not evidence (`refuse_abc_video_claim_as_evidence`); this file is the checklist.

## Explicitly still missing

- Labeled A/B/C wave counter (Elliott count)
- Running-flat detector (subtype taxonomy)

## Method used for the factor study

- **Primary geometry:** consecutive confirmed warehouse swings chained by `legs`.
- **Secondary arm:** causal-wave peaks/troughs confirmed one bar after the turn (`abc_wave|*`).
- **Factor:** `f = |C−B| / |B−A|`, knowable only at confirmation of C.
- **Controls:** placebo factor bins; shuffled-factor k-nearest-neighbours; FDR; lockbox bounce uses volatility-matched random.
- **Window:** factor scans on training data only; bounce tradesim on forward lockbox once.
