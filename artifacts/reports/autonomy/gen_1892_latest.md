# Autonomy public-indicator hunt gen 1892

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T224132Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1028_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1028_above_at_h` | one_head_filter_pi_star | 112 | 9.2055 | 1.2418 | 0.6161 | 1.0016 | 0.0042 | 0.1339 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1028_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.0033 | 0.5528 | 0.0155 | 0.0001 | 0.1138 | ok | RAN |
| ETHUSDT | 4 | `ema1028_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 0.9965 | 0.5505 | -0.0225 | -0.0001 | 0.1560 | ok | RAN |
| SOLUSDT | 8 | `ema1028_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 0.9895 | 0.5475 | -0.0733 | -0.0002 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `ema1028_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 0.9417 | 0.5372 | -0.3937 | -0.0012 | 0.1198 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1028_above_at_h` | one_head_filter_pi_star | 128 | 10.5636 | 0.9488 | 0.5547 | -0.2426 | -0.0022 | 0.1172 | ok | RAN |
| ETHUSDT | 8 | `ema1028_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 0.9058 | 0.5331 | -0.7038 | -0.0031 | 0.1446 | ok | RAN |
| ETHUSDT | 8 | `ema1028_above_at_h` | one_head_filter_pi_star | 113 | 9.3257 | 0.8681 | 0.5310 | -0.6327 | -0.0059 | 0.1239 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1028_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1028_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0301 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1028_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1028_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1028_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1028_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1028_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1028_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1028_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1028_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1028_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1028_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1028_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1028_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1028_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
