# Autonomy public-indicator hunt gen 1040

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T152739Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2200_above_at_h` | one_head_filter_pi_star | 45 | 4.4180 | 1.6033 | 0.6222 | 1.4392 | 0.0227 | 0.2889 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2200_above_at_h` | one_head_filter_pi_star | 43 | 4.2217 | 1.4124 | 0.6047 | 1.0918 | 0.0152 | 0.3023 | ok | RAN |
| ETHUSDT | 8 | `sma2200_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5487 | 0.6369 | 3.4159 | 0.0147 | 0.3065 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2200_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.5277 | 0.6366 | 3.2273 | 0.0143 | 0.3093 | ok | RAN |
| SOLUSDT | 4 | `sma2200_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7890 | 0.6408 | 4.1529 | 0.0116 | 0.3236 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2200_below_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 1.7739 | 0.6382 | 4.0440 | 0.0114 | 0.3092 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2200_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 1.7055 | 0.6719 | 1.7391 | 0.0102 | 0.2656 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2200_above_at_h` | one_head_filter_pi_star | 69 | 5.7358 | 1.5449 | 0.6377 | 1.5472 | 0.0084 | 0.2899 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2200_above_at_h` | one_head_filter_pi_star | 10 | 1.8365 | 0.4943 | 0.3000 | -1.2919 | -0.0603 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma2200_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0888 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
