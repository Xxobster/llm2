# Autonomy public-indicator hunt gen 228

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T002822Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema58_cross_up` | one_head_filter_pi_star | 17 | 1.4976 | 7.7246 | 0.7647 | 2.8950 | 0.0488 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema58_cross_down` | one_head_filter_pi_star | 23 | 1.9630 | 4.5084 | 0.7826 | 2.4078 | 0.0254 | 0.0870 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema58_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8170 | 0.6847 | 3.9723 | 0.0208 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema58_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.7713 | 0.6732 | 3.7933 | 0.0197 | 0.3659 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema58_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1303 | 0.6852 | 3.9588 | 0.0173 | 0.4136 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema58_below_at_h` | one_head_filter_pi_star | 155 | 12.6745 | 2.1091 | 0.6839 | 3.8156 | 0.0170 | 0.4323 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema58_above_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.2658 | 0.6023 | 1.2335 | 0.0082 | 0.2105 | ok | RAN |
| ETHUSDT | 8 | `ema58_above_at_h` | one_head_filter_pi_star | 168 | 13.8636 | 1.2587 | 0.6012 | 1.1915 | 0.0080 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `ema58_cross_down` | one_head_filter_pi_star | 25 | 2.0716 | 1.1452 | 0.5200 | 0.3095 | 0.0063 | 0.2400 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema58_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3768 | 0.6000 | 1.9855 | 0.0055 | 0.2512 | ok | RAN |
| ETHUSDT | 4 | `ema58_cross_up` | one_head_filter_pi_star | 17 | 1.5014 | 1.1207 | 0.5294 | 0.2012 | 0.0053 | 0.2941 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema58_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3550 | 0.5962 | 1.9251 | 0.0052 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema58_cross_up` | one_head_filter_pi_star | 20 | 1.7407 | 0.9340 | 0.5000 | -0.1329 | -0.0029 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema58_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema58_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema58_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema58_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema58_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema58_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema58_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema58_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema58_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema58_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema58_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
