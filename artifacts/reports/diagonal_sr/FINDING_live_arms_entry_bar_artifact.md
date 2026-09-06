# FINDING: both live diagonal S/R arms lose their edge once the stop clears single-bar noise

**Date:** 2026-08-27
**Class:** report-and-stop (execution realism), per `TRADING_BOT_RESEARCH_STANDARD_V2`
**Affects:** `llm2-dsr-eth-bu-1h` and `llm2-dsr-sol-bu-1h`, live on `Xxobster4` / `94.156.189.76`
**Effect on readiness:** invalidates inherited readiness for both arms. Cannot promote anything.

## What was already frozen

| | ETHUSDT `bounce_upper` 1h | SOLUSDT `bounce_upper` 1h |
|---|---|---|
| bracket | fixed TP 1.5% / SL 1.0% | fixed TP 1.5% / SL 1.0% |
| stitched outer out-of-sample trades | 503 | 490 |
| profit factor | 1.352 | 1.965 |
| annualised Sharpe | 1.389 | 3.020 |
| positive folds | 6/6 | 6/6 |
| **entry-bar exit rate** | **0.260** | **0.469** |
| average hold | 3.46 bars | 1.85 bars |
| preregistered entry-bar cap | 0.35 | 0.35 |

The Solana arm's entry-bar exit rate of 0.469 **breaches its own preregistered cap
of 0.35** in `configs/preregister/diagonal_sr_nested_settle_001.yaml`. 230 of its
490 trades were decided inside the candle that filled them. It should not have
cleared the settle gate.

## The signature

Across each arm's six outer folds, profit factor tracks entry-bar exit rate at
**+0.771 Spearman** for both symbols. The Solana fold 0 shows it plainly: entry-bar
rate 0.727, average hold 0.62 bars, profit factor 4.185. As the entry-bar rate
declines across later folds, profit factor declines with it.

This matches what edge lab hunt 002 measured independently across 10,269 arms: a
stop tight enough to sit inside a single candle's range inflates profit factor, and
widening it drives profit factor toward 1.0 monotonically (median profit factor
1.153 at 1.0x Average True Range, 1.065 at 1.5x, 1.039 at 2.0x).

## The decisive test

`scripts/diag_live_arms_atr_rescore.py` re-scored the **same events**, on the
**same outer out-of-sample folds**, with the **same limit entry prices**, changing
only the bracket: from fixed 1.5%/1.0% to a stop scaled by Average True Range,
holding reward-to-risk at 1.5 so the geometry that made the live pack attractive is
unchanged.

### ETHUSDT (live profit factor 1.352)

| ATR stop multiple | mean stop | n | profit factor | Sharpe | entry-bar rate | hold |
|---|---|---|---|---|---|---|
| 1.0 | 0.97% | 503 | 1.097 | 0.42 | 0.290 | 2.90 |
| 1.5 | 1.44% | 497 | **0.944** | −0.25 | 0.129 | 4.71 |
| 2.0 | 1.85% | 495 | **0.886** | −0.49 | 0.063 | 5.88 |
| 2.5 | 2.19% | 494 | **0.827** | −0.76 | 0.045 | 6.35 |
| 3.0 | 2.45% | 494 | **0.849** | −0.65 | 0.030 | 6.74 |

### SOLUSDT (live profit factor 1.965)

| ATR stop multiple | mean stop | n | profit factor | Sharpe | entry-bar rate | hold |
|---|---|---|---|---|---|---|
| 1.0 | 1.41% | 483 | 1.025 | 0.11 | 0.199 | 3.21 |
| 1.5 | 2.00% | 477 | **0.940** | −0.25 | 0.065 | 5.04 |
| 2.0 | 2.44% | 474 | **0.932** | −0.29 | 0.032 | 5.93 |
| 2.5 | 2.71% | 474 | **0.908** | −0.38 | 0.030 | 6.19 |
| 3.0 | 2.86% | 474 | **0.904** | −0.40 | 0.027 | 6.36 |

## The entry-bar outcomes were data-resolved, not guessed

Checked before drawing a conclusion, because it decides whether the frozen numbers
are *wrong* or merely *fragile*:

| | ETHUSDT | SOLUSDT |
|---|---|---|
| touch timeframe | 1m | 1m |
| touch rows in window | 2,277,960 | 2,269,320 |
| touch resolved | 503 / 503 | 489 / 490 |
| touch resolved rate | **1.000** | **0.998** |
| ambiguous rate | 0.000 | 0.000 |

So the simulator read the actual 1-minute sequence inside each entry candle to
decide whether the target or the stop came first. The frozen 1.352 and 1.965 are
**not** the product of an adverse or optimistic same-bar assumption, and calling
them simply "wrong" would be inaccurate.

## Conclusion

The defect is **extreme bracket fragility**, not a simulation error.

**Every bracket configuration that brings the entry-bar exit rate under the 25%
policy line yields a profit factor at or below 1.03 for both symbols, and below
1.00 for all but one.** The edge exists only in a knife-edge regime around a 1%
stop and disappears as soon as the stop widens by half an Average True Range.

At 1.0x Average True Range the Ethereum stop averages 0.97% — essentially the live
pack's fixed 1.0% — yet profit factor is 1.097 rather than 1.352. Merely letting
the stop *vary per trade* at the same average width removes about a quarter of the
apparent edge. A result that sensitive to bracket mechanics is characterising the
bracket, not the `bounce_upper` signal.

What the strategy actually does, on its own numbers, is collect 1.5% before 1% is
hit, usually within one to three hours. That is a short-horizon bet on noise, and
its profitability depends on a stop distance tuned to roughly the amplitude of that
noise. It is the classic overfitting signature, which is why it should not be
promoted even though the simulation is faithful.

## Open question: funding is exactly zero

All three arms report `total_funding = 0.0` across 443-503 trades spanning
2022-2026. Average hold is 1.85-3.56 hours with a max hold of 8 hours, and Bybit
settles funding every 8 hours, so some trades must span a settlement. Exactly zero
across every arm needs verification — it may be a genuine consequence of short
holds, or a missing funding application. Tracked separately; it does not change the
conclusion above, since funding costs would only reduce the profit factors.

Per-fold at 1.5x Average True Range, Ethereum has 1 of 6 folds above profit factor
1.0; Solana has 4 of 6 but with fold 2 at 0.423 and fold 4 at 0.648, which is not a
stable edge.

## Required actions

1. Both arms' inherited readiness is **invalidated**. No `SHADOW_READY` or
   `MICRO_LIVE_CANDIDATE` claim can rest on the 1.352 / 1.965 numbers.
2. Do not quote those profit factors in any future report without this finding
   attached.
3. Add `entry_bar_exit_rate` as a **hard** screen gate, not a diagnostic, in every
   preregister. The Solana arm passed a settle whose own configuration file capped
   it at 0.35.
4. The live units remain running at minimum exchange size by explicit user
   decision, recorded as a known risk. Stopping them requires user authorization.

## Reproduce

```
python -u scripts/diag_live_arms_atr_rescore.py --per-fold
python artifacts/_tmp_dsr_ebr_vs_pf.py
```

Raw output: `artifacts/reports/diagonal_sr/live_arms_atr_rescore_latest.json`
Frozen source: `artifacts/sqlite/diagonal_sr_nested_settle_001/settle.sqlite`

## Note on the live packs

`pack_meta.json` in each live pack directory is **not** edited by this finding. The
live certificates verify the pack by hash, so editing the pack would make both
running units fail their startup certificate check. This report is the record.
