# Autonomy public-indicator hunt gen 1148

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T043853Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema921_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1259 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema921_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.8348 | 0.6681 | 3.9820 | 0.0198 | 0.3581 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema921_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.8517 | 0.6610 | 3.9881 | 0.0196 | 0.3390 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema921_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 1.8433 | 0.6527 | 3.9586 | 0.0126 | 0.2971 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema921_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 1.7499 | 0.6485 | 3.6289 | 0.0117 | 0.2971 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema921_above_at_h` | one_head_filter_pi_star | 128 | 10.4372 | 1.7285 | 0.6406 | 2.5200 | 0.0106 | 0.3125 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema921_above_at_h` | one_head_filter_pi_star | 137 | 11.1710 | 1.5289 | 0.6131 | 2.0953 | 0.0079 | 0.3066 | ok | RAN |
| ETHUSDT | 8 | `ema921_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.1489 | 0.5752 | 0.7158 | 0.0060 | 0.2026 | ok | RAN |
| ETHUSDT | 4 | `ema921_above_at_h` | one_head_filter_pi_star | 136 | 11.2239 | 1.1371 | 0.5809 | 0.6473 | 0.0055 | 0.2132 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema921_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema921_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema921_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema921_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema921_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema921_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema921_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema921_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema921_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema921_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema921_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema921_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema921_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema921_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema921_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
