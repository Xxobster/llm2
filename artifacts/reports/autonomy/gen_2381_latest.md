# Autonomy public-indicator hunt gen 2381

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T112433Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret383_neg_at_h` | one_head_filter_pi_star | 147 | 12.0086 | 1.2529 | 0.6054 | 1.2616 | 0.0073 | 0.2109 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret383_neg_at_h` | one_head_filter_pi_star | 150 | 12.2536 | 1.2443 | 0.6000 | 1.2297 | 0.0070 | 0.1933 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret383_pos_at_h` | one_head_filter_pi_star | 159 | 13.0388 | 1.0855 | 0.5472 | 0.4391 | 0.0017 | 0.1069 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret383_pos_at_h` | one_head_filter_pi_star | 150 | 12.2311 | 0.9897 | 0.5267 | -0.0540 | -0.0002 | 0.1133 | ok | RAN |
| SOLUSDT | 4 | `ret383_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 0.9625 | 0.5536 | -0.2149 | -0.0008 | 0.1548 | ok | RAN |
| SOLUSDT | 8 | `ret383_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 0.9443 | 0.5531 | -0.3350 | -0.0012 | 0.1508 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret383_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.7839 | 0.5301 | -1.3774 | -0.0090 | 0.1148 | ok | RAN |
| ETHUSDT | 8 | `ret383_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7881 | 0.5376 | -1.3158 | -0.0092 | 0.1075 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret383_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret383_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret383_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret383_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret383_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret383_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret383_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret383_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret383_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret383_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret383_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret383_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret383_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret383_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret383_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret383_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
