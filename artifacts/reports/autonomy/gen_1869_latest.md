# Autonomy public-indicator hunt gen 1869

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T203626Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret310_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.2377 | 0.6064 | 1.3656 | 0.0070 | 0.1862 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret310_pos_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.2870 | 0.5778 | 1.2442 | 0.0052 | 0.1333 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret310_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.1764 | 0.5988 | 0.9440 | 0.0052 | 0.1852 | ok | RAN |
| SOLUSDT | 8 | `ret310_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0431 | 0.5667 | 0.2467 | 0.0009 | 0.1500 | ok | RAN |
| SOLUSDT | 8 | `ret310_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.0284 | 0.5455 | 0.1581 | 0.0006 | 0.1136 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ret310_pos_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 0.9698 | 0.5664 | -0.1567 | -0.0011 | 0.0979 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret310_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 0.9223 | 0.5432 | -0.4650 | -0.0017 | 0.1543 | ok | RAN |
| ETHUSDT | 8 | `ret310_pos_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 0.8225 | 0.5370 | -1.0097 | -0.0073 | 0.0926 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret310_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0729 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret310_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0742 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret310_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret310_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret310_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret310_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret310_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret310_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret310_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret310_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret310_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret310_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret310_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret310_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret310_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret310_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
