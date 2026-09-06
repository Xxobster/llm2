# Autonomy public-indicator hunt gen 385

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T225434Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema520_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.1759 | 0.7158 | 4.6678 | 0.0251 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema520_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.0107 | 0.6900 | 4.4481 | 0.0231 | 0.3800 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema520_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8673 | 0.6616 | 3.6877 | 0.0132 | 0.3485 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema520_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7340 | 0.6476 | 3.3383 | 0.0114 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema520_above_at_h` | one_head_filter_pi_star | 164 | 13.3726 | 1.6634 | 0.6220 | 2.7028 | 0.0098 | 0.3049 | ok | RAN |
| SOLUSDT | 8 | `ema520_above_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.5351 | 0.6104 | 2.2495 | 0.0082 | 0.3052 | ok | RAN |
| ETHUSDT | 8 | `ema520_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1772 | 0.5951 | 0.8821 | 0.0065 | 0.1963 | ok | RAN |
| ETHUSDT | 4 | `ema520_above_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.1146 | 0.5928 | 0.5936 | 0.0042 | 0.1856 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema520_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema520_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
