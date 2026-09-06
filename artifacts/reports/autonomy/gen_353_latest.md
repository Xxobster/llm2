# Autonomy public-indicator hunt gen 353

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T153229Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema440_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9487 | 0.6878 | 4.1594 | 0.0220 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema440_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.8649 | 0.6789 | 4.1065 | 0.0214 | 0.3532 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema440_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8527 | 0.6618 | 3.6776 | 0.0132 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema440_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8526 | 0.6569 | 3.6524 | 0.0127 | 0.3382 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema440_above_at_h` | one_head_filter_pi_star | 165 | 13.6160 | 1.2713 | 0.6182 | 1.2994 | 0.0096 | 0.2121 | ok | RAN |
| ETHUSDT | 4 | `ema440_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2428 | 0.6051 | 1.1795 | 0.0085 | 0.1911 | ok | RAN |
| SOLUSDT | 4 | `ema440_above_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5366 | 0.6114 | 2.4265 | 0.0084 | 0.2857 | ok | RAN |
| SOLUSDT | 8 | `ema440_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4591 | 0.6108 | 2.1763 | 0.0074 | 0.2595 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema440_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema440_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
