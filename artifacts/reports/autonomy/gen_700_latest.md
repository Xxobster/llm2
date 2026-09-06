# Autonomy public-indicator hunt gen 700

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T071010Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema635_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.9246 | 0.6780 | 4.0535 | 0.0215 | 0.3805 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema635_below_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 1.8531 | 0.6667 | 4.0060 | 0.0204 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema635_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.8600 | 0.6699 | 3.7464 | 0.0134 | 0.3301 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema635_below_at_h` | one_head_filter_pi_star | 224 | 18.3167 | 1.8702 | 0.6652 | 3.9246 | 0.0132 | 0.3170 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema635_above_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.5842 | 0.6181 | 2.3183 | 0.0090 | 0.3194 | ok | RAN |
| SOLUSDT | 4 | `ema635_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.4987 | 0.6172 | 1.9503 | 0.0079 | 0.3438 | ok | RAN |
| ETHUSDT | 4 | `ema635_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.2080 | 0.5976 | 0.9904 | 0.0074 | 0.2012 | ok | RAN |
| ETHUSDT | 8 | `ema635_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.1772 | 0.6081 | 0.8290 | 0.0064 | 0.1959 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema635_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0393 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema635_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema635_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema635_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema635_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema635_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
