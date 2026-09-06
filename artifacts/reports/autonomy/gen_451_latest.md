# Autonomy public-indicator hunt gen 451

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T144412Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma214_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.1603 | 0.7135 | 4.8839 | 0.0254 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma214_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0838 | 0.7065 | 4.6647 | 0.0253 | 0.3913 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma214_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1469 | 0.6864 | 4.0190 | 0.0165 | 0.3728 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma214_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1204 | 0.6829 | 3.9185 | 0.0164 | 0.3720 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma214_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2857 | 0.6010 | 1.4365 | 0.0097 | 0.2176 | ok | RAN |
| ETHUSDT | 4 | `sma214_above_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.2005 | 0.5885 | 1.0346 | 0.0070 | 0.2135 | ok | RAN |
| SOLUSDT | 4 | `sma214_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3781 | 0.5950 | 1.9304 | 0.0059 | 0.2650 | ok | RAN |
| SOLUSDT | 8 | `sma214_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3355 | 0.5959 | 1.7404 | 0.0054 | 0.2591 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma214_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma214_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma214_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma214_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma214_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma214_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma214_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma214_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma214_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma214_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma214_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma214_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma214_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma214_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma214_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma214_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
