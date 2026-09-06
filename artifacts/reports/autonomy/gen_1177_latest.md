# Autonomy public-indicator hunt gen 1177

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T080404Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2500_below_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 1.5923 | 0.6408 | 3.6890 | 0.0159 | 0.3017 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2500_below_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 1.5696 | 0.6429 | 3.5895 | 0.0156 | 0.3057 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2500_below_at_h` | one_head_filter_pi_star | 266 | 21.6396 | 1.8207 | 0.6466 | 4.0754 | 0.0124 | 0.3308 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2500_below_at_h` | one_head_filter_pi_star | 292 | 23.7548 | 1.8048 | 0.6404 | 4.1422 | 0.0118 | 0.3288 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2500_above_at_h` | one_head_filter_pi_star | 104 | 8.6437 | 1.6954 | 0.6635 | 2.2361 | 0.0103 | 0.2596 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2500_above_at_h` | one_head_filter_pi_star | 100 | 8.2192 | 1.4837 | 0.6200 | 1.6306 | 0.0076 | 0.2700 | ok | RAN |
| ETHUSDT | 4 | `ema2500_above_at_h` | one_head_filter_pi_star | 30 | 3.5253 | 1.0329 | 0.5000 | 0.0871 | 0.0015 | 0.2333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2500_above_at_h` | one_head_filter_pi_star | 16 | 1.8802 | 0.8049 | 0.4375 | -0.4662 | -0.0101 | 0.3125 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2500_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7376 | 0.3684 | -0.5246 | -0.0265 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2500_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
