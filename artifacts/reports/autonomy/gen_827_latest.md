# Autonomy public-indicator hunt gen 827

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T181326Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma528_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0967 | 0.6923 | 4.5467 | 0.0250 | 0.3901 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma528_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 2.0966 | 0.7010 | 4.8070 | 0.0240 | 0.3725 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma528_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.9215 | 0.6683 | 3.7928 | 0.0130 | 0.3367 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma528_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8680 | 0.6701 | 3.7560 | 0.0128 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma528_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.6775 | 0.6175 | 2.9515 | 0.0101 | 0.3060 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma528_above_at_h` | one_head_filter_pi_star | 161 | 13.1280 | 1.5790 | 0.6149 | 2.4415 | 0.0088 | 0.2919 | ok | RAN |
| ETHUSDT | 4 | `sma528_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1444 | 0.5938 | 0.7885 | 0.0052 | 0.2135 | ok | RAN |
| ETHUSDT | 8 | `sma528_above_at_h` | one_head_filter_pi_star | 149 | 12.2957 | 1.1108 | 0.5772 | 0.5428 | 0.0041 | 0.2148 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma528_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma528_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma528_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma528_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma528_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma528_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
