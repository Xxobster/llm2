# Autonomy public-indicator hunt gen 2062

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T165909Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma499_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1642 | 0.5955 | 0.9344 | 0.0049 | 0.1854 | ok | RAN |
| ETHUSDT | 4 | `wma499_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1528 | 0.5912 | 0.8962 | 0.0048 | 0.2099 | ok | RAN |
| SOLUSDT | 8 | `wma499_above_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.0981 | 0.5482 | 0.5187 | 0.0018 | 0.1024 | ok | RAN |
| SOLUSDT | 4 | `wma499_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0408 | 0.5401 | 0.2336 | 0.0008 | 0.1016 | ok | RAN |
| SOLUSDT | 8 | `wma499_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.0177 | 0.5580 | 0.1041 | 0.0004 | 0.1602 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma499_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 0.9920 | 0.5549 | -0.0465 | -0.0002 | 0.1484 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma499_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 0.8482 | 0.5398 | -0.9274 | -0.0061 | 0.0909 | ok | RAN |
| ETHUSDT | 4 | `wma499_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8036 | 0.5323 | -1.2716 | -0.0081 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma499_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma499_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma499_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma499_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma499_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma499_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma499_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma499_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma499_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma499_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma499_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma499_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma499_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma499_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma499_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma499_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
