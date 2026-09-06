# Autonomy public-indicator hunt gen 689

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T062319Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema1280_below_at_h` | one_head_filter_pi_star | 269 | 21.9748 | 1.8256 | 0.6654 | 4.2128 | 0.0191 | 0.3309 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1280_below_at_h` | one_head_filter_pi_star | 253 | 20.6678 | 1.7102 | 0.6522 | 3.6437 | 0.0173 | 0.3360 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1280_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.6994 | 0.6420 | 3.5867 | 0.0115 | 0.3268 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1280_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.6032 | 0.6237 | 3.3419 | 0.0101 | 0.3082 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1280_above_at_h` | one_head_filter_pi_star | 110 | 8.9694 | 1.6280 | 0.6545 | 2.1591 | 0.0088 | 0.2727 | ok | RAN |
| ETHUSDT | 8 | `ema1280_above_at_h` | one_head_filter_pi_star | 84 | 6.9324 | 1.1988 | 0.5833 | 0.7399 | 0.0080 | 0.2381 | ok | RAN |
| SOLUSDT | 4 | `ema1280_above_at_h` | one_head_filter_pi_star | 99 | 8.0725 | 1.5126 | 0.6364 | 1.7177 | 0.0077 | 0.2828 | ok | RAN |
| ETHUSDT | 4 | `ema1280_above_at_h` | one_head_filter_pi_star | 96 | 8.1689 | 1.0828 | 0.5521 | 0.3309 | 0.0034 | 0.2083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1280_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0295 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1280_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6169 | 0.2667 | -0.7191 | -0.0350 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
