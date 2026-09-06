# Autonomy public-indicator hunt gen 544

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T205131Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma960_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.2839 | 0.7126 | 4.6224 | 0.0259 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma960_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.2221 | 0.7119 | 4.4798 | 0.0253 | 0.3898 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma960_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7632 | 0.6571 | 3.4706 | 0.0123 | 0.3381 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma960_below_at_h` | one_head_filter_pi_star | 222 | 18.1531 | 1.7700 | 0.6441 | 3.5665 | 0.0121 | 0.3243 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma960_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.8285 | 0.6489 | 2.7591 | 0.0113 | 0.3053 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma960_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.6688 | 0.6357 | 2.4131 | 0.0099 | 0.2946 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma960_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2428 | 0.5897 | 1.1525 | 0.0087 | 0.2308 | ok | RAN |
| ETHUSDT | 8 | `sma960_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1686 | 0.5793 | 0.8440 | 0.0062 | 0.2134 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma960_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma960_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4442 | 0.2632 | -1.2722 | -0.0596 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
