# Autonomy public-indicator hunt gen 2036

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T132406Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1047_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1047_above_at_h` | one_head_filter_pi_star | 93 | 7.6438 | 1.3086 | 0.6237 | 1.1178 | 0.0049 | 0.1505 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1047_above_at_h` | one_head_filter_pi_star | 107 | 8.7248 | 1.1124 | 0.5794 | 0.4696 | 0.0020 | 0.1589 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1047_below_at_h` | one_head_filter_pi_star | 260 | 21.1515 | 0.9882 | 0.5462 | -0.0819 | -0.0003 | 0.1308 | ok | RAN |
| ETHUSDT | 4 | `ema1047_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.9866 | 0.5511 | -0.0885 | -0.0004 | 0.1511 | ok | RAN |
| ETHUSDT | 4 | `ema1047_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 0.9744 | 0.5600 | -0.1170 | -0.0011 | 0.1360 | ok | RAN |
| ETHUSDT | 8 | `ema1047_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9640 | 0.5474 | -0.2505 | -0.0011 | 0.1552 | ok | RAN |
| SOLUSDT | 4 | `ema1047_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9307 | 0.5391 | -0.4860 | -0.0015 | 0.1328 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1047_above_at_h` | one_head_filter_pi_star | 122 | 10.0676 | 0.8858 | 0.5328 | -0.5471 | -0.0049 | 0.1230 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1047_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1047_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0612 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1047_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1047_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1047_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1047_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1047_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1047_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1047_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1047_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1047_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1047_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1047_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1047_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1047_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
