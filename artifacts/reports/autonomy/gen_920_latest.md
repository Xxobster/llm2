# Autonomy public-indicator hunt gen 920

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T033812Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1900_below_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.5720 | 0.6394 | 3.4894 | 0.0156 | 0.3091 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma1900_below_at_h` | one_head_filter_pi_star | 304 | 24.8340 | 1.5072 | 0.6382 | 3.0766 | 0.0136 | 0.3224 | ok | RAN |
| SOLUSDT | 8 | `sma1900_below_at_h` | one_head_filter_pi_star | 300 | 24.4056 | 1.8710 | 0.6500 | 4.4340 | 0.0129 | 0.3233 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1900_below_at_h` | one_head_filter_pi_star | 305 | 24.8124 | 1.7602 | 0.6328 | 4.0226 | 0.0115 | 0.3180 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1900_above_at_h` | one_head_filter_pi_star | 72 | 5.9851 | 1.7672 | 0.6944 | 1.8854 | 0.0110 | 0.2917 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1900_above_at_h` | one_head_filter_pi_star | 62 | 5.1539 | 1.6536 | 0.6613 | 1.6820 | 0.0101 | 0.2742 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1900_above_at_h` | one_head_filter_pi_star | 39 | 3.5279 | 1.1043 | 0.5641 | 0.2724 | 0.0044 | 0.3077 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1900_above_at_h` | one_head_filter_pi_star | 42 | 3.7993 | 1.0718 | 0.5476 | 0.1957 | 0.0032 | 0.2619 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1900_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0585 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1900_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0624 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1900_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1900_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1900_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
