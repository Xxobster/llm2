# Autonomy public-indicator hunt gen 1980

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T065234Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1039_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.3735 | 0.6195 | 1.3993 | 0.0061 | 0.1504 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1039_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.2090 | 0.5982 | 0.8482 | 0.0036 | 0.1339 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1039_below_at_h` | one_head_filter_pi_star | 267 | 21.7210 | 0.9844 | 0.5393 | -0.1088 | -0.0003 | 0.1311 | ok | RAN |
| SOLUSDT | 4 | `ema1039_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 0.9459 | 0.5361 | -0.3851 | -0.0012 | 0.1293 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1039_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 0.9429 | 0.5365 | -0.4061 | -0.0018 | 0.1502 | ok | RAN |
| ETHUSDT | 8 | `ema1039_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 0.9418 | 0.5410 | -0.2684 | -0.0025 | 0.1311 | ok | RAN |
| ETHUSDT | 8 | `ema1039_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9042 | 0.5431 | -0.6982 | -0.0032 | 0.1509 | ok | RAN |
| ETHUSDT | 4 | `ema1039_above_at_h` | one_head_filter_pi_star | 120 | 9.8638 | 0.8858 | 0.5333 | -0.5480 | -0.0049 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1039_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1039_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1039_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1039_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1039_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1039_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1039_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1039_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1039_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1039_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1039_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1039_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1039_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1039_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1039_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1039_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
