# Autonomy public-indicator hunt gen 1235

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T133710Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma633_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.1043 | 0.6939 | 4.5928 | 0.0250 | 0.3827 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma633_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9353 | 0.6837 | 4.1786 | 0.0226 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma633_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 1.7793 | 0.6603 | 3.4557 | 0.0120 | 0.3254 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma633_above_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.7357 | 0.6398 | 2.9587 | 0.0115 | 0.3168 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma633_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7130 | 0.6571 | 3.3120 | 0.0113 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma633_above_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.5861 | 0.6084 | 2.5015 | 0.0090 | 0.3012 | ok | RAN |
| ETHUSDT | 8 | `sma633_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.2179 | 0.6108 | 1.0891 | 0.0080 | 0.2156 | ok | RAN |
| ETHUSDT | 4 | `sma633_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.1219 | 0.5962 | 0.6366 | 0.0047 | 0.1987 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma633_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma633_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma633_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma633_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma633_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma633_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma633_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma633_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma633_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma633_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma633_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma633_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma633_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma633_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma633_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma633_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
