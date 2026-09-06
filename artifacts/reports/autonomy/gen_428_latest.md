# Autonomy public-indicator hunt gen 428

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T085016Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema295_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.0258 | 0.6950 | 4.5680 | 0.0236 | 0.3800 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema295_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8374 | 0.6749 | 3.9554 | 0.0207 | 0.3645 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema295_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.9984 | 0.6702 | 3.9474 | 0.0149 | 0.3665 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema295_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.8842 | 0.6583 | 3.7339 | 0.0134 | 0.3518 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema295_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2493 | 0.5989 | 1.2653 | 0.0085 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `ema295_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5046 | 0.6089 | 2.3432 | 0.0077 | 0.2793 | ok | RAN |
| ETHUSDT | 8 | `ema295_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2249 | 0.6032 | 1.1618 | 0.0077 | 0.2116 | ok | RAN |
| SOLUSDT | 8 | `ema295_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4615 | 0.6000 | 2.2343 | 0.0070 | 0.2649 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema295_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema295_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema295_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema295_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
