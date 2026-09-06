# Autonomy public-indicator hunt gen 939

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T054715Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma624_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0233 | 0.6859 | 4.3486 | 0.0235 | 0.3822 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma624_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9473 | 0.6804 | 4.1877 | 0.0221 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma624_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8024 | 0.6717 | 3.5502 | 0.0124 | 0.3384 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma624_below_at_h` | one_head_filter_pi_star | 207 | 16.8399 | 1.7336 | 0.6570 | 3.3692 | 0.0117 | 0.3140 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma624_above_at_h` | one_head_filter_pi_star | 176 | 14.4329 | 1.6699 | 0.6364 | 2.8066 | 0.0100 | 0.2955 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma624_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.5586 | 0.6131 | 2.1976 | 0.0089 | 0.3212 | ok | RAN |
| ETHUSDT | 4 | `sma624_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.2137 | 0.5987 | 1.0353 | 0.0081 | 0.2229 | ok | RAN |
| ETHUSDT | 8 | `sma624_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2126 | 0.6044 | 1.1064 | 0.0076 | 0.2198 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma624_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma624_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma624_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma624_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma624_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma624_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma624_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma624_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma624_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma624_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma624_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma624_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma624_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma624_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma624_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma624_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
