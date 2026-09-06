# Autonomy public-indicator hunt gen 1556

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T080245Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema981_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema981_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.8055 | 0.6568 | 3.8576 | 0.0191 | 0.3432 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema981_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.7747 | 0.6565 | 3.7081 | 0.0185 | 0.3391 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema981_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.7352 | 0.6429 | 3.6907 | 0.0115 | 0.3056 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema981_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 1.7052 | 0.6423 | 3.6417 | 0.0112 | 0.2962 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema981_above_at_h` | one_head_filter_pi_star | 131 | 10.8103 | 1.3041 | 0.6031 | 1.2408 | 0.0110 | 0.2290 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema981_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.6749 | 0.6529 | 2.3938 | 0.0099 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema981_above_at_h` | one_head_filter_pi_star | 118 | 9.8073 | 1.5500 | 0.6356 | 2.0309 | 0.0086 | 0.3220 | ok | RAN |
| ETHUSDT | 4 | `ema981_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 1.2026 | 0.5926 | 0.8269 | 0.0073 | 0.2130 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema981_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0340 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema981_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema981_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema981_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema981_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema981_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema981_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema981_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema981_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema981_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema981_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema981_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema981_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema981_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema981_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
