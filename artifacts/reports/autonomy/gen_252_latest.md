# Autonomy public-indicator hunt gen 252

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T020604Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema88_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.9242 | 0.6919 | 4.2194 | 0.0227 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema88_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8089 | 0.6798 | 3.9830 | 0.0206 | 0.3645 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema88_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2296 | 0.6923 | 4.2657 | 0.0181 | 0.3964 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema88_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2509 | 0.6941 | 4.3163 | 0.0180 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema88_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2586 | 0.6044 | 1.2535 | 0.0083 | 0.2198 | ok | RAN |
| ETHUSDT | 8 | `ema88_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.1675 | 0.5926 | 0.8492 | 0.0056 | 0.2169 | ok | RAN |
| SOLUSDT | 8 | `ema88_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3395 | 0.5924 | 1.7920 | 0.0051 | 0.2559 | ok | RAN |
| SOLUSDT | 4 | `ema88_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.2618 | 0.5784 | 1.4265 | 0.0040 | 0.2549 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema88_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema88_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema88_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema88_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
