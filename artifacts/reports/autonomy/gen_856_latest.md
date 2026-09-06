# Autonomy public-indicator hunt gen 856

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T210041Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma1740_above_at_h` | one_head_filter_pi_star | 52 | 4.3226 | 2.5065 | 0.7500 | 2.8611 | 0.0202 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1740_below_at_h` | one_head_filter_pi_star | 302 | 24.6706 | 1.6208 | 0.6523 | 3.5998 | 0.0160 | 0.3179 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma1740_below_at_h` | one_head_filter_pi_star | 298 | 24.3439 | 1.5857 | 0.6443 | 3.4957 | 0.0153 | 0.3188 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1740_above_at_h` | one_head_filter_pi_star | 57 | 4.7382 | 2.0474 | 0.7018 | 2.2328 | 0.0146 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1740_below_at_h` | one_head_filter_pi_star | 317 | 25.7886 | 1.7245 | 0.6341 | 3.9722 | 0.0110 | 0.3123 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1740_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 1.6732 | 0.6270 | 3.6929 | 0.0103 | 0.3119 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1740_above_at_h` | one_head_filter_pi_star | 61 | 5.1975 | 1.1628 | 0.5738 | 0.5103 | 0.0070 | 0.2459 | ok | RAN |
| ETHUSDT | 4 | `sma1740_above_at_h` | one_head_filter_pi_star | 55 | 4.8367 | 1.0550 | 0.5455 | 0.1741 | 0.0024 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1740_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4722 | 0.2500 | -1.1303 | -0.0591 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1740_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.3380 | 0.2500 | -1.4955 | -0.0724 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
