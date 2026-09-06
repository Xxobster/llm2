# Autonomy public-indicator hunt gen 1708

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T054628Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1003_above_at_h` | one_head_filter_pi_star | 125 | 10.2506 | 1.1508 | 0.5760 | 0.6726 | 0.0027 | 0.1360 | ok | RAN |
| SOLUSDT | 8 | `ema1003_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.0338 | 0.5641 | 0.1526 | 0.0006 | 0.1282 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1003_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 0.9852 | 0.5451 | -0.1004 | -0.0003 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `ema1003_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9770 | 0.5471 | -0.1553 | -0.0007 | 0.1525 | ok | RAN |
| SOLUSDT | 8 | `ema1003_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9535 | 0.5349 | -0.3261 | -0.0010 | 0.1318 | ok | RAN |
| ETHUSDT | 4 | `ema1003_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 0.9708 | 0.5691 | -0.1337 | -0.0012 | 0.1220 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1003_above_at_h` | one_head_filter_pi_star | 132 | 10.8937 | 0.9482 | 0.5530 | -0.2506 | -0.0022 | 0.1212 | ok | RAN |
| ETHUSDT | 8 | `ema1003_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 0.9288 | 0.5455 | -0.4868 | -0.0023 | 0.1545 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1003_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1003_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1003_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1003_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1003_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1003_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1003_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1003_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1003_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1003_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1003_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1003_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1003_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1003_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1003_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1003_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
