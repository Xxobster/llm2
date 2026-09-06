# Autonomy public-indicator hunt gen 448

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T135822Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma720_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.2510 | 0.6957 | 4.7724 | 0.0259 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma720_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.1903 | 0.6914 | 4.5510 | 0.0247 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma720_above_at_h` | one_head_filter_pi_star | 119 | 9.8904 | 1.8192 | 0.6471 | 2.7395 | 0.0121 | 0.3277 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma720_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.7154 | 0.6584 | 3.2767 | 0.0112 | 0.3218 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma720_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7152 | 0.6585 | 3.2426 | 0.0111 | 0.3220 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma720_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.6302 | 0.6190 | 2.3001 | 0.0097 | 0.3095 | ok | RAN |
| ETHUSDT | 8 | `sma720_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.1476 | 0.5915 | 0.7131 | 0.0055 | 0.2394 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma720_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.0188 | 0.5723 | 0.0992 | 0.0008 | 0.2229 | ok | RAN |
| BTCUSDT | 4 | `sma720_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma720_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
