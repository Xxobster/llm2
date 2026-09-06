# Autonomy public-indicator hunt gen 1059

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T174357Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma605_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 2.0181 | 0.6866 | 4.4423 | 0.0231 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma605_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9147 | 0.6737 | 3.9847 | 0.0218 | 0.3895 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma605_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.8099 | 0.6683 | 3.5802 | 0.0126 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma605_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8111 | 0.6718 | 3.5753 | 0.0123 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma605_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.6156 | 0.6222 | 2.4412 | 0.0094 | 0.3185 | ok | RAN |
| SOLUSDT | 4 | `sma605_above_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.6072 | 0.6205 | 2.5642 | 0.0093 | 0.3072 | ok | RAN |
| ETHUSDT | 8 | `sma605_above_at_h` | one_head_filter_pi_star | 148 | 12.2132 | 1.2069 | 0.6149 | 0.9798 | 0.0074 | 0.2230 | ok | RAN |
| ETHUSDT | 4 | `sma605_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.1839 | 0.5967 | 0.9876 | 0.0066 | 0.2210 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma605_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma605_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma605_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma605_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
