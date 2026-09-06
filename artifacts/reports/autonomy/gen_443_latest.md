# Autonomy public-indicator hunt gen 443

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T123758Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma208_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1640 | 0.7111 | 4.7821 | 0.0266 | 0.3833 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma208_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.0505 | 0.7006 | 4.5139 | 0.0243 | 0.3842 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma208_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2010 | 0.6919 | 4.1973 | 0.0168 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma208_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1089 | 0.6829 | 3.8954 | 0.0161 | 0.3720 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma208_above_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.3272 | 0.6105 | 1.6417 | 0.0108 | 0.2316 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma208_above_at_h` | one_head_filter_pi_star | 197 | 16.2567 | 1.2001 | 0.5939 | 1.0553 | 0.0071 | 0.2132 | ok | RAN |
| SOLUSDT | 8 | `sma208_above_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3750 | 0.5942 | 1.9296 | 0.0059 | 0.2609 | ok | RAN |
| SOLUSDT | 4 | `sma208_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3393 | 0.5909 | 1.7543 | 0.0053 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma208_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma208_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma208_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma208_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma208_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma208_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma208_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma208_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma208_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma208_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma208_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma208_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma208_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma208_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma208_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma208_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
