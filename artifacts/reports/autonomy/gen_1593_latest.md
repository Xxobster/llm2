# Autonomy public-indicator hunt gen 1593

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T172107Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3540_above_at_h` | one_head_filter_pi_star | 72 | 5.9188 | 1.7110 | 0.6667 | 1.7509 | 0.0091 | 0.1250 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3540_above_at_h` | one_head_filter_pi_star | 74 | 6.0832 | 1.6026 | 0.6351 | 1.5744 | 0.0080 | 0.1081 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3540_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.0255 | 0.5448 | 0.1804 | 0.0005 | 0.1290 | ok | RAN |
| SOLUSDT | 8 | `ema3540_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.0103 | 0.5397 | 0.0748 | 0.0002 | 0.1258 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema3540_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9860 | 0.5607 | -0.1152 | -0.0005 | 0.1329 | ok | RAN |
| ETHUSDT | 4 | `ema3540_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9748 | 0.5559 | -0.2043 | -0.0008 | 0.1324 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema3540_above_at_h` | one_head_filter_pi_star | 28 | 8.4494 | 0.7720 | 0.4643 | -1.0020 | -0.0108 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3540_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3540_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3540_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
