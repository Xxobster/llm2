# Autonomy public-indicator hunt gen 2085

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T200510Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret341_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.2646 | 0.6087 | 1.4598 | 0.0079 | 0.1848 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret341_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.2610 | 0.5978 | 1.3817 | 0.0076 | 0.1955 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret341_pos_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.1837 | 0.5577 | 0.8824 | 0.0034 | 0.1218 | ok | RAN |
| SOLUSDT | 4 | `ret341_pos_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.1777 | 0.5644 | 0.8705 | 0.0032 | 0.1104 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret341_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 0.9506 | 0.5622 | -0.3023 | -0.0011 | 0.1514 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret341_neg_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.8995 | 0.5522 | -0.6410 | -0.0021 | 0.1493 | ok | RAN |
| ETHUSDT | 8 | `ret341_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.7967 | 0.5486 | -1.2092 | -0.0082 | 0.0914 | ok | RAN |
| ETHUSDT | 4 | `ret341_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.7744 | 0.5314 | -1.3709 | -0.0099 | 0.0971 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret341_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0638 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret341_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0726 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret341_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret341_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret341_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret341_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret341_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret341_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret341_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret341_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret341_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret341_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret341_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret341_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret341_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret341_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
