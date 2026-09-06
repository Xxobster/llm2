# Autonomy public-indicator hunt gen 2461

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T205440Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret397_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 1.2960 | 0.6118 | 1.4689 | 0.0087 | 0.1908 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret397_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 1.2913 | 0.6218 | 1.4576 | 0.0085 | 0.1667 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret397_pos_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.1034 | 0.5913 | 0.4564 | 0.0020 | 0.1217 | ok | RAN |
| SOLUSDT | 8 | `ret397_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0436 | 0.5747 | 0.2430 | 0.0009 | 0.1494 | ok | RAN |
| SOLUSDT | 4 | `ret397_pos_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.0165 | 0.5448 | 0.0820 | 0.0003 | 0.1269 | ok | RAN |
| SOLUSDT | 4 | `ret397_neg_at_h` | one_head_filter_pi_star | 194 | 15.7823 | 1.0065 | 0.5670 | 0.0390 | 0.0001 | 0.1340 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret397_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8594 | 0.5597 | -0.8048 | -0.0058 | 0.1132 | ok | RAN |
| ETHUSDT | 8 | `ret397_pos_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 0.7938 | 0.5357 | -1.1877 | -0.0093 | 0.1071 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret397_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret397_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0683 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret397_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret397_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret397_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret397_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret397_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret397_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret397_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret397_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret397_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret397_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret397_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret397_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret397_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret397_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
