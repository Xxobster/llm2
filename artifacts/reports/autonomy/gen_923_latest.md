# Autonomy public-indicator hunt gen 923

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T040134Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma612_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9785 | 0.6753 | 4.2763 | 0.0228 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma612_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9521 | 0.6667 | 4.1541 | 0.0217 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma612_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.8128 | 0.6633 | 3.5387 | 0.0126 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma612_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.7295 | 0.6618 | 3.3535 | 0.0115 | 0.3285 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma612_above_at_h` | one_head_filter_pi_star | 136 | 11.2229 | 1.2967 | 0.6103 | 1.3214 | 0.0104 | 0.2132 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma612_above_at_h` | one_head_filter_pi_star | 155 | 12.6388 | 1.6352 | 0.6194 | 2.5674 | 0.0096 | 0.3097 | ok | RAN |
| SOLUSDT | 4 | `sma612_above_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.5218 | 0.6107 | 2.1403 | 0.0084 | 0.3154 | ok | RAN |
| ETHUSDT | 8 | `sma612_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1994 | 0.6101 | 0.9972 | 0.0072 | 0.2201 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma612_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma612_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma612_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma612_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma612_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma612_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma612_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma612_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma612_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma612_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma612_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma612_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma612_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma612_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma612_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma612_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
