# Autonomy public-indicator hunt gen 1018

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T124127Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret872_neg_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 2.0206 | 0.6881 | 4.3691 | 0.0227 | 0.3762 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret872_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9006 | 0.6806 | 3.8034 | 0.0202 | 0.3770 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret872_neg_at_h` | one_head_filter_pi_star | 223 | 18.2349 | 2.0320 | 0.6682 | 4.3096 | 0.0164 | 0.3543 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret872_neg_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 1.9967 | 0.6708 | 4.1926 | 0.0151 | 0.3500 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret872_pos_at_h` | one_head_filter_pi_star | 83 | 6.8899 | 1.2757 | 0.6265 | 0.9779 | 0.0113 | 0.2169 | ok | RAN |
| ETHUSDT | 4 | `ret872_pos_at_h` | one_head_filter_pi_star | 107 | 8.8465 | 1.2374 | 0.5888 | 0.9712 | 0.0100 | 0.2523 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret872_pos_at_h` | one_head_filter_pi_star | 78 | 6.4113 | 1.6125 | 0.6795 | 1.7552 | 0.0086 | 0.2308 | ok | RAN |
| SOLUSDT | 4 | `ret872_pos_at_h` | one_head_filter_pi_star | 88 | 7.1756 | 1.4194 | 0.6136 | 1.3331 | 0.0060 | 0.2386 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret872_pos_at_h` | one_head_filter_pi_star | 10 | 0.8510 | 0.5168 | 0.3000 | -0.8073 | -0.0444 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret872_pos_at_h` | one_head_filter_pi_star | 11 | 0.9361 | 0.3534 | 0.2727 | -1.2833 | -0.0684 | 0.0909 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret872_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret872_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret872_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret872_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
