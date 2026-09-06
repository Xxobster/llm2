# ML lab nested settle 009 / 012 screen (+ 011 diagnostic)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T161502Z`.
Stitched arms: 3. Subset gate pass: **0**.
Window: 2022-01-01 to lockbox 2026-05-01. Maker 0.02%. EXEC-021. No retune.

| Symbol | TF | Idea | class | n | /mo | PF | WR | Sharpe | HAC | ebr | folds+ | gate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 1h | `quad_slope_follow` | inner_screen_pass | 933 | 17.929 | 0.977 | 0.445 | -0.135 | -0.133 | 0.066 | 2/6 | pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 1h | `fvg_confluence` | inner_screen_pass | 432 | 8.309 | 0.865 | 0.391 | -0.644 | -0.609 | 0.079 | 1/6 | pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 1h | `quarticity_spike_fade` | failed_screen_diagnostic | 803 | 15.474 | 0.994 | 0.412 | -0.040 | -0.037 | 0.148 | 2/6 | failed_screen_diagnostic |
