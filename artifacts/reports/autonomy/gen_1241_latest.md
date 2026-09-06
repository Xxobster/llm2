# Autonomy public-indicator hunt gen 1241

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T143226Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2660_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2660_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.6146 | 0.6437 | 3.6178 | 0.0164 | 0.3114 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema2660_below_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 1.5573 | 0.6392 | 3.5174 | 0.0152 | 0.3011 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2660_below_at_h` | one_head_filter_pi_star | 270 | 21.9650 | 1.9781 | 0.6630 | 4.6148 | 0.0140 | 0.3370 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2660_below_at_h` | one_head_filter_pi_star | 278 | 22.6158 | 1.9207 | 0.6583 | 4.4870 | 0.0136 | 0.3309 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2660_above_at_h` | one_head_filter_pi_star | 108 | 8.9762 | 1.6169 | 0.6389 | 2.1150 | 0.0090 | 0.2685 | ok | RAN |
| SOLUSDT | 8 | `ema2660_above_at_h` | one_head_filter_pi_star | 111 | 9.1025 | 1.5521 | 0.6306 | 1.9153 | 0.0085 | 0.2793 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2660_above_at_h` | one_head_filter_pi_star | 21 | 6.3371 | 0.5418 | 0.3810 | -2.1461 | -0.0301 | 0.2381 | ok | RAN |
| ETHUSDT | 8 | `ema2660_above_at_h` | one_head_filter_pi_star | 19 | 5.7336 | 0.4831 | 0.2632 | -2.4273 | -0.0363 | 0.3158 | ok | RAN |
| BTCUSDT | 8 | `ema2660_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5991 | 0.2941 | -0.8261 | -0.0438 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2660_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
