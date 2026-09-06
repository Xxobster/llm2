# Autonomy public-indicator hunt gen 2198

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T121349Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma521_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.0950 | 0.5812 | 0.5809 | 0.0030 | 0.1832 | ok | RAN |
| ETHUSDT | 4 | `wma521_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.0911 | 0.5838 | 0.5566 | 0.0029 | 0.1946 | ok | RAN |
| SOLUSDT | 8 | `wma521_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0409 | 0.5611 | 0.2381 | 0.0008 | 0.1611 | ok | RAN |
| SOLUSDT | 4 | `wma521_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.0390 | 0.5389 | 0.2214 | 0.0007 | 0.1000 | ok | RAN |
| SOLUSDT | 8 | `wma521_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0378 | 0.5495 | 0.2141 | 0.0007 | 0.0934 | ok | RAN |
| SOLUSDT | 4 | `wma521_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0180 | 0.5600 | 0.1058 | 0.0004 | 0.1486 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma521_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8490 | 0.5348 | -0.9403 | -0.0060 | 0.0909 | ok | RAN |
| ETHUSDT | 4 | `wma521_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.7967 | 0.5263 | -1.3203 | -0.0084 | 0.1000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma521_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma521_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma521_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma521_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma521_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma521_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma521_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma521_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma521_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma521_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma521_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma521_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma521_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma521_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma521_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma521_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
