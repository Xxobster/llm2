# Autonomy public-indicator hunt gen 396

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T012129Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema255_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9677 | 0.6959 | 4.3291 | 0.0233 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema255_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9379 | 0.6939 | 4.2748 | 0.0221 | 0.3827 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema255_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.2826 | 0.7033 | 4.5704 | 0.0178 | 0.3791 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema255_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.0856 | 0.6845 | 4.1698 | 0.0157 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema255_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2788 | 0.6170 | 1.4263 | 0.0092 | 0.2234 | ok | RAN |
| ETHUSDT | 4 | `ema255_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2399 | 0.6022 | 1.2678 | 0.0083 | 0.2204 | ok | RAN |
| SOLUSDT | 8 | `ema255_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3805 | 0.6062 | 1.9144 | 0.0060 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `ema255_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3779 | 0.5959 | 1.8977 | 0.0059 | 0.2642 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema255_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema255_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema255_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema255_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema255_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema255_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
