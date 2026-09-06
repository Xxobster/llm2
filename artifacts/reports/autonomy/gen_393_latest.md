# Autonomy public-indicator hunt gen 393

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T004101Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema540_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.1738 | 0.6979 | 4.8190 | 0.0252 | 0.3906 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema540_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.9177 | 0.6794 | 4.1897 | 0.0216 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema540_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 1.8464 | 0.6583 | 3.5924 | 0.0127 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema540_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.8273 | 0.6602 | 3.6066 | 0.0125 | 0.3398 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema540_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.7210 | 0.6284 | 3.0696 | 0.0106 | 0.2842 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema540_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.5654 | 0.6149 | 2.3526 | 0.0087 | 0.2905 | ok | RAN |
| ETHUSDT | 4 | `ema540_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.1795 | 0.5967 | 0.9211 | 0.0065 | 0.1989 | ok | RAN |
| ETHUSDT | 8 | `ema540_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1442 | 0.5915 | 0.7126 | 0.0052 | 0.2134 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema540_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema540_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
