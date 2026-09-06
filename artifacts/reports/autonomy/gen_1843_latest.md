# Autonomy public-indicator hunt gen 1843

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T181749Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma719_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.2430 | 0.5939 | 1.2822 | 0.0067 | 0.2000 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma719_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1796 | 0.5792 | 1.0325 | 0.0054 | 0.1803 | ok | RAN |
| SOLUSDT | 8 | `sma719_above_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.0788 | 0.5443 | 0.4051 | 0.0015 | 0.1076 | ok | RAN |
| SOLUSDT | 4 | `sma719_above_at_h` | one_head_filter_pi_star | 125 | 10.2506 | 1.0467 | 0.5440 | 0.2159 | 0.0009 | 0.1280 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma719_below_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 0.9719 | 0.5625 | -0.1738 | -0.0006 | 0.1346 | ok | RAN |
| SOLUSDT | 8 | `sma719_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.9539 | 0.5550 | -0.2836 | -0.0010 | 0.1400 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma719_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 0.8973 | 0.5638 | -0.5526 | -0.0043 | 0.1141 | ok | RAN |
| ETHUSDT | 8 | `sma719_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.8865 | 0.5507 | -0.5944 | -0.0046 | 0.1087 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma719_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma719_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma719_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma719_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma719_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma719_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma719_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma719_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma719_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma719_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma719_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma719_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma719_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma719_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma719_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma719_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
