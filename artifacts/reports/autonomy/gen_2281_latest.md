# Autonomy public-indicator hunt gen 2281

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T222419Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5260_above_at_h` | one_head_filter_pi_star | 47 | 4.3577 | 2.2231 | 0.6596 | 2.0636 | 0.0145 | 0.1277 | ok | RAN |
| SOLUSDT | 8 | `ema5260_above_at_h` | one_head_filter_pi_star | 49 | 4.5432 | 1.5961 | 0.6122 | 1.2551 | 0.0091 | 0.1224 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5260_below_at_h` | one_head_filter_pi_star | 303 | 24.7766 | 0.9597 | 0.5281 | -0.3054 | -0.0008 | 0.1353 | ok | RAN |
| SOLUSDT | 4 | `ema5260_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9531 | 0.5337 | -0.3699 | -0.0010 | 0.1288 | ok | RAN |
| ETHUSDT | 4 | `ema5260_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9558 | 0.5549 | -0.3712 | -0.0015 | 0.1358 | ok | RAN |
| ETHUSDT | 8 | `ema5260_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9524 | 0.5549 | -0.3902 | -0.0016 | 0.1387 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5260_above_at_h` | one_head_filter_pi_star | 43 | 7.3242 | 0.9252 | 0.5349 | -0.3281 | -0.0033 | 0.1628 | ok | RAN |
| ETHUSDT | 8 | `ema5260_above_at_h` | one_head_filter_pi_star | 48 | 5.6405 | 0.7845 | 0.5000 | -0.9087 | -0.0117 | 0.1458 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5260_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5260_above_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.5417 | 0.2857 | -1.1090 | -0.0579 | 0.0476 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
