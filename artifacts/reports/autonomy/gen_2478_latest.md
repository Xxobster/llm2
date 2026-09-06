# Autonomy public-indicator hunt gen 2478

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T224907Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma564_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.1472 | 0.5916 | 0.8690 | 0.0044 | 0.1780 | ok | RAN |
| ETHUSDT | 4 | `wma564_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1197 | 0.5866 | 0.7042 | 0.0037 | 0.1899 | ok | RAN |
| SOLUSDT | 4 | `wma564_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.0970 | 0.5608 | 0.5413 | 0.0018 | 0.1005 | ok | RAN |
| SOLUSDT | 8 | `wma564_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.0213 | 0.5497 | 0.1260 | 0.0004 | 0.0942 | ok | RAN |
| SOLUSDT | 4 | `wma564_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.0173 | 0.5533 | 0.1062 | 0.0004 | 0.1472 | ok | RAN |
| SOLUSDT | 8 | `wma564_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.0050 | 0.5556 | 0.0307 | 0.0001 | 0.1566 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma564_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 0.8269 | 0.5301 | -1.0952 | -0.0071 | 0.0929 | ok | RAN |
| ETHUSDT | 4 | `wma564_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8024 | 0.5275 | -1.2343 | -0.0084 | 0.1044 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma564_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma564_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma564_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma564_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma564_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma564_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
