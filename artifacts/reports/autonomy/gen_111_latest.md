# Autonomy public-indicator hunt gen 111

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T164651Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `harami_bull_start` | one_head_filter_pi_star | 130 | 10.6837 | 2.4345 | 0.7000 | 4.0190 | 0.0233 | 0.4231 | EBR>35% | RAN |
| ETHUSDT | 4 | `harami_bull_start` | one_head_filter_pi_star | 168 | 13.7241 | 1.6861 | 0.6726 | 3.1530 | 0.0210 | 0.3512 | EBR>35% | RAN |
| ETHUSDT | 8 | `harami_bull_start` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 8 | `harami_bear_start` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `harami_bull_start` | one_head_filter_pi_star | 379 | 30.8324 | 1.6957 | 0.6359 | 4.3582 | 0.0106 | 0.3193 | GATE_CAND | RAN |
| SOLUSDT | 8 | `harami_bear_start` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `harami_bear_start` | one_head_filter_pi_star | 147 | 12.1306 | 1.2923 | 0.5986 | 1.2641 | 0.0096 | 0.1973 | ok | RAN |
| SOLUSDT | 4 | `harami_bear_start` | one_head_filter_pi_star | 178 | 14.5142 | 1.4178 | 0.5899 | 1.9902 | 0.0073 | 0.2753 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `harami_bear_start` | one_head_filter_pi_star | 26 | 2.2125 | 0.9571 | 0.4231 | -0.0911 | -0.0039 | 0.1154 | TPM<MIN | RAN |
| BTCUSDT | 8 | `harami_bull_start` | one_head_filter_pi_star | 25 | 2.1274 | 0.9542 | 0.4400 | -0.0959 | -0.0041 | 0.1600 | TPM<MIN | RAN |
| BTCUSDT | 4 | `harami_bear_start` | one_head_filter_pi_star | 14 | 1.2848 | 0.4478 | 0.2857 | -1.1053 | -0.0511 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `harami_bull_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `harami_bear_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `harami_bull_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `harami_bear_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `harami_bull_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `harami_bear_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `harami_bull_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `harami_bear_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `harami_bull_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `harami_bear_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `harami_bull_start` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `harami_bull_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `harami_bear_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
