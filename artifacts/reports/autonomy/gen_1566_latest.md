# Autonomy public-indicator hunt gen 1566

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T171841Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma422_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9873 | 0.6907 | 4.4090 | 0.0232 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma422_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9099 | 0.6915 | 4.1674 | 0.0225 | 0.3883 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma422_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.2272 | 0.6961 | 4.4776 | 0.0170 | 0.3812 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma422_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1728 | 0.6949 | 4.2431 | 0.0163 | 0.3785 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma422_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2250 | 0.5946 | 1.1838 | 0.0078 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `wma422_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1933 | 0.5885 | 1.0138 | 0.0067 | 0.2240 | ok | RAN |
| SOLUSDT | 8 | `wma422_above_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.3566 | 0.6034 | 1.7339 | 0.0057 | 0.2644 | ok | RAN |
| SOLUSDT | 4 | `wma422_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3520 | 0.5949 | 1.7931 | 0.0056 | 0.2615 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma422_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma422_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma422_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma422_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma422_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma422_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma422_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma422_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma422_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma422_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma422_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma422_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma422_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma422_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma422_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma422_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
