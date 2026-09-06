# Autonomy public-indicator hunt gen 715

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T081549Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma436_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.1836 | 0.7160 | 4.7007 | 0.0262 | 0.4024 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma436_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0244 | 0.6973 | 4.4613 | 0.0239 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma436_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.9274 | 0.6701 | 3.8313 | 0.0138 | 0.3505 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma436_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8948 | 0.6649 | 3.6960 | 0.0132 | 0.3508 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma436_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.5927 | 0.6178 | 2.7111 | 0.0090 | 0.2723 | ok | RAN |
| ETHUSDT | 8 | `sma436_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2567 | 0.5944 | 1.2957 | 0.0090 | 0.2333 | ok | RAN |
| SOLUSDT | 4 | `sma436_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4972 | 0.6053 | 2.3251 | 0.0080 | 0.2789 | ok | RAN |
| ETHUSDT | 4 | `sma436_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2258 | 0.5944 | 1.1898 | 0.0080 | 0.2167 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma436_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma436_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma436_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma436_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma436_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma436_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
