# Autonomy public-indicator hunt gen 1747

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T093142Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma707_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2206 | 0.5868 | 1.2029 | 0.0065 | 0.1976 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma707_below_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 1.2098 | 0.5786 | 1.1137 | 0.0059 | 0.1950 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma707_above_at_h` | one_head_filter_pi_star | 116 | 9.5126 | 1.1012 | 0.5517 | 0.4417 | 0.0018 | 0.1121 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma707_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.0016 | 0.5323 | 0.0081 | 0.0000 | 0.1290 | ok | RAN |
| SOLUSDT | 4 | `sma707_below_at_h` | one_head_filter_pi_star | 196 | 15.9450 | 0.9474 | 0.5561 | -0.3195 | -0.0011 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma707_below_at_h` | one_head_filter_pi_star | 205 | 16.6772 | 0.9048 | 0.5415 | -0.6033 | -0.0020 | 0.1415 | ok | RAN |
| ETHUSDT | 8 | `sma707_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 0.9206 | 0.5714 | -0.4012 | -0.0031 | 0.1203 | ok | RAN |
| ETHUSDT | 4 | `sma707_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 0.8067 | 0.5359 | -1.1078 | -0.0084 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma707_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma707_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0689 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma707_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma707_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma707_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma707_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma707_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma707_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma707_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma707_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma707_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma707_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma707_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma707_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma707_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma707_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
