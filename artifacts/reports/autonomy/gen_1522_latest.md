# Autonomy public-indicator hunt gen 1522

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T044920Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1376_pos_at_h` | one_head_filter_pi_star | 34 | 2.8258 | 3.2940 | 0.7647 | 2.9168 | 0.0238 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1376_pos_at_h` | one_head_filter_pi_star | 37 | 3.1141 | 2.6757 | 0.7297 | 2.5682 | 0.0213 | 0.4054 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1376_neg_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 1.6123 | 0.6440 | 3.6207 | 0.0161 | 0.3127 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1376_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5640 | 0.6399 | 3.5106 | 0.0153 | 0.3095 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1376_neg_at_h` | one_head_filter_pi_star | 325 | 26.4394 | 1.7780 | 0.6431 | 4.2831 | 0.0115 | 0.3046 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1376_neg_at_h` | one_head_filter_pi_star | 317 | 25.7886 | 1.7787 | 0.6435 | 4.3308 | 0.0112 | 0.3091 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret1376_pos_at_h` | one_head_filter_pi_star | 36 | 3.5344 | 1.1242 | 0.5556 | 0.3239 | 0.0056 | 0.2222 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1376_pos_at_h` | one_head_filter_pi_star | 33 | 3.2399 | 0.7911 | 0.4848 | -0.6323 | -0.0100 | 0.2121 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1376_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4151 | 0.2143 | -1.1865 | -0.0573 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1376_pos_at_h` | one_head_filter_pi_star | 13 | 2.3874 | 0.4162 | 0.2308 | -1.7353 | -0.0584 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1376_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1376_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1376_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1376_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
