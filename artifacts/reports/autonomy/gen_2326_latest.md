# Autonomy public-indicator hunt gen 2326

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T034742Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma541_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1363 | 0.5912 | 0.7945 | 0.0042 | 0.1934 | ok | RAN |
| SOLUSDT | 8 | `wma541_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.2125 | 0.5745 | 1.1139 | 0.0036 | 0.0957 | GATE_CAND | RAN |
| ETHUSDT | 8 | `wma541_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1064 | 0.5829 | 0.6514 | 0.0033 | 0.1872 | ok | RAN |
| SOLUSDT | 4 | `wma541_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0333 | 0.5405 | 0.1926 | 0.0006 | 0.0973 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma541_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 0.9817 | 0.5480 | -0.1081 | -0.0004 | 0.1469 | ok | RAN |
| SOLUSDT | 8 | `wma541_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 0.9712 | 0.5561 | -0.1729 | -0.0006 | 0.1604 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma541_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8367 | 0.5340 | -1.0182 | -0.0067 | 0.1047 | ok | RAN |
| ETHUSDT | 4 | `wma541_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 0.7915 | 0.5294 | -1.3606 | -0.0089 | 0.0963 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma541_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma541_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma541_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma541_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma541_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma541_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma541_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma541_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma541_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma541_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma541_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma541_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma541_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma541_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma541_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma541_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
