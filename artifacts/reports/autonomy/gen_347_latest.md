# Autonomy public-indicator hunt gen 347

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T144656Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma130_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0082 | 0.6959 | 4.5450 | 0.0236 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma130_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9312 | 0.6872 | 4.3627 | 0.0223 | 0.3692 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma130_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2814 | 0.6959 | 4.3891 | 0.0178 | 0.3801 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma130_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2004 | 0.6919 | 4.2062 | 0.0168 | 0.3779 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma130_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2447 | 0.6108 | 1.2520 | 0.0083 | 0.2216 | ok | RAN |
| ETHUSDT | 8 | `sma130_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.1864 | 0.5936 | 0.9801 | 0.0065 | 0.2193 | ok | RAN |
| SOLUSDT | 4 | `sma130_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3420 | 0.5951 | 1.7765 | 0.0053 | 0.2634 | ok | RAN |
| SOLUSDT | 8 | `sma130_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.2905 | 0.5867 | 1.5325 | 0.0046 | 0.2653 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma130_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma130_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma130_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma130_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
