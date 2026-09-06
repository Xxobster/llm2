# Autonomy public-indicator hunt gen 666

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T044825Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret520_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 2.0889 | 0.6994 | 4.0693 | 0.0248 | 0.3988 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret520_neg_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 2.0323 | 0.6855 | 3.9498 | 0.0241 | 0.4151 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret520_neg_at_h` | one_head_filter_pi_star | 200 | 16.6382 | 1.9450 | 0.6700 | 3.8776 | 0.0135 | 0.3400 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret520_neg_at_h` | one_head_filter_pi_star | 198 | 16.2978 | 1.8630 | 0.6717 | 3.6262 | 0.0132 | 0.3384 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret520_pos_at_h` | one_head_filter_pi_star | 88 | 7.3144 | 1.7323 | 0.6591 | 2.2239 | 0.0103 | 0.2955 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret520_pos_at_h` | one_head_filter_pi_star | 108 | 8.9762 | 1.6649 | 0.6204 | 2.3048 | 0.0094 | 0.2778 | ok | RAN |
| ETHUSDT | 4 | `ret520_pos_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.1112 | 0.5800 | 0.5454 | 0.0044 | 0.2333 | ok | RAN |
| ETHUSDT | 8 | `ret520_pos_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1002 | 0.5779 | 0.5137 | 0.0039 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret520_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5580 | 0.2353 | -0.9085 | -0.0372 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret520_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0565 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret520_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret520_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
