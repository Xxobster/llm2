# Autonomy public-indicator hunt gen 092

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T153341Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema26_cross_up` | one_head_filter_pi_star | 12 | 0.9882 | 18.3983 | 0.8333 | 2.4998 | 0.0572 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema26_cross_down` | one_head_filter_pi_star | 23 | 2.0071 | 2.4948 | 0.6522 | 1.9504 | 0.0331 | 0.3043 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema26_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8239 | 0.6816 | 4.0067 | 0.0212 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema26_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.8214 | 0.6786 | 3.9995 | 0.0210 | 0.3705 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema26_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0180 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema26_cross_up` | one_head_filter_pi_star | 21 | 1.7968 | 1.4383 | 0.6190 | 0.7157 | 0.0179 | 0.2381 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema26_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1708 | 0.6914 | 4.0163 | 0.0178 | 0.4198 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema26_cross_down` | one_head_filter_pi_star | 27 | 2.2870 | 1.8419 | 0.7037 | 1.2661 | 0.0114 | 0.1111 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema26_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2067 | 0.5938 | 0.9491 | 0.0065 | 0.2062 | ok | RAN |
| ETHUSDT | 8 | `ema26_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1807 | 0.5912 | 0.8395 | 0.0058 | 0.2075 | ok | RAN |
| SOLUSDT | 4 | `ema26_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3846 | 0.6009 | 2.0796 | 0.0056 | 0.2431 | ok | RAN |
| SOLUSDT | 8 | `ema26_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3497 | 0.5953 | 1.9014 | 0.0051 | 0.2372 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema26_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema26_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema26_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema26_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema26_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema26_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema26_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema26_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema26_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema26_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema26_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema26_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
