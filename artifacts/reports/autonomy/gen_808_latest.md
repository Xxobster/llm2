# Autonomy public-indicator hunt gen 808

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T162648Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma1620_above_at_h` | one_head_filter_pi_star | 57 | 4.7382 | 2.4522 | 0.7193 | 2.8205 | 0.0184 | 0.3860 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1620_below_at_h` | one_head_filter_pi_star | 279 | 22.7917 | 1.7218 | 0.6487 | 3.9005 | 0.0176 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1620_above_at_h` | one_head_filter_pi_star | 60 | 5.2152 | 2.3643 | 0.7333 | 2.6821 | 0.0166 | 0.3167 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1620_below_at_h` | one_head_filter_pi_star | 304 | 24.8340 | 1.6371 | 0.6546 | 3.6917 | 0.0162 | 0.3191 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1620_below_at_h` | one_head_filter_pi_star | 300 | 24.4056 | 1.7408 | 0.6333 | 3.9399 | 0.0111 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1620_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.7353 | 0.6389 | 4.0435 | 0.0111 | 0.3179 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1620_above_at_h` | one_head_filter_pi_star | 97 | 8.0053 | 1.2670 | 0.5979 | 0.9448 | 0.0107 | 0.2062 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1620_above_at_h` | one_head_filter_pi_star | 96 | 7.9227 | 1.2343 | 0.5938 | 0.8823 | 0.0099 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1620_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1620_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
