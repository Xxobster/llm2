# Autonomy public-indicator hunt gen 094

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T154127Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `clpos_cross_up_08` | one_head_filter_pi_star | 17 | 1.4467 | 1.2622 | 0.5294 | 0.4120 | 0.0298 | 0.1765 | TPM<MIN | RAN |
| SOLUSDT | 4 | `clpos_cross_up_08` | one_head_filter_pi_star | 206 | 16.8448 | 2.2288 | 0.6942 | 4.6438 | 0.0172 | 0.3592 | EBR>35% | RAN |
| ETHUSDT | 8 | `clpos_cross_down_02` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 8 | `clpos_cross_up_08` | one_head_filter_pi_star | 383 | 31.1578 | 1.5455 | 0.6423 | 3.6302 | 0.0153 | 0.3029 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `clpos_cross_up_08` | one_head_filter_pi_star | 301 | 24.4869 | 1.5472 | 0.6346 | 3.3091 | 0.0147 | 0.3156 | GATE_CAND | RAN |
| ETHUSDT | 4 | `clpos_cross_down_02` | one_head_filter_pi_star | 227 | 18.6591 | 1.3405 | 0.6123 | 1.8451 | 0.0111 | 0.2247 | ok | RAN |
| SOLUSDT | 8 | `clpos_cross_up_08` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 8 | `clpos_cross_down_02` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `clpos_cross_down_02` | one_head_filter_pi_star | 288 | 23.4294 | 1.6014 | 0.6250 | 3.4399 | 0.0087 | 0.2743 | ok | RAN |
| BTCUSDT | 4 | `clpos_cross_down_02` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0067 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `clpos_cross_up_08` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `clpos_cross_down_02` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `clpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `clpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `clpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `clpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `clpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `clpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `clpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `clpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `clpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `clpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `clpos_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `clpos_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
