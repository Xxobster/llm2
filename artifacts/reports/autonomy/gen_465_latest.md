# Autonomy public-indicator hunt gen 465

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T153836Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema720_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 2.0944 | 0.6875 | 4.3362 | 0.0238 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema720_below_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.9442 | 0.6825 | 4.1925 | 0.0221 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema720_below_at_h` | one_head_filter_pi_star | 221 | 18.0714 | 1.8578 | 0.6652 | 3.8740 | 0.0131 | 0.3258 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema720_below_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.7636 | 0.6494 | 3.5479 | 0.0118 | 0.3117 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema720_above_at_h` | one_head_filter_pi_star | 110 | 9.1424 | 1.6997 | 0.6455 | 2.3644 | 0.0106 | 0.3455 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema720_above_at_h` | one_head_filter_pi_star | 143 | 11.7267 | 1.6476 | 0.6294 | 2.4699 | 0.0097 | 0.3007 | ok | RAN |
| ETHUSDT | 4 | `ema720_above_at_h` | one_head_filter_pi_star | 148 | 12.2132 | 1.2274 | 0.6081 | 1.0366 | 0.0080 | 0.2095 | ok | RAN |
| ETHUSDT | 8 | `ema720_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.1726 | 0.6000 | 0.8504 | 0.0062 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema720_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0393 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema720_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
