# Autonomy public-indicator hunt gen 737

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T095116Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1400_below_at_h` | one_head_filter_pi_star | 300 | 24.5073 | 1.7772 | 0.6600 | 4.2053 | 0.0190 | 0.3233 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1400_below_at_h` | one_head_filter_pi_star | 285 | 23.2819 | 1.7819 | 0.6596 | 4.1380 | 0.0188 | 0.3263 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1400_above_at_h` | one_head_filter_pi_star | 79 | 6.5197 | 1.3635 | 0.6203 | 1.2087 | 0.0139 | 0.2405 | ok | RAN |
| SOLUSDT | 4 | `ema1400_below_at_h` | one_head_filter_pi_star | 283 | 23.1412 | 1.7708 | 0.6396 | 4.0391 | 0.0121 | 0.3145 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1400_below_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 1.6719 | 0.6347 | 3.5556 | 0.0112 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1400_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.5562 | 0.6396 | 1.9250 | 0.0083 | 0.2793 | ok | RAN |
| SOLUSDT | 8 | `ema1400_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.4598 | 0.6261 | 1.6879 | 0.0072 | 0.2696 | ok | RAN |
| ETHUSDT | 4 | `ema1400_above_at_h` | one_head_filter_pi_star | 73 | 6.2118 | 1.1819 | 0.6027 | 0.6266 | 0.0070 | 0.2329 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1400_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1400_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
