# Autonomy public-indicator hunt gen 1764

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T110353Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1011_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.2590 | 0.6036 | 1.0340 | 0.0044 | 0.1351 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1011_above_at_h` | one_head_filter_pi_star | 116 | 9.5342 | 1.1501 | 0.6034 | 0.6468 | 0.0026 | 0.1466 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1011_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 0.9752 | 0.5447 | -0.1725 | -0.0005 | 0.1284 | ok | RAN |
| ETHUSDT | 4 | `ema1011_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9817 | 0.5426 | -0.1248 | -0.0006 | 0.1525 | ok | RAN |
| SOLUSDT | 8 | `ema1011_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9654 | 0.5402 | -0.2417 | -0.0007 | 0.1226 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1011_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 0.9388 | 0.5462 | -0.4477 | -0.0020 | 0.1471 | ok | RAN |
| ETHUSDT | 8 | `ema1011_above_at_h` | one_head_filter_pi_star | 132 | 10.8937 | 0.9387 | 0.5455 | -0.2983 | -0.0026 | 0.1136 | ok | RAN |
| ETHUSDT | 4 | `ema1011_above_at_h` | one_head_filter_pi_star | 138 | 11.3880 | 0.8594 | 0.5362 | -0.7241 | -0.0063 | 0.1087 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1011_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1011_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1011_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1011_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1011_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1011_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1011_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1011_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1011_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1011_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1011_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1011_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1011_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1011_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1011_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1011_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
