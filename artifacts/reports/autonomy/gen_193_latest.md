# Autonomy public-indicator hunt gen 193

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T220636Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema48_cross_up` | one_head_filter_pi_star | 19 | 1.6104 | 7.7530 | 0.7368 | 2.9072 | 0.0471 | 0.3158 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema48_cross_down` | one_head_filter_pi_star | 12 | 1.2429 | 2.0777 | 0.5833 | 1.1544 | 0.0393 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema48_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.8173 | 0.6808 | 3.9183 | 0.0212 | 0.3803 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema48_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7425 | 0.6746 | 3.6651 | 0.0194 | 0.3732 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema48_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1749 | 0.6848 | 4.0516 | 0.0179 | 0.4242 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema48_cross_down` | one_head_filter_pi_star | 24 | 2.0484 | 2.2242 | 0.6667 | 1.5197 | 0.0172 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema48_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.0902 | 0.6813 | 3.8181 | 0.0169 | 0.4188 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema48_above_at_h` | one_head_filter_pi_star | 168 | 13.8636 | 1.2791 | 0.6012 | 1.2961 | 0.0085 | 0.2083 | ok | RAN |
| ETHUSDT | 8 | `ema48_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2431 | 0.6049 | 1.1055 | 0.0076 | 0.2099 | ok | RAN |
| SOLUSDT | 8 | `ema48_above_at_h` | one_head_filter_pi_star | 219 | 17.8573 | 1.4204 | 0.6073 | 2.1887 | 0.0061 | 0.2511 | ok | RAN |
| SOLUSDT | 4 | `ema48_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3531 | 0.5962 | 1.9108 | 0.0052 | 0.2441 | ok | RAN |
| ETHUSDT | 8 | `ema48_cross_up` | one_head_filter_pi_star | 18 | 1.5667 | 1.0450 | 0.5556 | 0.0801 | 0.0019 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema48_cross_down` | one_head_filter_pi_star | 20 | 1.9929 | 0.9516 | 0.4500 | -0.1078 | -0.0020 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema48_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema48_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema48_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema48_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema48_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema48_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema48_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema48_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema48_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema48_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema48_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
