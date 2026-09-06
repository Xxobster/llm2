# Autonomy public-indicator hunt gen 1684

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T025335Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema999_above_at_h` | one_head_filter_pi_star | 125 | 10.2740 | 1.1989 | 0.6000 | 0.8519 | 0.0036 | 0.1360 | ok | RAN |
| ETHUSDT | 8 | `ema999_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 1.0162 | 0.5639 | 0.0729 | 0.0007 | 0.1278 | ok | RAN |
| SOLUSDT | 8 | `ema999_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.0223 | 0.5714 | 0.1018 | 0.0004 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema999_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 1.0032 | 0.5528 | 0.0210 | 0.0001 | 0.1220 | ok | RAN |
| ETHUSDT | 8 | `ema999_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.9753 | 0.5511 | -0.1671 | -0.0008 | 0.1556 | ok | RAN |
| SOLUSDT | 8 | `ema999_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9637 | 0.5367 | -0.2533 | -0.0008 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema999_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 0.9462 | 0.5547 | -0.2514 | -0.0023 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema999_below_at_h` | one_head_filter_pi_star | 244 | 19.9326 | 0.9216 | 0.5410 | -0.5759 | -0.0026 | 0.1475 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema999_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema999_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema999_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema999_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema999_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema999_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema999_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema999_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema999_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema999_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema999_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema999_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema999_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema999_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema999_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema999_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
