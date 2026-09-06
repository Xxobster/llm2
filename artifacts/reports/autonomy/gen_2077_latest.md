# Autonomy public-indicator hunt gen 2077

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T190223Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret340_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 1.1839 | 0.6000 | 0.9770 | 0.0058 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `ret340_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.1817 | 0.5896 | 1.0148 | 0.0055 | 0.1908 | ok | RAN |
| SOLUSDT | 8 | `ret340_pos_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.2494 | 0.5776 | 1.1968 | 0.0045 | 0.1180 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret340_pos_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.1839 | 0.5769 | 0.8924 | 0.0033 | 0.1218 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret340_neg_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9382 | 0.5561 | -0.3989 | -0.0013 | 0.1463 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret340_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 0.8992 | 0.5543 | -0.6251 | -0.0022 | 0.1522 | ok | RAN |
| ETHUSDT | 8 | `ret340_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8310 | 0.5393 | -1.0219 | -0.0070 | 0.0955 | ok | RAN |
| ETHUSDT | 4 | `ret340_pos_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 0.7881 | 0.5370 | -1.2104 | -0.0094 | 0.0926 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret340_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret340_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0759 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret340_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret340_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret340_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret340_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret340_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret340_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret340_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret340_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret340_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret340_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret340_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret340_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret340_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret340_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
