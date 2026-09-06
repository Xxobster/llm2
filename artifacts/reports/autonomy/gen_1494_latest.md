# Autonomy public-indicator hunt gen 1494

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T021457Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma411_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9350 | 0.6927 | 4.3501 | 0.0222 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma411_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8229 | 0.6825 | 3.8393 | 0.0207 | 0.3810 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma411_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2215 | 0.6994 | 4.2526 | 0.0168 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma411_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1677 | 0.6864 | 4.1812 | 0.0167 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma411_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.2319 | 0.5956 | 1.2125 | 0.0080 | 0.2186 | ok | RAN |
| ETHUSDT | 8 | `wma411_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2245 | 0.5969 | 1.1634 | 0.0079 | 0.2147 | ok | RAN |
| SOLUSDT | 8 | `wma411_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.5426 | 0.6218 | 2.5845 | 0.0079 | 0.2539 | ok | RAN |
| SOLUSDT | 4 | `wma411_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3737 | 0.6010 | 1.9251 | 0.0060 | 0.2660 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma411_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma411_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma411_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma411_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma411_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma411_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma411_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma411_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma411_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma411_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma411_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma411_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma411_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma411_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma411_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma411_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
