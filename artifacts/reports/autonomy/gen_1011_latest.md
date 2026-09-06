# Autonomy public-indicator hunt gen 1011

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T114901Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma892_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.5771 | 0.7229 | 5.0192 | 0.0281 | 0.3976 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma892_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0927 | 0.6995 | 4.3406 | 0.0246 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma892_below_at_h` | one_head_filter_pi_star | 219 | 17.9078 | 1.7158 | 0.6484 | 3.3949 | 0.0116 | 0.3242 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma892_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.7267 | 0.6509 | 3.3322 | 0.0114 | 0.3160 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma892_above_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.7752 | 0.6557 | 2.5906 | 0.0112 | 0.3115 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma892_above_at_h` | one_head_filter_pi_star | 153 | 12.4757 | 1.5508 | 0.6013 | 2.2342 | 0.0087 | 0.2941 | ok | RAN |
| ETHUSDT | 4 | `sma892_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.2106 | 0.5875 | 1.0287 | 0.0078 | 0.2188 | ok | RAN |
| ETHUSDT | 8 | `sma892_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.1059 | 0.5750 | 0.5163 | 0.0042 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma892_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma892_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma892_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma892_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma892_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma892_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma892_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma892_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma892_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma892_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma892_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma892_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma892_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma892_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma892_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma892_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
