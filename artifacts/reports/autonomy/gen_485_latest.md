# Autonomy public-indicator hunt gen 485

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T165608Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret69_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.7761 | 0.6755 | 3.8416 | 0.0204 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret69_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.7022 | 0.6566 | 3.4390 | 0.0186 | 0.3586 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret69_neg_at_h` | one_head_filter_pi_star | 163 | 13.4830 | 2.3490 | 0.6994 | 4.4592 | 0.0186 | 0.4049 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret69_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.1170 | 0.6774 | 4.1709 | 0.0164 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret69_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.4085 | 0.6368 | 1.9727 | 0.0126 | 0.2368 | ok | RAN |
| ETHUSDT | 8 | `ret69_pos_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.3574 | 0.6193 | 1.7417 | 0.0110 | 0.2284 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret69_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4415 | 0.6162 | 2.2060 | 0.0065 | 0.2486 | ok | RAN |
| SOLUSDT | 4 | `ret69_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4099 | 0.6146 | 2.0966 | 0.0063 | 0.2552 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret69_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret69_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret69_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret69_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret69_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret69_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret69_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret69_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret69_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret69_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret69_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret69_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret69_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret69_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret69_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret69_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
