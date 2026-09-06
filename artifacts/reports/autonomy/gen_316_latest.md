# Autonomy public-indicator hunt gen 316

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T063756Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema165_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0999 | 0.7062 | 4.8483 | 0.0240 | 0.3711 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema165_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0355 | 0.6943 | 4.5676 | 0.0239 | 0.3782 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema165_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1963 | 0.6944 | 4.3151 | 0.0175 | 0.3722 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema165_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1936 | 0.6936 | 4.2150 | 0.0172 | 0.3815 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema165_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2404 | 0.6000 | 1.2130 | 0.0082 | 0.2162 | ok | RAN |
| ETHUSDT | 4 | `ema165_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1540 | 0.5947 | 0.8135 | 0.0055 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `ema165_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3196 | 0.5850 | 1.6812 | 0.0049 | 0.2700 | ok | RAN |
| SOLUSDT | 8 | `ema165_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3132 | 0.5888 | 1.6465 | 0.0049 | 0.2741 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema165_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema165_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema165_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema165_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema165_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema165_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
