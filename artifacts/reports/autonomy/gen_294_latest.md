# Autonomy public-indicator hunt gen 294

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T050420Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma85_cross_up` | one_head_filter_pi_star | 24 | 1.9952 | 2.4419 | 0.6250 | 1.6081 | 0.0228 | 0.2083 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma85_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.8503 | 0.6845 | 3.9382 | 0.0217 | 0.3835 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma85_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.8176 | 0.6845 | 3.8980 | 0.0212 | 0.3738 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma85_cross_down` | one_head_filter_pi_star | 28 | 2.3898 | 2.3885 | 0.6786 | 1.8353 | 0.0210 | 0.1786 | TPM<MIN | RAN |
| SOLUSDT | 4 | `wma85_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.1017 | 0.6835 | 3.9124 | 0.0171 | 0.4114 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma85_below_at_h` | one_head_filter_pi_star | 153 | 12.5109 | 2.0549 | 0.6797 | 3.7398 | 0.0164 | 0.4183 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma85_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 1.2498 | 0.6000 | 1.1530 | 0.0075 | 0.2182 | ok | RAN |
| ETHUSDT | 8 | `wma85_above_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.2210 | 0.6024 | 1.0084 | 0.0068 | 0.2169 | ok | RAN |
| SOLUSDT | 8 | `wma85_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3817 | 0.6009 | 2.0107 | 0.0056 | 0.2523 | ok | RAN |
| SOLUSDT | 4 | `wma85_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3321 | 0.5943 | 1.7678 | 0.0049 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma85_cross_up` | one_head_filter_pi_star | 18 | 1.5667 | 0.9805 | 0.5000 | -0.0362 | -0.0008 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma85_cross_down` | one_head_filter_pi_star | 28 | 2.4434 | 0.8160 | 0.5000 | -0.4468 | -0.0089 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma85_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma85_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma85_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma85_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma85_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma85_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
