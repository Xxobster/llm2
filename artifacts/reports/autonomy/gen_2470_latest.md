# Autonomy public-indicator hunt gen 2470

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T215604Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma563_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1560 | 0.5899 | 0.9099 | 0.0047 | 0.1966 | ok | RAN |
| ETHUSDT | 8 | `wma563_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1483 | 0.5936 | 0.8722 | 0.0045 | 0.1872 | ok | RAN |
| SOLUSDT | 8 | `wma563_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0946 | 0.5495 | 0.5265 | 0.0017 | 0.0989 | ok | RAN |
| SOLUSDT | 4 | `wma563_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0773 | 0.5484 | 0.4387 | 0.0014 | 0.0968 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma563_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9798 | 0.5487 | -0.1263 | -0.0004 | 0.1590 | ok | RAN |
| SOLUSDT | 8 | `wma563_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9538 | 0.5487 | -0.2906 | -0.0010 | 0.1590 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma563_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8411 | 0.5294 | -0.9890 | -0.0064 | 0.0963 | ok | RAN |
| ETHUSDT | 8 | `wma563_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8079 | 0.5348 | -1.2522 | -0.0078 | 0.0963 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma563_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma563_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma563_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma563_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma563_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma563_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma563_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma563_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma563_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma563_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma563_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma563_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma563_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma563_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma563_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma563_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
