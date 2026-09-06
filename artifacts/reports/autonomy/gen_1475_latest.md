# Autonomy public-indicator hunt gen 1475

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T002818Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma670_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1620 | 0.6952 | 4.6892 | 0.0255 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma670_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0747 | 0.6904 | 4.4771 | 0.0246 | 0.3858 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma670_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 1.8408 | 0.6603 | 3.6589 | 0.0125 | 0.3158 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma670_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.7124 | 0.6667 | 3.2395 | 0.0115 | 0.3282 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma670_above_at_h` | one_head_filter_pi_star | 117 | 9.5946 | 1.7915 | 0.6325 | 2.5773 | 0.0113 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma670_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.5601 | 0.6131 | 2.2013 | 0.0086 | 0.3066 | ok | RAN |
| ETHUSDT | 4 | `sma670_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.1694 | 0.6014 | 0.8090 | 0.0061 | 0.2162 | ok | RAN |
| ETHUSDT | 8 | `sma670_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.0801 | 0.5789 | 0.4273 | 0.0031 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma670_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma670_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma670_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma670_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
