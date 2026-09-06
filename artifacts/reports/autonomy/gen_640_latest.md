# Autonomy public-indicator hunt gen 640

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T030440Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1200_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.1108 | 0.6904 | 4.2897 | 0.0237 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma1200_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.9205 | 0.6756 | 4.1975 | 0.0217 | 0.3467 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1200_below_at_h` | one_head_filter_pi_star | 274 | 22.4052 | 1.7495 | 0.6423 | 3.7556 | 0.0121 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1200_below_at_h` | one_head_filter_pi_star | 252 | 20.5007 | 1.7017 | 0.6310 | 3.5171 | 0.0112 | 0.3016 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1200_above_at_h` | one_head_filter_pi_star | 82 | 6.7397 | 1.4565 | 0.6341 | 1.4773 | 0.0071 | 0.2683 | ok | RAN |
| SOLUSDT | 4 | `sma1200_above_at_h` | one_head_filter_pi_star | 95 | 7.8082 | 1.4011 | 0.6316 | 1.3406 | 0.0064 | 0.2632 | ok | RAN |
| ETHUSDT | 4 | `sma1200_above_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 1.0377 | 0.5512 | 0.1767 | 0.0016 | 0.2047 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1200_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 1.0271 | 0.5620 | 0.1316 | 0.0011 | 0.1971 | ok | RAN |
| BTCUSDT | 8 | `sma1200_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1200_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
