# Autonomy public-indicator hunt gen 747

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T103540Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma466_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0808 | 0.7026 | 4.5946 | 0.0246 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma466_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0588 | 0.6959 | 4.5128 | 0.0241 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma466_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.9799 | 0.6780 | 3.8233 | 0.0147 | 0.3616 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma466_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.9296 | 0.6742 | 3.6360 | 0.0137 | 0.3652 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma466_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.3113 | 0.6118 | 1.4874 | 0.0103 | 0.2118 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma466_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.6124 | 0.6158 | 2.7544 | 0.0094 | 0.2789 | ok | RAN |
| SOLUSDT | 8 | `sma466_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4949 | 0.6054 | 2.3145 | 0.0080 | 0.2703 | ok | RAN |
| ETHUSDT | 4 | `sma466_above_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.1540 | 0.5780 | 0.7979 | 0.0057 | 0.2197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma466_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma466_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma466_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma466_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma466_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma466_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
