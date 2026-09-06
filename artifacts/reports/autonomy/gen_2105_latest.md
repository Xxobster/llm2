# Autonomy public-indicator hunt gen 2105

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T225346Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4820_above_at_h` | one_head_filter_pi_star | 23 | 2.1595 | 3.1563 | 0.7391 | 1.9548 | 0.0201 | 0.0870 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4820_above_at_h` | one_head_filter_pi_star | 57 | 4.8971 | 1.8169 | 0.6491 | 1.7687 | 0.0116 | 0.1053 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema4820_above_at_h` | one_head_filter_pi_star | 37 | 4.3479 | 1.0785 | 0.5676 | 0.2333 | 0.0037 | 0.1351 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4820_below_at_h` | one_head_filter_pi_star | 319 | 26.0849 | 0.9894 | 0.5361 | -0.0818 | -0.0002 | 0.1348 | ok | RAN |
| SOLUSDT | 4 | `ema4820_below_at_h` | one_head_filter_pi_star | 311 | 25.4307 | 0.9532 | 0.5273 | -0.3601 | -0.0010 | 0.1318 | ok | RAN |
| ETHUSDT | 8 | `ema4820_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9557 | 0.5556 | -0.3597 | -0.0015 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4820_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9407 | 0.5529 | -0.4882 | -0.0020 | 0.1382 | ok | RAN |
| ETHUSDT | 4 | `ema4820_above_at_h` | one_head_filter_pi_star | 39 | 11.3833 | 0.9405 | 0.5385 | -0.3447 | -0.0027 | 0.1282 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4820_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6251 | 0.3000 | -0.8291 | -0.0425 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4820_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
