# Autonomy public-indicator hunt gen 910

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T023101Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma475_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0366 | 0.7005 | 4.4524 | 0.0239 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma475_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9548 | 0.6919 | 4.2673 | 0.0227 | 0.3892 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma475_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1614 | 0.6901 | 4.1697 | 0.0164 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma475_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.9336 | 0.6684 | 3.7864 | 0.0139 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma475_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2152 | 0.5979 | 1.1223 | 0.0075 | 0.2222 | ok | RAN |
| ETHUSDT | 8 | `wma475_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2166 | 0.6000 | 1.1199 | 0.0075 | 0.2056 | ok | RAN |
| SOLUSDT | 8 | `wma475_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4295 | 0.6042 | 2.1195 | 0.0066 | 0.2604 | ok | RAN |
| SOLUSDT | 4 | `wma475_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3844 | 0.5959 | 1.9244 | 0.0061 | 0.2694 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma475_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma475_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma475_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma475_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma475_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma475_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
