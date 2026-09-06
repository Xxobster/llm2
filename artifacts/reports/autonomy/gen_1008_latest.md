# Autonomy public-indicator hunt gen 1008

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T112334Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2120_below_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.6198 | 0.6422 | 3.7457 | 0.0162 | 0.3180 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2120_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5865 | 0.6420 | 3.6348 | 0.0157 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma2120_above_at_h` | one_head_filter_pi_star | 55 | 4.5720 | 1.9268 | 0.6909 | 1.9582 | 0.0129 | 0.2727 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2120_above_at_h` | one_head_filter_pi_star | 57 | 4.7382 | 2.0046 | 0.6842 | 2.1937 | 0.0129 | 0.2807 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2120_above_at_h` | one_head_filter_pi_star | 46 | 4.2309 | 1.3510 | 0.5870 | 0.9065 | 0.0127 | 0.2609 | ok | RAN |
| SOLUSDT | 8 | `sma2120_below_at_h` | one_head_filter_pi_star | 299 | 24.3242 | 1.8003 | 0.6421 | 4.1790 | 0.0117 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2120_below_at_h` | one_head_filter_pi_star | 320 | 26.0326 | 1.7314 | 0.6375 | 4.0789 | 0.0111 | 0.3156 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma2120_above_at_h` | one_head_filter_pi_star | 51 | 4.4659 | 1.1990 | 0.5882 | 0.5518 | 0.0084 | 0.1961 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2120_above_at_h` | one_head_filter_pi_star | 11 | 2.0201 | 0.3638 | 0.2727 | -1.8830 | -0.0854 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2120_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
