# Autonomy public-indicator hunt gen 376

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T204943Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma540_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.0042 | 0.6901 | 4.1968 | 0.0232 | 0.4094 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma540_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9504 | 0.6850 | 4.2778 | 0.0222 | 0.3700 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma540_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 2.0167 | 0.6804 | 4.0986 | 0.0145 | 0.3402 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma540_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8394 | 0.6754 | 3.6051 | 0.0129 | 0.3455 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma540_above_at_h` | one_head_filter_pi_star | 168 | 13.7768 | 1.6429 | 0.6310 | 2.7257 | 0.0096 | 0.2976 | ok | RAN |
| SOLUSDT | 4 | `sma540_above_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.5567 | 0.6069 | 2.4438 | 0.0087 | 0.3006 | ok | RAN |
| ETHUSDT | 4 | `sma540_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.1746 | 0.6023 | 0.9121 | 0.0064 | 0.2330 | ok | RAN |
| ETHUSDT | 8 | `sma540_above_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.1558 | 0.5808 | 0.7836 | 0.0057 | 0.2156 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma540_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma540_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
