# Autonomy public-indicator hunt gen 315

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T063348Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma108_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9174 | 0.6816 | 4.3311 | 0.0223 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma108_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9354 | 0.6834 | 4.3743 | 0.0222 | 0.3618 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma108_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.3569 | 0.6983 | 4.6188 | 0.0188 | 0.3799 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma108_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2538 | 0.6946 | 4.2961 | 0.0184 | 0.4012 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma108_above_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.3159 | 0.6102 | 1.5075 | 0.0098 | 0.2147 | ok | RAN |
| ETHUSDT | 4 | `sma108_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2921 | 0.6111 | 1.4142 | 0.0092 | 0.2056 | ok | RAN |
| SOLUSDT | 4 | `sma108_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.2765 | 0.5960 | 1.4796 | 0.0044 | 0.2626 | ok | RAN |
| SOLUSDT | 8 | `sma108_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2799 | 0.5854 | 1.5126 | 0.0044 | 0.2585 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma108_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma108_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma108_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma108_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma108_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma108_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
