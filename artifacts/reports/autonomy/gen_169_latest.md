# Autonomy public-indicator hunt gen 169

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T203405Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema7_below_at_h` | one_head_filter_pi_star | 85 | 6.9505 | 2.6874 | 0.6824 | 3.5177 | 0.0258 | 0.4235 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema7_cross_up` | one_head_filter_pi_star | 17 | 1.3989 | 2.1489 | 0.6471 | 1.3184 | 0.0249 | 0.1765 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema7_above_at_h` | one_head_filter_pi_star | 67 | 5.5958 | 1.7189 | 0.6866 | 1.8013 | 0.0242 | 0.3284 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema7_below_at_h` | one_head_filter_pi_star | 149 | 12.1856 | 1.8089 | 0.6846 | 3.0295 | 0.0225 | 0.4094 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema7_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8308 | 0.6847 | 3.9641 | 0.0213 | 0.3784 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema7_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.2349 | 0.6875 | 4.1370 | 0.0185 | 0.4250 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema7_cross_up` | one_head_filter_pi_star | 225 | 18.3804 | 1.5277 | 0.6444 | 2.7353 | 0.0146 | 0.3378 | ok | RAN |
| SOLUSDT | 8 | `ema7_cross_up` | one_head_filter_pi_star | 196 | 15.9450 | 1.9519 | 0.6582 | 3.6903 | 0.0130 | 0.3163 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema7_cross_down` | one_head_filter_pi_star | 185 | 15.1569 | 1.3232 | 0.6000 | 1.5498 | 0.0091 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `ema7_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0070 | 0.2037 | ok | RAN |
| SOLUSDT | 8 | `ema7_above_at_h` | one_head_filter_pi_star | 59 | 5.0938 | 1.2960 | 0.5763 | 0.9763 | 0.0069 | 0.3390 | ok | RAN |
| SOLUSDT | 4 | `ema7_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3724 | 0.5953 | 2.0249 | 0.0055 | 0.2465 | ok | RAN |
| SOLUSDT | 8 | `ema7_cross_down` | one_head_filter_pi_star | 203 | 16.5527 | 1.2975 | 0.5911 | 1.5899 | 0.0043 | 0.2118 | ok | RAN |
| SOLUSDT | 4 | `ema7_cross_down` | one_head_filter_pi_star | 23 | 1.9474 | 1.3384 | 0.6522 | 0.5943 | 0.0036 | 0.0870 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema7_cross_down` | one_head_filter_pi_star | 16 | 1.6098 | 1.0020 | 0.5000 | 0.0034 | 0.0001 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema7_cross_down` | one_head_filter_pi_star | 17 | 1.4467 | 0.6555 | 0.2941 | -0.6420 | -0.0289 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema7_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema7_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema7_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema7_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema7_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema7_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema7_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema7_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
