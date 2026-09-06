# Autonomy public-indicator hunt gen 460

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T151944Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema335_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0599 | 0.7010 | 4.5965 | 0.0243 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema335_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8577 | 0.6750 | 4.0011 | 0.0211 | 0.3700 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema335_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.8549 | 0.6583 | 3.6444 | 0.0132 | 0.3618 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema335_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.8761 | 0.6649 | 3.6938 | 0.0131 | 0.3505 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema335_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5159 | 0.6102 | 2.4053 | 0.0080 | 0.2768 | ok | RAN |
| SOLUSDT | 4 | `ema335_above_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.4715 | 0.6047 | 2.1569 | 0.0076 | 0.2907 | ok | RAN |
| ETHUSDT | 8 | `ema335_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2057 | 0.6120 | 1.1002 | 0.0072 | 0.2131 | ok | RAN |
| ETHUSDT | 4 | `ema335_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1678 | 0.5956 | 0.8902 | 0.0060 | 0.2186 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema335_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema335_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema335_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema335_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema335_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema335_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
