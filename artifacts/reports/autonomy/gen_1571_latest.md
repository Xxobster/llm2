# Autonomy public-indicator hunt gen 1571

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T145150Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma684_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1270 | 0.5691 | 0.7468 | 0.0038 | 0.1934 | ok | RAN |
| ETHUSDT | 8 | `sma684_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.0737 | 0.5751 | 0.4662 | 0.0024 | 0.1710 | ok | RAN |
| SOLUSDT | 4 | `sma684_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.1119 | 0.5448 | 0.5306 | 0.0020 | 0.1119 | ok | RAN |
| SOLUSDT | 8 | `sma684_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.0243 | 0.5323 | 0.1189 | 0.0005 | 0.1371 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma684_below_at_h` | one_head_filter_pi_star | 195 | 15.8636 | 0.9409 | 0.5538 | -0.3594 | -0.0013 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma684_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.8990 | 0.5459 | -0.6505 | -0.0022 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `sma684_above_at_h` | one_head_filter_pi_star | 146 | 12.0481 | 0.8873 | 0.5548 | -0.5775 | -0.0045 | 0.1027 | ok | RAN |
| ETHUSDT | 8 | `sma684_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.8470 | 0.5475 | -0.9223 | -0.0062 | 0.1061 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma684_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma684_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma684_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma684_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma684_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma684_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma684_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma684_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma684_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma684_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma684_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma684_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma684_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma684_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma684_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma684_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
