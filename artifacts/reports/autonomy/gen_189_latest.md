# Autonomy public-indicator hunt gen 189

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T215104Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret44_neg_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.7961 | 0.6766 | 3.8232 | 0.0210 | 0.3483 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret44_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.7067 | 0.6717 | 3.4280 | 0.0191 | 0.3737 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret44_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.0513 | 0.6848 | 3.8472 | 0.0167 | 0.3818 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret44_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.0504 | 0.6810 | 3.7080 | 0.0167 | 0.3865 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret44_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2874 | 0.6032 | 1.4082 | 0.0090 | 0.2275 | ok | RAN |
| ETHUSDT | 8 | `ret44_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2471 | 0.6022 | 1.1925 | 0.0080 | 0.2431 | ok | RAN |
| SOLUSDT | 8 | `ret44_pos_at_h` | one_head_filter_pi_star | 223 | 18.1835 | 1.5441 | 0.6188 | 2.7402 | 0.0077 | 0.2691 | ok | RAN |
| SOLUSDT | 4 | `ret44_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.4813 | 0.6114 | 2.4451 | 0.0068 | 0.2654 | ok | RAN |
| SOLUSDT | 8 | `ret44_cross_down_0` | one_head_filter_pi_star | 38 | 3.3861 | 1.3370 | 0.5789 | 0.7422 | 0.0065 | 0.1053 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret44_cross_up_0` | one_head_filter_pi_star | 27 | 2.2571 | 1.2884 | 0.5556 | 0.5963 | 0.0064 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret44_cross_up_0` | one_head_filter_pi_star | 27 | 2.3838 | 0.9766 | 0.4815 | -0.0560 | -0.0010 | 0.0741 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret44_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret44_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret44_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret44_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret44_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret44_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret44_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret44_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret44_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret44_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret44_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret44_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret44_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
