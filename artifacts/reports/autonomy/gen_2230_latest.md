# Autonomy public-indicator hunt gen 2230

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T161746Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma526_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1519 | 0.5946 | 0.8956 | 0.0047 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `wma526_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1252 | 0.5882 | 0.7424 | 0.0038 | 0.1818 | ok | RAN |
| SOLUSDT | 8 | `wma526_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.0708 | 0.5500 | 0.3910 | 0.0013 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `wma526_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0409 | 0.5372 | 0.2353 | 0.0008 | 0.1064 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma526_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0035 | 0.5604 | 0.0202 | 0.0001 | 0.1593 | ok | RAN |
| SOLUSDT | 4 | `wma526_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0012 | 0.5611 | 0.0073 | 0.0000 | 0.1444 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma526_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8376 | 0.5397 | -1.0319 | -0.0066 | 0.0952 | ok | RAN |
| ETHUSDT | 8 | `wma526_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.7970 | 0.5288 | -1.3197 | -0.0086 | 0.0995 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma526_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma526_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma526_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma526_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma526_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma526_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma526_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma526_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma526_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma526_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma526_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma526_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma526_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma526_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma526_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma526_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
