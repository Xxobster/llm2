# Autonomy public-indicator hunt gen 2005

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T095001Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret330_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 1.2390 | 0.6051 | 1.2633 | 0.0071 | 0.1975 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret330_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.2141 | 0.6025 | 1.1894 | 0.0066 | 0.2050 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret330_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.2105 | 0.5723 | 1.0230 | 0.0036 | 0.1024 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret330_pos_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.1276 | 0.5548 | 0.6367 | 0.0024 | 0.1161 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret330_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 0.9962 | 0.5569 | -0.0218 | -0.0001 | 0.1497 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret330_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.8767 | 0.5440 | -0.8148 | -0.0028 | 0.1451 | ok | RAN |
| ETHUSDT | 4 | `ret330_pos_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.8627 | 0.5548 | -0.7775 | -0.0055 | 0.0968 | ok | RAN |
| ETHUSDT | 8 | `ret330_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.7827 | 0.5307 | -1.3052 | -0.0093 | 0.1061 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret330_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4688 | 0.2778 | -1.1839 | -0.0587 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret330_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret330_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret330_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret330_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret330_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret330_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret330_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret330_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret330_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret330_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret330_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret330_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret330_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret330_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret330_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
