# Autonomy public-indicator hunt gen 508

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T182610Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema395_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0617 | 0.6954 | 4.5750 | 0.0240 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema395_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.8449 | 0.6748 | 4.0917 | 0.0212 | 0.3738 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema395_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.9096 | 0.6618 | 3.8983 | 0.0137 | 0.3575 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema395_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.8832 | 0.6588 | 3.8366 | 0.0132 | 0.3318 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema395_above_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.2815 | 0.6158 | 1.3804 | 0.0095 | 0.2147 | ok | RAN |
| SOLUSDT | 4 | `ema395_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.6102 | 0.6290 | 2.7933 | 0.0095 | 0.2796 | ok | RAN |
| ETHUSDT | 8 | `ema395_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2271 | 0.6077 | 1.1537 | 0.0080 | 0.2210 | ok | RAN |
| SOLUSDT | 8 | `ema395_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5082 | 0.6162 | 2.4292 | 0.0079 | 0.2649 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema395_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema395_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema395_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema395_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema395_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema395_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
