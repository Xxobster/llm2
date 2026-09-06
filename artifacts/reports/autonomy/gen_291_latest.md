# Autonomy public-indicator hunt gen 291

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T045051Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma92_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9840 | 0.7005 | 4.4649 | 0.0239 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma92_below_at_h` | one_head_filter_pi_star | 207 | 16.9100 | 1.7527 | 0.6763 | 3.7342 | 0.0201 | 0.3623 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma92_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.3158 | 0.6964 | 4.4520 | 0.0192 | 0.4048 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma92_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.3036 | 0.6959 | 4.4430 | 0.0187 | 0.3977 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma92_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.3322 | 0.6124 | 1.5492 | 0.0101 | 0.2303 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma92_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.3103 | 0.6044 | 1.5009 | 0.0095 | 0.2253 | ok | RAN |
| SOLUSDT | 8 | `sma92_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3252 | 0.5991 | 1.7250 | 0.0049 | 0.2547 | ok | RAN |
| SOLUSDT | 4 | `sma92_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2739 | 0.5902 | 1.4815 | 0.0043 | 0.2585 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma92_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma92_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma92_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma92_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma92_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma92_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma92_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma92_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma92_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma92_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma92_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma92_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma92_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma92_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma92_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma92_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
