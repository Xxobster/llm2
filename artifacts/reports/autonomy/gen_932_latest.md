# Autonomy public-indicator hunt gen 932

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T045907Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema925_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.9632 | 0.6726 | 4.2634 | 0.0216 | 0.3540 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema925_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.8326 | 0.6681 | 3.9218 | 0.0199 | 0.3489 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema925_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 1.8185 | 0.6538 | 4.0713 | 0.0126 | 0.3077 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema925_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 1.7765 | 0.6506 | 3.7876 | 0.0119 | 0.3012 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema925_above_at_h` | one_head_filter_pi_star | 119 | 9.8904 | 1.6980 | 0.6471 | 2.4887 | 0.0104 | 0.3277 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema925_above_at_h` | one_head_filter_pi_star | 133 | 10.8449 | 1.6418 | 0.6316 | 2.3745 | 0.0095 | 0.3158 | ok | RAN |
| ETHUSDT | 8 | `ema925_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 1.2005 | 0.5915 | 0.9679 | 0.0079 | 0.2394 | ok | RAN |
| ETHUSDT | 4 | `ema925_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 1.1635 | 0.5948 | 0.7163 | 0.0063 | 0.2155 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema925_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema925_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema925_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema925_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema925_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema925_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema925_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema925_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema925_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema925_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema925_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema925_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema925_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema925_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema925_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema925_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
