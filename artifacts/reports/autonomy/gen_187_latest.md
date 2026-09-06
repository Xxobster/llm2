# Autonomy public-indicator hunt gen 187

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T214329Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma28_cross_up` | one_head_filter_pi_star | 21 | 1.8254 | 1.4627 | 0.6190 | 0.7924 | 0.0215 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma28_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8239 | 0.6816 | 4.0067 | 0.0212 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma28_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8007 | 0.6787 | 3.8626 | 0.0207 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma28_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1889 | 0.6933 | 4.0697 | 0.0180 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma28_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1870 | 0.6909 | 4.0766 | 0.0179 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma28_cross_down` | one_head_filter_pi_star | 15 | 1.4467 | 1.7636 | 0.6000 | 0.8918 | 0.0110 | 0.1333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma28_cross_down` | one_head_filter_pi_star | 23 | 2.1304 | 1.2159 | 0.5217 | 0.4069 | 0.0091 | 0.1739 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma28_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| ETHUSDT | 4 | `sma28_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.1875 | 0.5935 | 0.9013 | 0.0058 | 0.1935 | ok | RAN |
| SOLUSDT | 8 | `sma28_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3629 | 0.5935 | 1.9663 | 0.0054 | 0.2430 | ok | RAN |
| SOLUSDT | 4 | `sma28_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3492 | 0.5935 | 1.8987 | 0.0052 | 0.2383 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma28_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma28_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma28_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma28_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
