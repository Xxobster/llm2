# Autonomy public-indicator hunt gen 280

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T040340Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma300_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8863 | 0.6862 | 4.1350 | 0.0224 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma300_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.8825 | 0.6848 | 4.0420 | 0.0215 | 0.3804 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma300_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1626 | 0.6867 | 4.0515 | 0.0166 | 0.3795 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma300_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1335 | 0.6805 | 4.0744 | 0.0165 | 0.3669 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma300_above_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.2235 | 0.6042 | 1.1801 | 0.0080 | 0.2188 | ok | RAN |
| ETHUSDT | 8 | `sma300_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2127 | 0.5969 | 1.1328 | 0.0072 | 0.2194 | ok | RAN |
| SOLUSDT | 8 | `sma300_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3837 | 0.5990 | 1.9158 | 0.0060 | 0.2538 | ok | RAN |
| SOLUSDT | 4 | `sma300_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3755 | 0.6019 | 1.9582 | 0.0059 | 0.2573 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma300_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma300_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
