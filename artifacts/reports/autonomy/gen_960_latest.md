# Autonomy public-indicator hunt gen 960

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T080812Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2000_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.6306 | 0.6488 | 3.7654 | 0.0166 | 0.3125 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2000_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 1.5980 | 0.6427 | 3.6856 | 0.0163 | 0.3055 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2000_above_at_h` | one_head_filter_pi_star | 44 | 3.7038 | 2.0815 | 0.7045 | 2.1885 | 0.0156 | 0.3864 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma2000_above_at_h` | one_head_filter_pi_star | 60 | 4.9876 | 1.9739 | 0.6833 | 2.2995 | 0.0139 | 0.3000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2000_below_at_h` | one_head_filter_pi_star | 294 | 23.9175 | 1.8870 | 0.6531 | 4.3795 | 0.0124 | 0.3197 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2000_below_at_h` | one_head_filter_pi_star | 303 | 24.6496 | 1.7808 | 0.6403 | 4.1635 | 0.0117 | 0.3168 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2000_above_at_h` | one_head_filter_pi_star | 44 | 3.8529 | 1.2799 | 0.6136 | 0.6917 | 0.0106 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma2000_above_at_h` | one_head_filter_pi_star | 47 | 4.2516 | 1.1925 | 0.5745 | 0.5440 | 0.0076 | 0.2128 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2000_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0846 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2000_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
