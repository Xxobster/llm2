# Autonomy public-indicator hunt gen 1049

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T162707Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2180_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2180_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 1.5964 | 0.6445 | 3.6547 | 0.0159 | 0.3035 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2180_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.5935 | 0.6401 | 3.6019 | 0.0159 | 0.3097 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2180_below_at_h` | one_head_filter_pi_star | 270 | 21.9650 | 1.8503 | 0.6519 | 4.2088 | 0.0131 | 0.3259 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2180_below_at_h` | one_head_filter_pi_star | 270 | 21.9650 | 1.7835 | 0.6444 | 3.9423 | 0.0126 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2180_above_at_h` | one_head_filter_pi_star | 106 | 8.7123 | 1.7275 | 0.6604 | 2.3846 | 0.0100 | 0.2642 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2180_above_at_h` | one_head_filter_pi_star | 106 | 8.7123 | 1.6825 | 0.6604 | 2.1962 | 0.0095 | 0.2547 | GATE_CAND | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2180_above_at_h` | one_head_filter_pi_star | 25 | 2.9377 | 0.9415 | 0.4800 | -0.1505 | -0.0032 | 0.3200 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2180_above_at_h` | one_head_filter_pi_star | 14 | 4.3631 | 0.4570 | 0.2857 | -2.4895 | -0.0436 | 0.2857 | ok | RAN |
| BTCUSDT | 4 | `ema2180_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0444 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2180_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0463 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
