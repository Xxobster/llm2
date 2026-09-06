# Autonomy public-indicator hunt gen 1693

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T040816Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret285_neg_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 1.2570 | 0.6065 | 1.3377 | 0.0075 | 0.2000 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret285_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1730 | 0.6000 | 1.0053 | 0.0054 | 0.2000 | ok | RAN |
| SOLUSDT | 4 | `ret285_neg_at_h` | one_head_filter_pi_star | 145 | 11.8568 | 1.0982 | 0.5862 | 0.5134 | 0.0022 | 0.1586 | ok | RAN |
| SOLUSDT | 8 | `ret285_pos_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.0731 | 0.5531 | 0.3882 | 0.0013 | 0.1061 | ok | RAN |
| SOLUSDT | 4 | `ret285_pos_at_h` | one_head_filter_pi_star | 176 | 14.4329 | 1.0140 | 0.5398 | 0.0770 | 0.0003 | 0.1193 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret285_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 0.9492 | 0.5402 | -0.3038 | -0.0011 | 0.1494 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret285_pos_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 0.9087 | 0.5461 | -0.5137 | -0.0035 | 0.0921 | ok | RAN |
| ETHUSDT | 4 | `ret285_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 0.8268 | 0.5353 | -1.0397 | -0.0070 | 0.0941 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret285_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4364 | 0.3000 | -1.3199 | -0.0640 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret285_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0744 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret285_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret285_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret285_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret285_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret285_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret285_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret285_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret285_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret285_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret285_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret285_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret285_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret285_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret285_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
