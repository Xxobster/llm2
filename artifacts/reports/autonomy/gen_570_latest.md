# Autonomy public-indicator hunt gen 570

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T223316Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret424_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.3443 | 0.7251 | 4.9984 | 0.0288 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret424_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.1983 | 0.7066 | 4.6531 | 0.0259 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret424_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.6829 | 0.6667 | 2.8657 | 0.0114 | 0.3697 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret424_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.6732 | 0.6324 | 2.9494 | 0.0105 | 0.3189 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret424_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.6169 | 0.6566 | 2.5985 | 0.0103 | 0.3554 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret424_pos_at_h` | one_head_filter_pi_star | 151 | 12.3126 | 1.5119 | 0.6093 | 2.1994 | 0.0085 | 0.3046 | ok | RAN |
| ETHUSDT | 4 | `ret424_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2066 | 0.5956 | 1.0722 | 0.0076 | 0.2240 | ok | RAN |
| ETHUSDT | 8 | `ret424_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.0820 | 0.5754 | 0.4386 | 0.0033 | 0.2179 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret424_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4688 | 0.2778 | -1.1839 | -0.0544 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret424_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret424_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret424_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret424_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret424_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
