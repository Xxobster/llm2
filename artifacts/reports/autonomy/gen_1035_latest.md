# Autonomy public-indicator hunt gen 1035

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T145441Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma602_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.1657 | 0.6949 | 4.5363 | 0.0255 | 0.4011 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma602_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0443 | 0.6828 | 4.3885 | 0.0235 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma602_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8776 | 0.6716 | 3.7998 | 0.0128 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma602_below_at_h` | one_head_filter_pi_star | 210 | 17.0839 | 1.7393 | 0.6524 | 3.3589 | 0.0113 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma602_above_at_h` | one_head_filter_pi_star | 160 | 13.1208 | 1.6547 | 0.6250 | 2.6542 | 0.0099 | 0.3125 | ok | RAN |
| SOLUSDT | 8 | `sma602_above_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 1.5851 | 0.6327 | 2.3839 | 0.0093 | 0.3197 | ok | RAN |
| ETHUSDT | 8 | `sma602_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1552 | 0.5802 | 0.7929 | 0.0057 | 0.2099 | ok | RAN |
| ETHUSDT | 4 | `sma602_above_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.1218 | 0.5897 | 0.6678 | 0.0046 | 0.2051 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma602_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma602_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma602_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma602_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma602_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma602_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma602_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma602_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma602_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma602_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma602_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma602_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma602_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma602_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma602_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma602_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
