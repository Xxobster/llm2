# Autonomy public-indicator hunt gen 1051

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T164603Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma604_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.9945 | 0.6869 | 4.3749 | 0.0232 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma604_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9421 | 0.6802 | 4.2606 | 0.0219 | 0.3655 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma604_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.8233 | 0.6719 | 3.5820 | 0.0125 | 0.3229 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma604_below_at_h` | one_head_filter_pi_star | 210 | 17.0839 | 1.8017 | 0.6619 | 3.6209 | 0.0121 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma604_above_at_h` | one_head_filter_pi_star | 159 | 12.9649 | 1.5872 | 0.6164 | 2.4775 | 0.0092 | 0.2956 | ok | RAN |
| SOLUSDT | 4 | `sma604_above_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.5456 | 0.6144 | 2.2777 | 0.0086 | 0.3137 | ok | RAN |
| ETHUSDT | 8 | `sma604_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1877 | 0.5987 | 0.9433 | 0.0068 | 0.2229 | ok | RAN |
| ETHUSDT | 4 | `sma604_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.1494 | 0.6044 | 0.7879 | 0.0056 | 0.2253 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma604_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0411 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma604_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma604_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma604_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma604_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma604_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma604_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma604_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma604_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma604_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma604_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma604_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma604_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma604_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma604_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma604_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
