# Autonomy public-indicator hunt gen 2092

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T210648Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1054_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.2942 | 0.6102 | 1.1629 | 0.0051 | 0.1441 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1054_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.0723 | 0.5648 | 0.3101 | 0.0013 | 0.1296 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1054_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9937 | 0.5547 | -0.0427 | -0.0001 | 0.1328 | ok | RAN |
| ETHUSDT | 4 | `ema1054_below_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 0.9817 | 0.5571 | -0.1203 | -0.0006 | 0.1571 | ok | RAN |
| SOLUSDT | 8 | `ema1054_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 0.9710 | 0.5444 | -0.1979 | -0.0006 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1054_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 0.9100 | 0.5479 | -0.6224 | -0.0029 | 0.1553 | ok | RAN |
| ETHUSDT | 4 | `ema1054_above_at_h` | one_head_filter_pi_star | 128 | 10.5636 | 0.9222 | 0.5547 | -0.3728 | -0.0034 | 0.1094 | ok | RAN |
| ETHUSDT | 8 | `ema1054_above_at_h` | one_head_filter_pi_star | 123 | 10.1104 | 0.8769 | 0.5447 | -0.5832 | -0.0054 | 0.1220 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1054_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0321 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1054_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1054_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1054_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1054_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1054_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1054_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1054_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1054_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1054_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1054_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1054_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1054_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1054_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1054_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1054_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
