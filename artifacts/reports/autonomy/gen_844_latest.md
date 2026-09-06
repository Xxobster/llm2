# Autonomy public-indicator hunt gen 844

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T195036Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema815_below_at_h` | one_head_filter_pi_star | 207 | 16.9100 | 1.9817 | 0.6860 | 4.0660 | 0.0222 | 0.3816 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema815_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.8698 | 0.6741 | 3.9220 | 0.0204 | 0.3616 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema815_below_at_h` | one_head_filter_pi_star | 224 | 18.3167 | 1.8460 | 0.6607 | 3.8236 | 0.0127 | 0.3259 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema815_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.8029 | 0.6609 | 3.7173 | 0.0123 | 0.3090 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema815_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.5738 | 0.6269 | 2.2106 | 0.0088 | 0.3134 | ok | RAN |
| ETHUSDT | 8 | `ema815_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.2195 | 0.6013 | 1.0516 | 0.0079 | 0.2092 | ok | RAN |
| SOLUSDT | 8 | `ema815_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.4968 | 0.6143 | 2.0024 | 0.0078 | 0.3143 | ok | RAN |
| ETHUSDT | 4 | `ema815_above_at_h` | one_head_filter_pi_star | 149 | 12.2476 | 1.1437 | 0.5839 | 0.6852 | 0.0054 | 0.2081 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema815_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema815_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema815_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema815_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema815_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema815_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema815_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema815_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema815_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema815_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema815_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema815_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema815_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema815_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema815_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema815_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
