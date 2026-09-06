# Autonomy public-indicator hunt gen 403

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T025700Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma178_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9642 | 0.6973 | 4.3519 | 0.0231 | 0.3946 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma178_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.7553 | 0.6719 | 3.6545 | 0.0193 | 0.3698 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma178_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.3041 | 0.7029 | 4.4656 | 0.0177 | 0.3829 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma178_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1614 | 0.6923 | 4.0554 | 0.0167 | 0.3787 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma178_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.3113 | 0.6138 | 1.5151 | 0.0101 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma178_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.2653 | 0.6033 | 1.3445 | 0.0088 | 0.2228 | ok | RAN |
| SOLUSDT | 4 | `sma178_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3775 | 0.6000 | 1.9235 | 0.0059 | 0.2600 | ok | RAN |
| SOLUSDT | 8 | `sma178_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3429 | 0.5960 | 1.7863 | 0.0055 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma178_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma178_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma178_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma178_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma178_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma178_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma178_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma178_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma178_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma178_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma178_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma178_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma178_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma178_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma178_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma178_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
