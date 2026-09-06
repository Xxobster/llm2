# Autonomy public-indicator hunt gen 580

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T231250Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema485_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0039 | 0.6845 | 4.2801 | 0.0229 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema485_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9090 | 0.6784 | 4.1214 | 0.0213 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema485_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.9814 | 0.6733 | 4.0577 | 0.0146 | 0.3614 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema485_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.7830 | 0.6507 | 3.4714 | 0.0120 | 0.3254 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema485_above_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.6551 | 0.6264 | 2.7823 | 0.0098 | 0.2931 | ok | RAN |
| ETHUSDT | 4 | `ema485_above_at_h` | one_head_filter_pi_star | 153 | 12.6258 | 1.2587 | 0.6013 | 1.2261 | 0.0089 | 0.2026 | ok | RAN |
| SOLUSDT | 8 | `ema485_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5571 | 0.6196 | 2.5448 | 0.0085 | 0.2609 | ok | RAN |
| ETHUSDT | 8 | `ema485_above_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.1034 | 0.5904 | 0.5263 | 0.0039 | 0.1988 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema485_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema485_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema485_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema485_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema485_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema485_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
