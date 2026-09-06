# Autonomy public-indicator hunt gen 1757

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T102559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret294_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.0987 | 0.5829 | 0.5823 | 0.0031 | 0.1886 | ok | RAN |
| ETHUSDT | 4 | `ret294_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.0964 | 0.5882 | 0.5487 | 0.0030 | 0.1882 | ok | RAN |
| SOLUSDT | 8 | `ret294_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 1.0753 | 0.5769 | 0.4008 | 0.0016 | 0.1538 | ok | RAN |
| SOLUSDT | 8 | `ret294_pos_at_h` | one_head_filter_pi_star | 175 | 14.3509 | 1.0373 | 0.5429 | 0.2047 | 0.0007 | 0.1086 | ok | RAN |
| SOLUSDT | 4 | `ret294_pos_at_h` | one_head_filter_pi_star | 170 | 13.9408 | 1.0051 | 0.5353 | 0.0279 | 0.0001 | 0.1118 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret294_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.0003 | 0.5482 | 0.0020 | 0.0000 | 0.1506 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret294_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.9178 | 0.5506 | -0.4828 | -0.0031 | 0.0955 | ok | RAN |
| ETHUSDT | 4 | `ret294_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8689 | 0.5506 | -0.7792 | -0.0053 | 0.1124 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret294_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0718 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret294_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0742 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret294_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret294_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret294_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret294_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret294_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret294_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret294_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret294_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret294_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret294_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret294_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret294_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret294_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret294_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
