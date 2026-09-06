# Autonomy public-indicator hunt gen 1750

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T094753Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma451_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1505 | 0.5902 | 0.8878 | 0.0047 | 0.1967 | ok | RAN |
| ETHUSDT | 4 | `wma451_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.1362 | 0.5872 | 0.7954 | 0.0042 | 0.1977 | ok | RAN |
| SOLUSDT | 8 | `wma451_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0771 | 0.5690 | 0.4295 | 0.0016 | 0.1609 | ok | RAN |
| SOLUSDT | 4 | `wma451_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.0423 | 0.5650 | 0.2354 | 0.0009 | 0.1525 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma451_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0012 | 0.5440 | 0.0068 | 0.0000 | 0.0989 | ok | RAN |
| SOLUSDT | 4 | `wma451_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 0.9535 | 0.5312 | -0.2807 | -0.0009 | 0.1042 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma451_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8097 | 0.5236 | -1.1948 | -0.0078 | 0.0995 | ok | RAN |
| ETHUSDT | 8 | `wma451_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.7915 | 0.5266 | -1.3488 | -0.0086 | 0.0957 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma451_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma451_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma451_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma451_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma451_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma451_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma451_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma451_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma451_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma451_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma451_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma451_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma451_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma451_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma451_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma451_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
