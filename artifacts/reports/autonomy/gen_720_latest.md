# Autonomy public-indicator hunt gen 720

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T083720Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1400_below_at_h` | one_head_filter_pi_star | 254 | 20.7495 | 1.8584 | 0.6654 | 4.2325 | 0.0204 | 0.3268 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1400_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 1.7959 | 0.6611 | 3.8845 | 0.0189 | 0.3473 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1400_below_at_h` | one_head_filter_pi_star | 294 | 24.0406 | 1.7238 | 0.6361 | 3.8809 | 0.0114 | 0.3163 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1400_below_at_h` | one_head_filter_pi_star | 295 | 23.9988 | 1.7456 | 0.6373 | 3.9612 | 0.0114 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1400_above_at_h` | one_head_filter_pi_star | 60 | 4.9876 | 1.8300 | 0.6833 | 2.0992 | 0.0114 | 0.3000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1400_above_at_h` | one_head_filter_pi_star | 55 | 4.5720 | 1.4983 | 0.6545 | 1.3315 | 0.0079 | 0.2727 | ok | RAN |
| ETHUSDT | 4 | `sma1400_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 1.1667 | 0.5741 | 0.6734 | 0.0066 | 0.2315 | ok | RAN |
| ETHUSDT | 8 | `sma1400_above_at_h` | one_head_filter_pi_star | 75 | 6.3820 | 1.0660 | 0.5467 | 0.2367 | 0.0028 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1400_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1400_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0624 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
