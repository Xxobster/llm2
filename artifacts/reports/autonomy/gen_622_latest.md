# Autonomy public-indicator hunt gen 622

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T015543Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma295_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1741 | 0.7167 | 4.8070 | 0.0258 | 0.3833 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma295_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.8898 | 0.6895 | 4.0856 | 0.0216 | 0.3789 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma295_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2090 | 0.6977 | 4.2441 | 0.0171 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma295_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1505 | 0.6886 | 4.0351 | 0.0167 | 0.3772 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma295_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2462 | 0.6053 | 1.2272 | 0.0085 | 0.2316 | ok | RAN |
| SOLUSDT | 4 | `wma295_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3914 | 0.5980 | 1.9850 | 0.0061 | 0.2613 | ok | RAN |
| ETHUSDT | 8 | `wma295_above_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.1603 | 0.5900 | 0.8591 | 0.0057 | 0.2300 | ok | RAN |
| SOLUSDT | 8 | `wma295_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3630 | 0.5941 | 1.8846 | 0.0056 | 0.2624 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma295_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma295_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma295_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma295_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma295_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma295_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
