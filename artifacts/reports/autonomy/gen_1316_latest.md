# Autonomy public-indicator hunt gen 1316

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T215153Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema946_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 2.0207 | 0.6769 | 4.5106 | 0.0225 | 0.3537 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema946_below_at_h` | one_head_filter_pi_star | 244 | 19.9326 | 1.8359 | 0.6557 | 4.0283 | 0.0195 | 0.3320 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema946_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.7703 | 0.6598 | 3.7834 | 0.0123 | 0.2992 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema946_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.8223 | 0.6640 | 2.6991 | 0.0121 | 0.3360 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema946_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 1.7188 | 0.6415 | 3.7224 | 0.0113 | 0.3019 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema946_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.3111 | 0.6056 | 1.4052 | 0.0112 | 0.2254 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema946_above_at_h` | one_head_filter_pi_star | 128 | 10.4372 | 1.5908 | 0.6250 | 2.2218 | 0.0088 | 0.3125 | ok | RAN |
| ETHUSDT | 4 | `ema946_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.1870 | 0.5909 | 0.8251 | 0.0072 | 0.2273 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema946_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0313 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema946_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema946_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema946_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema946_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema946_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema946_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema946_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema946_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema946_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema946_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema946_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema946_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema946_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema946_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema946_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
