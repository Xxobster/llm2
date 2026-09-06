# Autonomy public-indicator hunt gen 2141

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T033111Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret349_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2331 | 0.5932 | 1.3100 | 0.0068 | 0.1864 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret349_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.2234 | 0.5964 | 1.2002 | 0.0067 | 0.1807 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret349_pos_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.0947 | 0.5548 | 0.4725 | 0.0018 | 0.1226 | ok | RAN |
| SOLUSDT | 4 | `ret349_pos_at_h` | one_head_filter_pi_star | 149 | 12.1495 | 1.0518 | 0.5570 | 0.2659 | 0.0010 | 0.1208 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret349_neg_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9471 | 0.5572 | -0.3275 | -0.0011 | 0.1443 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret349_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9087 | 0.5521 | -0.5548 | -0.0020 | 0.1458 | ok | RAN |
| ETHUSDT | 4 | `ret349_pos_at_h` | one_head_filter_pi_star | 206 | 16.8774 | 0.8130 | 0.5437 | -1.1874 | -0.0078 | 0.0971 | ok | RAN |
| ETHUSDT | 8 | `ret349_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8147 | 0.5450 | -1.1304 | -0.0078 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret349_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0706 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret349_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0775 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret349_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret349_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret349_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret349_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret349_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret349_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret349_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret349_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret349_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret349_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret349_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret349_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret349_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret349_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
