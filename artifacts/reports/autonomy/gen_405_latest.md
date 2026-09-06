# Autonomy public-indicator hunt gen 405

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T032326Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret49_cross_up_0` | one_head_filter_pi_star | 19 | 1.8385 | 5.2424 | 0.6316 | 2.2313 | 0.0285 | 0.1579 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret49_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.6667 | 0.6561 | 3.3558 | 0.0184 | 0.3651 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret49_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1303 | 0.6941 | 4.1031 | 0.0174 | 0.3882 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret49_neg_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.6141 | 0.6618 | 3.1364 | 0.0174 | 0.3578 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret49_neg_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.0760 | 0.6918 | 3.8593 | 0.0166 | 0.3899 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret49_pos_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.3582 | 0.6071 | 1.6899 | 0.0107 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret49_pos_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.5466 | 0.6212 | 2.6603 | 0.0074 | 0.2677 | ok | RAN |
| ETHUSDT | 8 | `ret49_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2253 | 0.5924 | 1.1137 | 0.0073 | 0.2283 | ok | RAN |
| SOLUSDT | 4 | `ret49_pos_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.4154 | 0.5990 | 2.1554 | 0.0061 | 0.2574 | ok | RAN |
| SOLUSDT | 8 | `ret49_cross_down_0` | one_head_filter_pi_star | 15 | 1.4513 | 1.3703 | 0.4667 | 0.5402 | 0.0060 | 0.1333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret49_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret49_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret49_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret49_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret49_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret49_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret49_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret49_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret49_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret49_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret49_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret49_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret49_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret49_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
