# Autonomy public-indicator hunt gen 427

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T083332Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma196_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0732 | 0.7043 | 4.6541 | 0.0246 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma196_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0057 | 0.6961 | 4.5103 | 0.0239 | 0.3867 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma196_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2407 | 0.6954 | 4.2950 | 0.0172 | 0.3793 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma196_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1542 | 0.6852 | 3.9667 | 0.0169 | 0.3827 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma196_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.3090 | 0.6062 | 1.5513 | 0.0102 | 0.2228 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma196_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2264 | 0.5907 | 1.1676 | 0.0078 | 0.2228 | ok | RAN |
| SOLUSDT | 4 | `sma196_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.4199 | 0.6059 | 2.1030 | 0.0065 | 0.2660 | ok | RAN |
| SOLUSDT | 8 | `sma196_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.2894 | 0.5825 | 1.5255 | 0.0046 | 0.2629 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma196_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma196_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma196_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma196_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma196_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma196_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma196_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma196_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma196_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma196_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma196_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma196_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma196_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma196_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma196_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma196_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
