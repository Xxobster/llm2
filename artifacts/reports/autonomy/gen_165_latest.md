# Autonomy public-indicator hunt gen 165

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T201821Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret40_neg_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.7699 | 0.6798 | 3.6783 | 0.0205 | 0.3596 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret40_neg_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.6880 | 0.6634 | 3.4810 | 0.0190 | 0.3713 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret40_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.0563 | 0.6871 | 3.7738 | 0.0166 | 0.4049 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret40_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.0409 | 0.6768 | 3.7427 | 0.0164 | 0.3780 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret40_cross_down_0` | one_head_filter_pi_star | 27 | 2.2374 | 1.3918 | 0.5185 | 0.7193 | 0.0146 | 0.1852 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret40_cross_up_0` | one_head_filter_pi_star | 30 | 2.5858 | 1.8564 | 0.5667 | 1.5210 | 0.0143 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret40_cross_down_0` | one_head_filter_pi_star | 45 | 3.7056 | 1.6164 | 0.5778 | 1.2705 | 0.0114 | 0.1778 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret40_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.3253 | 0.6136 | 1.5709 | 0.0099 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `ret40_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.5472 | 0.6204 | 2.7449 | 0.0077 | 0.2639 | ok | RAN |
| SOLUSDT | 4 | `ret40_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.5436 | 0.6161 | 2.7351 | 0.0075 | 0.2607 | ok | RAN |
| ETHUSDT | 4 | `ret40_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.1611 | 0.5866 | 0.8148 | 0.0052 | 0.2179 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret40_cross_up_0` | one_head_filter_pi_star | 20 | 1.7407 | 0.6368 | 0.4000 | -0.9089 | -0.0195 | 0.2000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret40_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret40_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret40_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret40_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret40_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret40_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret40_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret40_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret40_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret40_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret40_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret40_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
