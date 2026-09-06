# Autonomy public-indicator hunt gen 1220

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T121448Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema931_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8335 | 0.6682 | 3.7614 | 0.0193 | 0.3594 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema931_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 1.7130 | 0.6515 | 3.5227 | 0.0173 | 0.3320 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema931_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.7912 | 0.6494 | 3.8491 | 0.0123 | 0.3028 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema931_below_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 1.7743 | 0.6553 | 3.6936 | 0.0121 | 0.2979 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema931_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 1.2912 | 0.6029 | 1.2153 | 0.0106 | 0.2353 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema931_above_at_h` | one_head_filter_pi_star | 126 | 10.3562 | 1.6236 | 0.6349 | 2.2415 | 0.0095 | 0.3016 | ok | RAN |
| ETHUSDT | 4 | `ema931_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.2353 | 0.6093 | 1.1209 | 0.0087 | 0.2252 | ok | RAN |
| SOLUSDT | 8 | `ema931_above_at_h` | one_head_filter_pi_star | 112 | 9.2060 | 1.5636 | 0.6339 | 1.9535 | 0.0085 | 0.3125 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema931_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema931_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema931_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema931_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema931_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema931_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema931_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema931_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema931_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema931_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema931_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema931_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema931_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema931_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema931_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema931_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
