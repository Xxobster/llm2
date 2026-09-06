# Autonomy public-indicator hunt gen 2453

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T200007Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret395_neg_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.2387 | 0.5946 | 1.3235 | 0.0073 | 0.1784 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret395_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.1538 | 0.5858 | 0.8824 | 0.0049 | 0.1953 | ok | RAN |
| SOLUSDT | 8 | `ret395_pos_at_h` | one_head_filter_pi_star | 113 | 9.2671 | 1.1863 | 0.6106 | 0.7456 | 0.0033 | 0.1239 | ok | RAN |
| SOLUSDT | 4 | `ret395_pos_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.0672 | 0.5897 | 0.2926 | 0.0013 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `ret395_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0530 | 0.5659 | 0.3047 | 0.0011 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret395_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9763 | 0.5549 | -0.1398 | -0.0005 | 0.1387 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret395_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8291 | 0.5346 | -1.0055 | -0.0071 | 0.1132 | ok | RAN |
| ETHUSDT | 8 | `ret395_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 0.7523 | 0.5235 | -1.5383 | -0.0106 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret395_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret395_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4194 | 0.3000 | -1.4074 | -0.0698 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret395_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret395_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret395_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret395_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret395_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret395_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret395_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret395_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret395_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret395_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret395_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret395_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret395_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret395_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
