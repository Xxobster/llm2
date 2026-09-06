# Autonomy public-indicator hunt gen 1532

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T054915Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema977_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 2.0230 | 0.6712 | 4.3778 | 0.0227 | 0.3649 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema977_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.7473 | 0.6540 | 3.6263 | 0.0181 | 0.3376 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema977_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 1.7797 | 0.6550 | 3.8798 | 0.0121 | 0.3101 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema977_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.7414 | 0.6403 | 3.7287 | 0.0116 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema977_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.7318 | 0.6606 | 2.3862 | 0.0107 | 0.3211 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema977_above_at_h` | one_head_filter_pi_star | 119 | 9.8904 | 1.6365 | 0.6471 | 2.2759 | 0.0097 | 0.3277 | ok | RAN |
| ETHUSDT | 4 | `ema977_above_at_h` | one_head_filter_pi_star | 130 | 10.7287 | 1.2111 | 0.5846 | 0.9423 | 0.0082 | 0.2154 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema977_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 1.0077 | 0.5586 | 0.0356 | 0.0003 | 0.2162 | ok | RAN |
| BTCUSDT | 8 | `ema977_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema977_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema977_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema977_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema977_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema977_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema977_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema977_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema977_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema977_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema977_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema977_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema977_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema977_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema977_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema977_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
