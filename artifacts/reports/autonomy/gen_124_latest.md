# Autonomy public-indicator hunt gen 124

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T173654Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma55_cross_up` | one_head_filter_pi_star | 20 | 1.6951 | 6.0797 | 0.7000 | 2.7382 | 0.0390 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma55_cross_up` | one_head_filter_pi_star | 19 | 1.9230 | 1.7214 | 0.5789 | 1.1182 | 0.0218 | 0.2105 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma55_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7460 | 0.6757 | 3.7331 | 0.0203 | 0.3694 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma55_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.7310 | 0.6713 | 3.6460 | 0.0199 | 0.3611 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma55_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1509 | 0.6832 | 4.0656 | 0.0176 | 0.4099 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma55_below_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 2.1010 | 0.6859 | 3.8837 | 0.0170 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma55_cross_down` | one_head_filter_pi_star | 26 | 2.1545 | 1.4429 | 0.5769 | 0.7926 | 0.0133 | 0.2308 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma55_cross_down` | one_head_filter_pi_star | 25 | 2.4191 | 1.3305 | 0.6000 | 0.6435 | 0.0083 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma55_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2232 | 0.6000 | 1.0298 | 0.0069 | 0.2125 | ok | RAN |
| ETHUSDT | 8 | `sma55_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1988 | 0.5988 | 0.9291 | 0.0062 | 0.2160 | ok | RAN |
| SOLUSDT | 4 | `sma55_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3681 | 0.6009 | 1.9497 | 0.0054 | 0.2615 | ok | RAN |
| SOLUSDT | 8 | `sma55_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3098 | 0.5943 | 1.6961 | 0.0046 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma55_cross_down` | one_head_filter_pi_star | 12 | 1.1612 | 0.3318 | 0.5000 | -1.4227 | -0.0214 | 0.0833 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma55_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma55_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `sma55_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma55_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma55_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma55_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma55_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma55_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
