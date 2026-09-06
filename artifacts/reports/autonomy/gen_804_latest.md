# Autonomy public-indicator hunt gen 804

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T160456Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema765_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.9622 | 0.6765 | 4.0247 | 0.0221 | 0.3775 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema765_below_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 1.9560 | 0.6857 | 4.0770 | 0.0217 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema765_below_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.8644 | 0.6623 | 3.8665 | 0.0128 | 0.3247 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema765_below_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 1.8480 | 0.6625 | 3.9580 | 0.0127 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema765_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.8329 | 0.6716 | 2.9285 | 0.0117 | 0.3358 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema765_above_at_h` | one_head_filter_pi_star | 132 | 10.7633 | 1.6311 | 0.6212 | 2.4173 | 0.0093 | 0.3106 | ok | RAN |
| ETHUSDT | 4 | `ema765_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.1578 | 0.5796 | 0.7481 | 0.0056 | 0.1975 | ok | RAN |
| ETHUSDT | 8 | `ema765_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.1268 | 0.5816 | 0.5859 | 0.0049 | 0.1986 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema765_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0408 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema765_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0467 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema765_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema765_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
