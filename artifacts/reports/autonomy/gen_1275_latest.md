# Autonomy public-indicator hunt gen 1275

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T175026Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma639_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0858 | 0.6895 | 4.4602 | 0.0245 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma639_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8592 | 0.6733 | 3.9896 | 0.0207 | 0.3663 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma639_below_at_h` | one_head_filter_pi_star | 215 | 17.4907 | 1.8035 | 0.6605 | 3.6538 | 0.0122 | 0.3209 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma639_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 1.6639 | 0.6507 | 3.0667 | 0.0107 | 0.3206 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma639_above_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.6615 | 0.6203 | 2.6629 | 0.0097 | 0.3038 | ok | RAN |
| ETHUSDT | 8 | `sma639_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.2469 | 0.6211 | 1.2064 | 0.0090 | 0.2298 | ok | RAN |
| SOLUSDT | 4 | `sma639_above_at_h` | one_head_filter_pi_star | 152 | 12.4648 | 1.5520 | 0.6118 | 2.2736 | 0.0085 | 0.3092 | ok | RAN |
| ETHUSDT | 4 | `sma639_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 1.1516 | 0.5939 | 0.7731 | 0.0057 | 0.2182 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma639_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma639_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma639_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma639_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma639_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma639_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma639_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma639_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma639_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma639_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma639_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma639_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma639_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma639_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma639_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma639_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
