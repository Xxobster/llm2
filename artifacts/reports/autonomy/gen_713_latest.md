# Autonomy public-indicator hunt gen 713

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T080711Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1340_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1424 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1340_below_at_h` | one_head_filter_pi_star | 276 | 22.5467 | 1.7772 | 0.6522 | 4.0307 | 0.0186 | 0.3261 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1340_below_at_h` | one_head_filter_pi_star | 296 | 24.1805 | 1.6688 | 0.6520 | 3.7898 | 0.0170 | 0.3243 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1340_below_at_h` | one_head_filter_pi_star | 266 | 21.7510 | 1.6929 | 0.6353 | 3.5949 | 0.0115 | 0.3158 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1340_above_at_h` | one_head_filter_pi_star | 77 | 6.5521 | 1.2828 | 0.6104 | 0.9628 | 0.0105 | 0.2468 | ok | RAN |
| SOLUSDT | 4 | `ema1340_below_at_h` | one_head_filter_pi_star | 285 | 23.3047 | 1.6388 | 0.6281 | 3.5621 | 0.0103 | 0.3158 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema1340_above_at_h` | one_head_filter_pi_star | 76 | 6.2722 | 1.2133 | 0.6053 | 0.7408 | 0.0089 | 0.2500 | ok | RAN |
| SOLUSDT | 8 | `ema1340_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.5972 | 0.6522 | 2.0435 | 0.0084 | 0.2696 | ok | RAN |
| SOLUSDT | 4 | `ema1340_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.5731 | 0.6372 | 1.9431 | 0.0082 | 0.2832 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1340_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1340_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
