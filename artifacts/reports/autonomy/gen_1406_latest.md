# Autonomy public-indicator hunt gen 1406

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T062637Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma785_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1673 | 0.6995 | 4.7219 | 0.0256 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma785_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.9593 | 0.6768 | 4.3415 | 0.0223 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma785_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.7646 | 0.6495 | 3.3676 | 0.0119 | 0.3299 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma785_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.7236 | 0.6583 | 3.2509 | 0.0113 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma785_above_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.5599 | 0.6114 | 2.4423 | 0.0088 | 0.2971 | ok | RAN |
| SOLUSDT | 8 | `wma785_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.5739 | 0.6138 | 2.6309 | 0.0087 | 0.2857 | ok | RAN |
| ETHUSDT | 4 | `wma785_above_at_h` | one_head_filter_pi_star | 143 | 11.8006 | 1.1830 | 0.5944 | 0.8739 | 0.0065 | 0.2098 | ok | RAN |
| ETHUSDT | 8 | `wma785_above_at_h` | one_head_filter_pi_star | 149 | 12.2957 | 1.1767 | 0.5906 | 0.8658 | 0.0064 | 0.2148 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma785_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma785_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma785_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma785_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
