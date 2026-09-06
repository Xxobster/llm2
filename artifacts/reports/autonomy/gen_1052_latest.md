# Autonomy public-indicator hunt gen 1052

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T165235Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema907_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 1.8904 | 0.6722 | 4.1842 | 0.0208 | 0.3444 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema907_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8324 | 0.6697 | 3.7557 | 0.0194 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema907_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.7579 | 0.6457 | 3.7794 | 0.0118 | 0.3110 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema907_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.6942 | 0.6393 | 3.4742 | 0.0111 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema907_above_at_h` | one_head_filter_pi_star | 125 | 10.2506 | 1.7260 | 0.6480 | 2.6363 | 0.0102 | 0.3040 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema907_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.7035 | 0.6279 | 2.5142 | 0.0100 | 0.2946 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema907_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.1838 | 0.5938 | 0.8100 | 0.0067 | 0.1953 | ok | RAN |
| ETHUSDT | 8 | `ema907_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.1496 | 0.5867 | 0.7411 | 0.0056 | 0.2200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema907_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema907_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema907_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema907_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema907_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema907_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema907_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema907_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema907_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema907_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema907_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema907_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema907_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema907_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema907_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema907_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
