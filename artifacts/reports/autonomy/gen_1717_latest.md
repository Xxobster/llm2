# Autonomy public-indicator hunt gen 1717

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T064053Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret289_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1485 | 0.5848 | 0.8679 | 0.0047 | 0.2047 | ok | RAN |
| SOLUSDT | 4 | `ret289_pos_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.0900 | 0.5769 | 0.4544 | 0.0017 | 0.1026 | ok | RAN |
| ETHUSDT | 4 | `ret289_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.0439 | 0.5889 | 0.2752 | 0.0015 | 0.1833 | ok | RAN |
| SOLUSDT | 8 | `ret289_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0780 | 0.5543 | 0.4130 | 0.0014 | 0.1087 | ok | RAN |
| SOLUSDT | 4 | `ret289_neg_at_h` | one_head_filter_pi_star | 157 | 12.8380 | 1.0518 | 0.5732 | 0.2806 | 0.0011 | 0.1720 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret289_neg_at_h` | one_head_filter_pi_star | 154 | 12.5927 | 0.9530 | 0.5390 | -0.2532 | -0.0011 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret289_pos_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 0.9032 | 0.5535 | -0.5554 | -0.0037 | 0.1006 | ok | RAN |
| ETHUSDT | 4 | `ret289_pos_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.8832 | 0.5417 | -0.6910 | -0.0047 | 0.1012 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret289_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5142 | 0.2778 | -1.0713 | -0.0471 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret289_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret289_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret289_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret289_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret289_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret289_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret289_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret289_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret289_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret289_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret289_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret289_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret289_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret289_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret289_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
