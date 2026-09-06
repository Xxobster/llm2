# Autonomy public-indicator hunt gen 2131

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T020219Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma757_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1455 | 0.5815 | 0.8834 | 0.0042 | 0.1739 | ok | RAN |
| ETHUSDT | 4 | `sma757_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1391 | 0.5659 | 0.7996 | 0.0041 | 0.1923 | ok | RAN |
| SOLUSDT | 8 | `sma757_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.0486 | 0.5462 | 0.2359 | 0.0009 | 0.1385 | ok | RAN |
| SOLUSDT | 4 | `sma757_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.0321 | 0.5368 | 0.1597 | 0.0006 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma757_below_at_h` | one_head_filter_pi_star | 202 | 16.4331 | 0.9864 | 0.5644 | -0.0816 | -0.0003 | 0.1238 | ok | RAN |
| SOLUSDT | 8 | `sma757_below_at_h` | one_head_filter_pi_star | 217 | 17.6534 | 0.9672 | 0.5484 | -0.2076 | -0.0007 | 0.1336 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma757_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8798 | 0.5660 | -0.6606 | -0.0049 | 0.1195 | ok | RAN |
| ETHUSDT | 4 | `sma757_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.8164 | 0.5484 | -1.0205 | -0.0078 | 0.1032 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma757_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma757_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma757_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma757_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma757_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma757_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma757_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma757_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma757_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma757_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma757_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma757_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma757_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma757_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma757_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma757_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
