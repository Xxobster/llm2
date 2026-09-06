# Autonomy public-indicator hunt gen 305

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T055153Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema320_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9037 | 0.6888 | 4.1582 | 0.0216 | 0.3827 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema320_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8419 | 0.6834 | 3.9440 | 0.0209 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema320_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 2.0198 | 0.6772 | 4.0891 | 0.0150 | 0.3651 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema320_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 2.0181 | 0.6717 | 4.1113 | 0.0149 | 0.3535 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema320_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2644 | 0.6196 | 1.3668 | 0.0089 | 0.2174 | ok | RAN |
| SOLUSDT | 4 | `ema320_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.5226 | 0.6188 | 2.4037 | 0.0080 | 0.2762 | ok | RAN |
| SOLUSDT | 8 | `ema320_above_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.5014 | 0.6105 | 2.2795 | 0.0079 | 0.2733 | ok | RAN |
| ETHUSDT | 4 | `ema320_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.1708 | 0.5978 | 0.9046 | 0.0061 | 0.2179 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema320_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema320_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
