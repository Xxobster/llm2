# Autonomy public-indicator hunt gen 377

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T210300Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema500_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.2119 | 0.7098 | 4.8828 | 0.0259 | 0.3938 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema500_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9782 | 0.6866 | 4.3198 | 0.0228 | 0.3831 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema500_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8877 | 0.6599 | 3.7325 | 0.0130 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema500_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.8110 | 0.6538 | 3.5783 | 0.0124 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema500_above_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.5756 | 0.6084 | 2.4874 | 0.0090 | 0.2892 | ok | RAN |
| SOLUSDT | 8 | `ema500_above_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.5311 | 0.6127 | 2.3686 | 0.0083 | 0.2717 | ok | RAN |
| ETHUSDT | 4 | `ema500_above_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.1945 | 0.5988 | 0.9768 | 0.0070 | 0.1976 | ok | RAN |
| ETHUSDT | 8 | `ema500_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.0901 | 0.5915 | 0.4615 | 0.0034 | 0.1951 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema500_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema500_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
