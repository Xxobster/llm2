# Autonomy public-indicator hunt gen 763

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T115721Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma478_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.1696 | 0.7065 | 4.7656 | 0.0256 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma478_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0921 | 0.6954 | 4.7354 | 0.0243 | 0.3655 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma478_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.9273 | 0.6738 | 3.8009 | 0.0137 | 0.3476 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma478_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8686 | 0.6618 | 3.7975 | 0.0131 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma478_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2657 | 0.6000 | 1.3691 | 0.0091 | 0.2108 | ok | RAN |
| SOLUSDT | 8 | `sma478_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5557 | 0.6096 | 2.5236 | 0.0086 | 0.2674 | ok | RAN |
| ETHUSDT | 8 | `sma478_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2223 | 0.5987 | 1.0720 | 0.0081 | 0.2102 | ok | RAN |
| SOLUSDT | 4 | `sma478_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4649 | 0.5969 | 2.2722 | 0.0074 | 0.2755 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma478_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma478_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma478_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma478_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
