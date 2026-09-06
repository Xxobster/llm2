# Autonomy public-indicator hunt gen 340

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T131602Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema190_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.1007 | 0.7053 | 4.6736 | 0.0255 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema190_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0061 | 0.6943 | 4.4894 | 0.0230 | 0.3731 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema190_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.2611 | 0.6983 | 4.4517 | 0.0178 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema190_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.1796 | 0.6936 | 4.2441 | 0.0172 | 0.3815 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema190_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1547 | 0.5895 | 0.8205 | 0.0055 | 0.2211 | ok | RAN |
| ETHUSDT | 8 | `ema190_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.1482 | 0.5926 | 0.7769 | 0.0053 | 0.2222 | ok | RAN |
| SOLUSDT | 8 | `ema190_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3297 | 0.5900 | 1.7275 | 0.0052 | 0.2700 | ok | RAN |
| SOLUSDT | 4 | `ema190_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.2976 | 0.5821 | 1.5845 | 0.0047 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema190_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema190_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema190_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema190_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema190_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema190_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
