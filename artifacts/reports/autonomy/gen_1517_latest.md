# Autonomy public-indicator hunt gen 1517

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T042125Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret260_neg_at_h` | one_head_filter_pi_star | 137 | 11.1916 | 2.4604 | 0.7153 | 4.2999 | 0.0287 | 0.4088 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret260_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.1825 | 0.7024 | 4.5468 | 0.0272 | 0.3929 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret260_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.9199 | 0.6599 | 3.8219 | 0.0134 | 0.3401 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret260_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.8629 | 0.6722 | 3.5772 | 0.0131 | 0.3444 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret260_pos_at_h` | one_head_filter_pi_star | 177 | 14.5149 | 1.6074 | 0.6271 | 2.6912 | 0.0090 | 0.2768 | ok | RAN |
| ETHUSDT | 8 | `ret260_pos_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.2316 | 0.6067 | 1.0913 | 0.0079 | 0.2133 | ok | RAN |
| ETHUSDT | 4 | `ret260_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2276 | 0.6067 | 1.1032 | 0.0077 | 0.2135 | ok | RAN |
| SOLUSDT | 4 | `ret260_pos_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.4630 | 0.6089 | 2.1283 | 0.0072 | 0.2849 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret260_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret260_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret260_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret260_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret260_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret260_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret260_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret260_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret260_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret260_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret260_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret260_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret260_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret260_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret260_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret260_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
