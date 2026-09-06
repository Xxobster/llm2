# Autonomy public-indicator hunt gen 2089

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T203905Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4780_above_at_h` | one_head_filter_pi_star | 67 | 5.5078 | 1.8298 | 0.6716 | 1.8841 | 0.0111 | 0.0896 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4780_above_at_h` | one_head_filter_pi_star | 36 | 3.0929 | 1.5837 | 0.6111 | 1.0152 | 0.0087 | 0.0833 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4780_below_at_h` | one_head_filter_pi_star | 301 | 24.6130 | 0.9764 | 0.5316 | -0.1785 | -0.0005 | 0.1362 | ok | RAN |
| SOLUSDT | 8 | `ema4780_below_at_h` | one_head_filter_pi_star | 321 | 26.2484 | 0.9550 | 0.5358 | -0.3529 | -0.0009 | 0.1340 | ok | RAN |
| ETHUSDT | 4 | `ema4780_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9560 | 0.5565 | -0.3684 | -0.0015 | 0.1362 | ok | RAN |
| ETHUSDT | 8 | `ema4780_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9525 | 0.5539 | -0.3915 | -0.0016 | 0.1370 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4780_above_at_h` | one_head_filter_pi_star | 35 | 10.5618 | 0.8867 | 0.5143 | -0.5456 | -0.0059 | 0.1714 | ok | RAN |
| ETHUSDT | 4 | `ema4780_above_at_h` | one_head_filter_pi_star | 36 | 11.0997 | 0.8587 | 0.5000 | -0.8776 | -0.0072 | 0.1389 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4780_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4780_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
