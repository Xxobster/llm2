# Autonomy public-indicator hunt gen 1156

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T054144Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema922_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.9165 | 0.6726 | 4.1703 | 0.0209 | 0.3496 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema922_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 1.8823 | 0.6711 | 3.9869 | 0.0208 | 0.3640 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema922_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 1.7576 | 0.6471 | 3.6747 | 0.0118 | 0.2983 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema922_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.7413 | 0.6475 | 3.6472 | 0.0117 | 0.3033 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema922_above_at_h` | one_head_filter_pi_star | 125 | 10.3891 | 1.7060 | 0.6400 | 2.5314 | 0.0103 | 0.3040 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema922_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.2697 | 0.6087 | 1.2138 | 0.0101 | 0.2464 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema922_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.6194 | 0.6290 | 2.2461 | 0.0090 | 0.2984 | ok | RAN |
| ETHUSDT | 4 | `ema922_above_at_h` | one_head_filter_pi_star | 126 | 10.3570 | 1.1450 | 0.5794 | 0.6485 | 0.0057 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema922_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0314 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema922_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0531 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema922_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema922_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema922_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema922_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema922_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema922_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema922_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema922_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema922_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema922_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema922_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema922_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema922_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema922_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
