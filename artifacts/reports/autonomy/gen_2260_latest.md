# Autonomy public-indicator hunt gen 2260

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T195152Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1076_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.3207 | 0.6055 | 1.1986 | 0.0053 | 0.1376 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1076_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.1537 | 0.5965 | 0.6657 | 0.0027 | 0.1228 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1076_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9708 | 0.5517 | -0.2043 | -0.0009 | 0.1509 | ok | RAN |
| SOLUSDT | 8 | `ema1076_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 0.9361 | 0.5318 | -0.4613 | -0.0014 | 0.1273 | ok | RAN |
| SOLUSDT | 4 | `ema1076_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 0.9257 | 0.5373 | -0.5364 | -0.0016 | 0.1381 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1076_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 0.9342 | 0.5375 | -0.4689 | -0.0021 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `ema1076_above_at_h` | one_head_filter_pi_star | 115 | 9.4908 | 0.8918 | 0.5565 | -0.4927 | -0.0047 | 0.1130 | ok | RAN |
| ETHUSDT | 8 | `ema1076_above_at_h` | one_head_filter_pi_star | 107 | 8.8305 | 0.8040 | 0.5234 | -0.9319 | -0.0088 | 0.1215 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1076_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1076_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1076_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1076_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1076_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1076_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1076_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1076_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1076_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1076_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1076_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1076_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1076_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1076_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1076_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1076_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
