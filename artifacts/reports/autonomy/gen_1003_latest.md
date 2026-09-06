# Autonomy public-indicator hunt gen 1003

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T104707Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma886_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.4111 | 0.7193 | 4.7717 | 0.0275 | 0.4035 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma886_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.1143 | 0.6947 | 4.4982 | 0.0244 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma886_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.8079 | 0.6619 | 3.5773 | 0.0127 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma886_below_at_h` | one_head_filter_pi_star | 225 | 18.3984 | 1.7607 | 0.6622 | 3.6013 | 0.0123 | 0.3200 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma886_above_at_h` | one_head_filter_pi_star | 142 | 11.5787 | 1.6515 | 0.6268 | 2.5198 | 0.0096 | 0.3099 | ok | RAN |
| SOLUSDT | 4 | `sma886_above_at_h` | one_head_filter_pi_star | 142 | 11.5787 | 1.5368 | 0.6056 | 2.1718 | 0.0084 | 0.2817 | ok | RAN |
| ETHUSDT | 8 | `sma886_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.1597 | 0.5876 | 0.8051 | 0.0061 | 0.2203 | ok | RAN |
| ETHUSDT | 4 | `sma886_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1441 | 0.5779 | 0.7019 | 0.0056 | 0.2078 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma886_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5735 | 0.2632 | -0.9106 | -0.0430 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma886_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma886_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma886_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma886_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma886_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma886_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma886_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma886_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma886_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma886_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma886_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma886_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma886_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma886_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma886_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
