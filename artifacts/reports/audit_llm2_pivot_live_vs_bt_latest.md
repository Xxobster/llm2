# LLM2 pivot live vs backtest

**Maximum earned readiness:** `LIVE_STOP / RESEARCH_ONLY`
**Evidence class:** `LIVE_BT_PIVOT_RECONCILE_CONTAMINATED`
**Principal blocker:** 33 live ENTER cancelled as data-unsafe; backtest still fills those limits. Operational gate, not a frozen-pack bug.
Generated: 2026-08-27T02:42:47.076404+00:00

Only this project's live bots: `llm2-pivot-sol-geo-p75-w4` and `llm2-pivot-eth-p75-ctrl-atr-w4` on ln1. ln3 has no LLM2 units. Structure units stay live-stop.

## SOL `llm2-pivot-sol-geo-p75-w4`

- Candles 15-minute VPS vs warehouse: match_rate=1.0 missing=0 mismatch=0
- Decision replay (tip-bound): action 1398/1398 ; p_any 1396/1398 ; features 652/1398
- Live ENTER / filled / cancelled-data-unsafe: {'ENTER_LIMIT': 51, 'filled': 6, 'cancelled_data_unsafe': 26, 'cancelled': 13, 'no_result': 5, 'place_fail': 1}
- Backtest trades: n=11 PF=1.0907167086890812 net=0.029668700000911485
- Fill pairs: live_fills=6 bt=11 extra_bt=5
- Live fill ledger (pivot_fills): n=4
- Missed signals (BT ENTER, live not): 4 (replay 0 + no-row 4)
- Missed trades (live ENTER unfilled + extra BT fills): 50 unfilled=45 extra_bt=5

Action / probability flips:
- {'utc': '2026-08-12T13:45:00+00:00', 'live_action': 'FLAT', 'bt_action': 'FLAT', 'live_p': 0.2028301886792453, 'bt_p': 0.20695652173913043, 'live_side': 'Buy', 'bt_side': 'Buy', 'tip_bound': False}
- {'utc': '2026-08-12T15:15:00+00:00', 'live_action': 'FLAT', 'bt_action': 'FLAT', 'live_p': 0.17058165548098433, 'bt_p': 0.13043478260869565, 'live_side': 'Buy', 'bt_side': 'Buy', 'tip_bound': False}

## ETH `llm2-pivot-eth-p75-ctrl-atr-w4`

- Candles 15-minute VPS vs warehouse: match_rate=1.0 missing=0 mismatch=0
- Decision replay (tip-bound): action 1398/1398 ; p_any 1397/1398 ; features 691/1398
- Live ENTER / filled / cancelled-data-unsafe: {'ENTER_LIMIT': 12, 'filled': 1, 'cancelled_data_unsafe': 7, 'cancelled': 4, 'no_result': 0, 'place_fail': 0}
- Backtest trades: n=2 PF=inf net=0.09932169999774487
- Fill pairs: live_fills=1 bt=2 extra_bt=1
- Live fill ledger (pivot_fills): n=0
- Missed signals (BT ENTER, live not): 2 (replay 0 + no-row 2)
- Missed trades (live ENTER unfilled + extra BT fills): 12 unfilled=11 extra_bt=1

Action / probability flips:
- {'utc': '2026-08-12T15:15:00+00:00', 'live_action': 'FLAT', 'bt_action': 'FLAT', 'live_p': 0.16109422492401215, 'bt_p': 0.1402439024390244, 'live_side': 'Buy', 'bt_side': 'Sell', 'tip_bound': False}

## What is working as designed

- Same frozen pack, threshold 0.35, take-profit 1%, stop 1%, work 4 bars, max-hold 6 bars, minimum-exchange size.
- Live refuses new entries when candle-stale / data-unsafe; backtest has no collector gate, so extra backtest fills are expected.
- Small entry/exit price differences from slippage are allowed.

## Fixes applied or refused

- Did not change take-profit, stop, gate, or work/hold. Those are frozen pack values.
- Did not disable the live-data-001 fail-closed gate. Extra backtest trades vs cancelled-data-unsafe lives are expected.
- Refreshed warehouse Last+Mark locally (Binance REST reachable) and also fetched on live-network-1 then merged.
- Mark stored as source=binance_mark so it cannot overwrite Last (same timestamp primary key).
- Live collector still has zero 1-minute rows. Research 1-minute stays in the local warehouse only.
- Deployed pivot_fills + 2-second fill poll on live-network-1 (2026-08-20T21:04:07Z). No fills in the three post-restart flat bars.
