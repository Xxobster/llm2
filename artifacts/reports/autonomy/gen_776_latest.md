# Autonomy public-indicator hunt gen 776

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T131746Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1540_below_at_h` | one_head_filter_pi_star | 273 | 22.3016 | 1.7720 | 0.6557 | 4.0532 | 0.0186 | 0.3260 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1540_below_at_h` | one_head_filter_pi_star | 272 | 22.2199 | 1.7376 | 0.6507 | 4.0178 | 0.0181 | 0.3272 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1540_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 2.1822 | 0.7188 | 2.5655 | 0.0153 | 0.3125 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1540_below_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 1.8044 | 0.6349 | 4.1931 | 0.0120 | 0.3191 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1540_below_at_h` | one_head_filter_pi_star | 298 | 24.2429 | 1.7079 | 0.6275 | 3.8133 | 0.0109 | 0.3221 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1540_above_at_h` | one_head_filter_pi_star | 84 | 6.9324 | 1.2676 | 0.5952 | 0.9259 | 0.0098 | 0.2024 | ok | RAN |
| SOLUSDT | 4 | `sma1540_above_at_h` | one_head_filter_pi_star | 67 | 5.5686 | 1.6446 | 0.6866 | 1.8165 | 0.0093 | 0.2836 | ok | RAN |
| ETHUSDT | 4 | `sma1540_above_at_h` | one_head_filter_pi_star | 81 | 6.6848 | 1.0923 | 0.5679 | 0.3349 | 0.0040 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1540_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1540_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
