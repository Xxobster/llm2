# Autonomy public-indicator hunt gen 2469

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T214918Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret399_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2306 | 0.6012 | 1.2308 | 0.0069 | 0.1618 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret399_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1762 | 0.5939 | 0.9596 | 0.0054 | 0.1758 | ok | RAN |
| SOLUSDT | 4 | `ret399_pos_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.1302 | 0.5422 | 0.6704 | 0.0025 | 0.1205 | ok | RAN |
| SOLUSDT | 8 | `ret399_pos_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.0042 | 0.5620 | 0.0199 | 0.0001 | 0.1157 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret399_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 0.9605 | 0.5615 | -0.2354 | -0.0008 | 0.1390 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret399_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9193 | 0.5474 | -0.4926 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret399_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 0.8237 | 0.5312 | -1.1057 | -0.0074 | 0.1094 | ok | RAN |
| ETHUSDT | 8 | `ret399_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8086 | 0.5297 | -1.2038 | -0.0083 | 0.1189 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret399_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4194 | 0.3000 | -1.4074 | -0.0698 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret399_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0718 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret399_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret399_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret399_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret399_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret399_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret399_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret399_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret399_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret399_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret399_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret399_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret399_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret399_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret399_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
