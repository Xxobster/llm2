# Autonomy public-indicator hunt gen 576

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T225635Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1040_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.8365 | 0.6667 | 3.9602 | 0.0204 | 0.3511 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1040_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9273 | 0.6771 | 3.8474 | 0.0202 | 0.3490 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1040_below_at_h` | one_head_filter_pi_star | 241 | 19.7068 | 1.7486 | 0.6432 | 3.6254 | 0.0119 | 0.3154 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1040_below_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 1.6674 | 0.6368 | 3.2812 | 0.0114 | 0.3077 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1040_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.7412 | 0.6372 | 2.4345 | 0.0099 | 0.3009 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1040_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.5958 | 0.6336 | 2.1735 | 0.0088 | 0.2977 | ok | RAN |
| ETHUSDT | 4 | `sma1040_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1005 | 0.5732 | 0.5110 | 0.0039 | 0.2195 | ok | RAN |
| ETHUSDT | 8 | `sma1040_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.0518 | 0.5603 | 0.2406 | 0.0020 | 0.2057 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1040_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1040_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0582 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
