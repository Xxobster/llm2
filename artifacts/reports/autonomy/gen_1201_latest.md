# Autonomy public-indicator hunt gen 1201

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T102225Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2560_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0908 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2560_below_at_h` | one_head_filter_pi_star | 354 | 28.7986 | 1.5987 | 0.6441 | 3.7346 | 0.0160 | 0.2994 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2560_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.5685 | 0.6412 | 3.5189 | 0.0155 | 0.3088 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2560_below_at_h` | one_head_filter_pi_star | 267 | 21.7210 | 1.8875 | 0.6592 | 4.2201 | 0.0132 | 0.3371 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2560_below_at_h` | one_head_filter_pi_star | 271 | 22.0464 | 1.8810 | 0.6531 | 4.2741 | 0.0131 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2560_above_at_h` | one_head_filter_pi_star | 105 | 8.6301 | 1.5966 | 0.6381 | 1.9933 | 0.0089 | 0.2762 | ok | RAN |
| SOLUSDT | 4 | `ema2560_above_at_h` | one_head_filter_pi_star | 115 | 9.4521 | 1.5272 | 0.6174 | 1.9496 | 0.0086 | 0.2870 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2560_above_at_h` | one_head_filter_pi_star | 22 | 6.6389 | 0.8894 | 0.4091 | -0.4696 | -0.0066 | 0.2273 | ok | RAN |
| ETHUSDT | 8 | `ema2560_above_at_h` | one_head_filter_pi_star | 16 | 4.8283 | 0.6408 | 0.3750 | -1.4451 | -0.0218 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `ema2560_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0301 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2560_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0454 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
