# Autonomy public-indicator hunt gen 1491

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T015737Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma673_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0957 | 0.6882 | 4.4295 | 0.0248 | 0.4032 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma673_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0973 | 0.6966 | 4.3718 | 0.0245 | 0.3876 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma673_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.7151 | 0.6618 | 3.2270 | 0.0112 | 0.3235 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma673_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.7286 | 0.6599 | 3.2123 | 0.0112 | 0.3249 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma673_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.4783 | 0.6000 | 1.9502 | 0.0078 | 0.3154 | ok | RAN |
| SOLUSDT | 4 | `sma673_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.4795 | 0.6028 | 1.9729 | 0.0077 | 0.3191 | ok | RAN |
| ETHUSDT | 8 | `sma673_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.2084 | 0.6135 | 1.0227 | 0.0075 | 0.2086 | ok | RAN |
| ETHUSDT | 4 | `sma673_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 1.1314 | 0.5906 | 0.6559 | 0.0050 | 0.2215 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma673_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma673_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma673_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma673_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma673_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma673_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma673_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma673_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma673_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma673_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma673_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma673_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma673_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma673_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma673_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma673_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
