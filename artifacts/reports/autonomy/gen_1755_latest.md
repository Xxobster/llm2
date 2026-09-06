# Autonomy public-indicator hunt gen 1755

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T101511Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma708_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1642 | 0.5763 | 0.9453 | 0.0050 | 0.1921 | ok | RAN |
| SOLUSDT | 8 | `sma708_above_at_h` | one_head_filter_pi_star | 115 | 9.5580 | 1.2805 | 0.5739 | 1.1113 | 0.0048 | 0.1304 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma708_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1058 | 0.5699 | 0.6354 | 0.0032 | 0.1828 | ok | RAN |
| SOLUSDT | 4 | `sma708_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.1077 | 0.5556 | 0.4858 | 0.0020 | 0.1190 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma708_below_at_h` | one_head_filter_pi_star | 194 | 15.7823 | 0.9171 | 0.5567 | -0.5032 | -0.0018 | 0.1392 | ok | RAN |
| SOLUSDT | 8 | `sma708_below_at_h` | one_head_filter_pi_star | 207 | 16.8399 | 0.9117 | 0.5362 | -0.5642 | -0.0019 | 0.1304 | ok | RAN |
| ETHUSDT | 4 | `sma708_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 0.9152 | 0.5620 | -0.4360 | -0.0034 | 0.1168 | ok | RAN |
| ETHUSDT | 8 | `sma708_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8733 | 0.5646 | -0.6738 | -0.0053 | 0.1156 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma708_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0634 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma708_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0701 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma708_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma708_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma708_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma708_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma708_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma708_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma708_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma708_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma708_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma708_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma708_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma708_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma708_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma708_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
