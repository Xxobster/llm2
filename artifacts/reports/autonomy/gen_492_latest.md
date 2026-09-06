# Autonomy public-indicator hunt gen 492

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T172336Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema375_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0184 | 0.7000 | 4.4391 | 0.0235 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema375_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8784 | 0.6786 | 4.0216 | 0.0215 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema375_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.9214 | 0.6635 | 3.9436 | 0.0136 | 0.3510 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema375_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8101 | 0.6497 | 3.4947 | 0.0126 | 0.3452 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema375_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2894 | 0.6250 | 1.4318 | 0.0097 | 0.2228 | ok | RAN |
| SOLUSDT | 8 | `ema375_above_at_h` | one_head_filter_pi_star | 169 | 13.7803 | 1.6144 | 0.6213 | 2.6446 | 0.0095 | 0.2899 | ok | RAN |
| SOLUSDT | 4 | `ema375_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.6007 | 0.6209 | 2.7303 | 0.0092 | 0.2692 | ok | RAN |
| ETHUSDT | 4 | `ema375_above_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.2390 | 0.6127 | 1.1905 | 0.0084 | 0.2139 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema375_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema375_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema375_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema375_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
