# Autonomy public-indicator hunt gen 1507

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T032627Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma675_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0874 | 0.6911 | 4.3992 | 0.0249 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma675_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0653 | 0.6854 | 4.2696 | 0.0240 | 0.3933 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma675_above_at_h` | one_head_filter_pi_star | 106 | 8.6925 | 1.8371 | 0.6509 | 2.8322 | 0.0124 | 0.3302 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma675_below_at_h` | one_head_filter_pi_star | 204 | 16.5958 | 1.7169 | 0.6520 | 3.1882 | 0.0111 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma675_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.7018 | 0.6450 | 3.2320 | 0.0111 | 0.3250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma675_above_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.5953 | 0.6242 | 2.4607 | 0.0092 | 0.2994 | ok | RAN |
| ETHUSDT | 8 | `sma675_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.1980 | 0.5957 | 0.9341 | 0.0072 | 0.2340 | ok | RAN |
| ETHUSDT | 4 | `sma675_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.1914 | 0.5933 | 0.9203 | 0.0070 | 0.2200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma675_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma675_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma675_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma675_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
