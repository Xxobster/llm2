# Autonomy public-indicator hunt gen 356

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T154943Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema205_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0755 | 0.7081 | 4.5435 | 0.0244 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema205_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0737 | 0.7026 | 4.6747 | 0.0239 | 0.3744 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema205_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2081 | 0.6919 | 4.2724 | 0.0174 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema205_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.0761 | 0.6875 | 4.0187 | 0.0160 | 0.3693 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema205_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.1602 | 0.5926 | 0.8425 | 0.0057 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `ema205_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.1469 | 0.5892 | 0.7692 | 0.0053 | 0.2216 | ok | RAN |
| SOLUSDT | 4 | `ema205_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3273 | 0.5874 | 1.7430 | 0.0052 | 0.2573 | ok | RAN |
| SOLUSDT | 8 | `ema205_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.2984 | 0.5816 | 1.5783 | 0.0047 | 0.2602 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema205_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema205_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema205_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema205_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
