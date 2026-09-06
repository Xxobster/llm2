# Autonomy public-indicator hunt gen 1649

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T230343Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema3680_above_at_h` | one_head_filter_pi_star | 87 | 7.0952 | 1.4570 | 0.6552 | 1.3849 | 0.0070 | 0.1149 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3680_above_at_h` | one_head_filter_pi_star | 81 | 6.6587 | 1.3694 | 0.6420 | 1.0860 | 0.0050 | 0.0864 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3680_below_at_h` | one_head_filter_pi_star | 288 | 23.5500 | 1.0680 | 0.5486 | 0.4776 | 0.0013 | 0.1285 | ok | RAN |
| SOLUSDT | 4 | `ema3680_below_at_h` | one_head_filter_pi_star | 303 | 24.7766 | 1.0328 | 0.5413 | 0.2414 | 0.0007 | 0.1287 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema3680_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9902 | 0.5592 | -0.0773 | -0.0003 | 0.1331 | ok | RAN |
| ETHUSDT | 8 | `ema3680_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9839 | 0.5588 | -0.1294 | -0.0005 | 0.1324 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema3680_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.7080 | 0.4839 | -1.4325 | -0.0150 | 0.1290 | ok | RAN |
| ETHUSDT | 4 | `ema3680_above_at_h` | one_head_filter_pi_star | 35 | 4.1128 | 0.7102 | 0.4857 | -1.0774 | -0.0154 | 0.1143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3680_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3680_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
