# Edge lab hunt 003 — multi-timeframe swing structure

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T230244Z`.
**Evidence class:** inner screen on bars before 2022-01-01 only.

Concepts ported from `C:\projects\wavetheory`; **no numeric result inherited** (its own proxy failed out of sample and had a pivot look-ahead).

Arms recorded: 4320. Status: RAN=4077, TOO_FEW=198, TOO_FEW_GATED=45. Screen passes: 80.

| Symbol | TF | Event | Session | k_sl | tp:sl | n | /mo | PF | WR | Sharpe | HAC | Sortino | Recovery | MDD% | ebr | mean SL |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 1.5 | 1.0 | 219 | 14.093 | 1.864 | 0.639 | 3.226 | 2.710 | 2.707 | 7.255 | 0.000 | 0.146 | 0.017 |
| SOLUSDT | 1h | `wt_lh_ll_continuation_short` | no_weekend | 2.0 | 1.0 | 65 | 4.177 | 1.823 | 0.615 | 1.683 | 1.509 | 0.724 | 3.278 | 0.000 | 0.308 | 0.030 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 1.5 | 1.0 | 300 | 19.305 | 1.803 | 0.643 | 3.548 | 3.249 | 3.214 | 10.159 | 0.000 | 0.150 | 0.017 |
| SOLUSDT | 1h | `wt_lh_ll_continuation_short` | no_weekend | 1.5 | 1.0 | 65 | 4.177 | 1.746 | 0.600 | 1.622 | 1.454 | 0.710 | 2.952 | 0.000 | 0.338 | 0.028 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 1.5 | 1.0 | 87 | 5.614 | 1.721 | 0.609 | 1.775 | 1.665 | 0.881 | 3.291 | 0.000 | 0.161 | 0.019 |
| BTCUSDT | 1h | `wt_htf_bias_pullback_short` | all | 1.0 | 1.5 | 112 | 4.148 | 1.691 | 0.482 | 1.348 | 0.926 | 0.644 | 1.697 | 0.001 | 0.259 | 0.011 |
| ETHUSDT | 1h | `wt_htf_bias_pullback_long` | no_weekend | 1.5 | 1.0 | 128 | 5.178 | 1.659 | 0.602 | 1.453 | 1.508 | 0.708 | 4.592 | 0.000 | 0.219 | 0.020 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 1.0 | 1.5 | 85 | 5.485 | 1.620 | 0.459 | 1.466 | 1.277 | 0.877 | 2.790 | 0.000 | 0.224 | 0.013 |
| SOLUSDT | 4h | `wt_pullback_long` | all | 1.0 | 2.0 | 112 | 7.197 | 1.618 | 0.482 | 1.752 | 1.844 | 1.108 | 1.991 | 0.000 | 0.348 | 0.030 |
| SOLUSDT | 4h | `wt_pullback_long` | all | 1.5 | 2.0 | 112 | 7.197 | 1.601 | 0.482 | 1.714 | 1.798 | 1.075 | 1.896 | 0.001 | 0.348 | 0.030 |
| SOLUSDT | 4h | `wt_pullback_long` | all | 2.0 | 2.0 | 112 | 7.197 | 1.601 | 0.482 | 1.714 | 1.798 | 1.075 | 1.896 | 0.001 | 0.348 | 0.030 |
| SOLUSDT | 1h | `wt_pullback_short` | all | 1.5 | 1.0 | 297 | 19.085 | 1.594 | 0.606 | 2.955 | 2.653 | 2.479 | 6.779 | 0.000 | 0.343 | 0.028 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 2.0 | 1.5 | 80 | 5.163 | 1.579 | 0.487 | 1.315 | 1.151 | 0.756 | 2.198 | 0.000 | 0.062 | 0.023 |
| BTCUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 2.0 | 1.5 | 154 | 5.616 | 1.563 | 0.545 | 1.166 | 1.182 | 0.630 | 3.193 | 0.000 | 0.065 | 0.013 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 1.0 | 1.5 | 217 | 13.964 | 1.562 | 0.493 | 2.361 | 1.980 | 2.133 | 3.963 | 0.000 | 0.203 | 0.012 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 2.0 | 1.0 | 210 | 13.514 | 1.562 | 0.576 | 2.249 | 1.942 | 1.844 | 4.616 | 0.000 | 0.081 | 0.021 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 2.0 | 1.0 | 289 | 18.598 | 1.535 | 0.581 | 2.533 | 2.316 | 2.289 | 5.349 | 0.000 | 0.076 | 0.021 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 1.0 | 1.5 | 298 | 19.177 | 1.532 | 0.503 | 2.622 | 2.428 | 2.664 | 7.441 | 0.000 | 0.198 | 0.012 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 1.5 | 1.5 | 281 | 18.083 | 1.525 | 0.491 | 2.452 | 2.074 | 2.417 | 6.613 | 0.000 | 0.060 | 0.017 |
| SOLUSDT | 1h | `wt_pullback_short` | all | 2.0 | 1.0 | 295 | 18.957 | 1.523 | 0.600 | 2.610 | 2.337 | 2.147 | 5.796 | 0.000 | 0.332 | 0.030 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 1.5 | 1.5 | 204 | 13.128 | 1.521 | 0.490 | 2.101 | 1.625 | 1.778 | 3.061 | 0.000 | 0.059 | 0.017 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 2.0 | 1.5 | 274 | 17.632 | 1.509 | 0.493 | 2.330 | 1.962 | 2.359 | 5.284 | 0.000 | 0.044 | 0.021 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 2.0 | 1.5 | 199 | 12.806 | 1.506 | 0.492 | 1.999 | 1.604 | 1.786 | 3.301 | 0.000 | 0.045 | 0.021 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 1.5 | 1.5 | 82 | 5.292 | 1.503 | 0.463 | 1.285 | 1.067 | 0.745 | 1.779 | 0.000 | 0.085 | 0.019 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 2.0 | 1.0 | 84 | 5.421 | 1.498 | 0.548 | 1.250 | 1.198 | 0.622 | 1.700 | 0.000 | 0.083 | 0.023 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 1.5 | 2.0 | 197 | 12.677 | 1.495 | 0.431 | 1.761 | 1.314 | 1.742 | 3.256 | 0.000 | 0.041 | 0.017 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 2.0 | 2.0 | 191 | 12.291 | 1.491 | 0.461 | 1.688 | 1.309 | 1.679 | 3.204 | 0.000 | 0.026 | 0.021 |
| ETHUSDT | 1h | `wt_htf_bias_pullback_long` | all | 1.5 | 1.0 | 161 | 6.499 | 1.482 | 0.596 | 1.274 | 1.285 | 0.633 | 3.322 | 0.000 | 0.217 | 0.020 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 1.5 | 2.0 | 272 | 17.504 | 1.481 | 0.434 | 2.057 | 1.627 | 2.332 | 4.412 | 0.000 | 0.040 | 0.017 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 2.0 | 2.0 | 264 | 16.989 | 1.474 | 0.455 | 1.925 | 1.564 | 2.203 | 3.603 | 0.000 | 0.027 | 0.021 |
| SOLUSDT | 1h | `wt_pullback_confirmed_short` | no_weekend | 1.0 | 1.5 | 90 | 5.846 | 1.463 | 0.489 | 1.296 | 1.232 | 0.733 | 2.103 | 0.000 | 0.267 | 0.023 |
| SOLUSDT | 1h | `wt_lh_ll_continuation_short` | no_weekend | 1.0 | 1.5 | 65 | 4.177 | 1.456 | 0.462 | 1.106 | 0.986 | 0.532 | 1.754 | 0.000 | 0.277 | 0.022 |
| SOLUSDT | 1h | `wt_pullback_confirmed_short` | all | 1.0 | 1.5 | 129 | 8.351 | 1.454 | 0.496 | 1.562 | 1.567 | 1.018 | 3.007 | 0.000 | 0.271 | 0.023 |
| BTCUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 2.0 | 1.0 | 156 | 5.689 | 1.453 | 0.615 | 1.029 | 1.034 | 0.456 | 1.893 | 0.000 | 0.077 | 0.013 |
| SOLUSDT | 1h | `wt_pullback_confirmed_short` | all | 2.0 | 1.5 | 126 | 8.157 | 1.450 | 0.500 | 1.433 | 1.639 | 0.941 | 2.442 | 0.000 | 0.230 | 0.030 |
| BTCUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 1.5 | 1.0 | 161 | 5.871 | 1.443 | 0.615 | 1.143 | 1.202 | 0.489 | 3.007 | 0.000 | 0.143 | 0.010 |
| ETHUSDT | 5m | `wt_hh_hl_continuation_long` | ny_am_kz_no_weekend | 1.5 | 1.0 | 184 | 7.393 | 1.442 | 0.592 | 1.189 | 1.062 | 0.647 | 3.186 | 0.000 | 0.174 | 0.007 |
| ETHUSDT | 5m | `wt_hh_hl_continuation_long` | no_weekend | 1.0 | 1.0 | 1318 | 52.562 | 1.436 | 0.636 | 3.152 | 2.564 | 3.866 | 5.237 | 0.000 | 0.322 | 0.005 |
| SOLUSDT | 1h | `wt_lh_ll_continuation_short` | all | 2.0 | 1.0 | 95 | 6.105 | 1.427 | 0.579 | 1.218 | 1.053 | 0.566 | 2.037 | 0.000 | 0.274 | 0.030 |
| SOLUSDT | 1h | `wt_lh_ll_continuation_short` | all | 1.5 | 1.0 | 95 | 6.105 | 1.423 | 0.579 | 1.245 | 1.085 | 0.584 | 2.007 | 0.000 | 0.295 | 0.028 |
| ETHUSDT | 15m | `wt_hh_hl_continuation_long` | weekday_ny | 1.5 | 2.0 | 143 | 5.692 | 1.401 | 0.476 | 1.043 | 1.074 | 0.635 | 1.619 | 0.000 | 0.070 | 0.011 |
| ETHUSDT | 5m | `wt_lh_ll_continuation_short` | weekday_ny | 1.0 | 1.0 | 380 | 15.181 | 1.390 | 0.621 | 1.642 | 1.558 | 1.198 | 4.434 | 0.000 | 0.316 | 0.006 |
| SOLUSDT | 1h | `wt_pullback_confirmed_short` | no_weekend | 1.5 | 1.5 | 88 | 5.716 | 1.388 | 0.489 | 1.022 | 1.184 | 0.562 | 1.670 | 0.000 | 0.227 | 0.028 |
| SOLUSDT | 1h | `wt_pullback_confirmed_short` | all | 1.5 | 1.5 | 126 | 8.157 | 1.388 | 0.492 | 1.273 | 1.467 | 0.822 | 2.180 | 0.000 | 0.230 | 0.028 |
| BTCUSDT | 1h | `wt_bas_break_short` | no_weekend | 2.0 | 2.0 | 339 | 12.207 | 1.369 | 0.442 | 1.185 | 1.156 | 1.283 | 2.511 | 0.001 | 0.118 | 0.022 |
| ETHUSDT | 5m | `wt_pullback_long` | weekday_ny | 1.0 | 1.0 | 1423 | 56.592 | 1.358 | 0.642 | 2.532 | 2.076 | 2.678 | 3.477 | 0.001 | 0.349 | 0.005 |
| SOLUSDT | 1h | `wt_pullback_short` | weekday_ny | 1.0 | 1.5 | 83 | 5.482 | 1.355 | 0.482 | 1.073 | 1.229 | 0.617 | 1.969 | 0.000 | 0.289 | 0.023 |
| BTCUSDT | 1h | `wt_bas_break_short` | no_weekend | 2.0 | 1.5 | 377 | 13.576 | 1.353 | 0.475 | 1.404 | 1.335 | 1.405 | 3.503 | 0.001 | 0.141 | 0.022 |
| SOLUSDT | 1h | `wt_pullback_short` | no_weekend | 1.0 | 1.5 | 191 | 12.274 | 1.348 | 0.461 | 1.528 | 1.526 | 1.181 | 3.274 | 0.000 | 0.257 | 0.023 |
| BTCUSDT | 5m | `wt_htf_bias_pullback_short` | weekday_ny | 1.0 | 1.0 | 347 | 12.547 | 1.347 | 0.597 | 1.268 | 1.229 | 0.910 | 2.149 | 0.000 | 0.231 | 0.005 |
| BTCUSDT | 15m | `wt_pullback_confirmed_short` | no_weekend | 1.0 | 1.0 | 643 | 23.154 | 1.343 | 0.600 | 1.893 | 1.922 | 1.537 | 4.128 | 0.000 | 0.334 | 0.006 |
| ETHUSDT | 5m | `wt_lh_ll_continuation_short` | no_weekend | 1.0 | 1.0 | 1056 | 42.039 | 1.337 | 0.608 | 2.200 | 2.100 | 2.322 | 7.270 | 0.000 | 0.282 | 0.005 |
| BTCUSDT | 5m | `wt_hh_hl_continuation_long` | weekday_ny | 1.0 | 1.0 | 446 | 16.116 | 1.322 | 0.632 | 1.521 | 1.380 | 1.005 | 3.171 | 0.000 | 0.314 | 0.005 |
| ETHUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 1.0 | 1.5 | 383 | 15.259 | 1.320 | 0.449 | 1.296 | 1.185 | 1.105 | 3.705 | 0.000 | 0.170 | 0.008 |
| BTCUSDT | 15m | `wt_pullback_confirmed_short` | all | 1.0 | 1.0 | 871 | 31.365 | 1.310 | 0.596 | 2.061 | 2.176 | 1.938 | 5.644 | 0.000 | 0.326 | 0.006 |
| ETHUSDT | 5m | `wt_htf_bias_pullback_long` | no_weekend | 1.0 | 1.0 | 1298 | 51.687 | 1.302 | 0.638 | 2.579 | 2.208 | 2.122 | 7.327 | 0.000 | 0.336 | 0.005 |
| ETHUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 1.5 | 1.0 | 372 | 14.821 | 1.300 | 0.540 | 1.230 | 1.005 | 0.971 | 2.967 | 0.000 | 0.145 | 0.012 |
| ETHUSDT | 5m | `wt_hh_hl_continuation_long` | all | 1.0 | 1.0 | 1823 | 72.702 | 1.295 | 0.624 | 2.738 | 2.272 | 3.323 | 3.476 | 0.001 | 0.306 | 0.005 |
| ETHUSDT | 5m | `wt_pullback_confirmed_long` | weekday_ny | 1.0 | 1.0 | 626 | 25.148 | 1.290 | 0.613 | 1.653 | 1.511 | 1.184 | 3.041 | 0.000 | 0.324 | 0.005 |
| ETHUSDT | 5m | `wt_lh_ll_continuation_short` | all | 1.0 | 1.0 | 1473 | 58.640 | 1.267 | 0.600 | 2.067 | 1.720 | 2.614 | 4.796 | 0.000 | 0.271 | 0.005 |
| BTCUSDT | 1h | `wt_bas_break_short` | no_weekend | 2.0 | 1.0 | 451 | 16.241 | 1.267 | 0.539 | 1.121 | 1.126 | 1.102 | 3.326 | 0.001 | 0.169 | 0.022 |
| SOLUSDT | 15m | `wt_hh_hl_continuation_long` | no_weekend | 1.5 | 1.0 | 209 | 13.528 | 1.263 | 0.589 | 1.151 | 1.254 | 0.840 | 1.135 | 0.000 | 0.211 | 0.018 |
| BTCUSDT | 5m | `wt_lh_ll_continuation_short` | weekday_ny | 1.0 | 1.0 | 374 | 13.513 | 1.263 | 0.599 | 1.044 | 0.963 | 0.698 | 1.142 | 0.001 | 0.270 | 0.005 |
| BTCUSDT | 1h | `wt_bas_break_short` | no_weekend | 1.5 | 2.0 | 381 | 13.720 | 1.262 | 0.423 | 1.003 | 0.943 | 1.062 | 1.644 | 0.002 | 0.142 | 0.018 |
| SOLUSDT | 15m | `wt_pullback_short` | no_weekend | 1.5 | 1.0 | 681 | 43.794 | 1.260 | 0.543 | 2.024 | 2.073 | 2.043 | 4.242 | 0.000 | 0.163 | 0.018 |
| ETHUSDT | 5m | `wt_pullback_long` | no_weekend | 1.0 | 1.0 | 3719 | 147.904 | 1.255 | 0.616 | 3.019 | 2.370 | 3.626 | 5.171 | 0.001 | 0.314 | 0.005 |
| SOLUSDT | 15m | `wt_pullback_confirmed_short` | all | 1.5 | 1.0 | 436 | 28.047 | 1.254 | 0.539 | 1.715 | 1.685 | 1.581 | 3.317 | 0.000 | 0.158 | 0.018 |
| ETHUSDT | 5m | `wt_htf_bias_pullback_long` | weekday_ny | 2.0 | 2.0 | 392 | 15.609 | 1.245 | 0.467 | 1.104 | 0.986 | 0.597 | 2.674 | 0.000 | 0.038 | 0.009 |
| SOLUSDT | 15m | `wt_pullback_short` | all | 1.5 | 1.0 | 950 | 61.093 | 1.245 | 0.548 | 2.227 | 2.258 | 2.489 | 3.692 | 0.000 | 0.157 | 0.017 |
| BTCUSDT | 1h | `wt_bas_break_short` | no_weekend | 1.5 | 1.5 | 437 | 15.736 | 1.238 | 0.465 | 1.053 | 1.008 | 1.110 | 2.217 | 0.001 | 0.162 | 0.018 |
| ETHUSDT | 5m | `wt_pullback_short` | ny_am_kz_no_weekend | 1.0 | 1.0 | 518 | 20.648 | 1.235 | 0.602 | 1.200 | 1.325 | 0.903 | 3.102 | 0.000 | 0.344 | 0.005 |
| SOLUSDT | 15m | `wt_pullback_confirmed_short` | no_weekend | 1.0 | 1.5 | 312 | 20.070 | 1.232 | 0.455 | 1.431 | 1.446 | 1.129 | 2.266 | 0.000 | 0.215 | 0.013 |
| ETHUSDT | 5m | `wt_pullback_short` | no_weekend | 1.0 | 1.0 | 3594 | 142.892 | 1.230 | 0.600 | 2.897 | 2.358 | 3.525 | 5.446 | 0.001 | 0.272 | 0.005 |
| ETHUSDT | 5m | `wt_htf_bias_pullback_long` | all | 1.0 | 1.0 | 1785 | 71.079 | 1.224 | 0.625 | 2.295 | 2.009 | 2.018 | 4.413 | 0.000 | 0.304 | 0.005 |
| SOLUSDT | 15m | `wt_pullback_confirmed_short` | all | 1.0 | 1.5 | 440 | 28.304 | 1.219 | 0.457 | 1.532 | 1.578 | 1.452 | 3.102 | 0.000 | 0.207 | 0.012 |
| SOLUSDT | 15m | `wt_htf_bias_pullback_long` | no_weekend | 1.5 | 1.0 | 249 | 16.323 | 1.215 | 0.534 | 1.163 | 1.289 | 0.815 | 1.719 | 0.000 | 0.157 | 0.019 |
| SOLUSDT | 15m | `wt_pullback_confirmed_short` | no_weekend | 1.5 | 1.0 | 310 | 19.941 | 1.213 | 0.529 | 1.273 | 1.320 | 0.986 | 2.659 | 0.000 | 0.161 | 0.018 |
| SOLUSDT | 15m | `wt_htf_bias_pullback_long` | all | 1.5 | 1.0 | 344 | 22.550 | 1.212 | 0.547 | 1.389 | 1.535 | 1.117 | 1.966 | 0.000 | 0.154 | 0.018 |
| ETHUSDT | 5m | `wt_pullback_short` | weekday_ny | 1.0 | 1.0 | 1384 | 55.026 | 1.205 | 0.602 | 1.588 | 1.727 | 1.475 | 5.596 | 0.000 | 0.302 | 0.005 |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 1.0 | 2.0 | 289 | 18.598 | 1.202 | 0.384 | 1.090 | 0.912 | 1.134 | 1.094 | 0.000 | 0.114 | 0.012 |
