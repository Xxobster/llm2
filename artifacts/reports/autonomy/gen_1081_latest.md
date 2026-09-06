# Autonomy public-indicator hunt gen 1081

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T203544Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2260_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0833 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2260_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.6282 | 0.6465 | 3.6789 | 0.0165 | 0.3082 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2260_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.5964 | 0.6447 | 3.6946 | 0.0159 | 0.3009 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2260_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 1.9351 | 0.6618 | 4.5238 | 0.0142 | 0.3272 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2260_below_at_h` | one_head_filter_pi_star | 274 | 22.2904 | 1.8115 | 0.6496 | 4.0786 | 0.0125 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2260_above_at_h` | one_head_filter_pi_star | 98 | 8.0548 | 1.8244 | 0.6633 | 2.3980 | 0.0107 | 0.2653 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2260_above_at_h` | one_head_filter_pi_star | 98 | 8.0548 | 1.7370 | 0.6531 | 2.2501 | 0.0104 | 0.2653 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2260_above_at_h` | one_head_filter_pi_star | 14 | 1.6451 | 0.6510 | 0.3571 | -0.7870 | -0.0245 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema2260_above_at_h` | one_head_filter_pi_star | 16 | 4.9863 | 0.5406 | 0.3125 | -2.1365 | -0.0293 | 0.3125 | ok | RAN |
| BTCUSDT | 8 | `ema2260_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6134 | 0.3529 | -0.7970 | -0.0422 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2260_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3421 | 0.2143 | -1.4008 | -0.0764 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
