# Autonomy public-indicator hunt gen 1948

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T035542Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1035_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1035_above_at_h` | one_head_filter_pi_star | 109 | 9.0593 | 1.2871 | 0.6055 | 1.1191 | 0.0048 | 0.1376 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1035_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.0925 | 0.5882 | 0.4107 | 0.0017 | 0.1261 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1035_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9725 | 0.5426 | -0.1917 | -0.0006 | 0.1240 | ok | RAN |
| ETHUSDT | 4 | `ema1035_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9717 | 0.5471 | -0.1915 | -0.0009 | 0.1570 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1035_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.8985 | 0.5287 | -0.7406 | -0.0022 | 0.1226 | ok | RAN |
| ETHUSDT | 8 | `ema1035_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 0.9284 | 0.5409 | -0.4863 | -0.0023 | 0.1636 | ok | RAN |
| ETHUSDT | 4 | `ema1035_above_at_h` | one_head_filter_pi_star | 110 | 9.0781 | 0.9345 | 0.5636 | -0.2906 | -0.0028 | 0.1182 | ok | RAN |
| ETHUSDT | 8 | `ema1035_above_at_h` | one_head_filter_pi_star | 115 | 9.4908 | 0.9068 | 0.5391 | -0.4383 | -0.0041 | 0.1130 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1035_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0301 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1035_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1035_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1035_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1035_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1035_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1035_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1035_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1035_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1035_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1035_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1035_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1035_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1035_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1035_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
