# Autonomy public-indicator hunt gen 1502

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T025846Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma412_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9935 | 0.6989 | 4.3411 | 0.0229 | 0.3817 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma412_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8985 | 0.6862 | 4.0982 | 0.0221 | 0.3883 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma412_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2919 | 0.6988 | 4.3367 | 0.0174 | 0.3976 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma412_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2006 | 0.6936 | 4.2256 | 0.0167 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma412_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2427 | 0.6044 | 1.2448 | 0.0083 | 0.2198 | ok | RAN |
| ETHUSDT | 4 | `wma412_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2123 | 0.5907 | 1.0854 | 0.0074 | 0.2332 | ok | RAN |
| SOLUSDT | 8 | `wma412_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3935 | 0.5980 | 2.0185 | 0.0062 | 0.2563 | ok | RAN |
| SOLUSDT | 4 | `wma412_above_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3793 | 0.6019 | 1.9613 | 0.0060 | 0.2607 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma412_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma412_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma412_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma412_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma412_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma412_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
