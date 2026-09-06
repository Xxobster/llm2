# Autonomy public-indicator hunt gen 2053

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T153604Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret337_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 1.2183 | 0.6013 | 1.1135 | 0.0066 | 0.2152 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret337_pos_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.2928 | 0.5663 | 1.3850 | 0.0050 | 0.1145 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret337_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 1.1191 | 0.5793 | 0.6883 | 0.0038 | 0.2073 | ok | RAN |
| SOLUSDT | 8 | `ret337_pos_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.0873 | 0.5484 | 0.4467 | 0.0016 | 0.1032 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret337_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 0.9645 | 0.5635 | -0.2215 | -0.0008 | 0.1371 | ok | RAN |
| SOLUSDT | 4 | `ret337_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9520 | 0.5628 | -0.3028 | -0.0010 | 0.1307 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret337_pos_at_h` | one_head_filter_pi_star | 192 | 15.7304 | 0.8061 | 0.5469 | -1.2009 | -0.0081 | 0.1042 | ok | RAN |
| ETHUSDT | 8 | `ret337_pos_at_h` | one_head_filter_pi_star | 191 | 15.6485 | 0.7853 | 0.5393 | -1.3372 | -0.0093 | 0.0942 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret337_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0729 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret337_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0783 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret337_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret337_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret337_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret337_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret337_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret337_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret337_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret337_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret337_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret337_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret337_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret337_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret337_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret337_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
