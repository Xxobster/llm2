# Autonomy public-indicator hunt gen 532

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T200430Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema425_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0583 | 0.6968 | 4.4431 | 0.0238 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema425_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9731 | 0.6804 | 4.2608 | 0.0225 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema425_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.8582 | 0.6618 | 3.7052 | 0.0130 | 0.3527 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema425_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.8253 | 0.6538 | 3.6587 | 0.0125 | 0.3365 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema425_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.3608 | 0.6215 | 1.7211 | 0.0119 | 0.2203 | ok | RAN |
| SOLUSDT | 4 | `ema425_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.6978 | 0.6354 | 3.2020 | 0.0108 | 0.2708 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema425_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5393 | 0.6193 | 2.4099 | 0.0085 | 0.2727 | ok | RAN |
| ETHUSDT | 8 | `ema425_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1600 | 0.5938 | 0.8106 | 0.0059 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema425_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema425_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema425_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema425_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema425_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema425_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
