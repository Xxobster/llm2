# Autonomy public-indicator hunt gen 313

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T062524Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema340_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9811 | 0.6907 | 4.3076 | 0.0229 | 0.3866 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema340_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9242 | 0.6842 | 4.0993 | 0.0223 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema340_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.8997 | 0.6634 | 3.8596 | 0.0139 | 0.3366 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema340_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8630 | 0.6667 | 3.7372 | 0.0135 | 0.3578 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema340_above_at_h` | one_head_filter_pi_star | 175 | 14.4412 | 1.2736 | 0.6114 | 1.3476 | 0.0093 | 0.2286 | ok | RAN |
| SOLUSDT | 8 | `ema340_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5640 | 0.6328 | 2.5617 | 0.0086 | 0.2768 | ok | RAN |
| SOLUSDT | 4 | `ema340_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.5165 | 0.6167 | 2.3639 | 0.0080 | 0.2722 | ok | RAN |
| ETHUSDT | 4 | `ema340_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1670 | 0.5957 | 0.8967 | 0.0059 | 0.2128 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema340_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema340_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
