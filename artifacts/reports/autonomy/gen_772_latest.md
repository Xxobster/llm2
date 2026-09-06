# Autonomy public-indicator hunt gen 772

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T125822Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema725_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 2.0874 | 0.6931 | 4.4255 | 0.0237 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema725_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0273 | 0.6856 | 4.0706 | 0.0226 | 0.3866 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema725_below_at_h` | one_head_filter_pi_star | 229 | 18.7255 | 1.8954 | 0.6594 | 3.9767 | 0.0130 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema725_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.8286 | 0.6619 | 3.6590 | 0.0126 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema725_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.6482 | 0.6429 | 2.4832 | 0.0097 | 0.3071 | ok | RAN |
| SOLUSDT | 8 | `ema725_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.6564 | 0.6406 | 2.3585 | 0.0095 | 0.3125 | ok | RAN |
| ETHUSDT | 4 | `ema725_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.2198 | 0.6000 | 1.0504 | 0.0077 | 0.2062 | ok | RAN |
| ETHUSDT | 8 | `ema725_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.2145 | 0.6013 | 1.0123 | 0.0075 | 0.2025 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema725_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema725_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema725_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema725_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
