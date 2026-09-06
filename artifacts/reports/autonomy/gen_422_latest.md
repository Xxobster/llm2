# Autonomy public-indicator hunt gen 422

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T072211Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma170_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0434 | 0.7010 | 4.6557 | 0.0242 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma170_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9964 | 0.6943 | 4.5550 | 0.0235 | 0.3731 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma170_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2989 | 0.6977 | 4.4674 | 0.0184 | 0.3895 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma170_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2140 | 0.6886 | 4.2073 | 0.0182 | 0.3952 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma170_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.2142 | 0.5967 | 1.0909 | 0.0073 | 0.2210 | ok | RAN |
| ETHUSDT | 4 | `wma170_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.1429 | 0.5882 | 0.7506 | 0.0050 | 0.2193 | ok | RAN |
| SOLUSDT | 4 | `wma170_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3114 | 0.6010 | 1.6432 | 0.0049 | 0.2660 | ok | RAN |
| SOLUSDT | 8 | `wma170_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2654 | 0.5805 | 1.4265 | 0.0042 | 0.2634 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma170_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma170_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma170_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma170_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma170_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma170_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma170_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma170_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma170_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma170_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma170_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma170_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma170_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma170_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma170_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma170_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
