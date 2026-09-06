# Autonomy public-indicator hunt gen 556

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T213824Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema455_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 2.0273 | 0.6866 | 4.4346 | 0.0234 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema455_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8685 | 0.6716 | 4.0328 | 0.0211 | 0.3731 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema455_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.7949 | 0.6553 | 3.5062 | 0.0125 | 0.3544 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema455_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.8104 | 0.6540 | 3.5861 | 0.0125 | 0.3365 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema455_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5899 | 0.6158 | 2.6048 | 0.0090 | 0.2825 | ok | RAN |
| SOLUSDT | 8 | `ema455_above_at_h` | one_head_filter_pi_star | 167 | 13.6172 | 1.5103 | 0.6048 | 2.2535 | 0.0084 | 0.2934 | ok | RAN |
| ETHUSDT | 8 | `ema455_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2317 | 0.6012 | 1.0973 | 0.0079 | 0.1963 | ok | RAN |
| ETHUSDT | 4 | `ema455_above_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.1975 | 0.6024 | 0.9781 | 0.0070 | 0.2048 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema455_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema455_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema455_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema455_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema455_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema455_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
