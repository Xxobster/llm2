# Autonomy public-indicator hunt gen 864

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T214742Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1760_below_at_h` | one_head_filter_pi_star | 295 | 24.0988 | 1.6653 | 0.6542 | 3.7887 | 0.0165 | 0.3288 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1760_above_at_h` | one_head_filter_pi_star | 57 | 4.7382 | 2.2252 | 0.7193 | 2.6344 | 0.0160 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1760_below_at_h` | one_head_filter_pi_star | 316 | 25.8143 | 1.5959 | 0.6487 | 3.5396 | 0.0158 | 0.3196 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1760_above_at_h` | one_head_filter_pi_star | 59 | 4.9045 | 2.0072 | 0.6949 | 2.2474 | 0.0156 | 0.3220 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1760_below_at_h` | one_head_filter_pi_star | 305 | 24.8124 | 1.7722 | 0.6361 | 4.1039 | 0.0114 | 0.3049 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1760_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7183 | 0.6343 | 3.9036 | 0.0108 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1760_above_at_h` | one_head_filter_pi_star | 50 | 4.3970 | 1.1367 | 0.5600 | 0.3826 | 0.0055 | 0.2400 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1760_above_at_h` | one_head_filter_pi_star | 55 | 4.8367 | 0.9080 | 0.5273 | -0.3110 | -0.0044 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `sma1760_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1760_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3556 | 0.2857 | -1.3912 | -0.0763 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
