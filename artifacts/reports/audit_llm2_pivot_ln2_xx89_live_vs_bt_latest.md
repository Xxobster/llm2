# LLM2 pivot live vs backtest (live-network-2, Xxobster8 + Xxobster9)

**Maximum earned readiness:** `LIVE_STOP / RESEARCH_ONLY`
**Evidence class:** `LIVE_BT_PIVOT_RECONCILE_CONTAMINATED`
**Principal blocker:** 5 extra backtest fills vs live
Generated: 2026-08-27T02:44:05.985367+00:00

Scope: this project's pivot units on live-network-2 only. Structure units ignored.
Xxobster9 0.5%/0.5% remains RESEARCH_ONLY (~80% same-15-minute exits). Operational live is not a promote.

## Xxobster8 `llm2-pivot-eth-p75-ctrl-atr-w4` (1%/1%)

- Candles 15-minute VPS vs warehouse (`price_type=last`): match_rate=1.0 missing=0 mismatch=0 tip=2026-08-27T02:15:00+00:00
- Decision replay: action 586/586 ; p_any 586/586
- Live ENTER / filled / cancelled-data-unsafe: {'ENTER_LIMIT': 1, 'filled': 0, 'cancelled_data_unsafe': 0, 'cancelled': 0, 'no_result': 1, 'place_fail': 0}
- Backtest on live ENTER intents: n=0 PF=None net=None
- Fill pairs: live_fills=0 bt=0 extra_bt=0
- Live fill ledger: n=0
- Missed signals (BT ENTER, live not): 0 (replay 0 + no-row 0)
- Missed trades (unfilled + extra BT): 1

## Xxobster8 `llm2-pivot-sol-geo-p75-w4` (1%/1%)

- Candles 15-minute VPS vs warehouse (`price_type=last`): match_rate=1.0 missing=0 mismatch=0 tip=2026-08-27T02:15:00+00:00
- Decision replay: action 586/586 ; p_any 586/586
- Live ENTER / filled / cancelled-data-unsafe: {'ENTER_LIMIT': 10, 'filled': 2, 'cancelled_data_unsafe': 0, 'cancelled': 2, 'no_result': 6, 'place_fail': 0}
- Backtest on live ENTER intents: n=4 PF=0.8559564512885227 net=-0.03036679999968328
- Fill pairs: live_fills=2 bt=4 extra_bt=2
- Live fill ledger: n=4
- Missed signals (BT ENTER, live not): 0 (replay 0 + no-row 0)
- Missed trades (unfilled + extra BT): 10

## Xxobster9 `llm2-pivot-eth-p50-tp05-sl05` (0.5%/0.5%)

- Candles 15-minute VPS vs warehouse (`price_type=last`): match_rate=1.0 missing=0 mismatch=0 tip=2026-08-27T02:15:00+00:00
- Decision replay: action 586/586 ; p_any 586/586
- Live ENTER / filled / cancelled-data-unsafe: {'ENTER_LIMIT': 1, 'filled': 0, 'cancelled_data_unsafe': 0, 'cancelled': 0, 'no_result': 1, 'place_fail': 0}
- Backtest on live ENTER intents: n=0 PF=None net=None
- Fill pairs: live_fills=0 bt=0 extra_bt=0
- Live fill ledger: n=0
- Missed signals (BT ENTER, live not): 0 (replay 0 + no-row 0)
- Missed trades (unfilled + extra BT): 1

## Xxobster9 `llm2-pivot-sol-p50-tp05-sl05` (0.5%/0.5%)

- Candles 15-minute VPS vs warehouse (`price_type=last`): match_rate=1.0 missing=0 mismatch=0 tip=2026-08-27T02:15:00+00:00
- Decision replay: action 586/586 ; p_any 586/586
- Live ENTER / filled / cancelled-data-unsafe: {'ENTER_LIMIT': 10, 'filled': 1, 'cancelled_data_unsafe': 0, 'cancelled': 2, 'no_result': 6, 'place_fail': 1}
- Backtest on live ENTER intents: n=4 PF=2.1601776262281285 net=0.06668729999728384
- Fill pairs: live_fills=1 bt=4 extra_bt=3
- Live fill ledger: n=2
- Missed signals (BT ENTER, live not): 0 (replay 0 + no-row 0)
- Missed trades (unfilled + extra BT): 12

## Fixes applied or refused

- Did not change take-profit, stop, gate, work, or hold.
- Did not disable live-data-001.
- Did not add 1-minute to the live collector.
- Research load used price_type=last. Mark stays under source=binance_mark.
- Xxobster9 0.5%/0.5% was not retuned. Research still flags ~80% same-bar exits.
