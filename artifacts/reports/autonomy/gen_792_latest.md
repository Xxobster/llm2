# Autonomy public-indicator hunt gen 792

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T145609Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1580_below_at_h` | one_head_filter_pi_star | 273 | 22.3016 | 1.7567 | 0.6520 | 4.0192 | 0.0182 | 0.3187 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1580_below_at_h` | one_head_filter_pi_star | 278 | 22.7101 | 1.7202 | 0.6547 | 3.8863 | 0.0182 | 0.3273 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1580_above_at_h` | one_head_filter_pi_star | 56 | 4.6551 | 2.1185 | 0.7143 | 2.2076 | 0.0147 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma1580_above_at_h` | one_head_filter_pi_star | 57 | 4.7382 | 2.1031 | 0.7193 | 2.4497 | 0.0140 | 0.3509 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma1580_above_at_h` | one_head_filter_pi_star | 78 | 6.4372 | 1.3074 | 0.5897 | 0.9619 | 0.0115 | 0.2179 | ok | RAN |
| SOLUSDT | 4 | `sma1580_below_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 1.7821 | 0.6465 | 4.1761 | 0.0115 | 0.3217 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1580_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7572 | 0.6375 | 4.0362 | 0.0114 | 0.3139 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1580_above_at_h` | one_head_filter_pi_star | 72 | 6.0582 | 1.2104 | 0.5972 | 0.7068 | 0.0084 | 0.2361 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1580_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0532 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1580_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
