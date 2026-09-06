# Autonomy public-indicator hunt gen 360

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T164840Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma500_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0424 | 0.6957 | 4.4524 | 0.0242 | 0.4022 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma500_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0462 | 0.6856 | 4.5513 | 0.0232 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma500_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.9279 | 0.6798 | 3.7049 | 0.0135 | 0.3427 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma500_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.7818 | 0.6596 | 3.3899 | 0.0122 | 0.3404 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma500_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.3285 | 0.6178 | 1.5395 | 0.0115 | 0.2293 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma500_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2837 | 0.6000 | 1.4001 | 0.0098 | 0.2167 | ok | RAN |
| SOLUSDT | 4 | `sma500_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.5805 | 0.6182 | 2.4742 | 0.0091 | 0.3091 | ok | RAN |
| SOLUSDT | 8 | `sma500_above_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.5467 | 0.6071 | 2.3301 | 0.0083 | 0.2679 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma500_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma500_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
