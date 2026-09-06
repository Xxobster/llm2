# Autonomy public-indicator hunt gen 908

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T021902Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema895_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9977 | 0.6802 | 4.0516 | 0.0216 | 0.3909 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema895_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7920 | 0.6622 | 3.7121 | 0.0193 | 0.3649 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema895_below_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 1.7570 | 0.6496 | 3.5932 | 0.0118 | 0.3162 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema895_below_at_h` | one_head_filter_pi_star | 257 | 20.9075 | 1.7624 | 0.6381 | 3.7733 | 0.0117 | 0.3035 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema895_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.6964 | 0.6480 | 2.4772 | 0.0100 | 0.2960 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema895_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.5125 | 0.6148 | 1.9491 | 0.0077 | 0.3115 | ok | RAN |
| ETHUSDT | 4 | `ema895_above_at_h` | one_head_filter_pi_star | 127 | 10.4811 | 1.1970 | 0.5906 | 0.8858 | 0.0076 | 0.2205 | ok | RAN |
| ETHUSDT | 8 | `ema895_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 1.1606 | 0.5903 | 0.7736 | 0.0063 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema895_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema895_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema895_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema895_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema895_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema895_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema895_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema895_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema895_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema895_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema895_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema895_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema895_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema895_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema895_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema895_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
