# Autonomy public-indicator hunt gen 1796

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T140304Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1015_above_at_h` | one_head_filter_pi_star | 123 | 10.1096 | 1.1568 | 0.5691 | 0.6713 | 0.0028 | 0.1301 | ok | RAN |
| SOLUSDT | 8 | `ema1015_above_at_h` | one_head_filter_pi_star | 119 | 9.7586 | 1.0872 | 0.5630 | 0.3953 | 0.0016 | 0.1092 | ok | RAN |
| SOLUSDT | 8 | `ema1015_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.0409 | 0.5506 | 0.2672 | 0.0008 | 0.1255 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1015_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 0.9850 | 0.5486 | -0.1017 | -0.0003 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `ema1015_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 0.9869 | 0.5500 | -0.0925 | -0.0004 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1015_above_at_h` | one_head_filter_pi_star | 127 | 10.4811 | 0.9559 | 0.5669 | -0.2091 | -0.0019 | 0.1181 | ok | RAN |
| ETHUSDT | 8 | `ema1015_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 0.9169 | 0.5304 | -0.5943 | -0.0027 | 0.1478 | ok | RAN |
| ETHUSDT | 8 | `ema1015_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 0.7720 | 0.5135 | -1.0987 | -0.0107 | 0.1171 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1015_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1015_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1015_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1015_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1015_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1015_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1015_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1015_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1015_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1015_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1015_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1015_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1015_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1015_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1015_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1015_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
