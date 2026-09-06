# Autonomy public-indicator hunt gen 820

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T173342Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema785_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 2.0446 | 0.6842 | 4.3474 | 0.0231 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema785_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.9624 | 0.6697 | 4.1855 | 0.0220 | 0.3620 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema785_below_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.9277 | 0.6681 | 4.2076 | 0.0136 | 0.3149 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema785_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.7571 | 0.6567 | 3.5317 | 0.0116 | 0.3133 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema785_above_at_h` | one_head_filter_pi_star | 125 | 10.2506 | 1.6095 | 0.6320 | 2.2111 | 0.0091 | 0.3440 | ok | RAN |
| SOLUSDT | 4 | `ema785_above_at_h` | one_head_filter_pi_star | 140 | 11.4157 | 1.5826 | 0.6214 | 2.3278 | 0.0089 | 0.3214 | ok | RAN |
| ETHUSDT | 8 | `ema785_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.1811 | 0.5921 | 0.8609 | 0.0066 | 0.2171 | ok | RAN |
| ETHUSDT | 4 | `ema785_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.0921 | 0.5859 | 0.4290 | 0.0034 | 0.2031 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema785_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0408 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema785_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema785_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema785_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema785_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema785_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
