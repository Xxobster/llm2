# Autonomy public-indicator hunt gen 2374

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T102935Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma548_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1827 | 0.5967 | 1.0426 | 0.0055 | 0.1934 | ok | RAN |
| ETHUSDT | 4 | `wma548_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1453 | 0.5870 | 0.8549 | 0.0044 | 0.1902 | ok | RAN |
| SOLUSDT | 4 | `wma548_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.0395 | 0.5372 | 0.2313 | 0.0007 | 0.0957 | ok | RAN |
| SOLUSDT | 8 | `wma548_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0316 | 0.5376 | 0.1823 | 0.0006 | 0.0968 | ok | RAN |
| SOLUSDT | 4 | `wma548_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.0175 | 0.5550 | 0.1063 | 0.0004 | 0.1571 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma548_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 0.9561 | 0.5489 | -0.2688 | -0.0009 | 0.1522 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma548_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8222 | 0.5385 | -1.1200 | -0.0074 | 0.1044 | ok | RAN |
| ETHUSDT | 4 | `wma548_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8042 | 0.5330 | -1.2592 | -0.0083 | 0.0934 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma548_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma548_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma548_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma548_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma548_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma548_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma548_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma548_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma548_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma548_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma548_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma548_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma548_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma548_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma548_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma548_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
