# Autonomy public-indicator hunt gen 1342

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T001559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma745_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0910 | 0.7027 | 4.5497 | 0.0247 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma745_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0743 | 0.6842 | 4.5675 | 0.0245 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma745_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.7915 | 0.6684 | 3.4322 | 0.0121 | 0.3367 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma745_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.7578 | 0.6580 | 3.3505 | 0.0118 | 0.3368 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma745_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.5800 | 0.6182 | 2.4890 | 0.0091 | 0.3030 | ok | RAN |
| SOLUSDT | 8 | `wma745_above_at_h` | one_head_filter_pi_star | 165 | 13.4542 | 1.5241 | 0.6182 | 2.2836 | 0.0081 | 0.2909 | ok | RAN |
| ETHUSDT | 4 | `wma745_above_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.1893 | 0.5928 | 0.9780 | 0.0067 | 0.2156 | ok | RAN |
| ETHUSDT | 8 | `wma745_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.1840 | 0.5928 | 0.9428 | 0.0065 | 0.2096 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma745_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma745_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma745_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma745_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma745_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma745_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
