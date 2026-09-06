# Autonomy public-indicator hunt gen 664

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T044031Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1260_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.1372 | 0.6884 | 4.3717 | 0.0241 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1260_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 2.0665 | 0.6933 | 4.6258 | 0.0234 | 0.3644 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1260_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.8809 | 0.6442 | 4.1890 | 0.0130 | 0.3109 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1260_below_at_h` | one_head_filter_pi_star | 285 | 23.3047 | 1.7175 | 0.6351 | 3.8521 | 0.0116 | 0.3158 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1260_above_at_h` | one_head_filter_pi_star | 96 | 7.8279 | 1.5628 | 0.6562 | 1.8454 | 0.0091 | 0.2812 | ok | RAN |
| SOLUSDT | 4 | `sma1260_above_at_h` | one_head_filter_pi_star | 97 | 7.9545 | 1.4608 | 0.6392 | 1.5485 | 0.0070 | 0.2887 | ok | RAN |
| ETHUSDT | 4 | `sma1260_above_at_h` | one_head_filter_pi_star | 129 | 10.6036 | 1.0428 | 0.5581 | 0.1933 | 0.0018 | 0.2093 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1260_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 1.0210 | 0.5366 | 0.0989 | 0.0009 | 0.2114 | ok | RAN |
| BTCUSDT | 4 | `sma1260_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6510 | 0.3750 | -0.6531 | -0.0312 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1260_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0611 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
