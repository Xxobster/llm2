# Autonomy public-indicator hunt gen 2222

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T152051Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma524_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1176 | 0.5806 | 0.7083 | 0.0036 | 0.1882 | ok | RAN |
| ETHUSDT | 8 | `wma524_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1063 | 0.5860 | 0.6395 | 0.0033 | 0.1828 | ok | RAN |
| SOLUSDT | 4 | `wma524_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0657 | 0.5484 | 0.3714 | 0.0012 | 0.0968 | ok | RAN |
| SOLUSDT | 8 | `wma524_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.0454 | 0.5398 | 0.2528 | 0.0008 | 0.0966 | ok | RAN |
| SOLUSDT | 4 | `wma524_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.0225 | 0.5680 | 0.1284 | 0.0005 | 0.1479 | ok | RAN |
| SOLUSDT | 8 | `wma524_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.0119 | 0.5568 | 0.0714 | 0.0002 | 0.1622 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma524_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8275 | 0.5340 | -1.1003 | -0.0072 | 0.0995 | ok | RAN |
| ETHUSDT | 4 | `wma524_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8111 | 0.5340 | -1.2160 | -0.0080 | 0.0995 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma524_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma524_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma524_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma524_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma524_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma524_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma524_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma524_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma524_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma524_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma524_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma524_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma524_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma524_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma524_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma524_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
