# Autonomy public-indicator hunt gen 041

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T121246Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `vwma_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.8263 | 0.6828 | 3.9673 | 0.0209 | 0.3700 | EBR>35% | RAN |
| ETHUSDT | 4 | `vwma_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.7995 | 0.6771 | 3.8644 | 0.0205 | 0.3722 | EBR>35% | RAN |
| SOLUSDT | 8 | `vwma_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.2271 | 0.6914 | 4.1096 | 0.0186 | 0.4259 | EBR>35% | RAN |
| SOLUSDT | 4 | `vwma_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1790 | 0.6890 | 4.0338 | 0.0179 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 8 | `vwma_cross_down` | one_head_filter_pi_star | 48 | 4.0385 | 3.3617 | 0.7083 | 3.1556 | 0.0170 | 0.1667 | ok | RAN |
| ETHUSDT | 8 | `vwma_cross_up` | one_head_filter_pi_star | 36 | 2.9623 | 1.4373 | 0.5833 | 0.9468 | 0.0154 | 0.2778 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `vwma_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2007 | 0.5901 | 0.9283 | 0.0065 | 0.2050 | ok | RAN |
| SOLUSDT | 8 | `vwma_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3773 | 0.5935 | 2.0407 | 0.0057 | 0.2477 | ok | RAN |
| SOLUSDT | 4 | `vwma_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3698 | 0.5953 | 2.0046 | 0.0054 | 0.2465 | ok | RAN |
| ETHUSDT | 8 | `vwma_above_at_h` | one_head_filter_pi_star | 143 | 11.8006 | 1.0790 | 0.5664 | 0.3671 | 0.0028 | 0.1888 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `vwma_cross_down` | one_head_filter_pi_star | 44 | 4.0798 | 0.8328 | 0.5227 | -0.5165 | -0.0054 | 0.1591 | ok | RAN |
| SOLUSDT | 8 | `vwma_cross_up` | one_head_filter_pi_star | 13 | 1.4468 | 0.3470 | 0.3846 | -1.6533 | -0.0206 | 0.2308 | TPM<MIN | RAN |
| BTCUSDT | 8 | `vwma_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6245 | 0.3529 | -0.7502 | -0.0394 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `vwma_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `vwma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `vwma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `vwma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `vwma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `vwma_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `vwma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `vwma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `vwma_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `vwma_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `vwma_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
