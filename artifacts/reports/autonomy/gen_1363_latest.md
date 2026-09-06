# Autonomy public-indicator hunt gen 1363

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T021355Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma653_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0417 | 0.6919 | 4.4805 | 0.0243 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma653_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0090 | 0.6813 | 4.2148 | 0.0236 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma653_below_at_h` | one_head_filter_pi_star | 214 | 17.4093 | 1.8310 | 0.6636 | 3.6718 | 0.0124 | 0.3224 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma653_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.7341 | 0.6632 | 3.2949 | 0.0116 | 0.3368 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma653_above_at_h` | one_head_filter_pi_star | 150 | 12.3782 | 1.3077 | 0.6133 | 1.4147 | 0.0105 | 0.2133 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma653_above_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.5519 | 0.6174 | 2.3046 | 0.0088 | 0.3020 | ok | RAN |
| SOLUSDT | 4 | `sma653_above_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.5116 | 0.6111 | 2.0590 | 0.0083 | 0.3125 | ok | RAN |
| ETHUSDT | 8 | `sma653_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1477 | 0.6000 | 0.7547 | 0.0056 | 0.2176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma653_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma653_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma653_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma653_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma653_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma653_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma653_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma653_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma653_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma653_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma653_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma653_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma653_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma653_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma653_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma653_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
