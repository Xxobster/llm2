# Autonomy public-indicator hunt gen 1060

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T175028Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema908_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema908_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.9702 | 0.6774 | 4.2376 | 0.0212 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema908_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.8337 | 0.6716 | 3.6430 | 0.0195 | 0.3725 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema908_below_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 1.8632 | 0.6624 | 3.9824 | 0.0130 | 0.3120 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema908_below_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.8247 | 0.6612 | 3.9401 | 0.0128 | 0.3020 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema908_above_at_h` | one_head_filter_pi_star | 134 | 10.9264 | 1.7089 | 0.6269 | 2.5277 | 0.0102 | 0.2985 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema908_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.5480 | 0.6202 | 2.0818 | 0.0082 | 0.3256 | ok | RAN |
| ETHUSDT | 4 | `ema908_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.1573 | 0.5915 | 0.7546 | 0.0061 | 0.2183 | ok | RAN |
| ETHUSDT | 8 | `ema908_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 1.1281 | 0.5746 | 0.5943 | 0.0050 | 0.2239 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema908_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0506 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema908_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0531 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema908_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema908_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema908_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema908_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema908_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema908_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema908_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema908_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema908_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema908_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema908_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema908_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema908_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
