# Autonomy public-indicator hunt gen 1814

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T154100Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma461_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1493 | 0.5892 | 0.8706 | 0.0045 | 0.1892 | ok | RAN |
| ETHUSDT | 4 | `wma461_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.0926 | 0.5833 | 0.5803 | 0.0029 | 0.1927 | ok | RAN |
| SOLUSDT | 8 | `wma461_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0693 | 0.5706 | 0.3853 | 0.0014 | 0.1706 | ok | RAN |
| SOLUSDT | 4 | `wma461_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0638 | 0.5640 | 0.3547 | 0.0013 | 0.1570 | ok | RAN |
| SOLUSDT | 8 | `wma461_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0115 | 0.5397 | 0.0678 | 0.0002 | 0.1005 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma461_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 0.9543 | 0.5291 | -0.2764 | -0.0009 | 0.1058 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma461_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8185 | 0.5288 | -1.1604 | -0.0075 | 0.0995 | ok | RAN |
| ETHUSDT | 8 | `wma461_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.8043 | 0.5372 | -1.2348 | -0.0081 | 0.0904 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma461_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma461_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma461_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma461_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma461_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma461_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma461_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma461_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma461_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma461_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma461_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma461_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma461_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma461_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma461_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma461_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
