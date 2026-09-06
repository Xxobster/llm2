# Autonomy public-indicator hunt gen 1019

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T125107Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma898_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.2683 | 0.7111 | 4.6540 | 0.0260 | 0.3833 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma898_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.2368 | 0.7076 | 4.4845 | 0.0257 | 0.3801 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma898_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 1.7413 | 0.6498 | 3.4403 | 0.0121 | 0.3180 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma898_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.7861 | 0.6403 | 2.8795 | 0.0114 | 0.3165 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma898_below_at_h` | one_head_filter_pi_star | 229 | 18.7255 | 1.7048 | 0.6419 | 3.4013 | 0.0111 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma898_above_at_h` | one_head_filter_pi_star | 142 | 11.6447 | 1.6599 | 0.6408 | 2.5951 | 0.0102 | 0.3028 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma898_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.1104 | 0.5706 | 0.5654 | 0.0043 | 0.2203 | ok | RAN |
| ETHUSDT | 4 | `sma898_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.0720 | 0.5595 | 0.3730 | 0.0028 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma898_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma898_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma898_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma898_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma898_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma898_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma898_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma898_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma898_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma898_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma898_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma898_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma898_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma898_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma898_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma898_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
