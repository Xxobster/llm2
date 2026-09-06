# Autonomy public-indicator hunt gen 706

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T073619Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret560_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.1020 | 0.7045 | 4.4395 | 0.0238 | 0.3864 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret560_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.8789 | 0.6782 | 3.6803 | 0.0199 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret560_neg_at_h` | one_head_filter_pi_star | 184 | 15.1454 | 1.8537 | 0.6630 | 3.3929 | 0.0136 | 0.3315 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret560_neg_at_h` | one_head_filter_pi_star | 199 | 16.2957 | 1.7953 | 0.6533 | 3.4379 | 0.0124 | 0.3317 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret560_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.3283 | 0.6043 | 1.5873 | 0.0114 | 0.2299 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret560_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2076 | 0.5922 | 1.0514 | 0.0078 | 0.2346 | ok | RAN |
| SOLUSDT | 8 | `ret560_pos_at_h` | one_head_filter_pi_star | 122 | 10.1403 | 1.5074 | 0.6311 | 1.8986 | 0.0076 | 0.2705 | ok | RAN |
| SOLUSDT | 4 | `ret560_pos_at_h` | one_head_filter_pi_star | 125 | 10.3891 | 1.4581 | 0.6000 | 1.7650 | 0.0068 | 0.2640 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret560_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5653 | 0.2778 | -0.8933 | -0.0353 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret560_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5653 | 0.2778 | -0.8933 | -0.0353 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret560_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret560_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret560_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret560_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
