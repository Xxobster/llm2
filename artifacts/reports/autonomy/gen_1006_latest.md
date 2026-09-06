# Autonomy public-indicator hunt gen 1006

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T110941Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma535_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0422 | 0.7017 | 4.4642 | 0.0245 | 0.3867 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma535_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9296 | 0.6907 | 4.2483 | 0.0223 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma535_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9598 | 0.6737 | 3.9022 | 0.0142 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma535_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.9445 | 0.6684 | 3.8442 | 0.0139 | 0.3472 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma535_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.5301 | 0.6117 | 2.5066 | 0.0081 | 0.2660 | ok | RAN |
| ETHUSDT | 8 | `wma535_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2331 | 0.5979 | 1.2386 | 0.0081 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `wma535_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2156 | 0.6011 | 1.1484 | 0.0076 | 0.2181 | ok | RAN |
| SOLUSDT | 4 | `wma535_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4340 | 0.5946 | 2.0824 | 0.0069 | 0.2595 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma535_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma535_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma535_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma535_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
