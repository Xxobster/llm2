# Autonomy public-indicator hunt gen 446

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T132517Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma185_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9689 | 0.6935 | 4.4435 | 0.0230 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma185_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9379 | 0.6878 | 4.2830 | 0.0225 | 0.3704 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma185_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.3017 | 0.7000 | 4.4600 | 0.0183 | 0.3882 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma185_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2111 | 0.6946 | 4.1845 | 0.0177 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma185_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1786 | 0.5959 | 0.9335 | 0.0062 | 0.2228 | ok | RAN |
| SOLUSDT | 4 | `wma185_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3548 | 0.6010 | 1.8324 | 0.0055 | 0.2660 | ok | RAN |
| ETHUSDT | 4 | `wma185_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1463 | 0.5885 | 0.7755 | 0.0051 | 0.2240 | ok | RAN |
| SOLUSDT | 8 | `wma185_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.2975 | 0.5882 | 1.5909 | 0.0047 | 0.2647 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma185_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma185_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma185_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma185_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma185_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma185_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
