# Autonomy public-indicator hunt gen 566

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T221726Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma260_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0956 | 0.7095 | 4.6290 | 0.0246 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma260_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0304 | 0.7021 | 4.5401 | 0.0235 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma260_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.1799 | 0.6919 | 4.1869 | 0.0171 | 0.3837 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma260_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1875 | 0.6890 | 4.1009 | 0.0171 | 0.3841 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma260_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2052 | 0.6020 | 1.0719 | 0.0072 | 0.2296 | ok | RAN |
| ETHUSDT | 8 | `wma260_above_at_h` | one_head_filter_pi_star | 195 | 16.0917 | 1.1943 | 0.5949 | 1.0177 | 0.0068 | 0.2359 | ok | RAN |
| SOLUSDT | 4 | `wma260_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3212 | 0.5854 | 1.6931 | 0.0050 | 0.2585 | ok | RAN |
| SOLUSDT | 8 | `wma260_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.2948 | 0.5833 | 1.5570 | 0.0046 | 0.2647 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma260_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma260_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
