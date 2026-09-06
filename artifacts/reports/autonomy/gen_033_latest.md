# Autonomy public-indicator hunt gen 033

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T114236Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `tk_cross_up` | one_head_filter_pi_star | 21 | 1.8326 | 2.9225 | 0.6190 | 1.8930 | 0.0438 | 0.2857 | TPM<MIN | RAN |
| SOLUSDT | 8 | `tk_cross_down` | one_head_filter_pi_star | 16 | 1.3163 | 6.6339 | 0.7500 | 2.2246 | 0.0436 | 0.3125 | TPM<MIN | RAN |
| ETHUSDT | 4 | `tk_cross_down` | one_head_filter_pi_star | 34 | 2.8097 | 2.1371 | 0.7059 | 1.8448 | 0.0322 | 0.2941 | TPM<MIN | RAN |
| SOLUSDT | 4 | `tk_cross_down` | one_head_filter_pi_star | 12 | 0.9872 | 4.4748 | 0.7500 | 1.7306 | 0.0286 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `tk_cross_down` | one_head_filter_pi_star | 39 | 3.2229 | 1.8154 | 0.6923 | 1.5763 | 0.0237 | 0.2564 | TPM<MIN | RAN |
| ETHUSDT | 8 | `tk_cross_up` | one_head_filter_pi_star | 25 | 2.1816 | 1.4762 | 0.5600 | 0.8318 | 0.0228 | 0.2800 | TPM<MIN | RAN |
| ETHUSDT | 8 | `tk_bear_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.8178 | 0.6806 | 3.8400 | 0.0207 | 0.3796 | EBR>35% | RAN |
| ETHUSDT | 4 | `tk_bear_at_h` | one_head_filter_pi_star | 196 | 16.0141 | 1.7618 | 0.6684 | 3.5415 | 0.0189 | 0.3878 | EBR>35% | RAN |
| SOLUSDT | 4 | `tk_bear_at_h` | one_head_filter_pi_star | 155 | 12.6745 | 2.2475 | 0.7032 | 4.1117 | 0.0182 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 8 | `tk_bear_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.0857 | 0.6813 | 3.8352 | 0.0167 | 0.4188 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `tk_cross_up` | one_head_filter_pi_star | 29 | 2.5211 | 1.5390 | 0.5862 | 0.9650 | 0.0099 | 0.1724 | TPM<MIN | RAN |
| SOLUSDT | 4 | `tk_cross_up` | one_head_filter_pi_star | 17 | 1.7051 | 1.2534 | 0.5294 | 0.4485 | 0.0056 | 0.1765 | TPM<MIN | RAN |
| SOLUSDT | 8 | `tk_bull_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3570 | 0.5943 | 1.9411 | 0.0053 | 0.2453 | ok | RAN |
| SOLUSDT | 4 | `tk_bull_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.3424 | 0.5957 | 1.8125 | 0.0051 | 0.2500 | ok | RAN |
| ETHUSDT | 8 | `tk_bull_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.1452 | 0.5823 | 0.6817 | 0.0047 | 0.1899 | ok | RAN |
| ETHUSDT | 4 | `tk_bull_at_h` | one_head_filter_pi_star | 150 | 12.3782 | 1.0545 | 0.5733 | 0.2765 | 0.0019 | 0.1600 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `tk_bull_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `tk_bull_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `tk_bear_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `tk_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `tk_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `tk_bear_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `tk_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `tk_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
