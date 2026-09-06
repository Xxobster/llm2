# Autonomy public-indicator hunt gen 1044

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T155404Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema906_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 1.8653 | 0.6667 | 4.0366 | 0.0200 | 0.3504 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema906_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.8065 | 0.6597 | 3.8987 | 0.0192 | 0.3403 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema906_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.8616 | 0.6584 | 4.0088 | 0.0128 | 0.3045 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema906_below_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.7642 | 0.6531 | 3.7225 | 0.0119 | 0.3061 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema906_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.7760 | 0.6532 | 2.6944 | 0.0111 | 0.3145 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema906_above_at_h` | one_head_filter_pi_star | 137 | 11.3054 | 1.2773 | 0.5985 | 1.2245 | 0.0101 | 0.2117 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema906_above_at_h` | one_head_filter_pi_star | 119 | 9.7586 | 1.6610 | 0.6303 | 2.3528 | 0.0095 | 0.3361 | ok | RAN |
| ETHUSDT | 4 | `ema906_above_at_h` | one_head_filter_pi_star | 115 | 9.4908 | 1.1917 | 0.5913 | 0.8004 | 0.0072 | 0.2087 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema906_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0511 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema906_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema906_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema906_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema906_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema906_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema906_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema906_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema906_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema906_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema906_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema906_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema906_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema906_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema906_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema906_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
