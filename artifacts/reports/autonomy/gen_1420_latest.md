# Autonomy public-indicator hunt gen 1420

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T091534Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema961_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 1.8297 | 0.6667 | 3.9657 | 0.0194 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema961_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 1.7226 | 0.6524 | 3.5563 | 0.0176 | 0.3476 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema961_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.7974 | 0.6471 | 3.9507 | 0.0123 | 0.3020 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema961_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.6885 | 0.6342 | 3.5470 | 0.0112 | 0.2996 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema961_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.2994 | 0.6027 | 1.3453 | 0.0111 | 0.2192 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema961_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.6157 | 0.6328 | 2.2230 | 0.0095 | 0.3125 | ok | RAN |
| SOLUSDT | 8 | `ema961_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.5945 | 0.6423 | 2.1724 | 0.0089 | 0.3089 | ok | RAN |
| ETHUSDT | 4 | `ema961_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 1.0570 | 0.5586 | 0.2435 | 0.0022 | 0.1982 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema961_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema961_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema961_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema961_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema961_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema961_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema961_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema961_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema961_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema961_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema961_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema961_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema961_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema961_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema961_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema961_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
