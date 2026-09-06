# Autonomy public-indicator hunt gen 345

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T143756Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema420_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0181 | 0.6802 | 4.3474 | 0.0235 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema420_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9266 | 0.6856 | 4.1856 | 0.0217 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema420_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.9634 | 0.6683 | 4.0273 | 0.0141 | 0.3462 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema420_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8827 | 0.6569 | 3.7965 | 0.0130 | 0.3431 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema420_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.6412 | 0.6243 | 2.8438 | 0.0097 | 0.2762 | ok | RAN |
| ETHUSDT | 4 | `ema420_above_at_h` | one_head_filter_pi_star | 175 | 14.4412 | 1.2818 | 0.6114 | 1.3899 | 0.0095 | 0.2057 | ok | RAN |
| ETHUSDT | 8 | `ema420_above_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.2722 | 0.6048 | 1.3125 | 0.0092 | 0.1976 | ok | RAN |
| SOLUSDT | 8 | `ema420_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.5552 | 0.6180 | 2.5608 | 0.0085 | 0.2697 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema420_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema420_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
