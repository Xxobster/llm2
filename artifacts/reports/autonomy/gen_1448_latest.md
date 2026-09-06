# Autonomy public-indicator hunt gen 1448

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T213906Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `sma3220_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 3.0531 | 0.7000 | 1.7887 | 0.1132 | 0.2000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma3220_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.6669 | 0.6667 | 1.5019 | 0.1094 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma3220_below_at_h` | one_head_filter_pi_star | 374 | 30.4256 | 1.6242 | 0.6497 | 4.0028 | 0.0167 | 0.2968 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma3220_below_at_h` | one_head_filter_pi_star | 378 | 30.7510 | 1.6031 | 0.6481 | 3.8900 | 0.0166 | 0.2989 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma3220_below_at_h` | one_head_filter_pi_star | 295 | 23.9988 | 1.8204 | 0.6508 | 4.3858 | 0.0128 | 0.3356 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma3220_below_at_h` | one_head_filter_pi_star | 297 | 24.2859 | 1.8067 | 0.6532 | 4.2701 | 0.0126 | 0.3401 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma3220_above_at_h` | one_head_filter_pi_star | 75 | 6.1504 | 1.6460 | 0.6267 | 1.7359 | 0.0085 | 0.1867 | ok | RAN |
| SOLUSDT | 4 | `sma3220_above_at_h` | one_head_filter_pi_star | 61 | 5.0145 | 1.4624 | 0.6066 | 1.1705 | 0.0067 | 0.1803 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma3220_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma3220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma3220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma3220_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `sma3220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma3220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma3220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma3220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma3220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma3220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma3220_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma3220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma3220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma3220_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma3220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma3220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
