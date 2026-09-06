# Autonomy public-indicator hunt gen 102

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T161232Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `cz_low_at_h` | one_head_filter_pi_star | 11 | 1.7331 |  | 1.0000 | 4.1163 | 0.1027 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `cz_low_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.7291 | 0.6650 | 3.3657 | 0.0193 | 0.3858 | EBR>35% | RAN |
| SOLUSDT | 4 | `cz_low_at_h` | one_head_filter_pi_star | 154 | 12.5927 | 2.1883 | 0.6883 | 3.8984 | 0.0178 | 0.4221 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `cz_cross_down_neg1` | one_head_filter_pi_star | 36 | 2.9623 | 1.2486 | 0.6111 | 0.6247 | 0.0115 | 0.3056 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `cz_high_at_h` | one_head_filter_pi_star | 145 | 11.9656 | 1.2304 | 0.6000 | 1.0384 | 0.0074 | 0.2069 | ok | RAN |
| SOLUSDT | 4 | `cz_high_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3568 | 0.5879 | 1.8829 | 0.0056 | 0.2563 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `cz_cross_up_1` | one_head_filter_pi_star | 13 | 1.6301 | 0.9285 | 0.4615 | -0.1348 | -0.0037 | 0.1538 | TPM<MIN | RAN |
| BTCUSDT | 4 | `cz_high_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `cz_cross_up_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `cz_cross_down_neg1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `cz_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `cz_cross_up_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `cz_cross_down_neg1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `cz_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `cz_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `cz_cross_up_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `cz_cross_down_neg1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `cz_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `cz_cross_up_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `cz_cross_down_neg1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cz_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cz_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cz_cross_up_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cz_cross_down_neg1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
