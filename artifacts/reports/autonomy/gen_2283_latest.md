# Autonomy public-indicator hunt gen 2283

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T223835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma777_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.3065 | 0.5988 | 1.5348 | 0.0081 | 0.1916 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma777_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.1138 | 0.5740 | 0.6599 | 0.0034 | 0.1716 | ok | RAN |
| SOLUSDT | 4 | `sma777_above_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.1096 | 0.5634 | 0.5301 | 0.0020 | 0.1268 | ok | RAN |
| SOLUSDT | 8 | `sma777_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.0897 | 0.5620 | 0.3951 | 0.0016 | 0.1322 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma777_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 0.9444 | 0.5488 | -0.3583 | -0.0012 | 0.1395 | ok | RAN |
| SOLUSDT | 8 | `sma777_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.9421 | 0.5606 | -0.3565 | -0.0012 | 0.1364 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma777_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.9218 | 0.5723 | -0.4248 | -0.0031 | 0.1069 | ok | RAN |
| ETHUSDT | 4 | `sma777_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 0.8580 | 0.5542 | -0.7906 | -0.0058 | 0.1024 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma777_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma777_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma777_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma777_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma777_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma777_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma777_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma777_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma777_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma777_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma777_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma777_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma777_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma777_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma777_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma777_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
