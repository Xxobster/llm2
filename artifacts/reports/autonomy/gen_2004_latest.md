# Autonomy public-indicator hunt gen 2004

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T094150Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1043_above_at_h` | one_head_filter_pi_star | 110 | 8.9694 | 1.2260 | 0.5909 | 0.8900 | 0.0037 | 0.1273 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1043_above_at_h` | one_head_filter_pi_star | 111 | 9.2255 | 1.1364 | 0.5856 | 0.5777 | 0.0026 | 0.1441 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1043_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9848 | 0.5502 | -0.1033 | -0.0005 | 0.1528 | ok | RAN |
| SOLUSDT | 8 | `ema1043_below_at_h` | one_head_filter_pi_star | 259 | 21.0702 | 0.9653 | 0.5405 | -0.2392 | -0.0007 | 0.1236 | ok | RAN |
| SOLUSDT | 4 | `ema1043_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9642 | 0.5430 | -0.2489 | -0.0008 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1043_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 0.9378 | 0.5394 | -0.4574 | -0.0020 | 0.1494 | ok | RAN |
| ETHUSDT | 4 | `ema1043_above_at_h` | one_head_filter_pi_star | 118 | 9.7383 | 0.9257 | 0.5424 | -0.3350 | -0.0033 | 0.1186 | ok | RAN |
| ETHUSDT | 8 | `ema1043_above_at_h` | one_head_filter_pi_star | 118 | 9.6994 | 0.8745 | 0.5424 | -0.5868 | -0.0055 | 0.1186 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1043_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1043_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1043_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1043_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1043_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1043_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1043_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1043_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1043_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1043_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1043_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1043_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1043_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1043_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1043_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1043_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
