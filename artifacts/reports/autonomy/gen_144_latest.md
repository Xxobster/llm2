# Autonomy public-indicator hunt gen 144

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T185553Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma150_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9472 | 0.6875 | 4.3507 | 0.0224 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma150_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8568 | 0.6768 | 4.0469 | 0.0212 | 0.3687 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma150_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.2213 | 0.6906 | 4.3792 | 0.0168 | 0.3702 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma150_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.2354 | 0.6923 | 4.3779 | 0.0167 | 0.3681 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma150_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2354 | 0.6075 | 1.1653 | 0.0081 | 0.2258 | ok | RAN |
| ETHUSDT | 4 | `sma150_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.2084 | 0.6032 | 1.0459 | 0.0071 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `sma150_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3776 | 0.6019 | 1.9604 | 0.0060 | 0.2670 | ok | RAN |
| SOLUSDT | 8 | `sma150_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.3793 | 0.5989 | 1.9013 | 0.0060 | 0.2727 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma150_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma150_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma150_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma150_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma150_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma150_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
