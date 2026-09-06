# Autonomy public-indicator hunt gen 2259

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T194433Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma774_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.2438 | 0.5917 | 1.2661 | 0.0066 | 0.1834 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma774_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1658 | 0.5808 | 0.9205 | 0.0049 | 0.1856 | ok | RAN |
| SOLUSDT | 8 | `sma774_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.0751 | 0.5455 | 0.3574 | 0.0014 | 0.1212 | ok | RAN |
| SOLUSDT | 4 | `sma774_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.0358 | 0.5401 | 0.1758 | 0.0007 | 0.1168 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma774_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9292 | 0.5680 | -0.4418 | -0.0015 | 0.1359 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma774_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 0.9034 | 0.5421 | -0.6297 | -0.0021 | 0.1355 | ok | RAN |
| ETHUSDT | 8 | `sma774_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 0.9285 | 0.5704 | -0.3472 | -0.0028 | 0.1185 | ok | RAN |
| ETHUSDT | 4 | `sma774_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.8936 | 0.5677 | -0.5644 | -0.0043 | 0.1032 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma774_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma774_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma774_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma774_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma774_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma774_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma774_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma774_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma774_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma774_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma774_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma774_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma774_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma774_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma774_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma774_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
