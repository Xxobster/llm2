# Autonomy public-indicator hunt gen 2441

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T183844Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5660_above_at_h` | one_head_filter_pi_star | 40 | 3.7087 | 2.3757 | 0.6500 | 2.0291 | 0.0160 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5660_above_at_h` | one_head_filter_pi_star | 57 | 4.7986 | 1.3271 | 0.5965 | 0.8705 | 0.0055 | 0.1053 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5660_below_at_h` | one_head_filter_pi_star | 332 | 27.1479 | 0.9908 | 0.5422 | -0.0716 | -0.0002 | 0.1265 | ok | RAN |
| SOLUSDT | 8 | `ema5660_below_at_h` | one_head_filter_pi_star | 329 | 26.9026 | 0.9736 | 0.5380 | -0.2077 | -0.0005 | 0.1277 | ok | RAN |
| ETHUSDT | 8 | `ema5660_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 0.9675 | 0.5575 | -0.2680 | -0.0011 | 0.1351 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5660_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9473 | 0.5549 | -0.4436 | -0.0018 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `ema5660_above_at_h` | one_head_filter_pi_star | 49 | 5.7580 | 0.7856 | 0.4898 | -0.8492 | -0.0117 | 0.1429 | ok | RAN |
| ETHUSDT | 8 | `ema5660_above_at_h` | one_head_filter_pi_star | 43 | 12.5508 | 0.7734 | 0.4884 | -1.3566 | -0.0118 | 0.1628 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5660_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6281 | 0.3158 | -0.8186 | -0.0428 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5660_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0628 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
