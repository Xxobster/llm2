# Autonomy public-indicator hunt gen 835

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T185955Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma534_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0972 | 0.7072 | 4.5577 | 0.0242 | 0.3923 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma534_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0294 | 0.6831 | 4.3681 | 0.0236 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma534_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.8636 | 0.6733 | 3.7570 | 0.0130 | 0.3366 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma534_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8115 | 0.6552 | 3.6585 | 0.0124 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma534_above_at_h` | one_head_filter_pi_star | 169 | 13.8588 | 1.6376 | 0.6213 | 2.7023 | 0.0097 | 0.3077 | ok | RAN |
| SOLUSDT | 8 | `sma534_above_at_h` | one_head_filter_pi_star | 181 | 14.8429 | 1.5557 | 0.6243 | 2.5330 | 0.0084 | 0.2762 | ok | RAN |
| ETHUSDT | 8 | `sma534_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.2270 | 0.6000 | 1.1076 | 0.0081 | 0.2194 | ok | RAN |
| ETHUSDT | 4 | `sma534_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2251 | 0.6011 | 1.1637 | 0.0079 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma534_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma534_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma534_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma534_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma534_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma534_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
