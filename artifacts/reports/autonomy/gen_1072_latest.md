# Autonomy public-indicator hunt gen 1072

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T193045Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2280_above_at_h` | one_head_filter_pi_star | 54 | 4.7286 | 1.5609 | 0.6296 | 1.4175 | 0.0196 | 0.2407 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2280_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5813 | 0.6420 | 3.5828 | 0.0157 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2280_below_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.5741 | 0.6400 | 3.4413 | 0.0152 | 0.3108 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2280_below_at_h` | one_head_filter_pi_star | 297 | 24.1615 | 1.8396 | 0.6431 | 4.3057 | 0.0121 | 0.3232 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2280_above_at_h` | one_head_filter_pi_star | 71 | 5.9020 | 1.8780 | 0.6761 | 2.1841 | 0.0119 | 0.2676 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2280_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7462 | 0.6311 | 3.9824 | 0.0111 | 0.3139 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2280_above_at_h` | one_head_filter_pi_star | 49 | 4.2907 | 1.2737 | 0.5918 | 0.7319 | 0.0105 | 0.2245 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2280_above_at_h` | one_head_filter_pi_star | 58 | 4.8214 | 1.5331 | 0.6207 | 1.3767 | 0.0078 | 0.2759 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2280_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2280_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
