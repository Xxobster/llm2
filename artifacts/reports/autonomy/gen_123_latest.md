# Autonomy public-indicator hunt gen 123

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T173256Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema34_cross_up` | one_head_filter_pi_star | 14 | 1.2294 | 18.1332 | 0.8571 | 3.0131 | 0.0726 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema34_cross_down` | one_head_filter_pi_star | 25 | 2.1985 | 3.2974 | 0.7600 | 2.3084 | 0.0276 | 0.0800 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema34_cross_down` | one_head_filter_pi_star | 13 | 1.5812 | 2.1512 | 0.5385 | 1.3355 | 0.0245 | 0.2308 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema34_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8001 | 0.6787 | 3.8943 | 0.0209 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema34_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.7943 | 0.6776 | 3.8197 | 0.0202 | 0.3738 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema34_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1235 | 0.6829 | 3.9366 | 0.0172 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema34_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1174 | 0.6813 | 3.8762 | 0.0171 | 0.4125 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema34_cross_up` | one_head_filter_pi_star | 16 | 1.4130 | 1.1999 | 0.5000 | 0.3121 | 0.0076 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema34_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2256 | 0.5975 | 1.0273 | 0.0072 | 0.2075 | ok | RAN |
| ETHUSDT | 4 | `ema34_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2067 | 0.5938 | 0.9491 | 0.0064 | 0.2062 | ok | RAN |
| SOLUSDT | 8 | `ema34_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3671 | 0.5991 | 1.9633 | 0.0053 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ema34_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3633 | 0.6019 | 1.9621 | 0.0053 | 0.2454 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema34_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema34_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema34_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema34_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema34_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema34_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema34_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema34_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema34_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema34_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema34_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema34_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
