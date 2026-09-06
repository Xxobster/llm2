# Autonomy public-indicator hunt gen 500

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T175453Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema385_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9792 | 0.6839 | 4.3335 | 0.0232 | 0.3886 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema385_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8013 | 0.6717 | 3.8038 | 0.0200 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema385_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.9351 | 0.6633 | 3.8737 | 0.0142 | 0.3673 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema385_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7988 | 0.6537 | 3.5201 | 0.0118 | 0.3415 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema385_above_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5399 | 0.6114 | 2.4703 | 0.0085 | 0.2800 | ok | RAN |
| SOLUSDT | 4 | `ema385_above_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5467 | 0.6114 | 2.4429 | 0.0083 | 0.2686 | ok | RAN |
| ETHUSDT | 4 | `ema385_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2095 | 0.6034 | 1.0892 | 0.0075 | 0.2184 | ok | RAN |
| ETHUSDT | 8 | `ema385_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2059 | 0.6089 | 1.0732 | 0.0074 | 0.2291 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema385_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema385_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema385_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema385_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema385_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema385_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
