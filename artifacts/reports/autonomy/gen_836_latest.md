# Autonomy public-indicator hunt gen 836

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T190519Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema805_below_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.8971 | 0.6730 | 3.9098 | 0.0210 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema805_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.9025 | 0.6792 | 3.8695 | 0.0209 | 0.3821 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema805_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.7832 | 0.6532 | 3.7774 | 0.0121 | 0.3065 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema805_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 1.7889 | 0.6527 | 3.7229 | 0.0121 | 0.3054 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema805_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.5964 | 0.6412 | 2.2449 | 0.0089 | 0.3206 | ok | RAN |
| SOLUSDT | 8 | `ema805_above_at_h` | one_head_filter_pi_star | 131 | 10.6818 | 1.5883 | 0.6260 | 2.2099 | 0.0088 | 0.3130 | ok | RAN |
| ETHUSDT | 4 | `ema805_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.2049 | 0.5882 | 0.9657 | 0.0071 | 0.2026 | ok | RAN |
| ETHUSDT | 8 | `ema805_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.1329 | 0.5897 | 0.6466 | 0.0051 | 0.2115 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema805_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema805_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0423 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema805_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema805_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
