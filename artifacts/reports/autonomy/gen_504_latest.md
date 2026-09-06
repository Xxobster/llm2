# Autonomy public-indicator hunt gen 504

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T181011Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma860_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.2542 | 0.7072 | 4.7142 | 0.0260 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma860_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.1493 | 0.7000 | 4.5485 | 0.0252 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma860_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 1.7620 | 0.6589 | 3.5182 | 0.0119 | 0.3178 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma860_below_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 1.6589 | 0.6422 | 3.1593 | 0.0111 | 0.3119 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma860_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.5853 | 0.6241 | 2.3080 | 0.0090 | 0.2908 | ok | RAN |
| ETHUSDT | 8 | `sma860_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.2239 | 0.6067 | 1.0391 | 0.0083 | 0.2067 | ok | RAN |
| SOLUSDT | 4 | `sma860_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.4740 | 0.5956 | 1.8839 | 0.0075 | 0.3015 | ok | RAN |
| ETHUSDT | 4 | `sma860_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1776 | 0.5890 | 0.8473 | 0.0067 | 0.2147 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma860_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma860_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
