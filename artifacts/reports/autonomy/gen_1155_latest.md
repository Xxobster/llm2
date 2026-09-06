# Autonomy public-indicator hunt gen 1155

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T053406Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma621_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.1109 | 0.6902 | 4.5473 | 0.0251 | 0.4022 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma621_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.1332 | 0.6979 | 4.7244 | 0.0250 | 0.3802 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma621_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8748 | 0.6806 | 3.7041 | 0.0127 | 0.3298 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma621_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 1.7850 | 0.6555 | 3.5549 | 0.0120 | 0.3158 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma621_above_at_h` | one_head_filter_pi_star | 172 | 14.1048 | 1.6779 | 0.6395 | 2.8253 | 0.0101 | 0.3081 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma621_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.6230 | 0.6241 | 2.4346 | 0.0097 | 0.3262 | ok | RAN |
| ETHUSDT | 8 | `sma621_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.2264 | 0.6053 | 1.0925 | 0.0083 | 0.2368 | ok | RAN |
| ETHUSDT | 4 | `sma621_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1178 | 0.5988 | 0.6203 | 0.0046 | 0.2151 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma621_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma621_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma621_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma621_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma621_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma621_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma621_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma621_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma621_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma621_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma621_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma621_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma621_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma621_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma621_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma621_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
