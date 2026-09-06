# Autonomy public-indicator hunt gen 1356

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T013410Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema951_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.8385 | 0.6582 | 3.9806 | 0.0200 | 0.3418 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema951_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8719 | 0.6683 | 3.7355 | 0.0199 | 0.3805 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema951_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.8090 | 0.6479 | 4.0643 | 0.0124 | 0.3071 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema951_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 1.7377 | 0.6426 | 3.6393 | 0.0119 | 0.3052 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema951_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.7132 | 0.6581 | 2.4226 | 0.0104 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema951_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.2645 | 0.6122 | 1.2644 | 0.0100 | 0.2381 | ok | RAN |
| SOLUSDT | 4 | `ema951_above_at_h` | one_head_filter_pi_star | 128 | 10.5211 | 1.6596 | 0.6328 | 2.3715 | 0.0100 | 0.3047 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema951_above_at_h` | one_head_filter_pi_star | 131 | 10.7680 | 1.1226 | 0.5725 | 0.5569 | 0.0048 | 0.1985 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema951_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema951_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema951_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema951_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema951_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema951_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema951_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema951_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema951_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema951_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema951_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema951_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema951_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema951_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema951_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema951_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
