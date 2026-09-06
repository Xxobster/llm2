# Autonomy public-indicator hunt gen 164

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T201447Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema28_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8952 | 0.6847 | 4.2598 | 0.0222 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema28_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7814 | 0.6757 | 3.8443 | 0.0204 | 0.3694 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema28_cross_down` | one_head_filter_pi_star | 20 | 1.7588 | 2.6942 | 0.7500 | 1.7807 | 0.0196 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema28_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1669 | 0.6852 | 4.0295 | 0.0178 | 0.4198 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema28_cross_up` | one_head_filter_pi_star | 19 | 1.6780 | 1.4040 | 0.6316 | 0.6551 | 0.0175 | 0.2632 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema28_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1405 | 0.6832 | 3.9468 | 0.0174 | 0.4161 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema28_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2067 | 0.5938 | 0.9491 | 0.0065 | 0.2062 | ok | RAN |
| ETHUSDT | 8 | `ema28_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.1983 | 0.5949 | 0.9099 | 0.0063 | 0.2089 | ok | RAN |
| SOLUSDT | 4 | `ema28_above_at_h` | one_head_filter_pi_star | 219 | 17.8573 | 1.3944 | 0.6027 | 2.1222 | 0.0058 | 0.2466 | ok | RAN |
| SOLUSDT | 8 | `ema28_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3363 | 0.5943 | 1.8302 | 0.0050 | 0.2406 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema28_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema28_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema28_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema28_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema28_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema28_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
