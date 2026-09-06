# Autonomy public-indicator hunt gen 587

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T234120Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma328_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9830 | 0.6943 | 4.4133 | 0.0236 | 0.3886 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma328_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9301 | 0.6865 | 4.1999 | 0.0228 | 0.3784 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma328_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1450 | 0.6865 | 4.2425 | 0.0163 | 0.3730 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma328_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.1490 | 0.6872 | 4.2060 | 0.0162 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma328_above_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.2398 | 0.5969 | 1.2542 | 0.0081 | 0.2094 | ok | RAN |
| ETHUSDT | 4 | `sma328_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2064 | 0.5924 | 1.1019 | 0.0072 | 0.2174 | ok | RAN |
| SOLUSDT | 8 | `sma328_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4573 | 0.6031 | 2.2342 | 0.0071 | 0.2629 | ok | RAN |
| SOLUSDT | 4 | `sma328_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3829 | 0.5938 | 1.9229 | 0.0062 | 0.2604 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma328_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma328_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma328_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma328_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma328_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma328_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma328_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma328_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma328_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma328_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma328_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma328_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma328_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma328_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma328_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma328_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
