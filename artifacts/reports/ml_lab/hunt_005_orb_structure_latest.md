# ML lab hunt 005 (ORB / structure / NR7)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T041739Z`.
Rows: 72. Skill pass: **4**. Screen pass: **0**.
Do not nest-settle. Do not widen Average-True-Range after seeing entry-bar exits.

## Tradesim arms (full book)

| Symbol | TF | Idea | n_skill | DA | signed | n_tr | t/m | PF | Sharpe | HAC | WR | ebr | hold | fill | fees | fund | liq | screen |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SOLUSDT | 4h | `cvd_slope` | 2813 | 0.513 | 0.005 | 754 | 48.452 | 2.237 | 7.778 | 6.487 | 0.626 | 0.576 | 0.995 | 0.444 | 4.849 | -0.656 | 0 | fail |
| ETHUSDT | 4h | `cvd_slope` | 4565 | 0.524 | 0.003 | 645 | 25.641 | 1.488 | 2.637 | 2.168 | 0.544 | 0.327 | 2.566 | 0.284 | 8.269 | -3.266 | 0 | fail |
| SOLUSDT | 1h | `wick_reject_follow` | 149 | 0.537 | 0.005 | 53 | 3.482 | 0.992 | -0.023 | -0.025 | 0.434 | 0.208 | 4.170 | 0.376 | 0.353 | -0.036 | 0 | fail |
| SOLUSDT | 15m | `wick_reject_follow` | 428 | 0.554 | 0.002 | 141 | 9.122 | 0.957 | -0.195 | -0.224 | 0.376 | 0.092 | 6.518 | 0.390 | 1.056 | -0.005 | 0 | fail |

## Event-study ranking (signed expectancy after 11 bp floor)

| Symbol | TF | Idea | n_skill | DA | signed | skill |
|---|---|---|---:|---:|---:|---|
| SOLUSDT | 1h | `wick_reject_follow` | 149 | 0.537 | 0.005 | Y |
| SOLUSDT | 4h | `cvd_slope` | 2813 | 0.513 | 0.005 | Y |
| ETHUSDT | 4h | `cvd_slope` | 4565 | 0.524 | 0.003 | Y |
| ETHUSDT | 4h | `adx_rising` | 2120 | 0.487 | 0.002 |  |
| SOLUSDT | 15m | `wick_reject_follow` | 428 | 0.554 | 0.002 | Y |
| ETHUSDT | 4h | `structure_swings` | 1845 | 0.494 | 0.002 |  |
| ETHUSDT | 1h | `utc_orb_follow` | 8317 | 0.500 | 0.002 |  |
| ETHUSDT | 1h | `adx_rising` | 8354 | 0.489 | 0.001 |  |
| ETHUSDT | 1h | `structure_swings` | 7093 | 0.480 | 0.001 |  |
| BTCUSDT | 1h | `adx_rising` | 9152 | 0.483 | 0.001 |  |
| BTCUSDT | 1h | `utc_orb_follow` | 9154 | 0.486 | 0.001 |  |
| BTCUSDT | 4h | `adx_rising` | 2387 | 0.500 | 0.001 |  |
| BTCUSDT | 4h | `cvd_slope` | 5042 | 0.505 | 0.001 |  |
| ETHUSDT | 15m | `utc_orb_follow` | 32618 | 0.491 | 0.001 |  |
| ETHUSDT | 1h | `cvd_slope` | 18345 | 0.500 | 0.001 |  |
| BTCUSDT | 15m | `utc_orb_follow` | 35733 | 0.479 | 0.000 |  |
| BTCUSDT | 1h | `cvd_slope` | 20255 | 0.490 | 0.000 |  |
| BTCUSDT | 1h | `structure_swings` | 7547 | 0.465 | 0.000 |  |
| ETHUSDT | 1h | `nr7_break` | 1663 | 0.453 | 0.000 |  |
| ETHUSDT | 4h | `wick_reject_follow` | 53 | 0.453 | 0.000 |  |
| BTCUSDT | 15m | `adx_rising` | 36670 | 0.468 | 0.000 |  |
| SOLUSDT | 15m | `cvd_slope` | 45444 | 0.494 | 0.000 |  |
| BTCUSDT | 1h | `wick_reject_follow` | 306 | 0.526 | 0.000 |  |
| ETHUSDT | 15m | `utc_open_drive` | 72382 | 0.497 | 0.000 |  |
| ETHUSDT | 15m | `adx_rising` | 33502 | 0.466 | -0.000 |  |
| ETHUSDT | 4h | `utc_orb_follow` | 2236 | 0.477 | -0.000 |  |
| BTCUSDT | 15m | `utc_open_drive` | 80172 | 0.498 | -0.000 |  |
| ETHUSDT | 15m | `cvd_slope` | 73473 | 0.486 | -0.000 |  |
| BTCUSDT | 15m | `structure_swings` | 29440 | 0.449 | -0.000 |  |
| BTCUSDT | 15m | `nr7_break` | 7873 | 0.451 | -0.000 |  |
| ETHUSDT | 1h | `utc_open_drive` | 17564 | 0.495 | -0.000 |  |
| BTCUSDT | 15m | `cvd_slope` | 81113 | 0.480 | -0.000 |  |
| SOLUSDT | 15m | `utc_orb_follow` | 20651 | 0.472 | -0.000 |  |
| ETHUSDT | 15m | `nr7_break` | 7273 | 0.466 | -0.000 |  |
| ETHUSDT | 15m | `structure_swings` | 27366 | 0.458 | -0.000 |  |
| SOLUSDT | 1h | `structure_swings` | 4504 | 0.478 | -0.000 |  |
| SOLUSDT | 15m | `utc_open_drive` | 44899 | 0.491 | -0.000 |  |
| ETHUSDT | 4h | `nr7_break` | 412 | 0.481 | -0.000 |  |
| BTCUSDT | 15m | `wick_reject_follow` | 1069 | 0.533 | -0.000 |  |
| SOLUSDT | 1h | `utc_orb_follow` | 5252 | 0.481 | -0.000 |  |
