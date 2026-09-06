# Autonomy public-indicator hunt gen 1444

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T203538Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema964_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema964_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.9172 | 0.6741 | 4.1514 | 0.0208 | 0.3393 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema964_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.8355 | 0.6651 | 3.7943 | 0.0189 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema964_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 1.8325 | 0.6504 | 3.9229 | 0.0126 | 0.3049 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema964_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 1.7202 | 0.6402 | 3.6896 | 0.0113 | 0.3068 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema964_above_at_h` | one_head_filter_pi_star | 122 | 10.1398 | 1.6812 | 0.6393 | 2.3568 | 0.0105 | 0.3361 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema964_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 1.2246 | 0.5926 | 1.0000 | 0.0086 | 0.2444 | ok | RAN |
| SOLUSDT | 8 | `ema964_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.4319 | 0.6016 | 1.6933 | 0.0067 | 0.2927 | ok | RAN |
| ETHUSDT | 4 | `ema964_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 1.1114 | 0.5691 | 0.5145 | 0.0045 | 0.2033 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema964_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema964_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema964_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema964_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema964_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema964_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema964_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema964_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema964_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema964_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema964_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema964_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema964_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema964_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema964_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
