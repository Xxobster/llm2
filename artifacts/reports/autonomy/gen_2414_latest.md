# Autonomy public-indicator hunt gen 2414

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T152820Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma554_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1777 | 0.5955 | 1.0330 | 0.0054 | 0.1798 | ok | RAN |
| ETHUSDT | 8 | `wma554_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1038 | 0.5914 | 0.6261 | 0.0032 | 0.1935 | ok | RAN |
| SOLUSDT | 4 | `wma554_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.1021 | 0.5470 | 0.5619 | 0.0018 | 0.0994 | ok | RAN |
| SOLUSDT | 8 | `wma554_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.0862 | 0.5470 | 0.4732 | 0.0016 | 0.1050 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma554_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 0.9891 | 0.5598 | -0.0662 | -0.0002 | 0.1467 | ok | RAN |
| SOLUSDT | 8 | `wma554_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9464 | 0.5474 | -0.3338 | -0.0011 | 0.1526 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma554_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.8659 | 0.5435 | -0.8436 | -0.0055 | 0.0978 | ok | RAN |
| ETHUSDT | 8 | `wma554_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 0.8218 | 0.5291 | -1.1263 | -0.0074 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma554_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma554_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma554_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma554_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma554_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma554_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma554_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma554_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma554_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma554_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma554_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma554_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma554_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma554_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma554_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma554_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
