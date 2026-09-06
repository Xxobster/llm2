# Autonomy public-indicator hunt gen 710

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T075335Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma350_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0450 | 0.7033 | 4.5162 | 0.0241 | 0.3791 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma350_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9625 | 0.6959 | 4.3662 | 0.0229 | 0.3866 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma350_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2400 | 0.6964 | 4.2288 | 0.0176 | 0.3869 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma350_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.0370 | 0.6788 | 3.7908 | 0.0151 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma350_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2866 | 0.6073 | 1.4858 | 0.0098 | 0.2251 | ok | RAN |
| ETHUSDT | 4 | `wma350_above_at_h` | one_head_filter_pi_star | 194 | 16.0092 | 1.2105 | 0.5979 | 1.1236 | 0.0075 | 0.2216 | ok | RAN |
| SOLUSDT | 4 | `wma350_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3767 | 0.6000 | 1.9002 | 0.0059 | 0.2667 | ok | RAN |
| SOLUSDT | 8 | `wma350_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3411 | 0.5879 | 1.7759 | 0.0053 | 0.2563 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma350_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma350_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma350_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma350_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma350_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma350_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma350_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma350_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma350_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma350_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma350_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma350_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma350_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma350_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma350_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma350_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
