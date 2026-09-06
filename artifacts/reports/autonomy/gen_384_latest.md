# Autonomy public-indicator hunt gen 384

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T224046Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma560_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.0669 | 0.6932 | 4.3447 | 0.0245 | 0.4091 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma560_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.9024 | 0.6845 | 4.2111 | 0.0216 | 0.3689 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma560_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.9110 | 0.6700 | 3.9617 | 0.0137 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma560_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.7733 | 0.6584 | 3.4122 | 0.0119 | 0.3168 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma560_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.6773 | 0.6230 | 3.0149 | 0.0098 | 0.2775 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma560_above_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.4889 | 0.6067 | 2.0812 | 0.0078 | 0.2933 | ok | RAN |
| ETHUSDT | 8 | `sma560_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1729 | 0.5988 | 0.8947 | 0.0065 | 0.2267 | ok | RAN |
| ETHUSDT | 4 | `sma560_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.1339 | 0.5966 | 0.6944 | 0.0048 | 0.2159 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma560_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma560_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
