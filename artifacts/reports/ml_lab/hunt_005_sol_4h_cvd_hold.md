# Hunt 005 Solana 4h cvd_slope — hold audit (inner screen < 2022-01-01)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Window before `2022-01-01`.
This is **not** nested outer out-of-sample. Do not deploy.

Trades: **754**. Profit factor: **2.237**. Trades/month: **48.452**.
Decision-bar (4-hour) entry-bar exits: **434** (0.576).

Trade timestamps in the simulator are 4-hour bar opens. A same-4-hour-bar exit has hold_ms = 0. That is **not** a 1-minute round trip.

## 1-minute path (limit fill to first stop or take-profit)

Scored: **610** / 754. Missing 1-minute cover: 0. No limit touch on 1-minute: 0. No bracket after fill: 144.
Simulator 1-minute path from the 4-hour open would hit the bracket **before** the limit fill: **251** (take-profit 251, stop 0, both 0; summed realized pnl 83.395; take-profit branch 83.395; stop branch 0.000).

| Same candle as 1-minute fill | n | fraction of scored |
|---|---:|---:|
| 1-minute | 1 | 0.002 |
| 5-minute | 6 | 0.010 |
| 15-minute | 41 | 0.067 |
| 1-hour | 167 | 0.274 |

Hold minutes after fill: p10=21.000  median=164.500  mean=302.584  p90=769.000.
Path exits: stop=351  take-profit=259  both in same 1-minute=0.

