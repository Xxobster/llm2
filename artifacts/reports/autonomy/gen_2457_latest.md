# Autonomy public-indicator hunt gen 2457

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T202742Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5700_above_at_h` | one_head_filter_pi_star | 47 | 3.9567 | 1.9932 | 0.6170 | 1.7381 | 0.0118 | 0.1277 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5700_above_at_h` | one_head_filter_pi_star | 42 | 3.6507 | 1.7438 | 0.6190 | 1.3507 | 0.0099 | 0.1190 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5700_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9696 | 0.5368 | -0.2379 | -0.0006 | 0.1288 | ok | RAN |
| SOLUSDT | 4 | `ema5700_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9589 | 0.5314 | -0.3190 | -0.0009 | 0.1352 | ok | RAN |
| ETHUSDT | 4 | `ema5700_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9625 | 0.5581 | -0.3088 | -0.0012 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5700_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9468 | 0.5526 | -0.4398 | -0.0018 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `ema5700_above_at_h` | one_head_filter_pi_star | 35 | 10.5618 | 0.9344 | 0.5429 | -0.3222 | -0.0032 | 0.1143 | ok | RAN |
| ETHUSDT | 8 | `ema5700_above_at_h` | one_head_filter_pi_star | 46 | 13.3837 | 0.7272 | 0.4783 | -1.7996 | -0.0158 | 0.1739 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5700_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6281 | 0.3158 | -0.8186 | -0.0412 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5700_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
