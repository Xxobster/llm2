# ML lab nested settle 013 (predictive math screen passers)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T215846Z`.
Stitched arms: 3. Subset gate pass: **1**.
Window: 2022-01-01 to lockbox 2026-05-01. Maker 0.02%. EXEC-021. No retune.

| Symbol | TF | Idea | class | n | /mo | PF | WR | Sharpe | HAC | ebr | folds+ | gate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 1h | `kalman_accel_follow` | inner_screen_pass | 1054 | 20.286 | 1.084 | 0.470 | 0.517 | 0.519 | 0.061 | 5/6 | pf<1.2,sharpe<1.0,hac_sharpe<0.75 |
| ETHUSDT | 1h | `kalman_accel_follow` | inner_screen_pass | 1012 | 19.477 | 1.163 | 0.461 | 0.938 | 0.991 | 0.054 | 5/6 | pf<1.2,sharpe<1.0 |
| SOLUSDT | 1h | `hilbert_amp_fade` | inner_screen_pass | 726 | 13.962 | 1.266 | 0.468 | 1.242 | 1.322 | 0.088 | 6/6 | PASS |
