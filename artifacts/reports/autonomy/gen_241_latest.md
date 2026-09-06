# Autonomy public-indicator hunt gen 241

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T011955Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema130_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0855 | 0.6990 | 4.7307 | 0.0247 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema130_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0243 | 0.6915 | 4.5656 | 0.0239 | 0.3777 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema130_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2088 | 0.6964 | 4.2057 | 0.0176 | 0.3869 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema130_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2086 | 0.6875 | 4.2899 | 0.0174 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema130_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3688 | 0.5991 | 1.9239 | 0.0056 | 0.2642 | ok | RAN |
| ETHUSDT | 4 | `ema130_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1501 | 0.5947 | 0.7859 | 0.0054 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `ema130_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3036 | 0.5922 | 1.6120 | 0.0047 | 0.2670 | ok | RAN |
| ETHUSDT | 8 | `ema130_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.1296 | 0.5855 | 0.6791 | 0.0046 | 0.2280 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema130_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema130_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema130_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema130_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
