# Autonomy public-indicator hunt gen 976

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T223613Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2040_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.5817 | 0.6435 | 3.5004 | 0.0155 | 0.3112 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma2040_below_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 1.5518 | 0.6433 | 3.3410 | 0.0149 | 0.3140 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2040_above_at_h` | one_head_filter_pi_star | 70 | 5.8189 | 1.8628 | 0.6857 | 2.0992 | 0.0127 | 0.3000 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2040_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.8424 | 0.6424 | 4.3439 | 0.0124 | 0.3146 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2040_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7289 | 0.6278 | 3.9269 | 0.0111 | 0.3204 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2040_above_at_h` | one_head_filter_pi_star | 63 | 5.2370 | 1.3621 | 0.6349 | 0.9690 | 0.0056 | 0.2540 | ok | RAN |
| ETHUSDT | 8 | `sma2040_above_at_h` | one_head_filter_pi_star | 45 | 4.0706 | 1.0950 | 0.5556 | 0.2708 | 0.0040 | 0.2667 | ok | RAN |
| ETHUSDT | 4 | `sma2040_above_at_h` | one_head_filter_pi_star | 48 | 4.3420 | 1.0521 | 0.5417 | 0.1558 | 0.0020 | 0.2083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2040_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3356 | 0.2308 | -1.4359 | -0.0825 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma2040_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0910 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
