# Autonomy public-indicator hunt gen 1790

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T133035Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma457_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.1651 | 0.5916 | 0.9825 | 0.0050 | 0.1937 | ok | RAN |
| ETHUSDT | 4 | `wma457_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1061 | 0.5824 | 0.6409 | 0.0034 | 0.1923 | ok | RAN |
| SOLUSDT | 8 | `wma457_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.0704 | 0.5698 | 0.4067 | 0.0015 | 0.1620 | ok | RAN |
| SOLUSDT | 4 | `wma457_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.0577 | 0.5698 | 0.3211 | 0.0012 | 0.1508 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma457_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.0001 | 0.5389 | 0.0007 | 0.0000 | 0.1056 | ok | RAN |
| SOLUSDT | 4 | `wma457_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 0.9915 | 0.5417 | -0.0502 | -0.0002 | 0.1042 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma457_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8628 | 0.5514 | -0.8483 | -0.0055 | 0.0973 | ok | RAN |
| ETHUSDT | 4 | `wma457_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8421 | 0.5401 | -0.9844 | -0.0063 | 0.0963 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma457_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma457_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma457_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma457_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma457_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma457_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma457_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma457_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma457_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma457_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma457_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma457_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma457_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma457_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma457_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma457_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
