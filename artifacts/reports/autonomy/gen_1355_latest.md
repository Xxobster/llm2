# Autonomy public-indicator hunt gen 1355

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T012840Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma652_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.0368 | 0.6833 | 4.2607 | 0.0234 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma652_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0275 | 0.6774 | 4.3271 | 0.0234 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma652_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7533 | 0.6585 | 3.3913 | 0.0123 | 0.3220 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma652_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 1.7758 | 0.6602 | 3.3954 | 0.0118 | 0.3252 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma652_above_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.8381 | 0.6496 | 2.7502 | 0.0117 | 0.3248 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma652_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.2174 | 0.6051 | 1.0404 | 0.0078 | 0.2166 | ok | RAN |
| SOLUSDT | 4 | `sma652_above_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.4687 | 0.6026 | 2.0149 | 0.0074 | 0.3113 | ok | RAN |
| ETHUSDT | 8 | `sma652_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.1809 | 0.6067 | 0.8708 | 0.0066 | 0.2267 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma652_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma652_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma652_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma652_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma652_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma652_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma652_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma652_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma652_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma652_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma652_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma652_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma652_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma652_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma652_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma652_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
