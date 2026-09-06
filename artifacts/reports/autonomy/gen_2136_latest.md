# Autonomy public-indicator hunt gen 2136

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T023820Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4940_above_at_h` | one_head_filter_pi_star | 52 | 4.8090 | 1.6911 | 0.5769 | 1.4421 | 0.0092 | 0.1154 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma4940_above_at_h` | one_head_filter_pi_star | 48 | 4.0315 | 1.3156 | 0.5417 | 0.6924 | 0.0052 | 0.0833 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma4940_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.0000 | 0.5595 | 0.0005 | 0.0000 | 0.1339 | ok | RAN |
| SOLUSDT | 8 | `sma4940_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9814 | 0.5389 | -0.1467 | -0.0004 | 0.1228 | ok | RAN |
| SOLUSDT | 4 | `sma4940_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 0.9689 | 0.5359 | -0.2337 | -0.0006 | 0.1275 | ok | RAN |
| ETHUSDT | 8 | `sma4940_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9665 | 0.5543 | -0.2761 | -0.0011 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma4940_above_at_h` | one_head_filter_pi_star | 40 | 11.8025 | 0.6975 | 0.4750 | -2.0098 | -0.0178 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `sma4940_above_at_h` | one_head_filter_pi_star | 39 | 11.5074 | 0.6891 | 0.4872 | -1.7274 | -0.0188 | 0.1538 | ok | RAN |
| ETHUSDT | 4 | `sma4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4940_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4940_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4940_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4940_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4940_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
