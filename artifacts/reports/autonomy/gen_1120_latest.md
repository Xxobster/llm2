# Autonomy public-indicator hunt gen 1120

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T012542Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `sma2400_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 3.0531 | 0.7000 | 1.7887 | 0.1230 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2400_above_at_h` | one_head_filter_pi_star | 55 | 4.9156 | 1.4525 | 0.6182 | 1.2691 | 0.0170 | 0.2545 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2400_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5618 | 0.6369 | 3.4544 | 0.0152 | 0.3065 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2400_below_at_h` | one_head_filter_pi_star | 321 | 26.1140 | 1.5618 | 0.6355 | 3.3086 | 0.0150 | 0.3115 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2400_below_at_h` | one_head_filter_pi_star | 294 | 23.9175 | 1.8270 | 0.6497 | 4.2823 | 0.0124 | 0.3231 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2400_below_at_h` | one_head_filter_pi_star | 282 | 23.0594 | 1.7813 | 0.6454 | 3.9921 | 0.0122 | 0.3262 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma2400_above_at_h` | one_head_filter_pi_star | 43 | 3.8897 | 1.2146 | 0.5814 | 0.5523 | 0.0088 | 0.2558 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma2400_above_at_h` | one_head_filter_pi_star | 79 | 6.4935 | 1.6030 | 0.6582 | 1.6853 | 0.0082 | 0.2278 | ok | RAN |
| SOLUSDT | 4 | `sma2400_above_at_h` | one_head_filter_pi_star | 65 | 5.3010 | 1.6401 | 0.6308 | 1.6112 | 0.0081 | 0.2154 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2400_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2400_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
