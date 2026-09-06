# Autonomy public-indicator hunt gen 488

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T170759Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma820_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.3570 | 0.7150 | 5.0489 | 0.0277 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma820_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.3210 | 0.7143 | 4.8910 | 0.0274 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma820_below_at_h` | one_head_filter_pi_star | 230 | 18.8073 | 1.8148 | 0.6565 | 3.7703 | 0.0126 | 0.3087 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma820_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.7882 | 0.6538 | 3.5226 | 0.0121 | 0.3221 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma820_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.5502 | 0.6222 | 2.1525 | 0.0085 | 0.3037 | ok | RAN |
| SOLUSDT | 4 | `sma820_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.5158 | 0.6000 | 2.0676 | 0.0080 | 0.3000 | ok | RAN |
| ETHUSDT | 8 | `sma820_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.1936 | 0.6026 | 0.9313 | 0.0071 | 0.2119 | ok | RAN |
| ETHUSDT | 4 | `sma820_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1210 | 0.5912 | 0.6351 | 0.0047 | 0.2327 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma820_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma820_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
