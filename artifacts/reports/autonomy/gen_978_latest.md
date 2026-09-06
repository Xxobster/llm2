# Autonomy public-indicator hunt gen 978

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T230324Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret832_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0556 | 0.7005 | 4.1297 | 0.0230 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret832_neg_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.8222 | 0.6748 | 3.7644 | 0.0192 | 0.3689 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret832_neg_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 1.8307 | 0.6453 | 3.7860 | 0.0139 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret832_neg_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.7910 | 0.6517 | 3.9009 | 0.0129 | 0.3221 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret832_pos_at_h` | one_head_filter_pi_star | 91 | 7.4202 | 1.5858 | 0.6484 | 1.7822 | 0.0090 | 0.2857 | ok | RAN |
| ETHUSDT | 4 | `ret832_pos_at_h` | one_head_filter_pi_star | 117 | 9.6172 | 1.2130 | 0.5897 | 0.9174 | 0.0085 | 0.2564 | ok | RAN |
| SOLUSDT | 8 | `ret832_pos_at_h` | one_head_filter_pi_star | 82 | 6.7293 | 1.4578 | 0.6463 | 1.4444 | 0.0071 | 0.2683 | ok | RAN |
| ETHUSDT | 8 | `ret832_pos_at_h` | one_head_filter_pi_star | 115 | 9.4529 | 1.1328 | 0.5739 | 0.5468 | 0.0057 | 0.2435 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret832_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.8263 | 0.3750 | -0.2995 | -0.0145 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret832_pos_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.5370 | 0.3077 | -0.8842 | -0.0498 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret832_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret832_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret832_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret832_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret832_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret832_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret832_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret832_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret832_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret832_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret832_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret832_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret832_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret832_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
