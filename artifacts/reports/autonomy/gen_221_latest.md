# Autonomy public-indicator hunt gen 221

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T235903Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret9_cross_down_0` | one_head_filter_pi_star | 26 | 2.2247 | 2.5658 | 0.7308 | 1.9090 | 0.0301 | 0.2692 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret9_neg_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.8458 | 0.6804 | 3.9632 | 0.0216 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret9_neg_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7780 | 0.6758 | 3.7436 | 0.0201 | 0.3744 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret9_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1810 | 0.6905 | 4.0896 | 0.0179 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret9_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1083 | 0.6810 | 3.8584 | 0.0176 | 0.4233 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret9_cross_down_0` | one_head_filter_pi_star | 39 | 3.3022 | 2.1404 | 0.6923 | 1.8582 | 0.0139 | 0.1538 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret9_pos_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2078 | 0.5915 | 0.9698 | 0.0070 | 0.2012 | ok | RAN |
| SOLUSDT | 8 | `ret9_cross_up_0` | one_head_filter_pi_star | 16 | 1.3639 | 1.5031 | 0.7500 | 0.6580 | 0.0068 | 0.1875 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret9_pos_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.4149 | 0.5981 | 2.1890 | 0.0063 | 0.2536 | ok | RAN |
| ETHUSDT | 4 | `ret9_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1957 | 0.5875 | 0.9258 | 0.0062 | 0.1938 | ok | RAN |
| SOLUSDT | 4 | `ret9_pos_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3745 | 0.5915 | 2.0222 | 0.0056 | 0.2441 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret9_cross_up_0` | one_head_filter_pi_star | 20 | 1.6457 | 0.9077 | 0.5500 | -0.1873 | -0.0033 | 0.2000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret9_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret9_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret9_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret9_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret9_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret9_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret9_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret9_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret9_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret9_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret9_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret9_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
