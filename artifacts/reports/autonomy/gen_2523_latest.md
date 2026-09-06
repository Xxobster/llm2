# Autonomy public-indicator hunt gen 2523

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T033243Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma809_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.3796 | 0.6121 | 1.8400 | 0.0097 | 0.1818 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma809_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.2087 | 0.5912 | 1.2057 | 0.0060 | 0.1768 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma809_above_at_h` | one_head_filter_pi_star | 155 | 12.6388 | 1.0883 | 0.5548 | 0.4500 | 0.0016 | 0.1097 | ok | RAN |
| SOLUSDT | 8 | `sma809_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.0859 | 0.5612 | 0.4216 | 0.0016 | 0.1151 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma809_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 0.9861 | 0.5514 | -0.0868 | -0.0003 | 0.1449 | ok | RAN |
| SOLUSDT | 4 | `sma809_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.9478 | 0.5571 | -0.3307 | -0.0011 | 0.1381 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma809_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 0.8819 | 0.5528 | -0.6357 | -0.0049 | 0.1056 | ok | RAN |
| ETHUSDT | 8 | `sma809_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 0.8303 | 0.5455 | -0.9075 | -0.0075 | 0.1039 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma809_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma809_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma809_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma809_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma809_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma809_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma809_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma809_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma809_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma809_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma809_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma809_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma809_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma809_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma809_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma809_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
