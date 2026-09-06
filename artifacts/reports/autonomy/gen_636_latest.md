# Autonomy public-indicator hunt gen 636

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T024940Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema555_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.1729 | 0.6995 | 4.7514 | 0.0255 | 0.3886 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema555_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 2.0519 | 0.6990 | 4.5549 | 0.0240 | 0.3738 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema555_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 1.9210 | 0.6714 | 3.9324 | 0.0131 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema555_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 1.7950 | 0.6573 | 3.5703 | 0.0123 | 0.3239 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema555_above_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.6091 | 0.6273 | 2.5416 | 0.0094 | 0.2919 | ok | RAN |
| SOLUSDT | 8 | `ema555_above_at_h` | one_head_filter_pi_star | 159 | 13.0388 | 1.5624 | 0.6101 | 2.3801 | 0.0089 | 0.2956 | ok | RAN |
| ETHUSDT | 4 | `ema555_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1410 | 0.5930 | 0.7185 | 0.0051 | 0.1919 | ok | RAN |
| ETHUSDT | 8 | `ema555_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.1136 | 0.5976 | 0.5843 | 0.0043 | 0.2071 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema555_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema555_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema555_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema555_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema555_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema555_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
