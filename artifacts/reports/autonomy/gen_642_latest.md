# Autonomy public-indicator hunt gen 642

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T031252Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret496_neg_at_h` | one_head_filter_pi_star | 142 | 11.6001 | 2.4386 | 0.7183 | 4.7337 | 0.0295 | 0.4296 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret496_neg_at_h` | one_head_filter_pi_star | 149 | 12.1719 | 2.3992 | 0.7181 | 4.7191 | 0.0287 | 0.4094 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret496_neg_at_h` | one_head_filter_pi_star | 209 | 17.1145 | 1.8769 | 0.6699 | 3.8062 | 0.0129 | 0.3158 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret496_neg_at_h` | one_head_filter_pi_star | 188 | 15.6399 | 1.8117 | 0.6702 | 3.4078 | 0.0126 | 0.3404 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret496_pos_at_h` | one_head_filter_pi_star | 127 | 10.4873 | 1.7159 | 0.6457 | 2.5358 | 0.0105 | 0.2992 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret496_pos_at_h` | one_head_filter_pi_star | 122 | 10.0744 | 1.5688 | 0.6148 | 2.1851 | 0.0091 | 0.2541 | ok | RAN |
| ETHUSDT | 8 | `ret496_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.1173 | 0.5815 | 0.6186 | 0.0044 | 0.2228 | ok | RAN |
| ETHUSDT | 4 | `ret496_pos_at_h` | one_head_filter_pi_star | 131 | 10.8103 | 1.0690 | 0.5649 | 0.3295 | 0.0028 | 0.2137 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret496_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5735 | 0.2632 | -0.9106 | -0.0430 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret496_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0445 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret496_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret496_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
