# Autonomy public-indicator hunt gen 1546

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T070658Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1400_pos_at_h` | one_head_filter_pi_star | 30 | 2.5508 | 2.5124 | 0.7000 | 2.1528 | 0.0198 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret1400_neg_at_h` | one_head_filter_pi_star | 322 | 26.1953 | 1.5529 | 0.6429 | 3.3261 | 0.0147 | 0.3043 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1400_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.5367 | 0.6392 | 3.2296 | 0.0143 | 0.3070 | ok | RAN |
| SOLUSDT | 4 | `ret1400_pos_at_h` | one_head_filter_pi_star | 33 | 2.7779 | 1.8770 | 0.6667 | 1.5867 | 0.0139 | 0.3939 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1400_neg_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 1.6955 | 0.6289 | 3.9931 | 0.0105 | 0.3082 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1400_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.6701 | 0.6297 | 3.8608 | 0.0100 | 0.3006 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1400_pos_at_h` | one_head_filter_pi_star | 40 | 3.5176 | 1.1484 | 0.6000 | 0.3709 | 0.0059 | 0.2250 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1400_pos_at_h` | one_head_filter_pi_star | 34 | 3.2798 | 0.7985 | 0.5000 | -0.6614 | -0.0117 | 0.2059 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1400_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6092 | 0.3158 | -0.8112 | -0.0390 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1400_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5903 | 0.2778 | -0.8512 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1400_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1400_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1400_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1400_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
