# Autonomy public-indicator hunt gen 632

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T023358Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1180_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 2.0293 | 0.6796 | 4.1942 | 0.0232 | 0.3835 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1180_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0034 | 0.6915 | 3.9028 | 0.0216 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1180_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.8714 | 0.6492 | 4.1359 | 0.0132 | 0.2984 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1180_below_at_h` | one_head_filter_pi_star | 278 | 22.7323 | 1.8180 | 0.6475 | 4.1313 | 0.0123 | 0.3201 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1180_above_at_h` | one_head_filter_pi_star | 94 | 7.7085 | 1.7610 | 0.6702 | 2.3916 | 0.0107 | 0.2979 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1180_above_at_h` | one_head_filter_pi_star | 96 | 7.8725 | 1.5102 | 0.6354 | 1.6652 | 0.0076 | 0.2604 | ok | RAN |
| ETHUSDT | 8 | `sma1180_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.1013 | 0.5602 | 0.5177 | 0.0041 | 0.2169 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1180_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 0.9511 | 0.5547 | -0.2325 | -0.0021 | 0.2031 | ok | RAN |
| BTCUSDT | 8 | `sma1180_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1180_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0599 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
