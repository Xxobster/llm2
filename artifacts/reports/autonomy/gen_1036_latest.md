# Autonomy public-indicator hunt gen 1036

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T150117Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema904_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.9320 | 0.6757 | 4.1747 | 0.0214 | 0.3604 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema904_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.8687 | 0.6681 | 4.0083 | 0.0204 | 0.3534 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema904_below_at_h` | one_head_filter_pi_star | 258 | 20.9888 | 1.7536 | 0.6434 | 3.7975 | 0.0118 | 0.2984 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema904_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7220 | 0.6461 | 3.5700 | 0.0116 | 0.3045 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema904_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.6681 | 0.6260 | 2.4033 | 0.0096 | 0.3053 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema904_above_at_h` | one_head_filter_pi_star | 134 | 10.9264 | 1.6302 | 0.6194 | 2.3692 | 0.0091 | 0.3060 | ok | RAN |
| ETHUSDT | 4 | `ema904_above_at_h` | one_head_filter_pi_star | 132 | 10.8937 | 1.1875 | 0.5985 | 0.8755 | 0.0073 | 0.2197 | ok | RAN |
| ETHUSDT | 8 | `ema904_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.1042 | 0.5742 | 0.5281 | 0.0042 | 0.2129 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema904_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema904_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema904_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema904_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema904_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema904_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema904_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema904_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema904_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema904_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema904_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema904_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema904_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema904_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema904_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema904_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
