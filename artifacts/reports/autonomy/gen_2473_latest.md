# Autonomy public-indicator hunt gen 2473

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T221631Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5740_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 1.8542 | 0.6250 | 1.6760 | 0.0114 | 0.1458 | ok | RAN |
| SOLUSDT | 8 | `ema5740_above_at_h` | one_head_filter_pi_star | 49 | 4.2098 | 1.7561 | 0.6327 | 1.4624 | 0.0099 | 0.1020 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5740_below_at_h` | one_head_filter_pi_star | 320 | 26.1667 | 0.9951 | 0.5375 | -0.0374 | -0.0001 | 0.1281 | ok | RAN |
| SOLUSDT | 4 | `ema5740_below_at_h` | one_head_filter_pi_star | 325 | 26.5755 | 0.9424 | 0.5292 | -0.4565 | -0.0012 | 0.1323 | ok | RAN |
| ETHUSDT | 4 | `ema5740_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9524 | 0.5543 | -0.3924 | -0.0016 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5740_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9437 | 0.5526 | -0.4733 | -0.0019 | 0.1345 | ok | RAN |
| ETHUSDT | 8 | `ema5740_above_at_h` | one_head_filter_pi_star | 47 | 8.0055 | 0.7698 | 0.4894 | -1.1417 | -0.0119 | 0.1702 | ok | RAN |
| ETHUSDT | 4 | `ema5740_above_at_h` | one_head_filter_pi_star | 37 | 11.1653 | 0.7504 | 0.4865 | -1.3631 | -0.0136 | 0.1351 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5740_above_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.6195 | 0.3333 | -0.9018 | -0.0462 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5740_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
