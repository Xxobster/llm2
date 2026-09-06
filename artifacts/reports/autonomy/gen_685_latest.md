# Autonomy public-indicator hunt gen 685

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T060641Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret119_neg_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8118 | 0.6809 | 3.9140 | 0.0206 | 0.3670 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret119_neg_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.7606 | 0.6667 | 3.7434 | 0.0197 | 0.3627 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret119_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.2592 | 0.6831 | 4.4193 | 0.0165 | 0.3607 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret119_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.1384 | 0.6831 | 4.1520 | 0.0155 | 0.3607 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret119_pos_at_h` | one_head_filter_pi_star | 168 | 13.8636 | 1.3953 | 0.6369 | 1.7889 | 0.0123 | 0.2321 | ok | RAN |
| ETHUSDT | 4 | `ret119_pos_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 1.3420 | 0.6264 | 1.5963 | 0.0110 | 0.2184 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret119_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4136 | 0.6062 | 2.0570 | 0.0067 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `ret119_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.3886 | 0.6080 | 1.8942 | 0.0064 | 0.2670 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret119_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret119_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret119_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret119_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret119_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret119_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret119_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret119_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret119_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret119_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret119_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret119_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret119_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret119_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret119_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret119_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
