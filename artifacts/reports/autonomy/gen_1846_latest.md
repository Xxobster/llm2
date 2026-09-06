# Autonomy public-indicator hunt gen 1846

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T183333Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma466_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1775 | 0.5904 | 1.0243 | 0.0053 | 0.1915 | ok | RAN |
| ETHUSDT | 4 | `wma466_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1511 | 0.6000 | 0.8779 | 0.0047 | 0.1943 | ok | RAN |
| SOLUSDT | 4 | `wma466_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.0322 | 0.5614 | 0.1787 | 0.0007 | 0.1579 | ok | RAN |
| SOLUSDT | 8 | `wma466_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.0047 | 0.5469 | 0.0281 | 0.0001 | 0.0990 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma466_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 0.9780 | 0.5495 | -0.1279 | -0.0005 | 0.1648 | ok | RAN |
| SOLUSDT | 4 | `wma466_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 0.9534 | 0.5385 | -0.2837 | -0.0009 | 0.1026 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma466_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8320 | 0.5405 | -1.0564 | -0.0070 | 0.0973 | ok | RAN |
| ETHUSDT | 4 | `wma466_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8236 | 0.5368 | -1.1132 | -0.0071 | 0.0947 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma466_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma466_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma466_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma466_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
