# Autonomy public-indicator hunt gen 1016

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T122804Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2140_above_at_h` | one_head_filter_pi_star | 56 | 4.9037 | 1.6412 | 0.6429 | 1.6335 | 0.0234 | 0.2857 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2140_above_at_h` | one_head_filter_pi_star | 48 | 4.2211 | 1.4251 | 0.6250 | 1.0388 | 0.0164 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `sma2140_below_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 1.6095 | 0.6444 | 3.6399 | 0.0161 | 0.3131 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2140_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.6052 | 0.6405 | 3.6487 | 0.0161 | 0.3112 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma2140_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.8508 | 0.6471 | 4.3871 | 0.0124 | 0.3203 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2140_below_at_h` | one_head_filter_pi_star | 299 | 24.3242 | 1.7515 | 0.6355 | 3.9624 | 0.0110 | 0.3177 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2140_above_at_h` | one_head_filter_pi_star | 54 | 4.4889 | 1.5273 | 0.6481 | 1.2874 | 0.0082 | 0.2963 | ok | RAN |
| SOLUSDT | 4 | `sma2140_above_at_h` | one_head_filter_pi_star | 70 | 5.8189 | 1.4724 | 0.6429 | 1.3137 | 0.0074 | 0.3000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma2140_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0910 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2140_above_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.3638 | 0.2727 | -1.8830 | -0.0934 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
