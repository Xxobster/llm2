# Autonomy public-indicator hunt gen 2505

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T014044Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5820_above_at_h` | one_head_filter_pi_star | 45 | 3.8661 | 1.5305 | 0.6222 | 1.0871 | 0.0073 | 0.1111 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5820_above_at_h` | one_head_filter_pi_star | 51 | 4.3816 | 1.2946 | 0.5882 | 0.7004 | 0.0047 | 0.0784 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5820_below_at_h` | one_head_filter_pi_star | 334 | 27.3115 | 0.9792 | 0.5389 | -0.1654 | -0.0004 | 0.1257 | ok | RAN |
| ETHUSDT | 4 | `ema5820_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9746 | 0.5552 | -0.2035 | -0.0008 | 0.1373 | ok | RAN |
| SOLUSDT | 4 | `ema5820_below_at_h` | one_head_filter_pi_star | 309 | 25.2672 | 0.9606 | 0.5340 | -0.3001 | -0.0008 | 0.1327 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5820_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9416 | 0.5519 | -0.4816 | -0.0019 | 0.1365 | ok | RAN |
| ETHUSDT | 4 | `ema5820_above_at_h` | one_head_filter_pi_star | 36 | 10.8636 | 0.7989 | 0.5000 | -1.0242 | -0.0108 | 0.1389 | ok | RAN |
| ETHUSDT | 8 | `ema5820_above_at_h` | one_head_filter_pi_star | 45 | 13.1346 | 0.7785 | 0.4889 | -1.2608 | -0.0128 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5820_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5236 | 0.2632 | -1.0815 | -0.0531 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5820_above_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.5417 | 0.2857 | -1.1090 | -0.0559 | 0.0476 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
