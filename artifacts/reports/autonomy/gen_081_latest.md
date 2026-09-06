# Autonomy public-indicator hunt gen 081

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T145108Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `br_cross_up_p01` | one_head_filter_pi_star | 104 | 8.7905 | 2.8741 | 0.7692 | 4.3199 | 0.0479 | 0.5673 | EBR>35% | RAN |
| SOLUSDT | 4 | `br_wide_at_h` | one_head_filter_pi_star | 23 | 2.4580 | 5.1147 | 0.8696 | 3.4581 | 0.0413 | 0.7826 | EBR>35% | RAN |
| SOLUSDT | 8 | `br_cross_up_p01` | one_head_filter_pi_star | 91 | 7.8483 | 2.7176 | 0.7582 | 4.4602 | 0.0239 | 0.6044 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 8 | `br_cross_down_p004` | one_head_filter_pi_star | 20 | 1.7020 | 1.0398 | 0.4000 | 0.0723 | 0.0042 | 0.0500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `br_cross_down_p004` | one_head_filter_pi_star | 207 | 16.9508 | 1.1602 | 0.5700 | 0.9004 | 0.0024 | 0.1208 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `br_cross_down_p004` | one_head_filter_pi_star | 256 | 20.8261 | 1.0117 | 0.5781 | 0.0802 | 0.0004 | 0.1875 | ok | RAN |
| SOLUSDT | 4 | `br_cross_down_p004` | one_head_filter_pi_star | 118 | 9.6628 | 0.8808 | 0.5339 | -0.5702 | -0.0020 | 0.0847 | ok | RAN |
| SOLUSDT | 4 | `br_tight_at_h` | one_head_filter_pi_star | 60 | 5.0481 | 0.6620 | 0.5000 | -1.1627 | -0.0035 | 0.0500 | ok | RAN |
| SOLUSDT | 8 | `br_tight_at_h` | one_head_filter_pi_star | 83 | 6.9832 | 0.6752 | 0.4940 | -1.3878 | -0.0043 | 0.0602 | ok | RAN |
| ETHUSDT | 4 | `br_cross_down_p004` | one_head_filter_pi_star | 164 | 13.4364 | 0.8579 | 0.5305 | -0.8556 | -0.0047 | 0.1159 | ok | RAN |
| ETHUSDT | 8 | `br_tight_at_h` | one_head_filter_pi_star | 117 | 9.6689 | 0.7434 | 0.5299 | -1.2963 | -0.0068 | 0.0940 | ok | RAN |
| ETHUSDT | 4 | `br_tight_at_h` | one_head_filter_pi_star | 95 | 8.0126 | 0.6071 | 0.5053 | -1.9982 | -0.0113 | 0.0632 | ok | RAN |
| BTCUSDT | 8 | `br_tight_at_h` | one_head_filter_pi_star | 19 | 1.7436 | 0.6329 | 0.3158 | -0.7917 | -0.0322 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `br_cross_down_p004` | one_head_filter_pi_star | 12 | 1.1012 | 0.4469 | 0.2500 | -1.0671 | -0.0648 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `br_tight_at_h` | one_head_filter_pi_star | 14 | 3.1415 | 0.1390 | 0.2143 | -3.5786 | -0.0770 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `br_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `br_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `br_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `br_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `br_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `br_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `br_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `br_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `br_cross_up_p01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
