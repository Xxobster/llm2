# Autonomy public-indicator hunt gen 964

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T173857Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema965_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8882 | 0.6622 | 4.0089 | 0.0209 | 0.3559 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema965_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.7608 | 0.6550 | 3.6321 | 0.0183 | 0.3450 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema965_below_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.8050 | 0.6537 | 3.7409 | 0.0123 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema965_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.6697 | 0.6381 | 3.4776 | 0.0108 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema965_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.6954 | 0.6400 | 2.4484 | 0.0100 | 0.3120 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema965_above_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.6289 | 0.6393 | 2.2324 | 0.0094 | 0.3197 | ok | RAN |
| ETHUSDT | 8 | `ema965_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 1.2143 | 0.5970 | 0.9477 | 0.0082 | 0.2313 | ok | RAN |
| ETHUSDT | 4 | `ema965_above_at_h` | one_head_filter_pi_star | 124 | 10.1926 | 1.1115 | 0.5726 | 0.4998 | 0.0043 | 0.2258 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema965_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema965_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema965_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema965_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema965_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema965_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema965_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema965_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema965_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema965_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema965_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema965_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema965_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema965_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema965_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema965_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
