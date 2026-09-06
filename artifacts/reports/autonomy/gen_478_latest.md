# Autonomy public-indicator hunt gen 478

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T162840Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma205_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9476 | 0.6839 | 4.3533 | 0.0225 | 0.3679 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma205_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8637 | 0.6839 | 4.1196 | 0.0208 | 0.3627 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma205_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2534 | 0.6954 | 4.3816 | 0.0179 | 0.3851 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma205_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1155 | 0.6886 | 3.9720 | 0.0167 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma205_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2747 | 0.6067 | 1.3242 | 0.0091 | 0.2191 | ok | RAN |
| ETHUSDT | 4 | `wma205_above_at_h` | one_head_filter_pi_star | 189 | 15.5965 | 1.1956 | 0.5979 | 1.0218 | 0.0067 | 0.2222 | ok | RAN |
| SOLUSDT | 8 | `wma205_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3287 | 0.5930 | 1.7259 | 0.0051 | 0.2613 | ok | RAN |
| SOLUSDT | 4 | `wma205_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.2979 | 0.5960 | 1.5733 | 0.0046 | 0.2576 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma205_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma205_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma205_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma205_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma205_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma205_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
