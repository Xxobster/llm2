# Autonomy public-indicator hunt gen 2110

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T233126Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma507_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1726 | 0.5978 | 1.0150 | 0.0052 | 0.1902 | ok | RAN |
| ETHUSDT | 4 | `wma507_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.1358 | 0.5928 | 0.8340 | 0.0042 | 0.1856 | ok | RAN |
| SOLUSDT | 8 | `wma507_above_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.0845 | 0.5434 | 0.4557 | 0.0015 | 0.0983 | ok | RAN |
| SOLUSDT | 8 | `wma507_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.0510 | 0.5642 | 0.2953 | 0.0010 | 0.1620 | ok | RAN |
| SOLUSDT | 4 | `wma507_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0271 | 0.5435 | 0.1563 | 0.0005 | 0.0978 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma507_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 0.9847 | 0.5618 | -0.0882 | -0.0003 | 0.1461 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma507_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8210 | 0.5301 | -1.1219 | -0.0074 | 0.0984 | ok | RAN |
| ETHUSDT | 8 | `wma507_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7780 | 0.5215 | -1.4444 | -0.0094 | 0.0914 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma507_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma507_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma507_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma507_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma507_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma507_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma507_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma507_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma507_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma507_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma507_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma507_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma507_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma507_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma507_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma507_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
