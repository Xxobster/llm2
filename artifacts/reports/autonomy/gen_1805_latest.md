# Autonomy public-indicator hunt gen 1805

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T145204Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret301_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 1.2585 | 0.6129 | 1.3261 | 0.0073 | 0.2000 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret301_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.1688 | 0.6087 | 0.9636 | 0.0052 | 0.1925 | ok | RAN |
| SOLUSDT | 4 | `ret301_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.1604 | 0.5833 | 0.8304 | 0.0031 | 0.1488 | ok | RAN |
| SOLUSDT | 4 | `ret301_pos_at_h` | one_head_filter_pi_star | 168 | 13.7768 | 1.1259 | 0.5536 | 0.6718 | 0.0023 | 0.0952 | ok | RAN |
| SOLUSDT | 8 | `ret301_pos_at_h` | one_head_filter_pi_star | 159 | 13.0388 | 1.0607 | 0.5535 | 0.3123 | 0.0012 | 0.1069 | ok | RAN |
| SOLUSDT | 8 | `ret301_neg_at_h` | one_head_filter_pi_star | 151 | 12.4291 | 1.0393 | 0.5563 | 0.2112 | 0.0009 | 0.1656 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret301_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8364 | 0.5291 | -1.0052 | -0.0064 | 0.1005 | ok | RAN |
| ETHUSDT | 4 | `ret301_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 0.7664 | 0.5172 | -1.5015 | -0.0098 | 0.0977 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret301_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0678 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret301_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0678 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret301_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret301_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret301_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret301_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret301_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret301_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret301_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret301_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret301_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret301_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret301_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret301_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret301_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret301_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
