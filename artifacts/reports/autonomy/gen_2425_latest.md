# Autonomy public-indicator hunt gen 2425

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T164404Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5620_above_at_h` | one_head_filter_pi_star | 32 | 2.9670 | 2.3122 | 0.6250 | 1.7260 | 0.0135 | 0.0625 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema5620_above_at_h` | one_head_filter_pi_star | 37 | 3.4306 | 2.0410 | 0.6486 | 1.6713 | 0.0129 | 0.1081 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5620_below_at_h` | one_head_filter_pi_star | 325 | 26.5755 | 0.9660 | 0.5354 | -0.2670 | -0.0007 | 0.1323 | ok | RAN |
| SOLUSDT | 8 | `ema5620_below_at_h` | one_head_filter_pi_star | 306 | 25.0219 | 0.9323 | 0.5229 | -0.5288 | -0.0014 | 0.1307 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5620_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9485 | 0.5529 | -0.4265 | -0.0017 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `ema5620_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9479 | 0.5539 | -0.4445 | -0.0017 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `ema5620_above_at_h` | one_head_filter_pi_star | 39 | 10.5605 | 0.8071 | 0.4872 | -0.9599 | -0.0096 | 0.1282 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema5620_above_at_h` | one_head_filter_pi_star | 47 | 5.5230 | 0.7091 | 0.4894 | -1.2012 | -0.0166 | 0.1702 | ok | RAN |
| BTCUSDT | 8 | `ema5620_above_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.5417 | 0.2857 | -1.1090 | -0.0569 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5620_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
