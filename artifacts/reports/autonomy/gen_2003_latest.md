# Autonomy public-indicator hunt gen 2003

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T093423Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma741_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.2956 | 0.6061 | 1.5375 | 0.0081 | 0.2061 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma741_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1193 | 0.5722 | 0.7181 | 0.0036 | 0.1765 | ok | RAN |
| SOLUSDT | 8 | `sma741_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.1401 | 0.5662 | 0.6575 | 0.0026 | 0.1324 | ok | RAN |
| SOLUSDT | 4 | `sma741_above_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.0157 | 0.5294 | 0.0821 | 0.0003 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma741_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 0.9673 | 0.5944 | -0.1670 | -0.0013 | 0.1119 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma741_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.9142 | 0.5544 | -0.5322 | -0.0019 | 0.1347 | ok | RAN |
| SOLUSDT | 4 | `sma741_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9051 | 0.5485 | -0.6096 | -0.0020 | 0.1311 | ok | RAN |
| ETHUSDT | 4 | `sma741_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.8360 | 0.5541 | -0.8667 | -0.0070 | 0.1081 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma741_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma741_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma741_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma741_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma741_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma741_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma741_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma741_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma741_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma741_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma741_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma741_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma741_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma741_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma741_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma741_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
