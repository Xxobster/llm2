# Autonomy public-indicator hunt gen 675

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T052530Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma406_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9647 | 0.6865 | 4.2969 | 0.0230 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma406_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.8544 | 0.6907 | 4.0531 | 0.0210 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma406_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.9847 | 0.6667 | 3.7783 | 0.0143 | 0.3503 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma406_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.8966 | 0.6648 | 3.5908 | 0.0132 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma406_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2492 | 0.6010 | 1.2700 | 0.0087 | 0.2228 | ok | RAN |
| SOLUSDT | 4 | `sma406_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5252 | 0.6145 | 2.3882 | 0.0083 | 0.2682 | ok | RAN |
| ETHUSDT | 4 | `sma406_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2292 | 0.5924 | 1.1862 | 0.0081 | 0.2337 | ok | RAN |
| SOLUSDT | 8 | `sma406_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4778 | 0.6043 | 2.2829 | 0.0077 | 0.2620 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma406_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma406_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma406_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma406_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma406_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma406_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
