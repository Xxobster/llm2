# Autonomy public-indicator hunt gen 1614

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T192719Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma429_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1646 | 0.5957 | 0.9738 | 0.0051 | 0.1915 | ok | RAN |
| ETHUSDT | 4 | `wma429_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1107 | 0.5866 | 0.6598 | 0.0034 | 0.2011 | ok | RAN |
| SOLUSDT | 8 | `wma429_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.1185 | 0.5774 | 0.6409 | 0.0024 | 0.1548 | ok | RAN |
| SOLUSDT | 4 | `wma429_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 1.0812 | 0.5739 | 0.4432 | 0.0017 | 0.1591 | ok | RAN |
| SOLUSDT | 8 | `wma429_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0340 | 0.5495 | 0.1941 | 0.0006 | 0.0989 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma429_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 0.9137 | 0.5253 | -0.5403 | -0.0017 | 0.1061 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma429_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.8439 | 0.5389 | -0.9507 | -0.0063 | 0.1056 | ok | RAN |
| ETHUSDT | 8 | `wma429_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8211 | 0.5405 | -1.1440 | -0.0073 | 0.0919 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma429_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma429_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma429_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma429_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma429_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma429_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma429_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma429_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma429_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma429_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma429_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma429_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma429_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma429_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma429_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma429_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
