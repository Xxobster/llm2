# Autonomy public-indicator hunt gen 283

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T041557Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma88_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8579 | 0.6919 | 3.9941 | 0.0219 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma88_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8151 | 0.6782 | 3.9243 | 0.0212 | 0.3614 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma88_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2687 | 0.6905 | 4.3507 | 0.0186 | 0.3988 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma88_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2134 | 0.6933 | 4.1270 | 0.0179 | 0.4049 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma88_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.3263 | 0.6089 | 1.5410 | 0.0100 | 0.2346 | ok | RAN |
| ETHUSDT | 8 | `sma88_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2888 | 0.6056 | 1.3800 | 0.0087 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `sma88_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3371 | 0.5981 | 1.7880 | 0.0051 | 0.2617 | ok | RAN |
| SOLUSDT | 8 | `sma88_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3274 | 0.5991 | 1.7341 | 0.0049 | 0.2547 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma88_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma88_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma88_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma88_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma88_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma88_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
