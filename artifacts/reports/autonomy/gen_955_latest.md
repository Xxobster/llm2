# Autonomy public-indicator hunt gen 955

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T073452Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma636_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0461 | 0.6818 | 4.4920 | 0.0240 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma636_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9273 | 0.6789 | 4.0529 | 0.0219 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma636_below_at_h` | one_head_filter_pi_star | 215 | 17.4907 | 1.8203 | 0.6605 | 3.6827 | 0.0128 | 0.3209 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma636_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 1.7475 | 0.6573 | 3.4444 | 0.0117 | 0.3192 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma636_above_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.5697 | 0.6149 | 2.4365 | 0.0089 | 0.3106 | ok | RAN |
| SOLUSDT | 4 | `sma636_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5102 | 0.6043 | 2.0402 | 0.0081 | 0.3237 | ok | RAN |
| ETHUSDT | 8 | `sma636_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1643 | 0.6025 | 0.8257 | 0.0060 | 0.2236 | ok | RAN |
| ETHUSDT | 4 | `sma636_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.1294 | 0.5864 | 0.6681 | 0.0049 | 0.2099 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma636_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma636_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma636_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma636_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma636_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma636_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma636_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma636_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma636_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma636_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma636_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma636_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma636_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma636_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma636_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma636_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
