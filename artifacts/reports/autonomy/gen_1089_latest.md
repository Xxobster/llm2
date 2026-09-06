# Autonomy public-indicator hunt gen 1089

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T214027Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2280_below_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 1.5859 | 0.6410 | 3.7110 | 0.0158 | 0.3020 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2280_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5841 | 0.6429 | 3.5704 | 0.0157 | 0.3065 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2280_below_at_h` | one_head_filter_pi_star | 268 | 21.8023 | 1.8787 | 0.6530 | 4.2375 | 0.0134 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2280_below_at_h` | one_head_filter_pi_star | 271 | 22.0464 | 1.8461 | 0.6494 | 4.1403 | 0.0126 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2280_above_at_h` | one_head_filter_pi_star | 109 | 8.9589 | 1.6816 | 0.6422 | 2.2676 | 0.0098 | 0.2752 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2280_above_at_h` | one_head_filter_pi_star | 112 | 9.2055 | 1.5715 | 0.6429 | 1.9546 | 0.0080 | 0.2679 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2280_above_at_h` | one_head_filter_pi_star | 27 | 3.1728 | 0.9048 | 0.4444 | -0.2603 | -0.0050 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema2280_above_at_h` | one_head_filter_pi_star | 20 | 2.3502 | 0.8118 | 0.4000 | -0.5027 | -0.0110 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2280_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0435 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2280_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5634 | 0.2941 | -0.9188 | -0.0477 | 0.1176 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
