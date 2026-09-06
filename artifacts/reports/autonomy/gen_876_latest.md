# Autonomy public-indicator hunt gen 876

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T230123Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema855_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 2.0599 | 0.6773 | 4.4372 | 0.0230 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema855_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.8472 | 0.6667 | 3.8176 | 0.0204 | 0.3699 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema855_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 1.8693 | 0.6597 | 3.9952 | 0.0127 | 0.3067 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema855_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 1.7989 | 0.6504 | 3.8443 | 0.0122 | 0.3089 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema855_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.8447 | 0.6512 | 2.8292 | 0.0119 | 0.3178 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema855_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.7572 | 0.6434 | 2.6060 | 0.0105 | 0.3178 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema855_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.2652 | 0.5960 | 1.2921 | 0.0097 | 0.2185 | ok | RAN |
| ETHUSDT | 8 | `ema855_above_at_h` | one_head_filter_pi_star | 134 | 11.0588 | 1.0871 | 0.5821 | 0.4212 | 0.0036 | 0.2164 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema855_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema855_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema855_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema855_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema855_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema855_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema855_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema855_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema855_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema855_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema855_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema855_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema855_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema855_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema855_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema855_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
