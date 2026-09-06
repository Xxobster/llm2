# Autonomy public-indicator hunt gen 668

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T045627Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema595_below_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.9433 | 0.6777 | 4.1804 | 0.0221 | 0.3697 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema595_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8588 | 0.6716 | 3.8565 | 0.0207 | 0.3781 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema595_below_at_h` | one_head_filter_pi_star | 216 | 17.6625 | 1.8459 | 0.6574 | 3.7772 | 0.0131 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema595_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.8666 | 0.6557 | 3.7836 | 0.0127 | 0.3255 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema595_above_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.6248 | 0.6211 | 2.6342 | 0.0098 | 0.2919 | ok | RAN |
| SOLUSDT | 4 | `ema595_above_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.6308 | 0.6209 | 2.5802 | 0.0095 | 0.3072 | ok | RAN |
| ETHUSDT | 8 | `ema595_above_at_h` | one_head_filter_pi_star | 151 | 12.4607 | 1.1907 | 0.6093 | 0.8931 | 0.0068 | 0.1921 | ok | RAN |
| ETHUSDT | 4 | `ema595_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1231 | 0.5828 | 0.6104 | 0.0044 | 0.1963 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema595_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema595_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0595 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema595_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema595_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema595_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema595_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
