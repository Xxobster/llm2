# Autonomy public-indicator hunt gen 2169

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T075035Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4980_above_at_h` | one_head_filter_pi_star | 36 | 3.3801 | 1.9324 | 0.6389 | 1.4622 | 0.0130 | 0.0833 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4980_above_at_h` | one_head_filter_pi_star | 68 | 5.5900 | 1.5782 | 0.6471 | 1.4994 | 0.0088 | 0.1176 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4980_below_at_h` | one_head_filter_pi_star | 325 | 26.5755 | 0.9963 | 0.5415 | -0.0282 | -0.0001 | 0.1385 | ok | RAN |
| SOLUSDT | 4 | `ema4980_below_at_h` | one_head_filter_pi_star | 308 | 25.1854 | 0.9796 | 0.5292 | -0.1554 | -0.0004 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `ema4980_below_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 0.9822 | 0.5597 | -0.1470 | -0.0006 | 0.1364 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4980_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9481 | 0.5539 | -0.4280 | -0.0017 | 0.1370 | ok | RAN |
| ETHUSDT | 4 | `ema4980_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.9399 | 0.5405 | -0.3027 | -0.0030 | 0.1351 | ok | RAN |
| ETHUSDT | 8 | `ema4980_above_at_h` | one_head_filter_pi_star | 37 | 10.7995 | 0.8203 | 0.5135 | -1.0034 | -0.0098 | 0.1351 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4980_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4980_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
