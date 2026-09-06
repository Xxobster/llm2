# Autonomy public-indicator hunt gen 1867

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T202535Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma723_below_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.1957 | 0.5802 | 1.0449 | 0.0057 | 0.1852 | ok | RAN |
| ETHUSDT | 4 | `sma723_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.2032 | 0.5833 | 1.1596 | 0.0057 | 0.1833 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma723_above_at_h` | one_head_filter_pi_star | 110 | 9.1429 | 1.2578 | 0.6091 | 1.0154 | 0.0046 | 0.1455 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma723_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.1276 | 0.5613 | 0.6451 | 0.0024 | 0.1161 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma723_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9982 | 0.5561 | -0.0108 | -0.0000 | 0.1317 | ok | RAN |
| SOLUSDT | 8 | `sma723_below_at_h` | one_head_filter_pi_star | 214 | 17.4093 | 0.9368 | 0.5421 | -0.4029 | -0.0013 | 0.1355 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma723_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.9321 | 0.5714 | -0.3592 | -0.0028 | 0.1088 | ok | RAN |
| ETHUSDT | 4 | `sma723_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 0.8489 | 0.5526 | -0.8430 | -0.0064 | 0.1118 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma723_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma723_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma723_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma723_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma723_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma723_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma723_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma723_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma723_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma723_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma723_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma723_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma723_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma723_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma723_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma723_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
