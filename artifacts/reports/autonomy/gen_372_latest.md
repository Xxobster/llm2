# Autonomy public-indicator hunt gen 372

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T194718Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema225_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0315 | 0.7026 | 4.6058 | 0.0238 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema225_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0012 | 0.6963 | 4.3591 | 0.0236 | 0.3874 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema225_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2851 | 0.7029 | 4.4899 | 0.0176 | 0.3829 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema225_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.2011 | 0.6973 | 4.4412 | 0.0172 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema225_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.1977 | 0.6033 | 1.0208 | 0.0069 | 0.2120 | ok | RAN |
| ETHUSDT | 8 | `ema225_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.1979 | 0.6022 | 1.0063 | 0.0067 | 0.2097 | ok | RAN |
| SOLUSDT | 4 | `ema225_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3424 | 0.5867 | 1.7522 | 0.0053 | 0.2602 | ok | RAN |
| SOLUSDT | 8 | `ema225_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.2995 | 0.5885 | 1.5792 | 0.0048 | 0.2552 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema225_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema225_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema225_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema225_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
