# Autonomy public-indicator hunt gen 1219

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T120910Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma631_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1565 | 0.6940 | 4.5834 | 0.0259 | 0.3934 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma631_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9520 | 0.6734 | 4.2394 | 0.0223 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma631_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.6889 | 0.6599 | 3.1357 | 0.0110 | 0.3198 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma631_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.6462 | 0.6580 | 2.9709 | 0.0104 | 0.3316 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma631_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.5339 | 0.6220 | 1.9965 | 0.0081 | 0.3307 | ok | RAN |
| SOLUSDT | 4 | `sma631_above_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.5159 | 0.6051 | 2.1818 | 0.0080 | 0.3057 | ok | RAN |
| ETHUSDT | 8 | `sma631_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.1967 | 0.6000 | 0.9577 | 0.0071 | 0.2258 | ok | RAN |
| ETHUSDT | 4 | `sma631_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.0648 | 0.5714 | 0.3453 | 0.0025 | 0.2174 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma631_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma631_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma631_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma631_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma631_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma631_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma631_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma631_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma631_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma631_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma631_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma631_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma631_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma631_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma631_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma631_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
