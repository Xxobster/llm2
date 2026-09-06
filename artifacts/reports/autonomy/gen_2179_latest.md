# Autonomy public-indicator hunt gen 2179

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T094026Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma764_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.2091 | 0.5955 | 1.1179 | 0.0056 | 0.1742 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma764_below_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 1.1725 | 0.5854 | 0.9597 | 0.0047 | 0.1768 | ok | RAN |
| SOLUSDT | 8 | `sma764_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.1856 | 0.5739 | 0.7842 | 0.0033 | 0.1304 | ok | RAN |
| SOLUSDT | 4 | `sma764_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.0145 | 0.5391 | 0.0694 | 0.0003 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma764_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 0.9428 | 0.5519 | -0.3639 | -0.0012 | 0.1321 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma764_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9158 | 0.5477 | -0.5310 | -0.0018 | 0.1457 | ok | RAN |
| ETHUSDT | 8 | `sma764_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 0.9169 | 0.5597 | -0.4016 | -0.0035 | 0.1269 | ok | RAN |
| ETHUSDT | 4 | `sma764_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 0.8623 | 0.5556 | -0.6833 | -0.0059 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma764_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma764_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma764_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma764_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma764_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma764_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma764_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma764_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma764_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma764_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma764_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma764_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma764_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma764_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma764_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma764_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
