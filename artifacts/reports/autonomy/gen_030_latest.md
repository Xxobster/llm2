# Autonomy public-indicator hunt gen 030

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T112737Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `stochrsi_cross_up_20` | one_head_filter_pi_star | 205 | 16.7466 | 1.7007 | 0.6683 | 3.3862 | 0.0191 | 0.3659 | EBR>35% | RAN |
| ETHUSDT | 8 | `stochrsi_cross_up_20` | one_head_filter_pi_star | 217 | 17.7269 | 1.6226 | 0.6590 | 3.1117 | 0.0178 | 0.3687 | EBR>35% | RAN |
| SOLUSDT | 8 | `stochrsi_cross_up_20` | one_head_filter_pi_star | 163 | 13.3287 | 2.1482 | 0.6871 | 3.9193 | 0.0168 | 0.4049 | EBR>35% | RAN |
| SOLUSDT | 4 | `stochrsi_cross_up_20` | one_head_filter_pi_star | 146 | 11.9385 | 2.0949 | 0.6781 | 3.5400 | 0.0166 | 0.4110 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `stochrsi_overbought_at_h` | one_head_filter_pi_star | 16 | 1.4275 | 1.8116 | 0.6875 | 1.0671 | 0.0091 | 0.5000 | EBR>35% | RAN |
| ETHUSDT | 8 | `stochrsi_cross_down_80` | one_head_filter_pi_star | 164 | 13.4364 | 1.2042 | 0.5793 | 0.9553 | 0.0063 | 0.2012 | ok | RAN |
| ETHUSDT | 4 | `stochrsi_cross_down_80` | one_head_filter_pi_star | 151 | 12.4607 | 1.1921 | 0.5762 | 0.8852 | 0.0061 | 0.1921 | ok | RAN |
| SOLUSDT | 4 | `stochrsi_cross_down_80` | one_head_filter_pi_star | 202 | 16.4712 | 1.3402 | 0.5842 | 1.7888 | 0.0053 | 0.2574 | ok | RAN |
| SOLUSDT | 8 | `stochrsi_cross_down_80` | one_head_filter_pi_star | 215 | 17.5312 | 1.3271 | 0.5907 | 1.7945 | 0.0050 | 0.2512 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `stochrsi_cross_down_80` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `stochrsi_cross_down_80` | one_head_filter_pi_star | 18 | 1.5318 | 0.3749 | 0.2778 | -1.4788 | -0.0663 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `stochrsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `stochrsi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `stochrsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `stochrsi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `stochrsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `stochrsi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `stochrsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `stochrsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stochrsi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stochrsi_cross_up_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `stochrsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stochrsi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stochrsi_cross_up_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
