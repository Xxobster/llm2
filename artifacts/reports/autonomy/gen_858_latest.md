# Autonomy public-indicator hunt gen 858

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T211348Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret712_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.0493 | 0.6954 | 3.9641 | 0.0219 | 0.3621 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret712_neg_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9898 | 0.6865 | 4.0757 | 0.0214 | 0.3568 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret712_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.0862 | 0.6848 | 3.9298 | 0.0166 | 0.3533 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret712_neg_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 2.0623 | 0.6782 | 4.0962 | 0.0161 | 0.3465 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret712_pos_at_h` | one_head_filter_pi_star | 95 | 7.8082 | 1.7938 | 0.6737 | 2.4235 | 0.0112 | 0.2842 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret712_pos_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.2196 | 0.5776 | 0.9183 | 0.0038 | 0.2672 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret712_pos_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.0100 | 0.5535 | 0.0520 | 0.0004 | 0.2075 | ok | RAN |
| ETHUSDT | 8 | `ret712_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 0.9880 | 0.5412 | -0.0669 | -0.0005 | 0.2059 | ok | RAN |
| BTCUSDT | 4 | `ret712_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.5092 | 0.2857 | -0.9832 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret712_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3413 | 0.2308 | -1.4046 | -0.0785 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret712_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret712_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
