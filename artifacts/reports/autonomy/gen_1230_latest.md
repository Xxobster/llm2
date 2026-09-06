# Autonomy public-indicator hunt gen 1230

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T130934Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma675_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1540 | 0.7005 | 4.7315 | 0.0254 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma675_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1379 | 0.7059 | 4.6602 | 0.0250 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma675_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 1.9424 | 0.6698 | 4.0781 | 0.0139 | 0.3349 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma675_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.9051 | 0.6702 | 3.7140 | 0.0133 | 0.3457 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma675_above_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.5434 | 0.6084 | 2.3577 | 0.0085 | 0.2952 | ok | RAN |
| SOLUSDT | 4 | `wma675_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.5057 | 0.6022 | 2.3029 | 0.0079 | 0.2707 | ok | RAN |
| ETHUSDT | 4 | `wma675_above_at_h` | one_head_filter_pi_star | 168 | 13.8636 | 1.2221 | 0.5952 | 1.1204 | 0.0078 | 0.2083 | ok | RAN |
| ETHUSDT | 8 | `wma675_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1563 | 0.5824 | 0.7980 | 0.0057 | 0.2118 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma675_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma675_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma675_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma675_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma675_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma675_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
