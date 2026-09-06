# Autonomy public-indicator hunt gen 1188

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T090953Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema927_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8678 | 0.6728 | 3.9122 | 0.0201 | 0.3641 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema927_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.7780 | 0.6595 | 3.6886 | 0.0186 | 0.3448 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema927_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.8417 | 0.6557 | 3.9648 | 0.0129 | 0.3033 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema927_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 1.7804 | 0.6498 | 3.7167 | 0.0122 | 0.3038 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema927_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.6285 | 0.6260 | 2.2351 | 0.0092 | 0.3333 | ok | RAN |
| SOLUSDT | 4 | `ema927_above_at_h` | one_head_filter_pi_star | 136 | 11.0895 | 1.6142 | 0.6250 | 2.2947 | 0.0092 | 0.3088 | ok | RAN |
| ETHUSDT | 4 | `ema927_above_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 1.2060 | 0.5984 | 0.9134 | 0.0080 | 0.2205 | ok | RAN |
| ETHUSDT | 8 | `ema927_above_at_h` | one_head_filter_pi_star | 128 | 10.5636 | 1.1555 | 0.5781 | 0.6884 | 0.0059 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema927_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema927_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema927_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema927_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema927_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema927_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema927_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema927_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema927_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema927_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema927_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema927_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema927_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema927_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema927_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema927_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
