# Autonomy public-indicator hunt gen 1958

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T045231Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma483_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1695 | 0.5978 | 0.9925 | 0.0051 | 0.1902 | ok | RAN |
| ETHUSDT | 4 | `wma483_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1124 | 0.5851 | 0.6867 | 0.0036 | 0.1915 | ok | RAN |
| SOLUSDT | 8 | `wma483_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0531 | 0.5503 | 0.3034 | 0.0010 | 0.0952 | ok | RAN |
| SOLUSDT | 4 | `wma483_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0294 | 0.5640 | 0.1678 | 0.0006 | 0.1512 | ok | RAN |
| SOLUSDT | 4 | `wma483_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.0293 | 0.5436 | 0.1712 | 0.0005 | 0.1026 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma483_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9691 | 0.5464 | -0.1812 | -0.0007 | 0.1639 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma483_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 0.8227 | 0.5333 | -1.1571 | -0.0073 | 0.0974 | ok | RAN |
| ETHUSDT | 8 | `wma483_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.7722 | 0.5301 | -1.4721 | -0.0097 | 0.0929 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma483_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma483_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma483_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma483_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma483_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma483_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma483_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma483_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma483_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma483_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma483_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma483_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma483_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma483_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma483_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma483_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
