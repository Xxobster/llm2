# Autonomy public-indicator hunt gen 171

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T204222Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma65_cross_up` | one_head_filter_pi_star | 19 | 1.5795 | 7.0258 | 0.6842 | 2.4365 | 0.0394 | 0.2632 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma65_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8239 | 0.6816 | 3.8460 | 0.0215 | 0.3781 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma65_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.7709 | 0.6782 | 3.8061 | 0.0203 | 0.3762 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma65_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2069 | 0.6890 | 4.1305 | 0.0183 | 0.4085 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma65_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.0997 | 0.6835 | 3.9074 | 0.0170 | 0.4177 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma65_cross_down` | one_head_filter_pi_star | 20 | 2.0242 | 1.3754 | 0.5500 | 0.6730 | 0.0126 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma65_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.3234 | 0.6067 | 1.5120 | 0.0094 | 0.2191 | ok | RAN |
| ETHUSDT | 8 | `sma65_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2556 | 0.6037 | 1.1637 | 0.0076 | 0.2134 | ok | RAN |
| SOLUSDT | 4 | `sma65_above_at_h` | one_head_filter_pi_star | 219 | 17.8573 | 1.3843 | 0.6027 | 2.0224 | 0.0056 | 0.2557 | ok | RAN |
| SOLUSDT | 8 | `sma65_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3257 | 0.5915 | 1.7465 | 0.0048 | 0.2535 | ok | RAN |
| ETHUSDT | 8 | `sma65_cross_up` | one_head_filter_pi_star | 12 | 1.2394 | 1.0580 | 0.4167 | 0.0949 | 0.0023 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma65_cross_down` | one_head_filter_pi_star | 20 | 1.7070 | 0.9841 | 0.6000 | -0.0280 | -0.0004 | 0.2000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma65_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma65_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma65_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma65_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma65_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma65_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma65_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma65_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma65_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma65_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma65_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma65_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
