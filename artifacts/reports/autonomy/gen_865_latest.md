# Autonomy public-indicator hunt gen 865

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T215442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1720_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1720_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1720_below_at_h` | one_head_filter_pi_star | 303 | 24.7523 | 1.5937 | 0.6469 | 3.3873 | 0.0153 | 0.3135 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1720_below_at_h` | one_head_filter_pi_star | 320 | 26.1411 | 1.5417 | 0.6406 | 3.3160 | 0.0145 | 0.3156 | ok | RAN |
| SOLUSDT | 8 | `ema1720_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 1.8108 | 0.6507 | 4.1575 | 0.0128 | 0.3235 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1720_below_at_h` | one_head_filter_pi_star | 270 | 22.0781 | 1.7882 | 0.6519 | 4.0715 | 0.0126 | 0.3259 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema1720_above_at_h` | one_head_filter_pi_star | 52 | 4.5729 | 1.2608 | 0.5962 | 0.7189 | 0.0094 | 0.2308 | ok | RAN |
| SOLUSDT | 8 | `ema1720_above_at_h` | one_head_filter_pi_star | 82 | 6.6867 | 1.4971 | 0.6463 | 1.5466 | 0.0073 | 0.2317 | ok | RAN |
| SOLUSDT | 4 | `ema1720_above_at_h` | one_head_filter_pi_star | 99 | 8.0739 | 1.4895 | 0.6061 | 1.6010 | 0.0070 | 0.2323 | ok | RAN |
| ETHUSDT | 8 | `ema1720_above_at_h` | one_head_filter_pi_star | 52 | 4.5729 | 1.0847 | 0.5577 | 0.2555 | 0.0036 | 0.2308 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1720_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0463 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1720_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0599 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
