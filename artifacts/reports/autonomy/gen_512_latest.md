# Autonomy public-indicator hunt gen 512

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T184202Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma880_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1474 | 0.7074 | 4.5700 | 0.0257 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma880_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.1185 | 0.6954 | 4.1709 | 0.0241 | 0.3851 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma880_below_at_h` | one_head_filter_pi_star | 226 | 18.4802 | 1.6853 | 0.6460 | 3.3149 | 0.0111 | 0.3097 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma880_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 1.6172 | 0.6355 | 2.9896 | 0.0103 | 0.3131 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma880_above_at_h` | one_head_filter_pi_star | 144 | 11.7418 | 1.6552 | 0.6250 | 2.5356 | 0.0099 | 0.3056 | ok | RAN |
| SOLUSDT | 8 | `sma880_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5335 | 0.6115 | 2.1451 | 0.0085 | 0.3094 | ok | RAN |
| ETHUSDT | 8 | `sma880_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.1391 | 0.5811 | 0.6386 | 0.0055 | 0.2162 | ok | RAN |
| ETHUSDT | 4 | `sma880_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 1.0957 | 0.5786 | 0.4431 | 0.0038 | 0.2214 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma880_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma880_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
