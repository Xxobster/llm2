# Autonomy public-indicator hunt gen 516

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T185834Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema405_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0136 | 0.6968 | 4.4087 | 0.0236 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema405_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.9484 | 0.6796 | 4.2907 | 0.0222 | 0.3592 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema405_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8899 | 0.6667 | 3.8015 | 0.0135 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema405_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8536 | 0.6600 | 3.6559 | 0.0127 | 0.3450 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema405_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.6087 | 0.6230 | 2.7450 | 0.0092 | 0.2787 | ok | RAN |
| ETHUSDT | 4 | `ema405_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.2406 | 0.6176 | 1.1855 | 0.0085 | 0.2118 | ok | RAN |
| SOLUSDT | 8 | `ema405_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5332 | 0.6145 | 2.4470 | 0.0083 | 0.2682 | ok | RAN |
| ETHUSDT | 8 | `ema405_above_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.2404 | 0.6057 | 1.1987 | 0.0082 | 0.2171 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema405_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema405_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema405_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema405_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
