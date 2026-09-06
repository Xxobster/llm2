# Autonomy public-indicator hunt gen 1524

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T050031Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema976_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.8329 | 0.6597 | 3.9776 | 0.0194 | 0.3319 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema976_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.7452 | 0.6483 | 3.7553 | 0.0185 | 0.3432 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema976_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.7936 | 0.6557 | 3.7916 | 0.0123 | 0.3156 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema976_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 1.7641 | 0.6504 | 3.7322 | 0.0121 | 0.3008 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema976_above_at_h` | one_head_filter_pi_star | 126 | 10.3562 | 1.8108 | 0.6587 | 2.7479 | 0.0120 | 0.3095 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema976_above_at_h` | one_head_filter_pi_star | 127 | 10.3556 | 1.6857 | 0.6457 | 2.4696 | 0.0099 | 0.3150 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema976_above_at_h` | one_head_filter_pi_star | 115 | 9.4908 | 1.1882 | 0.5913 | 0.7711 | 0.0073 | 0.2087 | ok | RAN |
| ETHUSDT | 8 | `ema976_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 1.1932 | 0.5897 | 0.8062 | 0.0073 | 0.2137 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema976_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0340 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema976_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema976_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema976_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema976_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema976_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema976_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema976_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema976_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema976_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema976_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema976_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema976_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema976_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema976_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema976_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
