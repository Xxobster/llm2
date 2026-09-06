# Autonomy public-indicator hunt gen 650

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T034427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret504_neg_at_h` | one_head_filter_pi_star | 136 | 11.1100 | 2.5002 | 0.7353 | 4.7158 | 0.0290 | 0.4338 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret504_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 2.2866 | 0.7039 | 4.4741 | 0.0271 | 0.4079 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret504_neg_at_h` | one_head_filter_pi_star | 203 | 16.7998 | 1.7952 | 0.6601 | 3.4025 | 0.0120 | 0.3251 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret504_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.5935 | 0.6384 | 2.5946 | 0.0101 | 0.3559 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret504_pos_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.6375 | 0.6107 | 2.5636 | 0.0100 | 0.2752 | ok | RAN |
| SOLUSDT | 4 | `ret504_pos_at_h` | one_head_filter_pi_star | 115 | 9.5580 | 1.4528 | 0.5913 | 1.7418 | 0.0076 | 0.2870 | ok | RAN |
| ETHUSDT | 4 | `ret504_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.1115 | 0.5801 | 0.5919 | 0.0040 | 0.2265 | ok | RAN |
| ETHUSDT | 8 | `ret504_pos_at_h` | one_head_filter_pi_star | 127 | 10.4802 | 1.0848 | 0.5748 | 0.4096 | 0.0034 | 0.2205 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret504_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0437 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret504_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0619 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret504_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret504_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret504_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret504_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
