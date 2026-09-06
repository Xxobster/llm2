# Autonomy public-indicator hunt gen 132

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T180929Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema200_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0021 | 0.7074 | 4.4370 | 0.0238 | 0.3723 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema200_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0051 | 0.6968 | 4.4971 | 0.0231 | 0.3777 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema200_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.1997 | 0.6897 | 4.2731 | 0.0173 | 0.3736 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema200_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1683 | 0.7006 | 4.2360 | 0.0169 | 0.3729 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema200_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1992 | 0.5957 | 1.0248 | 0.0069 | 0.2234 | ok | RAN |
| SOLUSDT | 4 | `ema200_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3677 | 0.5911 | 1.9003 | 0.0057 | 0.2611 | ok | RAN |
| SOLUSDT | 8 | `ema200_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.3211 | 0.5916 | 1.6554 | 0.0050 | 0.2618 | ok | RAN |
| ETHUSDT | 4 | `ema200_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1330 | 0.5895 | 0.7128 | 0.0047 | 0.2158 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema200_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema200_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
