# Autonomy public-indicator hunt gen 2318

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T025104Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma539_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1023 | 0.5815 | 0.6078 | 0.0032 | 0.1902 | ok | RAN |
| ETHUSDT | 8 | `wma539_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.0905 | 0.5892 | 0.5452 | 0.0029 | 0.1892 | ok | RAN |
| SOLUSDT | 8 | `wma539_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0528 | 0.5484 | 0.3023 | 0.0010 | 0.0968 | ok | RAN |
| SOLUSDT | 8 | `wma539_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.0326 | 0.5707 | 0.1916 | 0.0007 | 0.1576 | ok | RAN |
| SOLUSDT | 4 | `wma539_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0283 | 0.5628 | 0.1665 | 0.0006 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `wma539_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0091 | 0.5368 | 0.0539 | 0.0002 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma539_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8258 | 0.5340 | -1.1213 | -0.0073 | 0.0995 | ok | RAN |
| ETHUSDT | 8 | `wma539_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8017 | 0.5344 | -1.3220 | -0.0083 | 0.1005 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma539_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma539_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma539_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma539_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma539_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma539_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma539_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma539_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma539_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma539_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma539_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma539_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma539_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma539_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma539_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma539_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
