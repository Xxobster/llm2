# Autonomy public-indicator hunt gen 185

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T213539Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema64_cross_up` | one_head_filter_pi_star | 19 | 1.6104 | 6.4564 | 0.7368 | 2.7008 | 0.0378 | 0.2632 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema64_cross_down` | one_head_filter_pi_star | 27 | 2.3044 | 3.4046 | 0.7407 | 2.3894 | 0.0244 | 0.1852 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema64_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.8426 | 0.6845 | 4.0463 | 0.0214 | 0.3786 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema64_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.7675 | 0.6766 | 3.7897 | 0.0198 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema64_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1695 | 0.6848 | 4.0282 | 0.0177 | 0.4061 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema64_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1596 | 0.6914 | 3.9686 | 0.0176 | 0.4136 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema64_above_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 1.3978 | 0.6221 | 1.7766 | 0.0118 | 0.2209 | ok | RAN |
| ETHUSDT | 8 | `ema64_cross_down` | one_head_filter_pi_star | 25 | 2.0716 | 1.2429 | 0.5200 | 0.5016 | 0.0110 | 0.2800 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema64_above_at_h` | one_head_filter_pi_star | 175 | 14.4412 | 1.2731 | 0.6057 | 1.2595 | 0.0086 | 0.2114 | ok | RAN |
| SOLUSDT | 8 | `ema64_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.4440 | 0.6065 | 2.2845 | 0.0064 | 0.2546 | ok | RAN |
| SOLUSDT | 4 | `ema64_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3548 | 0.5962 | 1.8757 | 0.0052 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema64_cross_up` | one_head_filter_pi_star | 21 | 1.8278 | 0.8251 | 0.4762 | -0.3928 | -0.0081 | 0.2857 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema64_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema64_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema64_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema64_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema64_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema64_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema64_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema64_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema64_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema64_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema64_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema64_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
