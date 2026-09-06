# Autonomy public-indicator hunt gen 2140

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T032144Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1061_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1061_above_at_h` | one_head_filter_pi_star | 109 | 9.0593 | 1.2400 | 0.6055 | 0.9589 | 0.0043 | 0.1560 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1061_above_at_h` | one_head_filter_pi_star | 110 | 9.0411 | 1.2018 | 0.6000 | 0.8355 | 0.0035 | 0.1364 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1061_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 0.9422 | 0.5424 | -0.3848 | -0.0012 | 0.1356 | ok | RAN |
| SOLUSDT | 4 | `ema1061_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9269 | 0.5364 | -0.5222 | -0.0016 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1061_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 0.9477 | 0.5411 | -0.3664 | -0.0017 | 0.1515 | ok | RAN |
| ETHUSDT | 4 | `ema1061_above_at_h` | one_head_filter_pi_star | 130 | 10.7287 | 0.9353 | 0.5538 | -0.3211 | -0.0028 | 0.1308 | ok | RAN |
| ETHUSDT | 8 | `ema1061_above_at_h` | one_head_filter_pi_star | 125 | 10.2748 | 0.9114 | 0.5440 | -0.4238 | -0.0038 | 0.1280 | ok | RAN |
| ETHUSDT | 8 | `ema1061_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.8709 | 0.5371 | -0.9493 | -0.0043 | 0.1528 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1061_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1061_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1061_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1061_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1061_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1061_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1061_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1061_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1061_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1061_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1061_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1061_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1061_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1061_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1061_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
