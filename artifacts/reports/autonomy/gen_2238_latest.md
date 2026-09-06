# Autonomy public-indicator hunt gen 2238

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T171535Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma527_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1158 | 0.5815 | 0.6976 | 0.0037 | 0.1957 | ok | RAN |
| ETHUSDT | 8 | `wma527_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.0794 | 0.5759 | 0.5017 | 0.0025 | 0.1885 | ok | RAN |
| SOLUSDT | 4 | `wma527_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.0519 | 0.5414 | 0.2940 | 0.0010 | 0.0994 | ok | RAN |
| SOLUSDT | 8 | `wma527_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0497 | 0.5479 | 0.2849 | 0.0009 | 0.1011 | ok | RAN |
| SOLUSDT | 4 | `wma527_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.0300 | 0.5638 | 0.1743 | 0.0006 | 0.1543 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma527_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9907 | 0.5519 | -0.0559 | -0.0002 | 0.1585 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma527_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8253 | 0.5294 | -1.1137 | -0.0072 | 0.0963 | ok | RAN |
| ETHUSDT | 4 | `wma527_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8144 | 0.5368 | -1.1675 | -0.0077 | 0.1000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma527_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma527_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma527_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma527_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma527_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma527_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma527_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma527_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma527_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma527_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma527_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma527_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma527_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma527_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma527_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma527_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
