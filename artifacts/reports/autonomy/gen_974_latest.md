# Autonomy public-indicator hunt gen 974

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T215614Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma515_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0167 | 0.6947 | 4.4432 | 0.0236 | 0.3895 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma515_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9407 | 0.6907 | 4.2908 | 0.0228 | 0.3866 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma515_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.0544 | 0.6831 | 4.1044 | 0.0151 | 0.3770 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma515_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.9958 | 0.6739 | 3.9276 | 0.0146 | 0.3641 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma515_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2324 | 0.5938 | 1.2139 | 0.0082 | 0.2240 | ok | RAN |
| SOLUSDT | 8 | `wma515_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.4873 | 0.6124 | 2.2582 | 0.0075 | 0.2640 | ok | RAN |
| ETHUSDT | 4 | `wma515_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2056 | 0.5968 | 1.0860 | 0.0074 | 0.2151 | ok | RAN |
| SOLUSDT | 4 | `wma515_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4169 | 0.6020 | 2.0958 | 0.0066 | 0.2653 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma515_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma515_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma515_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma515_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma515_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma515_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
