# Autonomy public-indicator hunt gen 1587

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T163821Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma686_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.1834 | 0.5896 | 1.0183 | 0.0053 | 0.2023 | ok | RAN |
| ETHUSDT | 8 | `sma686_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.1334 | 0.5690 | 0.7667 | 0.0041 | 0.1897 | ok | RAN |
| SOLUSDT | 8 | `sma686_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.1198 | 0.5496 | 0.5569 | 0.0023 | 0.1221 | ok | RAN |
| SOLUSDT | 4 | `sma686_above_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 1.0558 | 0.5442 | 0.2844 | 0.0011 | 0.1293 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma686_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9325 | 0.5661 | -0.4024 | -0.0015 | 0.1376 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma686_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 0.8782 | 0.5340 | -0.7868 | -0.0027 | 0.1311 | ok | RAN |
| ETHUSDT | 4 | `sma686_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 0.8826 | 0.5592 | -0.6228 | -0.0048 | 0.1053 | ok | RAN |
| ETHUSDT | 8 | `sma686_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.8743 | 0.5548 | -0.7034 | -0.0051 | 0.1161 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma686_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma686_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma686_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma686_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma686_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma686_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma686_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma686_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma686_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma686_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma686_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma686_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma686_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma686_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma686_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma686_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
