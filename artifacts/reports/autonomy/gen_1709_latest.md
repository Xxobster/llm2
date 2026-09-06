# Autonomy public-indicator hunt gen 1709

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T055217Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret287_neg_at_h` | one_head_filter_pi_star | 138 | 11.2733 | 1.3047 | 0.6304 | 1.4511 | 0.0085 | 0.2101 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret287_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1490 | 0.6000 | 0.8641 | 0.0049 | 0.2061 | ok | RAN |
| SOLUSDT | 4 | `ret287_neg_at_h` | one_head_filter_pi_star | 154 | 12.5927 | 1.0381 | 0.5649 | 0.1996 | 0.0008 | 0.1558 | ok | RAN |
| SOLUSDT | 8 | `ret287_neg_at_h` | one_head_filter_pi_star | 152 | 12.4292 | 1.0275 | 0.5592 | 0.1512 | 0.0006 | 0.1382 | ok | RAN |
| SOLUSDT | 4 | `ret287_pos_at_h` | one_head_filter_pi_star | 178 | 14.5969 | 1.0193 | 0.5393 | 0.1077 | 0.0004 | 0.1067 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret287_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0036 | 0.5435 | 0.0204 | 0.0001 | 0.1087 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret287_pos_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 0.9155 | 0.5641 | -0.4809 | -0.0033 | 0.1090 | ok | RAN |
| ETHUSDT | 4 | `ret287_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 0.8509 | 0.5460 | -0.9252 | -0.0059 | 0.0920 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret287_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0646 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret287_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0678 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret287_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret287_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret287_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret287_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret287_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret287_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret287_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret287_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret287_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret287_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret287_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret287_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret287_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret287_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
