# Autonomy public-indicator hunt gen 2197

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T120625Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret357_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.3366 | 0.6080 | 1.7354 | 0.0094 | 0.1932 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret357_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.2122 | 0.5938 | 1.1110 | 0.0066 | 0.1938 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret357_pos_at_h` | one_head_filter_pi_star | 160 | 13.0465 | 1.2775 | 0.5813 | 1.3183 | 0.0048 | 0.1187 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret357_pos_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.1826 | 0.5685 | 0.8596 | 0.0034 | 0.1164 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret357_neg_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.0005 | 0.5714 | 0.0035 | 0.0000 | 0.1379 | ok | RAN |
| SOLUSDT | 8 | `ret357_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.9277 | 0.5492 | -0.4709 | -0.0016 | 0.1399 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret357_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 0.8072 | 0.5398 | -1.1393 | -0.0079 | 0.1023 | ok | RAN |
| ETHUSDT | 4 | `ret357_pos_at_h` | one_head_filter_pi_star | 201 | 16.4677 | 0.8019 | 0.5373 | -1.2389 | -0.0085 | 0.0995 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret357_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret357_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0752 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret357_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret357_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret357_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret357_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret357_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret357_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret357_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret357_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret357_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret357_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret357_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret357_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret357_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret357_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
