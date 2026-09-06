# Autonomy public-indicator hunt gen 522

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T192323Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret376_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.1678 | 0.6978 | 4.4802 | 0.0246 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret376_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.9475 | 0.6760 | 3.8319 | 0.0218 | 0.3631 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret376_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.8443 | 0.6703 | 3.4326 | 0.0128 | 0.3405 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret376_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.7991 | 0.6720 | 3.3105 | 0.0124 | 0.3495 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret376_pos_at_h` | one_head_filter_pi_star | 153 | 12.4757 | 1.5234 | 0.6078 | 2.1953 | 0.0083 | 0.2941 | ok | RAN |
| ETHUSDT | 8 | `ret376_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.2120 | 0.6000 | 1.0950 | 0.0082 | 0.2294 | ok | RAN |
| ETHUSDT | 4 | `ret376_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.1974 | 0.6075 | 1.0407 | 0.0075 | 0.2366 | ok | RAN |
| SOLUSDT | 8 | `ret376_pos_at_h` | one_head_filter_pi_star | 154 | 12.5572 | 1.4298 | 0.5909 | 1.8942 | 0.0075 | 0.2792 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret376_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5580 | 0.2353 | -0.9085 | -0.0387 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret376_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5490 | 0.2632 | -1.0008 | -0.0466 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret376_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret376_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
