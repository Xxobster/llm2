# Autonomy public-indicator hunt gen 1961

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T050923Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4460_above_at_h` | one_head_filter_pi_star | 68 | 5.5900 | 2.0146 | 0.6618 | 2.1601 | 0.0126 | 0.1324 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4460_above_at_h` | one_head_filter_pi_star | 77 | 6.3298 | 1.7290 | 0.6623 | 1.8154 | 0.0098 | 0.1169 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4460_below_at_h` | one_head_filter_pi_star | 299 | 24.4495 | 0.9858 | 0.5284 | -0.1059 | -0.0003 | 0.1371 | ok | RAN |
| SOLUSDT | 4 | `ema4460_below_at_h` | one_head_filter_pi_star | 315 | 25.7578 | 0.9433 | 0.5333 | -0.4438 | -0.0012 | 0.1302 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4460_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9455 | 0.5533 | -0.4638 | -0.0018 | 0.1354 | ok | RAN |
| ETHUSDT | 4 | `ema4460_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9395 | 0.5536 | -0.5112 | -0.0021 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `ema4460_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.8512 | 0.5000 | -0.7665 | -0.0073 | 0.1389 | ok | RAN |
| ETHUSDT | 8 | `ema4460_above_at_h` | one_head_filter_pi_star | 27 | 8.1477 | 0.7659 | 0.4815 | -1.0663 | -0.0108 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4460_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4460_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
