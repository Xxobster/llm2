# Autonomy public-indicator hunt gen 141

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T184427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret64_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.7833 | 0.6825 | 3.8400 | 0.0209 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret64_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.7485 | 0.6809 | 3.6264 | 0.0197 | 0.3830 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret64_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2269 | 0.6941 | 4.2461 | 0.0177 | 0.3941 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret64_neg_at_h` | one_head_filter_pi_star | 154 | 12.7385 | 2.2227 | 0.6948 | 4.0968 | 0.0172 | 0.4091 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret64_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.3787 | 0.6196 | 1.7900 | 0.0114 | 0.2337 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret64_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2841 | 0.6141 | 1.4077 | 0.0091 | 0.2283 | ok | RAN |
| SOLUSDT | 4 | `ret64_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3936 | 0.6114 | 2.0047 | 0.0060 | 0.2539 | ok | RAN |
| SOLUSDT | 8 | `ret64_pos_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.2755 | 0.5879 | 1.4863 | 0.0042 | 0.2513 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret64_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret64_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret64_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret64_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret64_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret64_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret64_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret64_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret64_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret64_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret64_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret64_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret64_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret64_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret64_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret64_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
