# Autonomy public-indicator hunt gen 1662

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T001600Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma437_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1706 | 0.6067 | 0.9915 | 0.0052 | 0.1966 | ok | RAN |
| ETHUSDT | 8 | `wma437_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.1044 | 0.5825 | 0.6556 | 0.0033 | 0.1959 | ok | RAN |
| SOLUSDT | 4 | `wma437_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0704 | 0.5763 | 0.3919 | 0.0015 | 0.1582 | ok | RAN |
| SOLUSDT | 8 | `wma437_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0677 | 0.5647 | 0.3716 | 0.0014 | 0.1471 | ok | RAN |
| SOLUSDT | 8 | `wma437_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0299 | 0.5526 | 0.1743 | 0.0005 | 0.0947 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma437_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 0.9338 | 0.5272 | -0.3970 | -0.0013 | 0.1087 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma437_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.8233 | 0.5260 | -1.1134 | -0.0071 | 0.0990 | ok | RAN |
| ETHUSDT | 8 | `wma437_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.7927 | 0.5266 | -1.3356 | -0.0086 | 0.0957 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma437_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma437_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4116 | 0.2778 | -1.4041 | -0.0707 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma437_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma437_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma437_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma437_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma437_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma437_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma437_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma437_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma437_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma437_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma437_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma437_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma437_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma437_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
