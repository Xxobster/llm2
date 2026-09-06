# Autonomy public-indicator hunt gen 2158

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T062216Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma514_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1091 | 0.5924 | 0.6528 | 0.0034 | 0.1957 | ok | RAN |
| ETHUSDT | 8 | `wma514_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.0886 | 0.5792 | 0.5320 | 0.0028 | 0.1913 | ok | RAN |
| SOLUSDT | 8 | `wma514_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.0564 | 0.5730 | 0.3241 | 0.0012 | 0.1573 | ok | RAN |
| SOLUSDT | 4 | `wma514_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0277 | 0.5659 | 0.1594 | 0.0006 | 0.1538 | ok | RAN |
| SOLUSDT | 8 | `wma514_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0176 | 0.5410 | 0.1019 | 0.0003 | 0.1038 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma514_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 0.9885 | 0.5372 | -0.0674 | -0.0002 | 0.0957 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma514_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8038 | 0.5301 | -1.2586 | -0.0084 | 0.0984 | ok | RAN |
| ETHUSDT | 8 | `wma514_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7758 | 0.5183 | -1.4435 | -0.0093 | 0.0890 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma514_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma514_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma514_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma514_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
