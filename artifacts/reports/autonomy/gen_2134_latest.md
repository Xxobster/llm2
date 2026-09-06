# Autonomy public-indicator hunt gen 2134

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T022359Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma511_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.0982 | 0.5860 | 0.5985 | 0.0031 | 0.1935 | ok | RAN |
| ETHUSDT | 4 | `wma511_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.0781 | 0.5843 | 0.4689 | 0.0025 | 0.2022 | ok | RAN |
| SOLUSDT | 4 | `wma511_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0709 | 0.5756 | 0.3946 | 0.0014 | 0.1570 | ok | RAN |
| SOLUSDT | 8 | `wma511_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.0321 | 0.5579 | 0.1912 | 0.0007 | 0.1526 | ok | RAN |
| SOLUSDT | 8 | `wma511_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0288 | 0.5385 | 0.1645 | 0.0005 | 0.0989 | ok | RAN |
| SOLUSDT | 4 | `wma511_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0175 | 0.5351 | 0.1019 | 0.0003 | 0.1027 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma511_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8046 | 0.5294 | -1.2749 | -0.0081 | 0.0963 | ok | RAN |
| ETHUSDT | 4 | `wma511_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7965 | 0.5291 | -1.3275 | -0.0084 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma511_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0461 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma511_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma511_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma511_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma511_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma511_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma511_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma511_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma511_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma511_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma511_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma511_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma511_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma511_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma511_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma511_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
