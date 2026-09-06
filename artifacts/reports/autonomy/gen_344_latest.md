# Autonomy public-indicator hunt gen 344

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T141740Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma460_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.1013 | 0.6963 | 4.6484 | 0.0244 | 0.3665 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma460_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0941 | 0.6995 | 4.7361 | 0.0241 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma460_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.9831 | 0.6736 | 3.9873 | 0.0143 | 0.3523 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma460_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.8992 | 0.6798 | 3.6018 | 0.0133 | 0.3708 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma460_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.6179 | 0.6126 | 2.7168 | 0.0091 | 0.2670 | ok | RAN |
| ETHUSDT | 4 | `sma460_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.2517 | 0.5876 | 1.2454 | 0.0087 | 0.2090 | ok | RAN |
| ETHUSDT | 8 | `sma460_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.2382 | 0.5955 | 1.2070 | 0.0085 | 0.2079 | ok | RAN |
| SOLUSDT | 8 | `sma460_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.4268 | 0.5870 | 2.0131 | 0.0071 | 0.2826 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma460_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0409 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma460_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
