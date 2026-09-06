# Autonomy public-indicator hunt gen 166

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T202208Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma40_cross_up` | one_head_filter_pi_star | 25 | 2.0640 | 1.9650 | 0.6800 | 1.4158 | 0.0294 | 0.2400 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma40_cross_down` | one_head_filter_pi_star | 22 | 2.0463 | 1.9452 | 0.5909 | 1.2678 | 0.0216 | 0.1818 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma40_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8007 | 0.6787 | 3.8626 | 0.0207 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma40_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8007 | 0.6787 | 3.8626 | 0.0207 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma40_cross_up` | one_head_filter_pi_star | 12 | 0.9907 | 1.4953 | 0.6667 | 0.5803 | 0.0203 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma40_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2030 | 0.6970 | 4.1008 | 0.0181 | 0.4242 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma40_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1649 | 0.6890 | 4.0090 | 0.0176 | 0.4146 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma40_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1890 | 0.5901 | 0.8787 | 0.0060 | 0.2050 | ok | RAN |
| ETHUSDT | 8 | `wma40_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1686 | 0.5924 | 0.7850 | 0.0055 | 0.2038 | ok | RAN |
| SOLUSDT | 4 | `wma40_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3704 | 0.5972 | 2.0079 | 0.0055 | 0.2407 | ok | RAN |
| SOLUSDT | 8 | `wma40_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3430 | 0.5905 | 1.8696 | 0.0051 | 0.2429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma40_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma40_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma40_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma40_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
