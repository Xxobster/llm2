# Autonomy public-indicator hunt gen 1969

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T055234Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4480_above_at_h` | one_head_filter_pi_star | 56 | 4.8114 | 2.1114 | 0.6964 | 2.0652 | 0.0134 | 0.1250 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4480_above_at_h` | one_head_filter_pi_star | 64 | 5.2612 | 1.7822 | 0.6562 | 1.7479 | 0.0110 | 0.1094 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4480_below_at_h` | one_head_filter_pi_star | 323 | 26.4120 | 0.9601 | 0.5356 | -0.3114 | -0.0008 | 0.1300 | ok | RAN |
| SOLUSDT | 8 | `ema4480_below_at_h` | one_head_filter_pi_star | 323 | 26.4120 | 0.9484 | 0.5325 | -0.4105 | -0.0011 | 0.1300 | ok | RAN |
| ETHUSDT | 4 | `ema4480_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9643 | 0.5572 | -0.2868 | -0.0012 | 0.1320 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4480_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9488 | 0.5549 | -0.4347 | -0.0017 | 0.1358 | ok | RAN |
| ETHUSDT | 8 | `ema4480_above_at_h` | one_head_filter_pi_star | 35 | 10.5618 | 0.8709 | 0.5143 | -0.6577 | -0.0066 | 0.1143 | ok | RAN |
| ETHUSDT | 4 | `ema4480_above_at_h` | one_head_filter_pi_star | 27 | 8.1477 | 0.7653 | 0.4815 | -1.0042 | -0.0111 | 0.1481 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4480_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4480_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
