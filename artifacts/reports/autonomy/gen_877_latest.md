# Autonomy public-indicator hunt gen 877

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T230704Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret167_neg_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0084 | 0.6906 | 4.2516 | 0.0246 | 0.3867 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret167_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.9989 | 0.6944 | 4.3851 | 0.0244 | 0.3833 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret167_neg_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1742 | 0.6875 | 4.1877 | 0.0169 | 0.3812 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret167_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 2.1662 | 0.6731 | 3.9491 | 0.0165 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret167_pos_at_h` | one_head_filter_pi_star | 201 | 16.5868 | 1.2593 | 0.6070 | 1.3568 | 0.0082 | 0.2139 | ok | RAN |
| SOLUSDT | 4 | `ret167_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.5051 | 0.6186 | 2.4270 | 0.0079 | 0.2732 | ok | RAN |
| SOLUSDT | 8 | `ret167_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4187 | 0.6031 | 2.0701 | 0.0067 | 0.2680 | ok | RAN |
| ETHUSDT | 8 | `ret167_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.1703 | 0.6000 | 0.9230 | 0.0059 | 0.2158 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret167_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret167_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret167_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret167_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret167_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret167_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret167_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret167_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret167_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret167_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret167_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret167_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret167_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret167_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret167_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret167_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
