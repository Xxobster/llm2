# Autonomy public-indicator hunt gen 2497

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T005046Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5800_above_at_h` | one_head_filter_pi_star | 43 | 3.6943 | 1.5962 | 0.5814 | 1.1467 | 0.0088 | 0.1163 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5800_above_at_h` | one_head_filter_pi_star | 43 | 4.0373 | 1.6238 | 0.6279 | 1.2656 | 0.0085 | 0.1628 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5800_below_at_h` | one_head_filter_pi_star | 333 | 27.2297 | 0.9526 | 0.5345 | -0.3782 | -0.0010 | 0.1261 | ok | RAN |
| ETHUSDT | 4 | `ema5800_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9706 | 0.5569 | -0.2439 | -0.0010 | 0.1341 | ok | RAN |
| SOLUSDT | 8 | `ema5800_below_at_h` | one_head_filter_pi_star | 332 | 27.1479 | 0.9317 | 0.5301 | -0.5496 | -0.0014 | 0.1295 | ok | RAN |
| ETHUSDT | 8 | `ema5800_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9527 | 0.5536 | -0.3874 | -0.0015 | 0.1369 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5800_above_at_h` | one_head_filter_pi_star | 39 | 11.7689 | 0.7657 | 0.4872 | -1.2253 | -0.0118 | 0.1282 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5800_above_at_h` | one_head_filter_pi_star | 47 | 8.0055 | 0.6066 | 0.4468 | -2.0776 | -0.0225 | 0.1489 | ok | RAN |
| BTCUSDT | 8 | `ema5800_above_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.5417 | 0.2857 | -1.1090 | -0.0549 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5800_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
