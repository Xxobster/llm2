# Autonomy public-indicator hunt gen 268

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T031306Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema105_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9166 | 0.6850 | 4.2518 | 0.0223 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema105_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.8826 | 0.6853 | 4.1382 | 0.0219 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema105_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 2.2272 | 0.6919 | 4.3099 | 0.0177 | 0.3895 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema105_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1413 | 0.6829 | 3.9941 | 0.0171 | 0.3963 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema105_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2188 | 0.5978 | 1.0651 | 0.0072 | 0.2174 | ok | RAN |
| ETHUSDT | 4 | `ema105_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2193 | 0.6000 | 1.0776 | 0.0072 | 0.2111 | ok | RAN |
| SOLUSDT | 8 | `ema105_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3134 | 0.5905 | 1.6612 | 0.0048 | 0.2619 | ok | RAN |
| SOLUSDT | 4 | `ema105_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2941 | 0.5854 | 1.5593 | 0.0045 | 0.2683 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema105_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema105_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema105_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema105_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
