# Autonomy public-indicator hunt gen 1168

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T070808Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `sma2520_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 3.0531 | 0.7000 | 1.7887 | 0.1230 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2520_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.5324 | 0.6328 | 3.3857 | 0.0148 | 0.3134 | ok | RAN |
| ETHUSDT | 8 | `sma2520_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5407 | 0.6361 | 3.3867 | 0.0147 | 0.3077 | ok | RAN |
| SOLUSDT | 4 | `sma2520_below_at_h` | one_head_filter_pi_star | 302 | 24.6948 | 1.8055 | 0.6523 | 4.2245 | 0.0122 | 0.3344 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2520_below_at_h` | one_head_filter_pi_star | 310 | 25.2191 | 1.7453 | 0.6387 | 4.0974 | 0.0115 | 0.3258 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma2520_above_at_h` | one_head_filter_pi_star | 50 | 4.1103 | 1.5225 | 0.6200 | 1.1626 | 0.0076 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `sma2520_above_at_h` | one_head_filter_pi_star | 53 | 4.4057 | 1.3347 | 0.6038 | 0.9536 | 0.0050 | 0.2264 | ok | RAN |
| ETHUSDT | 4 | `sma2520_above_at_h` | one_head_filter_pi_star | 44 | 4.0470 | 1.0943 | 0.5455 | 0.2663 | 0.0040 | 0.2273 | ok | RAN |
| ETHUSDT | 8 | `sma2520_above_at_h` | one_head_filter_pi_star | 37 | 3.6326 | 1.0904 | 0.5405 | 0.2389 | 0.0037 | 0.2162 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2520_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2520_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
