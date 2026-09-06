# Autonomy public-indicator hunt gen 1385

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T041445Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema3020_below_at_h` | one_head_filter_pi_star | 353 | 28.7172 | 1.5813 | 0.6431 | 3.6494 | 0.0158 | 0.3003 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema3020_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.5544 | 0.6395 | 3.4520 | 0.0151 | 0.3023 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3020_below_at_h` | one_head_filter_pi_star | 282 | 23.0594 | 1.9220 | 0.6525 | 4.5847 | 0.0136 | 0.3262 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3020_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.8503 | 0.6616 | 4.1290 | 0.0131 | 0.3498 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema3020_above_at_h` | one_head_filter_pi_star | 75 | 6.1644 | 1.7318 | 0.6667 | 1.8786 | 0.0099 | 0.2400 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3020_above_at_h` | one_head_filter_pi_star | 92 | 7.5629 | 1.6063 | 0.6413 | 1.7830 | 0.0089 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `ema3020_above_at_h` | one_head_filter_pi_star | 36 | 4.1036 | 1.1743 | 0.5556 | 0.4567 | 0.0072 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema3020_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7147 | 0.3158 | -0.5739 | -0.0285 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema3020_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0290 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3020_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
