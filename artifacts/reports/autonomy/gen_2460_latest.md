# Autonomy public-indicator hunt gen 2460

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T204754Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1103_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1103_above_at_h` | one_head_filter_pi_star | 107 | 8.7745 | 1.2240 | 0.5981 | 0.8912 | 0.0038 | 0.1495 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1103_above_at_h` | one_head_filter_pi_star | 111 | 9.2255 | 1.2145 | 0.6036 | 0.8457 | 0.0037 | 0.1441 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1103_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.0051 | 0.5409 | 0.0345 | 0.0001 | 0.1323 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1103_below_at_h` | one_head_filter_pi_star | 269 | 21.8837 | 0.9347 | 0.5316 | -0.4708 | -0.0014 | 0.1301 | ok | RAN |
| ETHUSDT | 4 | `ema1103_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 0.9464 | 0.5438 | -0.3574 | -0.0016 | 0.1567 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1103_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 0.9300 | 0.5391 | -0.4900 | -0.0022 | 0.1522 | ok | RAN |
| ETHUSDT | 8 | `ema1103_above_at_h` | one_head_filter_pi_star | 117 | 9.6550 | 0.9132 | 0.5470 | -0.3953 | -0.0039 | 0.1026 | ok | RAN |
| ETHUSDT | 4 | `ema1103_above_at_h` | one_head_filter_pi_star | 112 | 9.2432 | 0.8974 | 0.5357 | -0.4648 | -0.0046 | 0.1161 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1103_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1103_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1103_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1103_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1103_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1103_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1103_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1103_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1103_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1103_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1103_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1103_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1103_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1103_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1103_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
