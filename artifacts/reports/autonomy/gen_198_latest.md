# Autonomy public-indicator hunt gen 198

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T222628Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma18_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.8074 | 0.6776 | 3.8865 | 0.0209 | 0.3738 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma18_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma18_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1790 | 0.6875 | 3.9673 | 0.0177 | 0.4188 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma18_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1589 | 0.6871 | 3.9713 | 0.0176 | 0.4233 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma18_cross_up` | one_head_filter_pi_star | 60 | 4.9372 | 1.2564 | 0.6167 | 0.8022 | 0.0079 | 0.2667 | ok | RAN |
| ETHUSDT | 8 | `wma18_above_at_h` | one_head_filter_pi_star | 149 | 12.2957 | 1.2119 | 0.5839 | 0.9606 | 0.0075 | 0.2148 | ok | RAN |
| ETHUSDT | 4 | `wma18_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 8 | `wma18_cross_down` | one_head_filter_pi_star | 72 | 6.0963 | 1.4448 | 0.6250 | 1.3387 | 0.0063 | 0.1389 | ok | RAN |
| SOLUSDT | 8 | `wma18_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3925 | 0.5935 | 2.1163 | 0.0060 | 0.2523 | ok | RAN |
| SOLUSDT | 4 | `wma18_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3825 | 0.5972 | 2.0679 | 0.0056 | 0.2454 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `wma18_cross_up` | one_head_filter_pi_star | 18 | 1.5359 | 0.8997 | 0.5556 | -0.1893 | -0.0026 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma18_cross_down` | one_head_filter_pi_star | 38 | 3.4364 | 0.6744 | 0.5263 | -1.0153 | -0.0109 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma18_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6382 | 0.3750 | -0.7079 | -0.0379 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma18_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma18_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma18_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
