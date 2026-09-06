# Autonomy public-indicator hunt gen 2445

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T190620Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret393_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 1.3940 | 0.6275 | 1.9148 | 0.0110 | 0.2092 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret393_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 1.3034 | 0.6275 | 1.4811 | 0.0088 | 0.2026 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret393_pos_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.2532 | 0.6047 | 1.0924 | 0.0045 | 0.1163 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret393_pos_at_h` | one_head_filter_pi_star | 98 | 8.0365 | 1.1473 | 0.6020 | 0.5667 | 0.0027 | 0.1224 | ok | RAN |
| SOLUSDT | 4 | `ret393_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.0071 | 0.5714 | 0.0419 | 0.0001 | 0.1488 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret393_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 0.9301 | 0.5484 | -0.4341 | -0.0015 | 0.1505 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret393_pos_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.9023 | 0.5500 | -0.5498 | -0.0040 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `ret393_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 0.8122 | 0.5480 | -1.1311 | -0.0079 | 0.1017 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret393_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret393_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret393_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret393_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret393_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret393_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret393_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret393_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret393_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret393_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret393_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret393_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret393_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret393_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret393_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret393_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
