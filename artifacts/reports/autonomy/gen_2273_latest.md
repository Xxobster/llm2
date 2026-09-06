# Autonomy public-indicator hunt gen 2273

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T212648Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5240_above_at_h` | one_head_filter_pi_star | 52 | 4.2747 | 1.7412 | 0.6346 | 1.4574 | 0.0100 | 0.1154 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema5240_above_at_h` | one_head_filter_pi_star | 49 | 4.2098 | 1.4539 | 0.6327 | 0.9519 | 0.0070 | 0.1224 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema5240_below_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 0.9848 | 0.5584 | -0.1253 | -0.0005 | 0.1368 | ok | RAN |
| SOLUSDT | 8 | `ema5240_below_at_h` | one_head_filter_pi_star | 313 | 25.5943 | 0.9668 | 0.5304 | -0.2547 | -0.0007 | 0.1342 | ok | RAN |
| ETHUSDT | 8 | `ema5240_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9545 | 0.5546 | -0.3704 | -0.0015 | 0.1386 | ok | RAN |
| SOLUSDT | 4 | `ema5240_below_at_h` | one_head_filter_pi_star | 319 | 26.0849 | 0.9227 | 0.5235 | -0.6085 | -0.0016 | 0.1348 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5240_above_at_h` | one_head_filter_pi_star | 37 | 11.1653 | 0.8862 | 0.5135 | -0.6622 | -0.0053 | 0.1081 | ok | RAN |
| ETHUSDT | 8 | `ema5240_above_at_h` | one_head_filter_pi_star | 41 | 11.9670 | 0.7759 | 0.4878 | -1.3512 | -0.0118 | 0.1220 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5240_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5240_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
