# Autonomy public-indicator hunt gen 129

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T175720Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma200_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1112 | 0.7112 | 4.7799 | 0.0255 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma200_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9527 | 0.6984 | 4.3476 | 0.0224 | 0.3704 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma200_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2329 | 0.6954 | 4.2614 | 0.0173 | 0.3793 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma200_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1304 | 0.6790 | 3.9112 | 0.0165 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma200_above_at_h` | one_head_filter_pi_star | 196 | 16.1742 | 1.2375 | 0.5969 | 1.2234 | 0.0082 | 0.2245 | ok | RAN |
| ETHUSDT | 4 | `sma200_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2299 | 0.5990 | 1.1669 | 0.0078 | 0.2234 | ok | RAN |
| SOLUSDT | 4 | `sma200_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.4042 | 0.6000 | 2.0585 | 0.0062 | 0.2585 | ok | RAN |
| SOLUSDT | 8 | `sma200_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.2700 | 0.5825 | 1.4323 | 0.0043 | 0.2577 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma200_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma200_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
