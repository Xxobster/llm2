# Autonomy public-indicator hunt gen 1870

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T204147Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma469_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1893 | 0.6032 | 1.0895 | 0.0056 | 0.1905 | ok | RAN |
| ETHUSDT | 4 | `wma469_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1250 | 0.5946 | 0.7635 | 0.0039 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `wma469_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.1080 | 0.5489 | 0.5914 | 0.0019 | 0.0978 | ok | RAN |
| SOLUSDT | 4 | `wma469_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0694 | 0.5508 | 0.3910 | 0.0013 | 0.1016 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma469_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 1.0005 | 0.5610 | 0.0027 | 0.0000 | 0.1524 | ok | RAN |
| SOLUSDT | 8 | `wma469_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9855 | 0.5464 | -0.0853 | -0.0003 | 0.1639 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma469_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 0.8695 | 0.5455 | -0.7812 | -0.0052 | 0.0909 | ok | RAN |
| ETHUSDT | 4 | `wma469_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.7975 | 0.5278 | -1.2719 | -0.0085 | 0.1000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma469_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5135 | 0.2941 | -1.0520 | -0.0487 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma469_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma469_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma469_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma469_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma469_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma469_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma469_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma469_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma469_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma469_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma469_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma469_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma469_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma469_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma469_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
