# ML lab hunt 014 (higher-timeframe Fair Value Gap + new formulas)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T221437Z`.
Rows: 72. Skill pass: **14**. Screen pass: **2**.
Maker 0.02% resting legs. EXEC-021 1-minute fill clock. Inner screen before 2022-01-01.

| Symbol | TF | Idea | n | DA | signed | PF | ebr | skill | screen |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4h | `displace_fvg_follow` | 40 | 0.600 | 0.019 |  |  |  | fail |
| ETHUSDT | 4h | `htf_fvg_confluence` | 44 | 0.636 | 0.018 |  |  |  | fail |
| SOLUSDT | 4h | `fvg_stack_long` | 47 | 0.555 | 0.016 | 1.199 | 0.404 | Y | fail |
| ETHUSDT | 4h | `htf_fvg_follow` | 61 | 0.607 | 0.015 |  |  |  | fail |
| SOLUSDT | 1h | `fvg_stack_long` | 149 | 0.553 | 0.010 | 1.206 | 0.114 | Y | PASS |
| ETHUSDT | 4h | `fvg_stack_long` | 33 | 0.591 | 0.009 | 2.076 | 0.091 | Y | fail |
| ETHUSDT | 1h | `htf_fvg_confluence` | 72 | 0.592 | 0.006 | 1.927 | 0.000 | Y | fail |
| SOLUSDT | 15m | `htf_fvg_inside` | 50 | 0.640 | 0.005 |  |  |  | fail |
| SOLUSDT | 4h | `fvg_fill_continue` | 58 | 0.584 | 0.004 | 1.107 | 0.569 | Y | fail |
| ETHUSDT | 1h | `htf_fvg_follow` | 122 | 0.531 | 0.004 | 1.213 | 0.033 | Y | PASS |
| BTCUSDT | 1h | `htf_fvg_confluence` | 55 | 0.545 | 0.004 | 0.904 | 0.073 | Y | fail |
| BTCUSDT | 4h | `fvg_fill_continue` | 119 | 0.496 | 0.004 |  |  |  | fail |
| BTCUSDT | 1h | `htf_fvg_follow` | 96 | 0.530 | 0.004 | 1.005 | 0.052 | Y | fail |
| BTCUSDT | 4h | `fvg_stack_long` | 183 | 0.503 | 0.004 |  |  |  | fail |
| ETHUSDT | 1h | `fvg_stack_long` | 543 | 0.527 | 0.003 |  |  | Y | fail |
| SOLUSDT | 15m | `htf_fvg_confluence` | 597 | 0.528 | 0.003 |  |  | Y | fail |
| SOLUSDT | 1h | `htf_fvg_confluence` | 141 | 0.518 | 0.003 |  |  | Y | fail |
| SOLUSDT | 15m | `fvg_stack_long` | 1593 | 0.515 | 0.003 |  |  | Y | fail |
| SOLUSDT | 15m | `htf_fvg_follow` | 1083 | 0.514 | 0.002 |  |  | Y | fail |
| ETHUSDT | 1h | `displace_fvg_follow` | 133 | 0.564 | 0.002 |  |  | Y | fail |
| SOLUSDT | 1h | `htf_fvg_follow` | 237 | 0.511 | 0.001 |  |  |  | fail |
| BTCUSDT | 15m | `htf_fvg_confluence` | 761 | 0.495 | 0.001 |  |  |  | fail |
| ETHUSDT | 15m | `fvg_stack_long` | 2116 | 0.500 | 0.001 |  |  |  | fail |
| BTCUSDT | 1h | `fvg_stack_long` | 497 | 0.479 | 0.001 |  |  |  | fail |
| ETHUSDT | 15m | `htf_fvg_confluence` | 779 | 0.520 | 0.001 |  |  |  | fail |
| BTCUSDT | 15m | `htf_fvg_follow` | 1425 | 0.491 | 0.001 |  |  |  | fail |
| BTCUSDT | 15m | `displace_fvg_follow` | 558 | 0.484 | 0.001 |  |  |  | fail |
| ETHUSDT | 15m | `htf_fvg_follow` | 1427 | 0.492 | 0.000 |  |  |  | fail |
| SOLUSDT | 15m | `parkinson_expand_follow` | 6112 | 0.505 | 0.000 |  |  |  | fail |
| BTCUSDT | 15m | `fvg_stack_long` | 1910 | 0.470 | 0.000 |  |  |  | fail |
| SOLUSDT | 15m | `displace_fvg_follow` | 406 | 0.505 | 0.000 |  |  |  | fail |
| BTCUSDT | 15m | `htf_fvg_inside` | 64 | 0.547 | 0.000 |  |  |  | fail |
| ETHUSDT | 15m | `fvg_fill_continue` | 2443 | 0.470 | 0.000 |  |  |  | fail |
| BTCUSDT | 15m | `fvg_fill_continue` | 2613 | 0.469 | 0.000 |  |  |  | fail |
| SOLUSDT | 15m | `fvg_fill_continue` | 1528 | 0.491 | 0.000 |  |  |  | fail |
| BTCUSDT | 1h | `fvg_fill_continue` | 578 | 0.467 | -0.000 |  |  |  | fail |
| BTCUSDT | 1h | `parkinson_expand_follow` | 2792 | 0.472 | -0.000 |  |  |  | fail |
| BTCUSDT | 15m | `parkinson_expand_follow` | 10839 | 0.478 | -0.000 |  |  |  | fail |
| ETHUSDT | 15m | `parkinson_expand_follow` | 9563 | 0.472 | -0.000 |  |  |  | fail |
| ETHUSDT | 1h | `parkinson_expand_follow` | 2397 | 0.481 | -0.001 |  |  |  | fail |
