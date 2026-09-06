# Autonomy public-indicator hunt gen 201

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T223940Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema70_cross_up` | one_head_filter_pi_star | 15 | 1.3214 | 4.6721 | 0.7333 | 2.3521 | 0.0338 | 0.2667 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema70_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8496 | 0.6832 | 4.0542 | 0.0216 | 0.3713 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema70_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.7883 | 0.6748 | 3.8721 | 0.0203 | 0.3592 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema70_cross_down` | one_head_filter_pi_star | 32 | 3.0965 | 2.8119 | 0.6875 | 2.3561 | 0.0192 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema70_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2020 | 0.6890 | 4.0866 | 0.0179 | 0.4085 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema70_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.0951 | 0.6835 | 3.7705 | 0.0168 | 0.4114 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema70_cross_down` | one_head_filter_pi_star | 30 | 2.4860 | 1.4034 | 0.5667 | 0.8234 | 0.0153 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema70_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.3234 | 0.6167 | 1.5082 | 0.0099 | 0.2278 | ok | RAN |
| ETHUSDT | 8 | `ema70_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2573 | 0.6033 | 1.2240 | 0.0082 | 0.2228 | ok | RAN |
| SOLUSDT | 8 | `ema70_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3520 | 0.5962 | 1.8607 | 0.0052 | 0.2535 | ok | RAN |
| SOLUSDT | 4 | `ema70_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3237 | 0.5943 | 1.7249 | 0.0048 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema70_cross_up` | one_head_filter_pi_star | 27 | 2.2312 | 0.9750 | 0.4815 | -0.0564 | -0.0010 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema70_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema70_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema70_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema70_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
