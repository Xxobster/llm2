# Autonomy public-indicator hunt gen 010

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T074932Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema_cross_down` | one_head_filter_pi_star | 25 | 2.0546 | 5.7971 | 0.6800 | 2.6311 | 0.0474 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema_cross_down` | one_head_filter_pi_star | 18 | 1.4934 | 3.8849 | 0.6111 | 1.8767 | 0.0360 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 4 | `close_below_ema50_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.8086 | 0.6822 | 3.8881 | 0.0210 | 0.3738 | EBR>35% | RAN |
| ETHUSDT | 8 | `close_below_ema50_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.7911 | 0.6792 | 3.8282 | 0.0205 | 0.3774 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema_cross_up` | one_head_filter_pi_star | 19 | 1.7672 | 1.7077 | 0.5789 | 0.9813 | 0.0173 | 0.2105 | TPM<MIN | RAN |
| SOLUSDT | 4 | `close_below_ema50_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.0993 | 0.6790 | 3.8260 | 0.0170 | 0.4198 | EBR>35% | RAN |
| SOLUSDT | 8 | `close_below_ema50_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.0909 | 0.6792 | 3.8023 | 0.0169 | 0.4214 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema_cross_down` | one_head_filter_pi_star | 35 | 2.8923 | 1.4867 | 0.6286 | 1.0245 | 0.0161 | 0.3143 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema_cross_up` | one_head_filter_pi_star | 37 | 3.5803 | 1.6358 | 0.6216 | 1.3096 | 0.0124 | 0.1622 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema_cross_down` | one_head_filter_pi_star | 44 | 3.6361 | 1.3388 | 0.5909 | 0.8529 | 0.0121 | 0.2955 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema_cross_up` | one_head_filter_pi_star | 21 | 1.9533 | 1.3234 | 0.5714 | 0.5476 | 0.0096 | 0.1905 | TPM<MIN | RAN |
| ETHUSDT | 8 | `close_above_ema50_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.3045 | 0.6074 | 1.3392 | 0.0092 | 0.2147 | ok | RAN |
| ETHUSDT | 4 | `close_above_ema50_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2989 | 0.6087 | 1.3470 | 0.0089 | 0.2112 | ok | RAN |
| SOLUSDT | 4 | `ema_cross_up` | one_head_filter_pi_star | 35 | 3.3868 | 1.3979 | 0.6000 | 0.8653 | 0.0085 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `close_above_ema50_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3973 | 0.5991 | 2.0564 | 0.0058 | 0.2547 | ok | RAN |
| SOLUSDT | 4 | `close_above_ema50_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3436 | 0.5962 | 1.8656 | 0.0051 | 0.2441 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `close_above_ema50_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `close_above_ema50_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `close_below_ema50_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `close_below_ema50_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
