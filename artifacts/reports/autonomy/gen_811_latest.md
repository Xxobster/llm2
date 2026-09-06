# Autonomy public-indicator hunt gen 811

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T164424Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma514_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.1710 | 0.7081 | 4.8236 | 0.0255 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma514_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.1346 | 0.7000 | 4.8345 | 0.0246 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma514_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 1.8528 | 0.6740 | 3.4900 | 0.0127 | 0.3536 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma514_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.7894 | 0.6531 | 3.3882 | 0.0119 | 0.3367 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma514_above_at_h` | one_head_filter_pi_star | 152 | 12.5433 | 1.2965 | 0.6053 | 1.3608 | 0.0102 | 0.2105 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma514_above_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.5729 | 0.6114 | 2.5162 | 0.0088 | 0.2914 | ok | RAN |
| SOLUSDT | 8 | `sma514_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5448 | 0.6080 | 2.4571 | 0.0084 | 0.2614 | ok | RAN |
| ETHUSDT | 4 | `sma514_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1855 | 0.5864 | 0.9028 | 0.0069 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma514_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma514_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma514_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma514_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma514_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma514_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
