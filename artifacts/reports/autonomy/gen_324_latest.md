# Autonomy public-indicator hunt gen 324

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T110208Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema175_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0881 | 0.7005 | 4.7439 | 0.0247 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema175_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0940 | 0.7026 | 4.7224 | 0.0244 | 0.3692 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema175_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1402 | 0.6970 | 4.0041 | 0.0167 | 0.3879 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema175_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.1212 | 0.6910 | 4.1664 | 0.0164 | 0.3708 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema175_above_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.2213 | 0.6044 | 1.0975 | 0.0077 | 0.2308 | ok | RAN |
| SOLUSDT | 4 | `ema175_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3365 | 0.5874 | 1.7901 | 0.0052 | 0.2670 | ok | RAN |
| SOLUSDT | 8 | `ema175_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3370 | 0.5959 | 1.7290 | 0.0052 | 0.2642 | ok | RAN |
| ETHUSDT | 4 | `ema175_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.1363 | 0.5873 | 0.7253 | 0.0048 | 0.2169 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema175_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema175_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema175_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema175_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
