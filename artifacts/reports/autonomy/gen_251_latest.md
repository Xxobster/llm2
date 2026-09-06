# Autonomy public-indicator hunt gen 251

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T020150Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma68_cross_up` | one_head_filter_pi_star | 20 | 1.6665 | 6.1643 | 0.7000 | 2.7438 | 0.0365 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma68_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8312 | 0.6866 | 3.9014 | 0.0213 | 0.3781 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma68_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2260 | 0.6909 | 4.1720 | 0.0184 | 0.4121 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma68_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.6615 | 0.6683 | 3.3977 | 0.0178 | 0.3618 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma68_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.1175 | 0.6899 | 3.9411 | 0.0171 | 0.4177 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma68_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.3905 | 0.6167 | 1.7842 | 0.0114 | 0.2278 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma68_cross_down` | one_head_filter_pi_star | 24 | 2.3207 | 1.2764 | 0.5417 | 0.5839 | 0.0099 | 0.2917 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma68_above_at_h` | one_head_filter_pi_star | 168 | 13.8636 | 1.2938 | 0.6131 | 1.3531 | 0.0088 | 0.2202 | ok | RAN |
| SOLUSDT | 8 | `sma68_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3761 | 0.5991 | 1.9844 | 0.0055 | 0.2535 | ok | RAN |
| SOLUSDT | 4 | `sma68_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3464 | 0.5972 | 1.8464 | 0.0051 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma68_cross_down` | one_head_filter_pi_star | 21 | 2.0321 | 0.8096 | 0.5714 | -0.4312 | -0.0052 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma68_cross_up` | one_head_filter_pi_star | 14 | 1.4408 | 0.8176 | 0.3571 | -0.3576 | -0.0068 | 0.2857 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma68_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma68_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma68_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma68_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma68_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma68_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma68_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma68_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma68_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma68_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma68_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma68_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
