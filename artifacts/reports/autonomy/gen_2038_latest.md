# Autonomy public-indicator hunt gen 2038

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T133732Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma496_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.1324 | 0.5864 | 0.7956 | 0.0041 | 0.1937 | ok | RAN |
| ETHUSDT | 8 | `wma496_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.0850 | 0.5798 | 0.5221 | 0.0027 | 0.1809 | ok | RAN |
| SOLUSDT | 4 | `wma496_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.0670 | 0.5740 | 0.3691 | 0.0014 | 0.1598 | ok | RAN |
| SOLUSDT | 8 | `wma496_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0519 | 0.5632 | 0.2975 | 0.0011 | 0.1609 | ok | RAN |
| SOLUSDT | 8 | `wma496_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.0541 | 0.5506 | 0.3028 | 0.0010 | 0.0955 | ok | RAN |
| SOLUSDT | 4 | `wma496_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0074 | 0.5421 | 0.0436 | 0.0001 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma496_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 0.8175 | 0.5323 | -1.1574 | -0.0076 | 0.0914 | ok | RAN |
| ETHUSDT | 8 | `wma496_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.7872 | 0.5294 | -1.3429 | -0.0089 | 0.0856 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma496_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma496_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma496_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma496_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma496_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma496_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
