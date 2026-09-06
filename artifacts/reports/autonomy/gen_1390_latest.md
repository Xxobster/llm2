# Autonomy public-indicator hunt gen 1390

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T044611Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma775_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.1411 | 0.6950 | 4.7779 | 0.0248 | 0.3600 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma775_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 2.0125 | 0.6845 | 4.5333 | 0.0231 | 0.3641 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma775_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.8941 | 0.6651 | 3.8497 | 0.0132 | 0.3255 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma775_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.8297 | 0.6602 | 3.6256 | 0.0124 | 0.3058 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma775_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.2475 | 0.6037 | 1.2095 | 0.0088 | 0.2195 | ok | RAN |
| SOLUSDT | 8 | `wma775_above_at_h` | one_head_filter_pi_star | 159 | 13.0388 | 1.5573 | 0.6101 | 2.3788 | 0.0088 | 0.2893 | ok | RAN |
| SOLUSDT | 4 | `wma775_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5410 | 0.5989 | 2.4209 | 0.0085 | 0.2881 | ok | RAN |
| ETHUSDT | 8 | `wma775_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.2100 | 0.6012 | 1.0578 | 0.0074 | 0.2083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma775_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma775_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma775_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma775_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma775_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma775_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
