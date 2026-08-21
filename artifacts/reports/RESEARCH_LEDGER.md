# LLM2 Research Ledger

## [INFO] 2026-08-02 08:18:01 UTC (tier 0)

START gen=gen_001_btc_1h_fwd BTCUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 08:18:05 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.57226426217494e-09, 'circular_shift': 3.57226426217494e-09, 'fourier_phase': 3.57226426217494e-09, 'row_shuffle': 3.57226426217494e-09} passed=False

## [INFO] 2026-08-02 08:18:28 UTC (tier 0)

trial `3f426a10-6a29-450a-b316-f3733be2a573` model=hist_mean tier=0 pf=0.723 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:18:28 UTC (tier 0)

trial `e07f8144-ff04-4018-bb90-6be613d9aaea` model=last_value tier=0 pf=0.696 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:18:28 UTC (tier 0)

trial `5eecc49b-1a68-4dbb-8c5b-c3aa0e7657a2` model=seasonal_naive tier=0 pf=0.689 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:18:29 UTC (tier 0)

trial `ad27f79f-31a7-42c2-a43d-ee56847f30d2` model=ridge tier=0 pf=0.713 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:18:54 UTC (tier 0)

trial `4cd9e506-a4e8-4892-a122-2f7cc889c967` model=lgbm_regressor tier=0 pf=0.687 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:19:49 UTC (tier 0)

trial `4472ba82-1017-428b-ad7f-1f02492a1a1c` model=lgbm_classifier tier=0 pf=0.713 trades=32726 gates=FAIL

## [INFO] 2026-08-02 08:22:54 UTC (tier 0)

trial `966581ac-01af-47c4-a2b7-b80323fd0361` model=torch_mlp tier=0 pf=0.722 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:22:54 UTC (tier 0)

Hunt complete: {"generation_id": "gen_001_btc_1h_fwd", "status": "COMPLETE", "n_trials": 7, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:27:41 UTC (tier 0)

START gen=gen_002_btc_1h_vol BTCUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 08:27:47 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 7.451705918981588e-10, 'circular_shift': 7.451705918981588e-10, 'fourier_phase': 7.451705918981588e-10, 'row_shuffle': 7.451705918981588e-10} passed=False

## [INFO] 2026-08-02 08:27:56 UTC (tier 0)

trial `327cd184-99b8-4678-b218-4fde8258299c` model=hist_mean tier=0 pf=inf trades=32855 gates=UNKNOWN

## [INFO] 2026-08-02 08:27:56 UTC (tier 0)

SURROGATE FAIL model=last_value mae_s=0.015530

## [INFO] 2026-08-02 08:27:56 UTC (tier 0)

trial `92031fbe-9ee4-434c-bb2f-f6ccb0a92e0f` model=last_value tier=0 pf=inf trades=32855 gates=UNKNOWN

## [INFO] 2026-08-02 08:27:57 UTC (tier 0)

trial `8fd673c0-b58c-49f4-acf7-62a971bcf674` model=seasonal_naive tier=0 pf=inf trades=32855 gates=UNKNOWN

## [INFO] 2026-08-02 08:27:57 UTC (tier 0)

trial `dc3c6f7b-a130-4bb6-b378-8578c0d82e92` model=ridge tier=0 pf=inf trades=32855 gates=UNKNOWN

## [INFO] 2026-08-02 08:27:57 UTC (tier 0)

Hunt complete: {"generation_id": "gen_002_btc_1h_vol", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:28:14 UTC (tier 0)

START gen=gen_003_eth_1h_fwd ETHUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 08:28:19 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.2880143335513026e-09, 'circular_shift': 2.2880143335513026e-09, 'fourier_phase': 2.2880143335513026e-09, 'row_shuffle': 2.2880143335513026e-09} passed=False

## [INFO] 2026-08-02 08:28:34 UTC (tier 0)

trial `e3afd661-a291-440c-a5db-cfadc14268dc` model=hist_mean tier=0 pf=0.764 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:28:35 UTC (tier 0)

trial `65060eff-893c-4316-a8bb-d3713cb061a2` model=last_value tier=0 pf=0.793 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:28:35 UTC (tier 0)

trial `a2fc6e18-b30d-4c07-a7e2-5a2986aa04c3` model=seasonal_naive tier=0 pf=0.736 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:28:38 UTC (tier 0)

trial `c2a37946-c814-41da-9207-69f8fe08993b` model=ridge tier=0 pf=0.799 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:28:38 UTC (tier 0)

Hunt complete: {"generation_id": "gen_003_eth_1h_fwd", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:28:54 UTC (tier 0)

START gen=gen_004_sol_1h_fwd SOLUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 08:28:59 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.33865651475685e-10, 'circular_shift': 9.33865651475685e-10, 'fourier_phase': 9.33865651475685e-10, 'row_shuffle': 9.33865651475685e-10} passed=False

## [INFO] 2026-08-02 08:29:19 UTC (tier 0)

trial `dcf8b25c-5f47-44b9-b6f0-453784908bf7` model=hist_mean tier=0 pf=0.848 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:29:19 UTC (tier 0)

trial `2c89feec-67e0-4e87-bac5-cb8bded9fcf5` model=last_value tier=0 pf=0.896 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:29:19 UTC (tier 0)

trial `a3ce0402-0c9f-4f1e-9cbc-26e835ea1056` model=seasonal_naive tier=0 pf=0.866 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:29:20 UTC (tier 0)

trial `32cba003-618f-488e-bd96-5c4cba6342b2` model=ridge tier=0 pf=0.868 trades=32855 gates=FAIL

## [INFO] 2026-08-02 08:29:20 UTC (tier 0)

Hunt complete: {"generation_id": "gen_004_sol_1h_fwd", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:30:25 UTC (tier 0)

START gen=gen_005_btc_1h_tradesim BTCUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 08:30:29 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.57226426217494e-09, 'circular_shift': 3.57226426217494e-09, 'fourier_phase': 3.57226426217494e-09, 'row_shuffle': 3.57226426217494e-09} passed=False

## [INFO] 2026-08-02 08:30:43 UTC (tier 0)

trial `b76c3a59-23b4-4e87-b632-7727fddc42c6` model=hist_mean tier=0 pf=0.000 trades=0 gates=FAIL

## [INFO] 2026-08-02 08:30:49 UTC (tier 0)

TRIAL ERROR model=ridge: float() argument must be a string or a real number, not 'Timestamp'
Traceback (most recent call last):
  File "D:\projects\LLM2\llm2\hunt\runner.py", line 346, in run_nested_hunt
    eq = np.asarray(bundle.result.daily_equity, dtype=float)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\projects\LLM2\.venv\Lib\site-packages\pandas\core\generic.py", line 2171, in __array__
    arr = np.asarray(values, dtype=dtype)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: float() argument must be a string or a real number, not 'Timestamp'

## [INFO] 2026-08-02 08:30:58 UTC (tier 0)

START gen=gen_005_btc_1h_tradesim BTCUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 08:31:04 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.57226426217494e-09, 'circular_shift': 3.57226426217494e-09, 'fourier_phase': 3.57226426217494e-09, 'row_shuffle': 3.57226426217494e-09} passed=False

## [INFO] 2026-08-02 08:31:25 UTC (tier 0)

trial `8333868e-79a8-4ccd-869f-dff95dd4e8a5` model=hist_mean tier=0 pf=0.000 trades=0 gates=FAIL

## [INFO] 2026-08-02 08:31:31 UTC (tier 0)

TRIAL ERROR model=ridge: float() argument must be a string or a real number, not 'Timestamp'
Traceback (most recent call last):
  File "D:\projects\LLM2\llm2\hunt\runner.py", line 346, in run_nested_hunt
    eq = np.asarray(bundle.result.daily_equity, dtype=float)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\projects\LLM2\.venv\Lib\site-packages\pandas\core\generic.py", line 2171, in __array__
    arr = np.asarray(values, dtype=dtype)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: float() argument must be a string or a real number, not 'Timestamp'

## [INFO] 2026-08-02 08:32:01 UTC (tier 0)

TRIAL ERROR model=lgbm_regressor: float() argument must be a string or a real number, not 'Timestamp'
Traceback (most recent call last):
  File "D:\projects\LLM2\llm2\hunt\runner.py", line 346, in run_nested_hunt
    eq = np.asarray(bundle.result.daily_equity, dtype=float)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\projects\LLM2\.venv\Lib\site-packages\pandas\core\generic.py", line 2171, in __array__
    arr = np.asarray(values, dtype=dtype)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: float() argument must be a string or a real number, not 'Timestamp'

## [INFO] 2026-08-02 08:32:01 UTC (tier 0)

Hunt complete: {"generation_id": "gen_005_btc_1h_tradesim", "status": "COMPLETE", "n_trials": 1, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:32:11 UTC (tier 0)

TRIAL ERROR model=lgbm_regressor: float() argument must be a string or a real number, not 'Timestamp'
Traceback (most recent call last):
  File "D:\projects\LLM2\llm2\hunt\runner.py", line 346, in run_nested_hunt
    eq = np.asarray(bundle.result.daily_equity, dtype=float)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\projects\LLM2\.venv\Lib\site-packages\pandas\core\generic.py", line 2171, in __array__
    arr = np.asarray(values, dtype=dtype)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: float() argument must be a string or a real number, not 'Timestamp'

## [INFO] 2026-08-02 08:32:11 UTC (tier 0)

Hunt complete: {"generation_id": "gen_005_btc_1h_tradesim", "status": "COMPLETE", "n_trials": 1, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:33:27 UTC (tier 0)

START gen=gen_006_btc_1h_tradesim BTCUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 08:33:31 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.57226426217494e-09, 'circular_shift': 3.57226426217494e-09, 'fourier_phase': 3.57226426217494e-09, 'row_shuffle': 3.57226426217494e-09} passed=False

## [INFO] 2026-08-02 08:34:05 UTC (tier 0)

trial `d716b771-d209-458e-a92c-7dfaca50e496` model=ridge tier=0 pf=0.790 trades=2193 gates=FAIL

## [INFO] 2026-08-02 08:34:47 UTC (tier 0)

trial `f48db46a-90be-4f85-a3c1-4def62011705` model=lgbm_regressor tier=0 pf=0.881 trades=1783 gates=FAIL

## [INFO] 2026-08-02 08:37:44 UTC (tier 0)

trial `3f9ac4a0-3e05-4660-94cd-5bf6468bf7d0` model=torch_mlp tier=0 pf=0.797 trades=3616 gates=FAIL

## [INFO] 2026-08-02 08:37:44 UTC (tier 0)

Hunt complete: {"generation_id": "gen_006_btc_1h_tradesim", "status": "COMPLETE", "n_trials": 3, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:37:58 UTC (tier 0)

START gen=gen_007_btc_4h_fwd BTCUSDT 4h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 08:38:01 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.749191371393295e-10, 'circular_shift': 8.749191371393295e-10, 'fourier_phase': 8.749191371393295e-10, 'row_shuffle': 8.749191371393295e-10} passed=False

## [INFO] 2026-08-02 08:38:06 UTC (tier 0)

trial `98c1112c-f6ae-46b9-a255-37414d1ad3a1` model=hist_mean tier=0 pf=0.683 trades=1638 gates=FAIL

## [INFO] 2026-08-02 08:38:06 UTC (tier 0)

trial `a364266c-c6ae-4026-ad45-23de8f2cc933` model=last_value tier=0 pf=0.876 trades=8214 gates=FAIL

## [INFO] 2026-08-02 08:38:06 UTC (tier 0)

trial `eeb6b01c-bdd6-4def-ad1b-6a27f004fa87` model=seasonal_naive tier=0 pf=0.959 trades=3413 gates=FAIL

## [INFO] 2026-08-02 08:38:06 UTC (tier 0)

trial `fb8547d3-a4ea-42dd-b79f-27af6580ee92` model=ridge tier=0 pf=1.018 trades=5223 gates=FAIL

## [INFO] 2026-08-02 08:38:32 UTC (tier 0)

trial `7210161e-e36f-4d5b-bc27-f571fc8dfb41` model=lgbm_regressor tier=0 pf=0.864 trades=5565 gates=FAIL

## [INFO] 2026-08-02 08:38:32 UTC (tier 0)

Hunt complete: {"generation_id": "gen_007_btc_4h_fwd", "status": "COMPLETE", "n_trials": 5, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:38:46 UTC (tier 0)

START gen=gen_008_btc_1h_dir BTCUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-02 08:39:17 UTC (tier 0)

START gen=gen_008_btc_1h_dir BTCUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-02 08:39:22 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.0007550343971161e-12, 'circular_shift': 1.0007550343971161e-12, 'fourier_phase': 1.0007550343971161e-12, 'row_shuffle': 1.0007550343971161e-12} passed=False

## [INFO] 2026-08-02 08:39:35 UTC (tier 0)

trial `c9d746ba-1c4e-48d2-b3d3-1fdd8585f4f8` model=hist_mean tier=0 pf=1.039 trades=32856 gates=FAIL

## [INFO] 2026-08-02 08:39:35 UTC (tier 0)

trial `991245dc-0083-4b90-9028-a7f7289fdadd` model=last_value tier=0 pf=0.983 trades=32856 gates=FAIL

## [INFO] 2026-08-02 08:39:35 UTC (tier 0)

trial `b9eb7305-c8e2-4fa4-8ce2-df8a1a2cc6ff` model=seasonal_naive tier=0 pf=1.015 trades=32306 gates=FAIL

## [INFO] 2026-08-02 08:39:36 UTC (tier 0)

trial `e9833fc0-a199-486e-a1f7-fc4aa07cba90` model=ridge tier=0 pf=1.125 trades=32497 gates=FAIL

## [INFO] 2026-08-02 08:39:56 UTC (tier 0)

trial `8c7c9234-2e6a-4ba1-b32a-9e160f7f6c2a` model=lgbm_regressor tier=0 pf=1.109 trades=32560 gates=FAIL

## [INFO] 2026-08-02 08:39:56 UTC (tier 0)

Hunt complete: {"generation_id": "gen_008_btc_1h_dir", "status": "COMPLETE", "n_trials": 5, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:40:09 UTC (tier 0)

START gen=gen_009_btc_1h_pivot BTCUSDT 1h target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 08:40:11 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.5743014104028248e-09, 'circular_shift': 3.5743014104028248e-09, 'fourier_phase': 3.5743014104028248e-09, 'row_shuffle': 3.5743014104028248e-09} passed=False

## [INFO] 2026-08-02 08:40:23 UTC (tier 0)

trial `8d11bd5b-49ce-4f8f-b3c6-6d87726f748c` model=hist_mean tier=0 pf=0.000 trades=0 gates=FAIL

## [INFO] 2026-08-02 08:40:23 UTC (tier 0)

trial `4425b0b8-baf0-4827-b70d-b871da98423d` model=last_value tier=0 pf=0.715 trades=26304 gates=FAIL

## [INFO] 2026-08-02 08:40:23 UTC (tier 0)

trial `94de7488-1e30-4834-a4df-dee8174c4418` model=seasonal_naive tier=0 pf=0.570 trades=819 gates=FAIL

## [INFO] 2026-08-02 08:40:25 UTC (tier 0)

trial `1db91d74-a884-4802-b4b7-b8ba874e476d` model=ridge tier=0 pf=0.782 trades=2380 gates=FAIL

## [INFO] 2026-08-02 08:41:04 UTC (tier 0)

trial `6aa9e85f-63f5-443f-b7a9-92954ba7384b` model=lgbm_regressor tier=0 pf=0.730 trades=7895 gates=FAIL

## [INFO] 2026-08-02 08:41:04 UTC (tier 0)

Hunt complete: {"generation_id": "gen_009_btc_1h_pivot", "status": "COMPLETE", "n_trials": 5, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:42:25 UTC (tier 0)

START gen=gen_010_btc_1h_dir_tradesim BTCUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-02 08:42:33 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.0007550343971161e-12, 'circular_shift': 1.0007550343971161e-12, 'fourier_phase': 1.0007550343971161e-12, 'row_shuffle': 1.0007550343971161e-12} passed=False

## [INFO] 2026-08-02 08:43:21 UTC (tier 0)

trial `e209fd83-6128-407b-8381-f22554a98ccc` model=ridge tier=0 pf=0.786 trades=3827 gates=FAIL

## [INFO] 2026-08-02 08:45:55 UTC (tier 0)

trial `695eb8b5-2df9-4b79-bb85-c11ee2803b88` model=lgbm_classifier tier=0 pf=0.774 trades=3772 gates=FAIL

## [INFO] 2026-08-02 08:48:49 UTC (tier 0)

trial `0ea23fdf-23d3-4fb5-8e75-3bfd2d498ee2` model=lgbm_regressor tier=0 pf=0.771 trades=3775 gates=FAIL

## [INFO] 2026-08-02 08:48:49 UTC (tier 0)

Hunt complete: {"generation_id": "gen_010_btc_1h_dir_tradesim", "status": "COMPLETE", "n_trials": 3, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:50:47 UTC (tier 0)

AUTONOMY start 54 combos

## [INFO] 2026-08-02 08:50:47 UTC (tier 0)

START gen=auto_000_BTCUSDT_1h_fwd_return_ohlcv_v1 BTCUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 08:50:51 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.57226426217494e-09, 'circular_shift': 3.57226426217494e-09, 'fourier_phase': 3.57226426217494e-09, 'row_shuffle': 3.57226426217494e-09} passed=False

## [INFO] 2026-08-02 08:51:12 UTC (tier 0)

trial `9d80c5a5-d7e9-4df2-b1d2-4ada743ec094` model=hist_mean tier=0 pf=0.000 trades=0 gates=FAIL

## [INFO] 2026-08-02 08:51:13 UTC (tier 0)

trial `ffa23559-249c-4e0d-8d44-6cfe9eeb0402` model=ridge tier=0 pf=0.824 trades=6802 gates=FAIL

## [INFO] 2026-08-02 08:52:36 UTC (tier 0)

trial `42158485-e6f4-4d26-85a5-d26249bcaba3` model=lgbm_regressor tier=0 pf=0.769 trades=4203 gates=FAIL

## [INFO] 2026-08-02 08:54:30 UTC (tier 0)

trial `b220ad0e-b3db-410c-a613-b2f31a154a4e` model=lgbm_classifier tier=0 pf=0.713 trades=32726 gates=FAIL

## [INFO] 2026-08-02 08:54:30 UTC (tier 0)

Hunt complete: {"generation_id": "auto_000_BTCUSDT_1h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 08:54:30 UTC (tier 0)

AUTONOMY done auto_000_BTCUSDT_1h_fwd_return_ohlcv_v1 tier=0 pf=0.8241790932610158

## [INFO] 2026-08-02 08:54:30 UTC (tier 0)

START gen=auto_001_BTCUSDT_1h_fwd_return_indicators_v1 BTCUSDT 1h target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 08:54:40 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.5701032130575072e-09, 'circular_shift': 3.5701032130575072e-09, 'fourier_phase': 3.5701032130575072e-09, 'row_shuffle': 3.5701032130575072e-09} passed=False

## [INFO] 2026-08-02 08:55:23 UTC (tier 0)

trial `b643ad73-1caa-4d9f-a67d-f138741766ac` model=hist_mean tier=0 pf=0.000 trades=0 gates=FAIL

## [INFO] 2026-08-02 08:55:25 UTC (tier 0)

trial `8f441e41-4279-4577-8ce9-080fb69c56bf` model=ridge tier=0 pf=0.802 trades=14771 gates=FAIL

## [INFO] 2026-08-02 09:07:55 UTC (tier 0)

trial `d674d6e4-8d9b-4ade-8a6c-dfb600a924d0` model=lgbm_regressor tier=0 pf=0.729 trades=12986 gates=FAIL

## [INFO] 2026-08-02 09:12:42 UTC (tier 0)

AUTONOMY start 162 combos (non-directional targets first)

## [INFO] 2026-08-02 09:12:42 UTC (tier 0)

START gen=auto_000_BTCUSDT_1h_vol_ratio_ohlcv_v1 BTCUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:12:46 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.795497746267756e-13, 'circular_shift': 9.795497746267756e-13, 'fourier_phase': 9.795497746267756e-13, 'row_shuffle': 9.795497746267756e-13} passed=False

## [INFO] 2026-08-02 09:13:05 UTC (tier 0)

SURROGATE FAIL model=hist_mean mae_s=0.604153

## [ALERT] 2026-08-02 09:13:05 UTC (tier 2)

trial `5c89a8f4-2d57-490f-88ed-a3877c9bf780` model=hist_mean tier=2 pf=2.000 trades=32855 gates=UNKNOWN

## [INFO] 2026-08-02 09:13:06 UTC (tier 0)

SURROGATE FAIL model=ridge mae_s=0.603211

## [ALERT] 2026-08-02 09:13:06 UTC (tier 2)

trial `507e0a13-d60c-4d64-a14d-282f042ad271` model=ridge tier=2 pf=2988.968 trades=32855 gates=UNKNOWN

## [INFO] 2026-08-02 09:19:59 UTC (tier 0)

START gen=verify_vol_ratio BTCUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:20:03 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.795497746267756e-13, 'circular_shift': 9.795497746267756e-13, 'fourier_phase': 9.795497746267756e-13, 'row_shuffle': 9.795497746267756e-13} passed=False

## [INFO] 2026-08-02 09:20:23 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:20:23 UTC (tier 0)

trial `4c85d87b-3544-4199-b2fa-215dbe447c77` model=hist_mean tier=0 pf=1.000 trades=32855 gates=FAIL

## [INFO] 2026-08-02 09:20:24 UTC (tier 0)

trial `a1c1e50b-8c1e-4649-8bdd-2585b8bacc3b` model=ridge tier=0 pf=1.063 trades=32855 gates=FAIL

## [INFO] 2026-08-02 09:20:24 UTC (tier 0)

Hunt complete: {"generation_id": "verify_vol_ratio", "status": "COMPLETE", "n_trials": 2, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:20:24 UTC (tier 0)

START gen=verify_xs_rank BTCUSDT 1h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 09:20:43 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3075096561010469e-11, 'circular_shift': 1.3075096561010469e-11, 'fourier_phase': 1.3075096561010469e-11, 'row_shuffle': 1.3075096561010469e-11} passed=False

## [INFO] 2026-08-02 09:21:11 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:21:12 UTC (tier 0)

trial `e47e74f5-dbab-4e0c-9b1f-d67a628f55a2` model=hist_mean tier=0 pf=0.723 trades=32855 gates=FAIL

## [INFO] 2026-08-02 09:21:13 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00348 skill_surrogate=-0.00074

## [INFO] 2026-08-02 09:21:13 UTC (tier 0)

trial `5c58d1a4-9e25-4675-9bbb-1fc91227e4d7` model=ridge tier=0 pf=0.712 trades=32394 gates=FAIL

## [INFO] 2026-08-02 09:21:13 UTC (tier 0)

Hunt complete: {"generation_id": "verify_xs_rank", "status": "COMPLETE", "n_trials": 2, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:22:26 UTC (tier 0)

AUTONOMY start 162 combos (non-directional targets first)

## [INFO] 2026-08-02 09:22:26 UTC (tier 0)

START gen=auto_000_BTCUSDT_1h_vol_ratio_ohlcv_v1 BTCUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:22:31 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.795497746267756e-13, 'circular_shift': 9.795497746267756e-13, 'fourier_phase': 9.795497746267756e-13, 'row_shuffle': 9.795497746267756e-13} passed=False

## [INFO] 2026-08-02 09:22:40 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:22:40 UTC (tier 0)

trial `d23aae27-b3dd-44c7-bfdc-3751b35732d9` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:22:41 UTC (tier 0)

trial `6d8ac13c-e17d-4ac3-93bf-8cfb3e59c606` model=ridge tier=0 target=vol_ratio skill=1.063 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:23:29 UTC (tier 0)

trial `e893e79a-494e-4121-a356-0f6afb4e82f6` model=lgbm_regressor tier=0 target=vol_ratio skill=1.129 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:23:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06290 skill_surrogate=+0.06290

## [INFO] 2026-08-02 09:23:32 UTC (tier 0)

trial `417ea104-3e06-46c3-9dea-16393cec4074` model=lgbm_classifier tier=0 target=vol_ratio skill=1.060 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:23:32 UTC (tier 0)

Hunt complete: {"generation_id": "auto_000_BTCUSDT_1h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:23:32 UTC (tier 0)

AUTONOMY screen auto_000_BTCUSDT_1h_vol_ratio_ohlcv_v1 tier=0 proxy_pf=1.1287881645516609 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:23:32 UTC (tier 0)

START gen=auto_001_BTCUSDT_1h_vol_ratio_indicators_v1 BTCUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 09:23:38 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.788836408120005e-13, 'circular_shift': 9.788836408120005e-13, 'fourier_phase': 9.788836408120005e-13, 'row_shuffle': 9.788836408120005e-13} passed=False

## [INFO] 2026-08-02 09:23:51 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:23:51 UTC (tier 0)

trial `bd9e5cf1-fb69-4314-b82f-da58076a7b4e` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:23:53 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01111 skill_surrogate=-0.01347

## [INFO] 2026-08-02 09:23:53 UTC (tier 0)

trial `f979e092-9bf3-49a2-8b49-eee21ab61f46` model=ridge tier=0 target=vol_ratio skill=1.065 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:24:40 UTC (tier 0)

trial `0f52b132-14bf-4fb6-a0e2-d615e8e0119e` model=lgbm_regressor tier=0 target=vol_ratio skill=1.002 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:24:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06305 skill_surrogate=+0.06305

## [INFO] 2026-08-02 09:24:43 UTC (tier 0)

trial `7a723690-42b2-4e26-ac11-25c9c1462ee9` model=lgbm_classifier tier=0 target=vol_ratio skill=1.060 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:24:43 UTC (tier 0)

Hunt complete: {"generation_id": "auto_001_BTCUSDT_1h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:24:43 UTC (tier 0)

AUTONOMY screen auto_001_BTCUSDT_1h_vol_ratio_indicators_v1 tier=0 proxy_pf=1.0654752580145348 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:24:43 UTC (tier 0)

START gen=auto_002_BTCUSDT_1h_vol_ratio_pivot_v1 BTCUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 09:24:45 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.802159084415507e-13, 'circular_shift': 9.802159084415507e-13, 'fourier_phase': 9.802159084415507e-13, 'row_shuffle': 9.802159084415507e-13} passed=False

## [INFO] 2026-08-02 09:24:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:24:55 UTC (tier 0)

trial `e4d894a0-24e3-4982-bffb-7386d7fa0df0` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:24:55 UTC (tier 0)

trial `04d4056a-a6ed-4751-9841-7b7740508bf7` model=ridge tier=0 target=vol_ratio skill=1.107 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:25:22 UTC (tier 0)

trial `8b118050-e444-4eba-a5ca-3d43f5528eb8` model=lgbm_regressor tier=0 target=vol_ratio skill=1.116 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:25:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06281 skill_surrogate=+0.06281

## [INFO] 2026-08-02 09:25:23 UTC (tier 0)

trial `f27b75fd-72ee-46b8-9604-6c4be56ae8c6` model=lgbm_classifier tier=0 target=vol_ratio skill=1.059 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:25:23 UTC (tier 0)

Hunt complete: {"generation_id": "auto_002_BTCUSDT_1h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:25:23 UTC (tier 0)

AUTONOMY screen auto_002_BTCUSDT_1h_vol_ratio_pivot_v1 tier=0 proxy_pf=1.116215847766803 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:25:23 UTC (tier 0)

START gen=auto_003_ETHUSDT_1h_vol_ratio_ohlcv_v1 ETHUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:25:27 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.472044708350495e-12, 'circular_shift': 1.472044708350495e-12, 'fourier_phase': 1.472044708350495e-12, 'row_shuffle': 1.472044708350495e-12} passed=False

## [INFO] 2026-08-02 09:25:47 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:25:47 UTC (tier 0)

trial `f506835b-d20d-4c33-876d-9309521d52b4` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:25:48 UTC (tier 0)

trial `655591ed-b4e7-44ce-97cc-a530e1f5d0c2` model=ridge tier=0 target=vol_ratio skill=1.053 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:26:04 UTC (tier 0)

trial `72cdae0b-bc64-42bc-b1db-a4b00c0e91bb` model=lgbm_regressor tier=0 target=vol_ratio skill=1.103 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:26:05 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05804 skill_surrogate=+0.05804

## [INFO] 2026-08-02 09:26:05 UTC (tier 0)

trial `bee8a6ac-7617-4161-8303-3cc0c3f4b9e6` model=lgbm_classifier tier=0 target=vol_ratio skill=1.054 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:26:05 UTC (tier 0)

Hunt complete: {"generation_id": "auto_003_ETHUSDT_1h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:26:05 UTC (tier 0)

AUTONOMY screen auto_003_ETHUSDT_1h_vol_ratio_ohlcv_v1 tier=0 proxy_pf=1.103409254981764 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:26:05 UTC (tier 0)

START gen=auto_004_ETHUSDT_1h_vol_ratio_indicators_v1 ETHUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 09:26:08 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.4707124407209449e-12, 'circular_shift': 1.4707124407209449e-12, 'fourier_phase': 1.4707124407209449e-12, 'row_shuffle': 1.4707124407209449e-12} passed=False

## [INFO] 2026-08-02 09:26:14 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:26:14 UTC (tier 0)

trial `c72f0f51-f903-4c7e-8274-590bc09abb8d` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:26:15 UTC (tier 0)

trial `04e10119-660d-40f5-893f-14e378e147c2` model=ridge tier=0 target=vol_ratio skill=1.089 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:26:35 UTC (tier 0)

trial `94e609c9-06fa-4161-b451-f33d71a8b081` model=lgbm_regressor tier=0 target=vol_ratio skill=0.978 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:26:37 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05813 skill_surrogate=+0.05813

## [INFO] 2026-08-02 09:26:37 UTC (tier 0)

trial `8a84206f-394b-4eef-8062-60e8619a45f6` model=lgbm_classifier tier=0 target=vol_ratio skill=1.054 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:26:37 UTC (tier 0)

Hunt complete: {"generation_id": "auto_004_ETHUSDT_1h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:26:37 UTC (tier 0)

AUTONOMY screen auto_004_ETHUSDT_1h_vol_ratio_indicators_v1 tier=0 proxy_pf=1.0890694563877426 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:26:37 UTC (tier 0)

START gen=auto_005_ETHUSDT_1h_vol_ratio_pivot_v1 ETHUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 09:26:39 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.47226675295542e-12, 'circular_shift': 1.47226675295542e-12, 'fourier_phase': 1.47226675295542e-12, 'row_shuffle': 1.47226675295542e-12} passed=False

## [INFO] 2026-08-02 09:26:45 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 09:26:45 UTC (tier 0)

trial `6dca9ce6-5b7a-4bcc-9827-827190364bdb` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:26:45 UTC (tier 0)

trial `76c6536a-aff7-41fd-824e-b8fba84aece7` model=ridge tier=0 target=vol_ratio skill=1.109 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:26:55 UTC (tier 0)

trial `16d5bc35-bfa8-44a8-9a50-ae9ba2642108` model=lgbm_regressor tier=0 target=vol_ratio skill=1.121 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:26:56 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05777 skill_surrogate=+0.05777

## [INFO] 2026-08-02 09:26:56 UTC (tier 0)

trial `b7dec022-3f4e-4e61-a32d-5cd97b6fe718` model=lgbm_classifier tier=0 target=vol_ratio skill=1.053 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:26:56 UTC (tier 0)

Hunt complete: {"generation_id": "auto_005_ETHUSDT_1h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:26:56 UTC (tier 0)

AUTONOMY screen auto_005_ETHUSDT_1h_vol_ratio_pivot_v1 tier=0 proxy_pf=1.1207453579891 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:26:56 UTC (tier 0)

START gen=auto_006_SOLUSDT_1h_vol_ratio_ohlcv_v1 SOLUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:26:59 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.7901236049056024e-12, 'circular_shift': 1.7901236049056024e-12, 'fourier_phase': 1.7901236049056024e-12, 'row_shuffle': 1.7901236049056024e-12} passed=False

## [INFO] 2026-08-02 09:27:18 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:27:18 UTC (tier 0)

trial `fc05561e-7119-46a2-8fa8-df852057e220` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:27:19 UTC (tier 0)

trial `3f99834e-f74d-485f-9eb6-4f426aaa9dc8` model=ridge tier=0 target=vol_ratio skill=1.033 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:28:03 UTC (tier 0)

RETRACTION - the two [ALERT] tier 2 entries at 2026-08-02 09:13:05 and 09:13:06 (trials 5c89a8f4 hist_mean pf=2.000 and 507e0a13 ridge pf=2988.968, gen auto_000_BTCUSDT_1h_vol_ratio_ohlcv_v1) are WITHDRAWN. They are scoring artefacts, not candidates: the proxy computed side*y-cost on vol_ratio, which is positive by construction, so every bar was a winning long and even a constant predictor scored above 1.0. Fixed by target-family routing (DECISIONS D-004) and by capping tier at 0 when the surrogate screen fails (D-005). Re-checked after the fix: tier 0. No tier>=2 candidate has ever been observed in LLM2.

## [INFO] 2026-08-02 09:28:21 UTC (tier 0)

trial `038dc3e8-4cf8-4f8d-88a2-38f181124b4c` model=lgbm_regressor tier=0 target=vol_ratio skill=1.028 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:28:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04932 skill_surrogate=+0.04932

## [INFO] 2026-08-02 09:28:23 UTC (tier 0)

trial `677e0035-f153-4ab8-80d6-0e27802bdd6a` model=lgbm_classifier tier=0 target=vol_ratio skill=1.046 n=32855 gates=FAIL

## [INFO] 2026-08-02 09:28:23 UTC (tier 0)

Hunt complete: {"generation_id": "auto_006_SOLUSDT_1h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:28:23 UTC (tier 0)

AUTONOMY screen auto_006_SOLUSDT_1h_vol_ratio_ohlcv_v1 tier=0 proxy_pf=1.0458746760359234 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:28:23 UTC (tier 0)

START gen=auto_007_SOLUSDT_1h_vol_ratio_indicators_v1 SOLUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 09:28:28 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.7882362257637396e-12, 'circular_shift': 1.7882362257637396e-12, 'fourier_phase': 1.7882362257637396e-12, 'row_shuffle': 1.7882362257637396e-12} passed=False

## [INFO] 2026-08-02 09:28:38 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 09:28:38 UTC (tier 0)

trial `d8cc8249-a177-4112-bc13-a75b695ab912` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:28:38 UTC (tier 0)

trial `56e9c718-7764-41b5-8f37-38907b93d679` model=ridge tier=0 target=vol_ratio skill=1.044 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:29:04 UTC (tier 0)

trial `55644369-07ee-43e5-81bf-159d93bb4fea` model=lgbm_regressor tier=0 target=vol_ratio skill=0.890 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:29:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04937 skill_surrogate=+0.04937

## [INFO] 2026-08-02 09:29:06 UTC (tier 0)

trial `969cca7c-ecd9-4882-8275-5c2031b3d18d` model=lgbm_classifier tier=0 target=vol_ratio skill=1.046 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:29:06 UTC (tier 0)

Hunt complete: {"generation_id": "auto_007_SOLUSDT_1h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:29:06 UTC (tier 0)

AUTONOMY screen auto_007_SOLUSDT_1h_vol_ratio_indicators_v1 tier=0 proxy_pf=1.0459545582059804 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:29:06 UTC (tier 0)

START gen=auto_008_SOLUSDT_1h_vol_ratio_pivot_v1 SOLUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 09:29:08 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.7897905379982149e-12, 'circular_shift': 1.7897905379982149e-12, 'fourier_phase': 1.7897905379982149e-12, 'row_shuffle': 1.7897905379982149e-12} passed=False

## [INFO] 2026-08-02 09:29:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:29:16 UTC (tier 0)

trial `a0fa8cc5-47ec-497d-8932-8d7c4af321a5` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:29:17 UTC (tier 0)

trial `0cb4f59b-be23-40a0-a57b-14bfad93f997` model=ridge tier=0 target=vol_ratio skill=1.089 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:29:38 UTC (tier 0)

trial `7a5812b9-5fc0-4d4d-8324-32c1bd9e5591` model=lgbm_regressor tier=0 target=vol_ratio skill=1.104 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:29:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04920 skill_surrogate=+0.04920

## [INFO] 2026-08-02 09:29:39 UTC (tier 0)

trial `cda34566-6a18-4f8d-b6f4-d87a470fc53b` model=lgbm_classifier tier=0 target=vol_ratio skill=1.046 n=32856 gates=FAIL

## [INFO] 2026-08-02 09:29:39 UTC (tier 0)

Hunt complete: {"generation_id": "auto_008_SOLUSDT_1h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:29:39 UTC (tier 0)

AUTONOMY screen auto_008_SOLUSDT_1h_vol_ratio_pivot_v1 tier=0 proxy_pf=1.1038453941790123 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:29:39 UTC (tier 0)

START gen=auto_009_BTCUSDT_4h_vol_ratio_ohlcv_v1 BTCUSDT 4h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:29:41 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.4648282586904315e-12, 'circular_shift': 1.4648282586904315e-12, 'fourier_phase': 1.4648282586904315e-12, 'row_shuffle': 1.4648282586904315e-12} passed=False

## [INFO] 2026-08-02 09:29:45 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:29:45 UTC (tier 0)

trial `bcc5a4ec-3f12-4418-a567-48b0da67c5e5` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:29:45 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00585 skill_surrogate=-0.00060

## [INFO] 2026-08-02 09:29:45 UTC (tier 0)

trial `f5c4a992-1d8d-479e-afe5-98e7888a7594` model=ridge tier=0 target=vol_ratio skill=1.021 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:30:01 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01273 skill_surrogate=-0.00969

## [INFO] 2026-08-02 09:30:01 UTC (tier 0)

trial `498164c8-64d6-4994-8255-acddc9d29efa` model=lgbm_regressor tier=0 target=vol_ratio skill=1.041 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:30:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05352 skill_surrogate=+0.05352

## [INFO] 2026-08-02 09:30:02 UTC (tier 0)

trial `c9a7bb81-f2b1-412f-91bf-c4ad541169c1` model=lgbm_classifier tier=0 target=vol_ratio skill=1.059 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:30:02 UTC (tier 0)

Hunt complete: {"generation_id": "auto_009_BTCUSDT_4h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:30:02 UTC (tier 0)

AUTONOMY screen auto_009_BTCUSDT_4h_vol_ratio_ohlcv_v1 tier=0 proxy_pf=1.058917175717542 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:30:02 UTC (tier 0)

START gen=auto_010_BTCUSDT_4h_vol_ratio_indicators_v1 BTCUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 09:30:04 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.478039912683471e-12, 'circular_shift': 1.478039912683471e-12, 'fourier_phase': 1.478039912683471e-12, 'row_shuffle': 1.478039912683471e-12} passed=False

## [INFO] 2026-08-02 09:30:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:30:08 UTC (tier 0)

trial `12fce9ac-0fa4-4a9a-bb91-5d39cf8ec067` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:30:08 UTC (tier 0)

trial `f1d08f5d-09d6-43be-9219-1c40d8873f2d` model=ridge tier=0 target=vol_ratio skill=1.056 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:30:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.71588 skill_surrogate=-0.03184

## [INFO] 2026-08-02 09:30:32 UTC (tier 0)

trial `5990c684-a1b7-4296-bf1a-490e3a5a163d` model=lgbm_regressor tier=0 target=vol_ratio skill=0.707 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:30:33 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05113 skill_surrogate=+0.05113

## [INFO] 2026-08-02 09:30:33 UTC (tier 0)

trial `d19dac3c-4d85-4d69-9d30-5ca7bb1274d9` model=lgbm_classifier tier=0 target=vol_ratio skill=1.056 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:30:33 UTC (tier 0)

Hunt complete: {"generation_id": "auto_010_BTCUSDT_4h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:30:33 UTC (tier 0)

AUTONOMY screen auto_010_BTCUSDT_4h_vol_ratio_indicators_v1 tier=0 proxy_pf=1.0555832731547092 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:30:33 UTC (tier 0)

START gen=auto_011_BTCUSDT_4h_vol_ratio_pivot_v1 BTCUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 09:30:34 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.4678258608569195e-12, 'circular_shift': 1.4678258608569195e-12, 'fourier_phase': 1.4678258608569195e-12, 'row_shuffle': 1.4678258608569195e-12} passed=False

## [INFO] 2026-08-02 09:30:37 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:30:37 UTC (tier 0)

trial `51e92415-27e7-4eb5-bd75-74657155c8ff` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:30:37 UTC (tier 0)

trial `e6b2a925-b5d8-416e-a7d5-0d4df5618942` model=ridge tier=0 target=vol_ratio skill=1.037 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:32:00 UTC (tier 0)

trial `0f372213-c96a-4ab2-912d-ac8666eea10e` model=lgbm_regressor tier=0 target=vol_ratio skill=1.018 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:32:01 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05321 skill_surrogate=+0.05321

## [INFO] 2026-08-02 09:32:01 UTC (tier 0)

trial `eb842788-f396-4111-97c5-720c0d98a5bc` model=lgbm_classifier tier=0 target=vol_ratio skill=1.058 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:32:01 UTC (tier 0)

Hunt complete: {"generation_id": "auto_011_BTCUSDT_4h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:32:01 UTC (tier 0)

AUTONOMY screen auto_011_BTCUSDT_4h_vol_ratio_pivot_v1 tier=0 proxy_pf=1.0584943492689187 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:32:01 UTC (tier 0)

START gen=auto_012_ETHUSDT_4h_vol_ratio_ohlcv_v1 ETHUSDT 4h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:32:03 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.5226708782734022e-12, 'circular_shift': 1.5226708782734022e-12, 'fourier_phase': 1.5226708782734022e-12, 'row_shuffle': 1.5226708782734022e-12} passed=False

## [INFO] 2026-08-02 09:32:07 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 09:32:07 UTC (tier 0)

trial `98d6bb10-cbed-4a89-9b3d-c05a32750c78` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:32:07 UTC (tier 0)

trial `7760b817-f32b-413a-9866-69b88e9f63c6` model=ridge tier=0 target=vol_ratio skill=1.058 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:32:26 UTC (tier 0)

trial `674679f6-3e58-4d5d-bab8-518844dacd6c` model=lgbm_regressor tier=0 target=vol_ratio skill=0.993 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:32:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06059 skill_surrogate=+0.06059

## [INFO] 2026-08-02 09:32:27 UTC (tier 0)

trial `01dac75f-23fe-47c7-b20d-4a9d4f6f4321` model=lgbm_classifier tier=0 target=vol_ratio skill=1.058 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:32:27 UTC (tier 0)

Hunt complete: {"generation_id": "auto_012_ETHUSDT_4h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:32:27 UTC (tier 0)

AUTONOMY screen auto_012_ETHUSDT_4h_vol_ratio_ohlcv_v1 tier=0 proxy_pf=1.0580094881335798 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:32:27 UTC (tier 0)

START gen=auto_013_ETHUSDT_4h_vol_ratio_indicators_v1 ETHUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 09:32:30 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.5186740753847516e-12, 'circular_shift': 1.5186740753847516e-12, 'fourier_phase': 1.5186740753847516e-12, 'row_shuffle': 1.5186740753847516e-12} passed=False

## [INFO] 2026-08-02 09:32:33 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:32:33 UTC (tier 0)

trial `2adeb4f0-50e8-4743-af9b-69f165e71c4d` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:32:34 UTC (tier 0)

trial `c7197087-106e-4545-b468-55843e2803b8` model=ridge tier=0 target=vol_ratio skill=1.105 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:36:02 UTC (tier 0)

trial `e2e3499f-f200-4605-8dec-0baaee45a687` model=lgbm_regressor tier=0 target=vol_ratio skill=0.922 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:36:03 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06086 skill_surrogate=+0.06086

## [INFO] 2026-08-02 09:36:03 UTC (tier 0)

trial `b61faffa-27f2-41be-adf3-ad5ebef822f9` model=lgbm_classifier tier=0 target=vol_ratio skill=1.058 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:36:03 UTC (tier 0)

Hunt complete: {"generation_id": "auto_013_ETHUSDT_4h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:36:04 UTC (tier 0)

AUTONOMY screen auto_013_ETHUSDT_4h_vol_ratio_indicators_v1 tier=0 proxy_pf=1.105217771789115 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:36:04 UTC (tier 0)

START gen=auto_014_ETHUSDT_4h_vol_ratio_pivot_v1 ETHUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 09:36:05 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.5240031459029524e-12, 'circular_shift': 1.5240031459029524e-12, 'fourier_phase': 1.5240031459029524e-12, 'row_shuffle': 1.5240031459029524e-12} passed=False

## [INFO] 2026-08-02 09:36:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:36:12 UTC (tier 0)

trial `1c185985-5de6-479a-b5e1-f6f79812064d` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:36:12 UTC (tier 0)

trial `298d01cb-245e-4e89-9d2b-8533b6eb6e2a` model=ridge tier=0 target=vol_ratio skill=1.081 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:38:55 UTC (tier 0)

trial `86d74f5a-fecc-4c92-8dfc-8e17c81dca76` model=lgbm_regressor tier=0 target=vol_ratio skill=1.058 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:38:56 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05969 skill_surrogate=+0.05969

## [INFO] 2026-08-02 09:38:56 UTC (tier 0)

trial `9903c077-f7d5-4099-9497-709aad0398a4` model=lgbm_classifier tier=0 target=vol_ratio skill=1.056 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:38:56 UTC (tier 0)

Hunt complete: {"generation_id": "auto_014_ETHUSDT_4h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:38:56 UTC (tier 0)

AUTONOMY screen auto_014_ETHUSDT_4h_vol_ratio_pivot_v1 tier=0 proxy_pf=1.0812966863479607 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:38:56 UTC (tier 0)

START gen=auto_015_SOLUSDT_4h_vol_ratio_ohlcv_v1 SOLUSDT 4h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:38:58 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.8364199050324714e-12, 'circular_shift': 1.8364199050324714e-12, 'fourier_phase': 1.8364199050324714e-12, 'row_shuffle': 1.8364199050324714e-12} passed=False

## [INFO] 2026-08-02 09:39:05 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:39:05 UTC (tier 0)

trial `05a8e8bd-9773-4379-a282-94ad02ac9b98` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:39:05 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01402 skill_surrogate=+0.00193

## [INFO] 2026-08-02 09:39:05 UTC (tier 0)

trial `effd8b56-dc54-4d00-a043-23d804af4e48` model=ridge tier=0 target=vol_ratio skill=0.992 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:39:21 UTC (tier 0)

trial `07b1a9bb-10e6-4edc-a830-42574419f7b3` model=lgbm_regressor tier=0 target=vol_ratio skill=0.955 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:39:22 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05371 skill_surrogate=+0.05371

## [INFO] 2026-08-02 09:39:22 UTC (tier 0)

trial `5f1f2cbb-d630-4380-af76-93c8c00be240` model=lgbm_classifier tier=0 target=vol_ratio skill=1.068 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:39:22 UTC (tier 0)

Hunt complete: {"generation_id": "auto_015_SOLUSDT_4h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:39:22 UTC (tier 0)

AUTONOMY screen auto_015_SOLUSDT_4h_vol_ratio_ohlcv_v1 tier=0 proxy_pf=1.0677841132194306 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:39:22 UTC (tier 0)

START gen=auto_016_SOLUSDT_4h_vol_ratio_indicators_v1 SOLUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 09:39:25 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.8323120798413584e-12, 'circular_shift': 1.8323120798413584e-12, 'fourier_phase': 1.8323120798413584e-12, 'row_shuffle': 1.8323120798413584e-12} passed=False

## [INFO] 2026-08-02 09:39:28 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:39:28 UTC (tier 0)

trial `bbc59333-69f2-4111-8e06-0fc01c23b61c` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:39:29 UTC (tier 0)

trial `74577f3d-ca82-4e37-9006-4cd19a300334` model=ridge tier=0 target=vol_ratio skill=0.988 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:39:50 UTC (tier 0)

trial `27d9c164-72f9-4ca7-b73d-10f5f8ba4299` model=lgbm_regressor tier=0 target=vol_ratio skill=0.912 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:39:51 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05435 skill_surrogate=+0.05435

## [INFO] 2026-08-02 09:39:51 UTC (tier 0)

trial `ee15a97f-d5e0-4f5a-8f9f-b89219ceaffb` model=lgbm_classifier tier=0 target=vol_ratio skill=1.069 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:39:51 UTC (tier 0)

Hunt complete: {"generation_id": "auto_016_SOLUSDT_4h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:39:51 UTC (tier 0)

AUTONOMY screen auto_016_SOLUSDT_4h_vol_ratio_indicators_v1 tier=0 proxy_pf=1.0692300072789345 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:39:51 UTC (tier 0)

START gen=auto_017_SOLUSDT_4h_vol_ratio_pivot_v1 SOLUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 09:39:56 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.8381962618718717e-12, 'circular_shift': 1.8381962618718717e-12, 'fourier_phase': 1.8381962618718717e-12, 'row_shuffle': 1.8381962618718717e-12} passed=False

## [INFO] 2026-08-02 09:40:02 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:40:02 UTC (tier 0)

trial `eef06e39-7097-4f24-b450-332e31b6c43c` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:40:02 UTC (tier 0)

trial `9563b6de-de2e-415d-94af-ff88c8c323a8` model=ridge tier=0 target=vol_ratio skill=1.048 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:40:17 UTC (tier 0)

trial `d1cd7a86-c1a5-43be-85ca-e3fd2397316e` model=lgbm_regressor tier=0 target=vol_ratio skill=1.037 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:40:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05235 skill_surrogate=+0.05235

## [INFO] 2026-08-02 09:40:18 UTC (tier 0)

trial `7c2dcccd-dfdc-4da8-8780-0bdde67421e1` model=lgbm_classifier tier=0 target=vol_ratio skill=1.065 n=8214 gates=FAIL

## [INFO] 2026-08-02 09:40:18 UTC (tier 0)

Hunt complete: {"generation_id": "auto_017_SOLUSDT_4h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:40:18 UTC (tier 0)

AUTONOMY screen auto_017_SOLUSDT_4h_vol_ratio_pivot_v1 tier=0 proxy_pf=1.0648410231263934 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:40:18 UTC (tier 0)

START gen=auto_018_BTCUSDT_15m_vol_ratio_ohlcv_v1 BTCUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:40:38 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.0050849041931542e-12, 'circular_shift': 1.0050849041931542e-12, 'fourier_phase': 1.0050849041931542e-12, 'row_shuffle': 1.0050849041931542e-12} passed=False

## [INFO] 2026-08-02 09:42:26 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 09:42:26 UTC (tier 0)

trial `a76e6f51-f82c-4d25-ac03-d121915f0cd6` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-02 09:42:30 UTC (tier 0)

trial `6728d99d-8721-4afb-890d-91a0999eccbb` model=ridge tier=0 target=vol_ratio skill=1.073 n=131421 gates=FAIL

## [INFO] 2026-08-02 09:46:35 UTC (tier 0)

trial `fcf9a51a-13e6-4fbc-96a7-207fdb1ce9aa` model=lgbm_regressor tier=0 target=vol_ratio skill=1.151 n=131421 gates=FAIL

## [INFO] 2026-08-02 09:46:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.07156 skill_surrogate=+0.07156

## [INFO] 2026-08-02 09:46:43 UTC (tier 0)

trial `fbc85119-41a4-492f-bedb-6f50524919a8` model=lgbm_classifier tier=0 target=vol_ratio skill=1.069 n=131421 gates=FAIL

## [INFO] 2026-08-02 09:46:43 UTC (tier 0)

Hunt complete: {"generation_id": "auto_018_BTCUSDT_15m_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:46:43 UTC (tier 0)

AUTONOMY screen auto_018_BTCUSDT_15m_vol_ratio_ohlcv_v1 tier=0 proxy_pf=1.1510304051943747 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:46:43 UTC (tier 0)

START gen=auto_019_BTCUSDT_15m_vol_ratio_indicators_v1 BTCUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 09:47:19 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.0049738818906917e-12, 'circular_shift': 1.0049738818906917e-12, 'fourier_phase': 1.0049738818906917e-12, 'row_shuffle': 1.0049738818906917e-12} passed=False

## [INFO] 2026-08-02 09:49:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:49:12 UTC (tier 0)

trial `8fe55595-a5d2-4c38-94ee-a4eb224d52c3` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 09:49:16 UTC (tier 0)

trial `4ba326c3-e916-4be4-bcf6-3976901b2296` model=ridge tier=0 target=vol_ratio skill=1.055 n=131424 gates=FAIL

## [INFO] 2026-08-02 09:51:07 UTC (tier 0)

trial `c5951fca-0b66-4faa-b129-dc163e01e42c` model=lgbm_regressor tier=0 target=vol_ratio skill=0.988 n=131424 gates=FAIL

## [INFO] 2026-08-02 09:51:16 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.07156 skill_surrogate=+0.07156

## [INFO] 2026-08-02 09:51:16 UTC (tier 0)

trial `3a0f2111-f949-481f-b66f-dc37c2f1f1ab` model=lgbm_classifier tier=0 target=vol_ratio skill=1.069 n=131424 gates=FAIL

## [INFO] 2026-08-02 09:51:16 UTC (tier 0)

Hunt complete: {"generation_id": "auto_019_BTCUSDT_15m_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:51:16 UTC (tier 0)

AUTONOMY screen auto_019_BTCUSDT_15m_vol_ratio_indicators_v1 tier=0 proxy_pf=1.0694616787793854 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:51:16 UTC (tier 0)

START gen=auto_020_BTCUSDT_15m_vol_ratio_pivot_v1 BTCUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 09:51:59 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.0049738818906917e-12, 'circular_shift': 1.0049738818906917e-12, 'fourier_phase': 1.0049738818906917e-12, 'row_shuffle': 1.0049738818906917e-12} passed=False

## [INFO] 2026-08-02 09:53:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:53:57 UTC (tier 0)

trial `a900d407-2d4b-43bc-9f2e-15dd31068ed7` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 09:53:59 UTC (tier 0)

trial `a7a8cd90-3e83-4dba-a2e7-75f9e06a8a65` model=ridge tier=0 target=vol_ratio skill=1.098 n=131424 gates=FAIL

## [INFO] 2026-08-02 09:55:16 UTC (tier 0)

trial `7c292e77-9fbc-4c12-b314-7adeec74ba99` model=lgbm_regressor tier=0 target=vol_ratio skill=1.125 n=131424 gates=FAIL

## [INFO] 2026-08-02 09:55:26 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.07154 skill_surrogate=+0.07154

## [INFO] 2026-08-02 09:55:27 UTC (tier 0)

trial `cc860e5c-20de-44e9-93a8-096ef1129ee6` model=lgbm_classifier tier=0 target=vol_ratio skill=1.069 n=131424 gates=FAIL

## [INFO] 2026-08-02 09:55:27 UTC (tier 0)

Hunt complete: {"generation_id": "auto_020_BTCUSDT_15m_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 09:55:27 UTC (tier 0)

AUTONOMY screen auto_020_BTCUSDT_15m_vol_ratio_pivot_v1 tier=0 proxy_pf=1.124786825423441 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 09:55:27 UTC (tier 0)

START gen=auto_021_ETHUSDT_15m_vol_ratio_ohlcv_v1 ETHUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 09:56:15 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.2200240817605845e-12, 'circular_shift': 1.2200240817605845e-12, 'fourier_phase': 1.2200240817605845e-12, 'row_shuffle': 1.2200240817605845e-12} passed=False

## [INFO] 2026-08-02 09:59:59 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 09:59:59 UTC (tier 0)

trial `978cba05-5c9e-4cba-8a55-fcd000f72e6f` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:00:05 UTC (tier 0)

trial `c174ae99-f570-4500-abf8-ac75b08d19a1` model=ridge tier=0 target=vol_ratio skill=1.074 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:01:50 UTC (tier 0)

trial `b19b723e-ec7e-4bc6-9c4f-aa5fe01b7c48` model=lgbm_regressor tier=0 target=vol_ratio skill=1.134 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:02:01 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06668 skill_surrogate=+0.06668

## [INFO] 2026-08-02 10:02:02 UTC (tier 0)

trial `8957b524-e0d3-4a38-99c6-ed487b4e93d5` model=lgbm_classifier tier=0 target=vol_ratio skill=1.057 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:02:02 UTC (tier 0)

Hunt complete: {"generation_id": "auto_021_ETHUSDT_15m_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:02:02 UTC (tier 0)

AUTONOMY screen auto_021_ETHUSDT_15m_vol_ratio_ohlcv_v1 tier=0 proxy_pf=1.1342657671980088 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:02:02 UTC (tier 0)

START gen=auto_022_ETHUSDT_15m_vol_ratio_indicators_v1 ETHUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 10:02:36 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.220135104063047e-12, 'circular_shift': 1.220135104063047e-12, 'fourier_phase': 1.220135104063047e-12, 'row_shuffle': 1.220135104063047e-12} passed=False

## [INFO] 2026-08-02 10:03:56 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:03:56 UTC (tier 0)

trial `4539ca0e-7ea4-4bda-8898-fa76d1e983b2` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:04:00 UTC (tier 0)

trial `3293387e-657b-4813-b821-9afb0b51c0a7` model=ridge tier=0 target=vol_ratio skill=1.091 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:05:06 UTC (tier 0)

trial `6e265064-8b37-459a-a932-deabddd03d47` model=lgbm_regressor tier=0 target=vol_ratio skill=1.012 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:05:41 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06670 skill_surrogate=+0.06670

## [INFO] 2026-08-02 10:05:41 UTC (tier 0)

trial `244b909f-8ee2-44a7-9a12-f9e7dff6b469` model=lgbm_classifier tier=0 target=vol_ratio skill=1.057 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:05:41 UTC (tier 0)

Hunt complete: {"generation_id": "auto_022_ETHUSDT_15m_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:05:41 UTC (tier 0)

AUTONOMY screen auto_022_ETHUSDT_15m_vol_ratio_indicators_v1 tier=0 proxy_pf=1.0907317885110825 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:05:41 UTC (tier 0)

START gen=auto_023_ETHUSDT_15m_vol_ratio_pivot_v1 ETHUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 10:06:00 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.220135104063047e-12, 'circular_shift': 1.220135104063047e-12, 'fourier_phase': 1.220135104063047e-12, 'row_shuffle': 1.220135104063047e-12} passed=False

## [INFO] 2026-08-02 10:06:10 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:06:10 UTC (tier 0)

trial `d488b4a6-20b0-4a8a-840a-916dd7631bea` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:06:12 UTC (tier 0)

trial `aabd4a70-c394-414e-9b8a-96548b5762f0` model=ridge tier=0 target=vol_ratio skill=1.113 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:07:03 UTC (tier 0)

trial `4a5b9618-f9b4-49d4-9b3f-058383660cda` model=lgbm_regressor tier=0 target=vol_ratio skill=1.141 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:07:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06660 skill_surrogate=+0.06660

## [INFO] 2026-08-02 10:07:06 UTC (tier 0)

trial `7dd93952-d8fc-44fb-92c8-0457087eb5f8` model=lgbm_classifier tier=0 target=vol_ratio skill=1.057 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:07:06 UTC (tier 0)

Hunt complete: {"generation_id": "auto_023_ETHUSDT_15m_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:07:06 UTC (tier 0)

AUTONOMY screen auto_023_ETHUSDT_15m_vol_ratio_pivot_v1 tier=0 proxy_pf=1.1409015723741756 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:07:06 UTC (tier 0)

START gen=auto_024_SOLUSDT_15m_vol_ratio_ohlcv_v1 SOLUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 10:07:25 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.66733293838206e-12, 'circular_shift': 1.66733293838206e-12, 'fourier_phase': 1.66733293838206e-12, 'row_shuffle': 1.66733293838206e-12} passed=False

## [INFO] 2026-08-02 10:07:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:07:36 UTC (tier 0)

trial `861f9936-24fd-4435-8a2f-5ad3aac9cc8a` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:07:39 UTC (tier 0)

trial `866a9a24-fad8-4bc0-93a1-d58a66cabd74` model=ridge tier=0 target=vol_ratio skill=1.052 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:09:59 UTC (tier 0)

AUTONOMY start 162 combos (non-directional first; xs_rank→xs_v1)

## [INFO] 2026-08-02 10:10:00 UTC (tier 0)

START gen=auto_025_SOLUSDT_15m_vol_ratio_indicators_v1 SOLUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 10:10:14 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.66733293838206e-12, 'circular_shift': 1.66733293838206e-12, 'fourier_phase': 1.66733293838206e-12, 'row_shuffle': 1.66733293838206e-12} passed=False

## [INFO] 2026-08-02 10:10:35 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 10:10:35 UTC (tier 0)

trial `360abef2-dfec-4441-a20e-77bbf91dfd3e` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:10:38 UTC (tier 0)

trial `357544cb-64d5-4f3c-b044-a315f77d06cc` model=ridge tier=0 target=vol_ratio skill=1.076 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:11:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.15270 skill_surrogate=-0.01579

## [INFO] 2026-08-02 10:11:38 UTC (tier 0)

trial `ccacbdd6-a2e2-415d-91c7-fec76bbe9af7` model=lgbm_regressor tier=0 target=vol_ratio skill=0.966 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:11:48 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04519 skill_surrogate=+0.04519

## [INFO] 2026-08-02 10:11:48 UTC (tier 0)

trial `7a9b5712-b9bd-476a-a1cf-874a40584cea` model=lgbm_classifier tier=0 target=vol_ratio skill=1.045 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:11:48 UTC (tier 0)

Hunt complete: {"generation_id": "auto_025_SOLUSDT_15m_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:11:48 UTC (tier 0)

AUTONOMY screen auto_025_SOLUSDT_15m_vol_ratio_indicators_v1 tier=0 proxy_skill=1.075884630587128 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:11:48 UTC (tier 0)

START gen=auto_026_SOLUSDT_15m_vol_ratio_pivot_v1 SOLUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 10:11:55 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.66733293838206e-12, 'circular_shift': 1.66733293838206e-12, 'fourier_phase': 1.66733293838206e-12, 'row_shuffle': 1.66733293838206e-12} passed=False

## [INFO] 2026-08-02 10:12:06 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:12:06 UTC (tier 0)

trial `b3d0bf2d-e93b-4f90-9633-4ae890a0ef97` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:12:07 UTC (tier 0)

trial `4dbcce42-e761-441e-9a24-7614cabf2da1` model=ridge tier=0 target=vol_ratio skill=1.100 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:12:55 UTC (tier 0)

trial `d1a0def7-2ebc-454a-8c59-554464eac93a` model=lgbm_regressor tier=0 target=vol_ratio skill=1.123 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:12:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04509 skill_surrogate=+0.04509

## [INFO] 2026-08-02 10:12:59 UTC (tier 0)

trial `10a100aa-8e3b-45ea-aec8-457cd8a2ed9d` model=lgbm_classifier tier=0 target=vol_ratio skill=1.045 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:12:59 UTC (tier 0)

Hunt complete: {"generation_id": "auto_026_SOLUSDT_15m_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:13:00 UTC (tier 0)

AUTONOMY screen auto_026_SOLUSDT_15m_vol_ratio_pivot_v1 tier=0 proxy_skill=1.1231874658307415 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:13:00 UTC (tier 0)

START gen=auto_027_BTCUSDT_1h_volatility_ohlcv_v1 BTCUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:13:04 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 7.451705918981588e-10, 'circular_shift': 7.451705918981588e-10, 'fourier_phase': 7.451705918981588e-10, 'row_shuffle': 7.451705918981588e-10} passed=False

## [INFO] 2026-08-02 10:13:26 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:13:26 UTC (tier 0)

trial `522e4f28-3967-4623-b7f3-8d26290c7acd` model=hist_mean tier=0 target=volatility skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:13:27 UTC (tier 0)

trial `f76cc178-f649-43fb-861c-eb10178d5234` model=ridge tier=0 target=volatility skill=1.366 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 10:14:12 UTC (tier 0)

trial `fd31a333-4a67-45c1-827c-3a3b620855a8` model=lgbm_regressor tier=0 target=volatility skill=1.485 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 10:14:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-40.83757 skill_surrogate=-40.83757

## [INFO] 2026-08-02 10:14:14 UTC (tier 0)

trial `ce7ff106-c9fb-44de-9856-940b923617d9` model=lgbm_classifier tier=0 target=volatility skill=0.025 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:14:14 UTC (tier 0)

Hunt complete: {"generation_id": "auto_027_BTCUSDT_1h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:14:14 UTC (tier 0)

AUTONOMY screen auto_027_BTCUSDT_1h_volatility_ohlcv_v1 tier=0 proxy_skill=1.4853096764285245 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:14:14 UTC (tier 0)

START gen=auto_028_BTCUSDT_1h_volatility_indicators_v1 BTCUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:14:19 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 7.446671057564913e-10, 'circular_shift': 7.446671057564913e-10, 'fourier_phase': 7.446671057564913e-10, 'row_shuffle': 7.446671057564913e-10} passed=False

## [INFO] 2026-08-02 10:14:29 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:14:29 UTC (tier 0)

trial `a2e40c5d-5459-4d6d-8295-d8c2f96c71e6` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:14:30 UTC (tier 0)

trial `03b22ce4-86de-4435-a565-288e51d815f4` model=ridge tier=0 target=volatility skill=1.466 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 10:15:02 UTC (tier 0)

trial `962151e2-d300-4fe4-8486-876ac2288d27` model=lgbm_regressor tier=0 target=volatility skill=1.279 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 10:15:05 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-40.81540 skill_surrogate=-40.81540

## [INFO] 2026-08-02 10:15:05 UTC (tier 0)

trial `8410b222-b945-4181-9603-3d211ae19ba7` model=lgbm_classifier tier=0 target=volatility skill=0.025 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:15:05 UTC (tier 0)

Hunt complete: {"generation_id": "auto_028_BTCUSDT_1h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:15:05 UTC (tier 0)

AUTONOMY screen auto_028_BTCUSDT_1h_volatility_indicators_v1 tier=0 proxy_skill=1.4659121912133612 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:15:05 UTC (tier 0)

START gen=auto_029_BTCUSDT_1h_volatility_pivot_v1 BTCUSDT 1h target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:15:08 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 7.456535389138708e-10, 'circular_shift': 7.456535389138708e-10, 'fourier_phase': 7.456535389138708e-10, 'row_shuffle': 7.456535389138708e-10} passed=False

## [INFO] 2026-08-02 10:15:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:15:17 UTC (tier 0)

trial `ab0c91f3-7082-44ed-9787-3d4a63fe50de` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:15:17 UTC (tier 0)

trial `9ab597f4-19d8-474e-ab09-c7e5de805b33` model=ridge tier=0 target=volatility skill=1.008 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 10:15:40 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01818 skill_surrogate=-0.00445

## [INFO] 2026-08-02 10:15:40 UTC (tier 0)

trial `2bc53ed8-0310-49a4-b9e0-470bdd8fa721` model=lgbm_regressor tier=0 target=volatility skill=1.018 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:15:41 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-40.85346 skill_surrogate=-40.85346

## [INFO] 2026-08-02 10:15:41 UTC (tier 0)

trial `afc02c83-af2d-4dbd-8346-44196e6ea1a0` model=lgbm_classifier tier=0 target=volatility skill=0.025 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:15:41 UTC (tier 0)

Hunt complete: {"generation_id": "auto_029_BTCUSDT_1h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:15:41 UTC (tier 0)

AUTONOMY screen auto_029_BTCUSDT_1h_volatility_pivot_v1 tier=0 proxy_skill=1.0179591852924466 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:15:41 UTC (tier 0)

START gen=auto_030_ETHUSDT_1h_volatility_ohlcv_v1 ETHUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:15:45 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.956442868295994e-10, 'circular_shift': 2.956442868295994e-10, 'fourier_phase': 2.956442868295994e-10, 'row_shuffle': 2.956442868295994e-10} passed=False

## [INFO] 2026-08-02 10:16:06 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 10:16:06 UTC (tier 0)

trial `043e9b0f-b009-47be-9d05-68f07acb12a3` model=hist_mean tier=0 target=volatility skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:16:07 UTC (tier 0)

trial `ee659bcc-23fc-48d4-9445-b7e4b044795f` model=ridge tier=0 target=volatility skill=1.408 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 10:16:36 UTC (tier 0)

trial `d960672f-c674-4fb5-b982-b217ef9384bb` model=lgbm_regressor tier=0 target=volatility skill=1.505 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 10:16:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.42057 skill_surrogate=-35.42057

## [INFO] 2026-08-02 10:16:39 UTC (tier 0)

trial `6644d784-f627-4865-bb44-0584886680a9` model=lgbm_classifier tier=0 target=volatility skill=0.033 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:16:39 UTC (tier 0)

Hunt complete: {"generation_id": "auto_030_ETHUSDT_1h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:16:39 UTC (tier 0)

AUTONOMY screen auto_030_ETHUSDT_1h_volatility_ohlcv_v1 tier=0 proxy_skill=1.5051713954550512 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:16:39 UTC (tier 0)

START gen=auto_031_ETHUSDT_1h_volatility_indicators_v1 ETHUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:16:43 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.954112510167306e-10, 'circular_shift': 2.954112510167306e-10, 'fourier_phase': 2.954112510167306e-10, 'row_shuffle': 2.954112510167306e-10} passed=False

## [INFO] 2026-08-02 10:16:54 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:16:54 UTC (tier 0)

trial `702b4ee6-5109-4179-a2f9-81c93001e8b0` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:16:55 UTC (tier 0)

trial `5180791b-70b7-4544-9f78-e8e579b927ad` model=ridge tier=0 target=volatility skill=1.490 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 10:17:38 UTC (tier 0)

trial `1a51cf4d-fdc0-4ec8-a8e3-ec0fada7e05c` model=lgbm_regressor tier=0 target=volatility skill=1.308 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 10:17:42 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.41141 skill_surrogate=-35.41141

## [INFO] 2026-08-02 10:17:42 UTC (tier 0)

trial `58b35aaf-6797-4ee0-87a2-77f0f928ffb1` model=lgbm_classifier tier=0 target=volatility skill=0.033 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:17:42 UTC (tier 0)

Hunt complete: {"generation_id": "auto_031_ETHUSDT_1h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:17:42 UTC (tier 0)

AUTONOMY screen auto_031_ETHUSDT_1h_volatility_indicators_v1 tier=0 proxy_skill=1.4899209735588588 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:17:42 UTC (tier 0)

START gen=auto_032_ETHUSDT_1h_volatility_pivot_v1 ETHUSDT 1h target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:17:44 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.9579028115733763e-10, 'circular_shift': 2.9579028115733763e-10, 'fourier_phase': 2.9579028115733763e-10, 'row_shuffle': 2.9579028115733763e-10} passed=False

## [INFO] 2026-08-02 10:17:54 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:17:54 UTC (tier 0)

trial `bedd3702-6750-4f7f-958b-8eb879ff0478` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:17:54 UTC (tier 0)

trial `5b02abd5-c2f1-42e2-924d-9871f692b06b` model=ridge tier=0 target=volatility skill=0.992 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:18:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01743 skill_surrogate=-0.00568

## [INFO] 2026-08-02 10:18:11 UTC (tier 0)

trial `1c32fca9-425d-42e3-be9f-25650372a91b` model=lgbm_regressor tier=0 target=volatility skill=0.988 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:18:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.42126 skill_surrogate=-35.42126

## [INFO] 2026-08-02 10:18:12 UTC (tier 0)

trial `e55ab81f-c004-4839-8032-05991a051231` model=lgbm_classifier tier=0 target=volatility skill=0.033 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:18:12 UTC (tier 0)

Hunt complete: {"generation_id": "auto_032_ETHUSDT_1h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:18:12 UTC (tier 0)

AUTONOMY screen auto_032_ETHUSDT_1h_volatility_pivot_v1 tier=0 proxy_skill=1.0 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:18:12 UTC (tier 0)

START gen=auto_033_SOLUSDT_1h_volatility_ohlcv_v1 SOLUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:18:15 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.1326818089306698e-10, 'circular_shift': 2.1326818089306698e-10, 'fourier_phase': 2.1326818089306698e-10, 'row_shuffle': 2.1326818089306698e-10} passed=False

## [INFO] 2026-08-02 10:18:24 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:18:24 UTC (tier 0)

trial `4def86fc-c9f6-4fbc-9baa-c41df1eb927f` model=hist_mean tier=0 target=volatility skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:18:24 UTC (tier 0)

trial `e4c13f26-c04d-4074-9275-6f68202d709e` model=ridge tier=0 target=volatility skill=1.580 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 10:18:46 UTC (tier 0)

trial `44112d47-6fef-4a4f-a4e1-1c763786a44b` model=lgbm_regressor tier=0 target=volatility skill=1.596 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 10:18:49 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-22.15869 skill_surrogate=-22.15869

## [INFO] 2026-08-02 10:18:49 UTC (tier 0)

trial `345d5ea2-6bb5-4c21-987f-eb85d23e8d09` model=lgbm_classifier tier=0 target=volatility skill=0.054 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:18:49 UTC (tier 0)

Hunt complete: {"generation_id": "auto_033_SOLUSDT_1h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:18:49 UTC (tier 0)

AUTONOMY screen auto_033_SOLUSDT_1h_volatility_ohlcv_v1 tier=0 proxy_skill=1.595746376466047 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:18:49 UTC (tier 0)

START gen=auto_034_SOLUSDT_1h_volatility_indicators_v1 SOLUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:18:55 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.136081311832072e-10, 'circular_shift': 2.136081311832072e-10, 'fourier_phase': 2.136081311832072e-10, 'row_shuffle': 2.136081311832072e-10} passed=False

## [INFO] 2026-08-02 10:19:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:19:04 UTC (tier 0)

trial `9b5e18d3-2a2a-48dc-a50c-456b0335a122` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:19:05 UTC (tier 0)

trial `4d717ca2-22fa-4c15-84ca-3b50e54cd558` model=ridge tier=0 target=volatility skill=1.569 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 10:19:34 UTC (tier 0)

trial `fc60d8d7-5d26-4a2c-a421-878df3266d80` model=lgbm_regressor tier=0 target=volatility skill=1.246 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 10:19:36 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-22.20659 skill_surrogate=-22.20659

## [INFO] 2026-08-02 10:19:36 UTC (tier 0)

trial `9d7d67e5-75ea-4beb-9c13-97c4d3ad301a` model=lgbm_classifier tier=0 target=volatility skill=0.054 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:19:36 UTC (tier 0)

Hunt complete: {"generation_id": "auto_034_SOLUSDT_1h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:19:36 UTC (tier 0)

AUTONOMY screen auto_034_SOLUSDT_1h_volatility_indicators_v1 tier=0 proxy_skill=1.5693395431819315 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:19:36 UTC (tier 0)

START gen=auto_035_SOLUSDT_1h_volatility_pivot_v1 SOLUSDT 1h target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:19:38 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.1275647910101725e-10, 'circular_shift': 2.1275647910101725e-10, 'fourier_phase': 2.1275647910101725e-10, 'row_shuffle': 2.1275647910101725e-10} passed=False

## [INFO] 2026-08-02 10:19:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:19:46 UTC (tier 0)

trial `5dd357bc-8b6d-4637-8821-d4ad053a9ce5` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:19:46 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00323 skill_surrogate=-0.00203

## [INFO] 2026-08-02 10:19:46 UTC (tier 0)

trial `24e8a2e1-65ee-4bd9-b4b2-3c313c8d22bc` model=ridge tier=0 target=volatility skill=1.005 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 10:20:01 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02000 skill_surrogate=-0.00177

## [INFO] 2026-08-02 10:20:01 UTC (tier 0)

trial `ab296b37-bb3a-449a-8525-0931e6440798` model=lgbm_regressor tier=0 target=volatility skill=0.997 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:20:01 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-22.11338 skill_surrogate=-22.11338

## [INFO] 2026-08-02 10:20:01 UTC (tier 0)

trial `cb180097-dd87-4b62-bf06-9f39b693e1d0` model=lgbm_classifier tier=0 target=volatility skill=0.054 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:20:01 UTC (tier 0)

Hunt complete: {"generation_id": "auto_035_SOLUSDT_1h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:20:01 UTC (tier 0)

AUTONOMY screen auto_035_SOLUSDT_1h_volatility_pivot_v1 tier=0 proxy_skill=1.004751764657602 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:20:01 UTC (tier 0)

START gen=auto_036_BTCUSDT_4h_volatility_ohlcv_v1 BTCUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:20:03 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.429311196650019e-10, 'circular_shift': 2.429311196650019e-10, 'fourier_phase': 2.429311196650019e-10, 'row_shuffle': 2.429311196650019e-10} passed=False

## [INFO] 2026-08-02 10:20:10 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:20:10 UTC (tier 0)

trial `377cb3c7-96d2-4fcc-b8bc-f6a9e6e594ea` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:20:10 UTC (tier 0)

trial `25810dc6-b6f6-49e5-8a62-c3fbcf8077ac` model=ridge tier=0 target=volatility skill=1.265 n=8214 gates=UNKNOWN

## [INFO] 2026-08-02 10:20:40 UTC (tier 0)

trial `c9407a22-95bc-4b55-82aa-a5c5da8f856f` model=lgbm_regressor tier=0 target=volatility skill=1.285 n=8214 gates=UNKNOWN

## [INFO] 2026-08-02 10:20:42 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-20.13682 skill_surrogate=-20.13682

## [INFO] 2026-08-02 10:20:42 UTC (tier 0)

trial `a5d604e6-a2c0-45fb-9b76-a3ea12bc006c` model=lgbm_classifier tier=0 target=volatility skill=0.049 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:20:42 UTC (tier 0)

Hunt complete: {"generation_id": "auto_036_BTCUSDT_4h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:20:42 UTC (tier 0)

AUTONOMY screen auto_036_BTCUSDT_4h_volatility_ohlcv_v1 tier=0 proxy_skill=1.2845413152826792 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:20:42 UTC (tier 0)

START gen=auto_037_BTCUSDT_4h_volatility_indicators_v1 BTCUSDT 4h target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:20:45 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.435217583141025e-10, 'circular_shift': 2.435217583141025e-10, 'fourier_phase': 2.43521780518563e-10, 'row_shuffle': 2.435217583141025e-10} passed=False

## [INFO] 2026-08-02 10:20:48 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:20:48 UTC (tier 0)

trial `4e9c0a18-b967-4e8e-a884-a6b808fd96f0` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:20:49 UTC (tier 0)

trial `2afeefa3-d2b9-4280-886f-81fd787f4956` model=ridge tier=0 target=volatility skill=1.422 n=8214 gates=UNKNOWN

## [INFO] 2026-08-02 10:21:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.12206 skill_surrogate=-0.06321

## [INFO] 2026-08-02 10:21:12 UTC (tier 0)

trial `791c65f0-e7cf-4119-8ee2-77ec6f14c452` model=lgbm_regressor tier=0 target=volatility skill=0.785 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:21:13 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-20.18784 skill_surrogate=-20.18784

## [INFO] 2026-08-02 10:21:13 UTC (tier 0)

trial `dfe926fa-eb19-4d8e-850c-9fe2ad1dbedd` model=lgbm_classifier tier=0 target=volatility skill=0.049 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:21:13 UTC (tier 0)

Hunt complete: {"generation_id": "auto_037_BTCUSDT_4h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:21:13 UTC (tier 0)

AUTONOMY screen auto_037_BTCUSDT_4h_volatility_indicators_v1 tier=0 proxy_skill=1.422183366648676 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:21:13 UTC (tier 0)

START gen=auto_038_BTCUSDT_4h_volatility_pivot_v1 BTCUSDT 4h target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:21:15 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.432110068895099e-10, 'circular_shift': 2.432110068895099e-10, 'fourier_phase': 2.432110068895099e-10, 'row_shuffle': 2.432110068895099e-10} passed=False

## [INFO] 2026-08-02 10:21:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:21:17 UTC (tier 0)

trial `64f5d0d8-4ea5-4f83-9071-59e5c901038a` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:21:17 UTC (tier 0)

trial `7a763a6c-1e74-48b1-81f0-564bd2d3452b` model=ridge tier=0 target=volatility skill=0.994 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:21:40 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02062 skill_surrogate=-0.01398

## [INFO] 2026-08-02 10:21:40 UTC (tier 0)

trial `2bf3857d-a080-4653-885d-cf0e95e1f002` model=lgbm_regressor tier=0 target=volatility skill=0.980 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:21:40 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-20.20560 skill_surrogate=-20.20560

## [INFO] 2026-08-02 10:21:40 UTC (tier 0)

trial `8cbcbc88-e1bb-429e-88b6-493acef4eb53` model=lgbm_classifier tier=0 target=volatility skill=0.049 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:21:40 UTC (tier 0)

Hunt complete: {"generation_id": "auto_038_BTCUSDT_4h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:21:40 UTC (tier 0)

AUTONOMY screen auto_038_BTCUSDT_4h_volatility_pivot_v1 tier=0 proxy_skill=1.0 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:21:40 UTC (tier 0)

START gen=auto_039_ETHUSDT_4h_volatility_ohlcv_v1 ETHUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:21:42 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.0900969016347517e-10, 'circular_shift': 1.0900969016347517e-10, 'fourier_phase': 1.0900969016347517e-10, 'row_shuffle': 1.0900969016347517e-10} passed=False

## [INFO] 2026-08-02 10:21:47 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:21:47 UTC (tier 0)

trial `6f410289-3a62-4d67-a79e-8d4f03955dc1` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:21:48 UTC (tier 0)

trial `4a7bb432-e3ab-4e0f-8be4-838d923d930a` model=ridge tier=0 target=volatility skill=1.298 n=8214 gates=UNKNOWN

## [INFO] 2026-08-02 10:22:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.08621 skill_surrogate=-0.01717

## [INFO] 2026-08-02 10:22:06 UTC (tier 0)

trial `b9c1ecef-5e3d-4077-afe9-da700c709ba8` model=lgbm_regressor tier=0 target=volatility skill=1.276 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-17.23510 skill_surrogate=-17.23510

## [INFO] 2026-08-02 10:22:07 UTC (tier 0)

trial `e7cfcd4b-93de-4dc0-a034-fd81e56eac3f` model=lgbm_classifier tier=0 target=volatility skill=0.068 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:07 UTC (tier 0)

Hunt complete: {"generation_id": "auto_039_ETHUSDT_4h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:22:07 UTC (tier 0)

AUTONOMY screen auto_039_ETHUSDT_4h_volatility_ohlcv_v1 tier=0 proxy_skill=1.2978023057047012 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:22:07 UTC (tier 0)

START gen=auto_040_ETHUSDT_4h_volatility_indicators_v1 ETHUSDT 4h target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:22:10 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.088019674355678e-10, 'circular_shift': 1.088019674355678e-10, 'fourier_phase': 1.088019674355678e-10, 'row_shuffle': 1.088019674355678e-10} passed=False

## [INFO] 2026-08-02 10:22:14 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:22:14 UTC (tier 0)

trial `bcf0a4a0-7929-4594-a337-1bd7fb4b7c42` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:14 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01814 skill_surrogate=-0.00512

## [INFO] 2026-08-02 10:22:14 UTC (tier 0)

trial `fada0a79-2622-4d8c-9eb7-ff939839aebe` model=ridge tier=0 target=volatility skill=1.316 n=8214 gates=UNKNOWN

## [INFO] 2026-08-02 10:22:30 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.15671 skill_surrogate=-0.04793

## [INFO] 2026-08-02 10:22:30 UTC (tier 0)

trial `5ba40684-1c70-4212-8d7b-89b55feb6b25` model=lgbm_regressor tier=0 target=volatility skill=1.084 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:31 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-17.19931 skill_surrogate=-17.19931

## [INFO] 2026-08-02 10:22:31 UTC (tier 0)

trial `a68fb425-3d43-4504-b6c9-41713d7f1425` model=lgbm_classifier tier=0 target=volatility skill=0.068 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:31 UTC (tier 0)

Hunt complete: {"generation_id": "auto_040_ETHUSDT_4h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:22:31 UTC (tier 0)

AUTONOMY screen auto_040_ETHUSDT_4h_volatility_indicators_v1 tier=0 proxy_skill=1.3159898277040334 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:22:31 UTC (tier 0)

START gen=auto_041_ETHUSDT_4h_volatility_pivot_v1 ETHUSDT 4h target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:22:32 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.0918632664669303e-10, 'circular_shift': 1.0918632664669303e-10, 'fourier_phase': 1.0918632664669303e-10, 'row_shuffle': 1.0918632664669303e-10} passed=False

## [INFO] 2026-08-02 10:22:34 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:22:34 UTC (tier 0)

trial `acf482f1-0e03-42b6-a8ca-51984166fb74` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:34 UTC (tier 0)

trial `eaac336d-fbed-4075-89fb-fda24d76cb65` model=ridge tier=0 target=volatility skill=0.989 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03446 skill_surrogate=-0.01364

## [INFO] 2026-08-02 10:22:44 UTC (tier 0)

trial `652939de-cf0b-4d20-b740-5f66bc42fcac` model=lgbm_regressor tier=0 target=volatility skill=0.939 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-17.26916 skill_surrogate=-17.26916

## [INFO] 2026-08-02 10:22:45 UTC (tier 0)

trial `c4e9dce1-61b9-4bc4-ac11-aede16e52d48` model=lgbm_classifier tier=0 target=volatility skill=0.067 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:45 UTC (tier 0)

Hunt complete: {"generation_id": "auto_041_ETHUSDT_4h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:22:45 UTC (tier 0)

AUTONOMY screen auto_041_ETHUSDT_4h_volatility_pivot_v1 tier=0 proxy_skill=1.0 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:22:45 UTC (tier 0)

START gen=auto_042_SOLUSDT_4h_volatility_ohlcv_v1 SOLUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:22:47 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 6.198186408568063e-11, 'circular_shift': 6.198186408568063e-11, 'fourier_phase': 6.198186408568063e-11, 'row_shuffle': 6.198186408568063e-11} passed=False

## [INFO] 2026-08-02 10:22:54 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:22:54 UTC (tier 0)

trial `e01a67e2-e365-41c7-8d84-c7a905e348f1` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:22:54 UTC (tier 0)

trial `05789a5c-1987-477d-8530-32283d73e943` model=ridge tier=0 target=volatility skill=1.400 n=8214 gates=UNKNOWN

## [INFO] 2026-08-02 10:23:13 UTC (tier 0)

trial `aec01024-d75c-458d-865b-0d26d8cabedb` model=lgbm_regressor tier=0 target=volatility skill=1.360 n=8214 gates=UNKNOWN

## [INFO] 2026-08-02 10:23:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-10.23145 skill_surrogate=-10.23145

## [INFO] 2026-08-02 10:23:14 UTC (tier 0)

trial `f2dd40ea-e707-45c3-ae24-a3e525d548c3` model=lgbm_classifier tier=0 target=volatility skill=0.117 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:23:14 UTC (tier 0)

Hunt complete: {"generation_id": "auto_042_SOLUSDT_4h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:23:14 UTC (tier 0)

AUTONOMY screen auto_042_SOLUSDT_4h_volatility_ohlcv_v1 tier=0 proxy_skill=1.4004070131362052 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:23:14 UTC (tier 0)

START gen=auto_043_SOLUSDT_4h_volatility_indicators_v1 SOLUSDT 4h target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:23:17 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 6.17464968044601e-11, 'circular_shift': 6.17464968044601e-11, 'fourier_phase': 6.17464968044601e-11, 'row_shuffle': 6.17464968044601e-11} passed=False

## [INFO] 2026-08-02 10:23:19 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:23:19 UTC (tier 0)

trial `b7554424-51ef-4031-bf4b-03220b1ac9ba` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:23:19 UTC (tier 0)

trial `b0c2dce3-70cf-47ca-99b1-3f2ec9a4d043` model=ridge tier=0 target=volatility skill=1.313 n=8214 gates=UNKNOWN

## [INFO] 2026-08-02 10:23:38 UTC (tier 0)

trial `f8a14895-9fb3-4fde-b527-16cecf83185a` model=lgbm_regressor tier=0 target=volatility skill=1.090 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:23:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-10.21190 skill_surrogate=-10.21190

## [INFO] 2026-08-02 10:23:39 UTC (tier 0)

trial `7b1f9d2c-cef5-4b52-adbd-9c022fe7299a` model=lgbm_classifier tier=0 target=volatility skill=0.117 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:23:39 UTC (tier 0)

Hunt complete: {"generation_id": "auto_043_SOLUSDT_4h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:23:39 UTC (tier 0)

AUTONOMY screen auto_043_SOLUSDT_4h_volatility_indicators_v1 tier=0 proxy_skill=1.3132728154456093 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:23:39 UTC (tier 0)

START gen=auto_044_SOLUSDT_4h_volatility_pivot_v1 SOLUSDT 4h target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:23:40 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 6.195077784099112e-11, 'circular_shift': 6.195077784099112e-11, 'fourier_phase': 6.195077784099112e-11, 'row_shuffle': 6.195077784099112e-11} passed=False

## [INFO] 2026-08-02 10:23:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 10:23:44 UTC (tier 0)

trial `394ed95e-5575-4e02-8391-7713020454b3` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:23:44 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.05379 skill_surrogate=+0.00687

## [INFO] 2026-08-02 10:23:44 UTC (tier 0)

trial `672e9fa5-eeba-4834-8a68-75d5392b1548` model=ridge tier=0 target=volatility skill=0.997 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:24:03 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.07073 skill_surrogate=-0.01793

## [INFO] 2026-08-02 10:24:03 UTC (tier 0)

trial `f434101d-9ed7-4bf2-bdde-c66b91187f26` model=lgbm_regressor tier=0 target=volatility skill=0.993 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:24:04 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-10.18045 skill_surrogate=-10.18045

## [INFO] 2026-08-02 10:24:04 UTC (tier 0)

trial `68f2f922-0ae0-4cc0-be7c-724427ca70cc` model=lgbm_classifier tier=0 target=volatility skill=0.117 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:24:04 UTC (tier 0)

Hunt complete: {"generation_id": "auto_044_SOLUSDT_4h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:24:04 UTC (tier 0)

AUTONOMY screen auto_044_SOLUSDT_4h_volatility_pivot_v1 tier=0 proxy_skill=1.0 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:24:04 UTC (tier 0)

START gen=auto_045_BTCUSDT_15m_volatility_ohlcv_v1 BTCUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:24:15 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.407335997212101e-09, 'circular_shift': 2.407335997212101e-09, 'fourier_phase': 2.407335997212101e-09, 'row_shuffle': 2.407335997212101e-09} passed=False

## [INFO] 2026-08-02 10:25:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:25:42 UTC (tier 0)

trial `bcfec55f-b3f8-4f7b-a73e-ae5d436be418` model=hist_mean tier=0 target=volatility skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:25:44 UTC (tier 0)

trial `7d54ba22-078e-4153-9b10-eafeb98bef4e` model=ridge tier=0 target=volatility skill=1.510 n=131421 gates=UNKNOWN

## [INFO] 2026-08-02 10:26:17 UTC (tier 0)

trial `6279c5f6-48f5-49d8-ae4f-23c785c80478` model=lgbm_regressor tier=0 target=volatility skill=1.658 n=131421 gates=UNKNOWN

## [INFO] 2026-08-02 10:26:24 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-80.87244 skill_surrogate=-80.87244

## [INFO] 2026-08-02 10:26:24 UTC (tier 0)

trial `1ba0b58d-87be-43cd-a6fe-4876fa9e73b5` model=lgbm_classifier tier=0 target=volatility skill=0.013 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:26:24 UTC (tier 0)

Hunt complete: {"generation_id": "auto_045_BTCUSDT_15m_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:26:24 UTC (tier 0)

AUTONOMY screen auto_045_BTCUSDT_15m_volatility_ohlcv_v1 tier=0 proxy_skill=1.65788100618668 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:26:24 UTC (tier 0)

START gen=auto_046_BTCUSDT_15m_volatility_indicators_v1 BTCUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:26:36 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.4069506388002537e-09, 'circular_shift': 2.4069506388002537e-09, 'fourier_phase': 2.4069506388002537e-09, 'row_shuffle': 2.4069506388002537e-09} passed=False

## [INFO] 2026-08-02 10:27:19 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:27:19 UTC (tier 0)

trial `402b3667-4db6-47f5-b9bf-87dafe3f28ca` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:27:20 UTC (tier 0)

trial `40ffd040-e751-47fa-8819-41317ca03148` model=ridge tier=0 target=volatility skill=1.501 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:27:49 UTC (tier 0)

trial `71bf17a9-ef5a-4447-902e-389a86e64463` model=lgbm_regressor tier=0 target=volatility skill=1.382 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:27:56 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-80.87717 skill_surrogate=-80.87717

## [INFO] 2026-08-02 10:27:56 UTC (tier 0)

trial `3e497db2-557d-452a-bbac-d81e126b1357` model=lgbm_classifier tier=0 target=volatility skill=0.013 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:27:56 UTC (tier 0)

Hunt complete: {"generation_id": "auto_046_BTCUSDT_15m_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:27:57 UTC (tier 0)

AUTONOMY screen auto_046_BTCUSDT_15m_volatility_indicators_v1 tier=0 proxy_skill=1.5006966284139462 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:27:57 UTC (tier 0)

START gen=auto_047_BTCUSDT_15m_volatility_pivot_v1 BTCUSDT 15m target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:28:04 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.4077196902894116e-09, 'circular_shift': 2.4077196902894116e-09, 'fourier_phase': 2.4077199123340165e-09, 'row_shuffle': 2.4077196902894116e-09} passed=False

## [INFO] 2026-08-02 10:28:43 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:28:43 UTC (tier 0)

trial `2a33aa70-bc93-4ea7-b3a7-857ffed4f0cf` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:28:45 UTC (tier 0)

trial `fe850de5-95a9-47f6-a865-9fd2ea8624dd` model=ridge tier=0 target=volatility skill=1.001 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:29:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02497 skill_surrogate=-0.00079

## [INFO] 2026-08-02 10:29:07 UTC (tier 0)

trial `61c8101c-6d46-4cdd-ba4f-d11fe24768e8` model=lgbm_regressor tier=0 target=volatility skill=1.005 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:29:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-80.87991 skill_surrogate=-80.87991

## [INFO] 2026-08-02 10:29:11 UTC (tier 0)

trial `938c6d60-27db-4513-8e63-ccee693d1904` model=lgbm_classifier tier=0 target=volatility skill=0.013 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:29:11 UTC (tier 0)

Hunt complete: {"generation_id": "auto_047_BTCUSDT_15m_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:29:11 UTC (tier 0)

AUTONOMY screen auto_047_BTCUSDT_15m_volatility_pivot_v1 tier=0 proxy_skill=1.0053906087224702 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:29:11 UTC (tier 0)

START gen=auto_048_ETHUSDT_15m_volatility_ohlcv_v1 ETHUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:29:20 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.525815609061738e-10, 'circular_shift': 8.525815609061738e-10, 'fourier_phase': 8.525815609061738e-10, 'row_shuffle': 8.525815609061738e-10} passed=False

## [INFO] 2026-08-02 10:30:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:30:44 UTC (tier 0)

trial `65815b07-b762-4470-acd6-a52b4bab1ce5` model=hist_mean tier=0 target=volatility skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:30:46 UTC (tier 0)

trial `05eadba8-96fb-4c09-aaf9-42a95064e5a8` model=ridge tier=0 target=volatility skill=1.549 n=131421 gates=UNKNOWN

## [INFO] 2026-08-02 10:31:06 UTC (tier 0)

trial `91b41242-52c0-4f61-9d0b-a08ba36575ca` model=lgbm_regressor tier=0 target=volatility skill=1.631 n=131421 gates=UNKNOWN

## [INFO] 2026-08-02 10:31:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-71.77345 skill_surrogate=-71.77345

## [INFO] 2026-08-02 10:31:11 UTC (tier 0)

trial `3d72b925-fa78-4b63-93b0-e2a63bddfc59` model=lgbm_classifier tier=0 target=volatility skill=0.017 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:31:11 UTC (tier 0)

Hunt complete: {"generation_id": "auto_048_ETHUSDT_15m_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:31:11 UTC (tier 0)

AUTONOMY screen auto_048_ETHUSDT_15m_volatility_ohlcv_v1 tier=0 proxy_skill=1.6306570921647627 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:31:11 UTC (tier 0)

START gen=auto_049_ETHUSDT_15m_volatility_indicators_v1 ETHUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:31:16 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.525484762600399e-10, 'circular_shift': 8.525484762600399e-10, 'fourier_phase': 8.525484762600399e-10, 'row_shuffle': 8.525484762600399e-10} passed=False

## [INFO] 2026-08-02 10:31:43 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:31:43 UTC (tier 0)

trial `d944a0e6-6bca-45c2-b953-fcd759323cb9` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:31:45 UTC (tier 0)

trial `b4c1a645-2d67-456e-a0d4-8c3a8b0a0f27` model=ridge tier=0 target=volatility skill=1.435 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:32:01 UTC (tier 0)

trial `820344fd-beaf-4c0f-a347-d3eb2a7b60d2` model=lgbm_regressor tier=0 target=volatility skill=1.452 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:32:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-71.78078 skill_surrogate=-71.78078

## [INFO] 2026-08-02 10:32:07 UTC (tier 0)

trial `20a1c962-e799-4c03-a681-8a79b28a6079` model=lgbm_classifier tier=0 target=volatility skill=0.017 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:32:07 UTC (tier 0)

Hunt complete: {"generation_id": "auto_049_ETHUSDT_15m_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:32:07 UTC (tier 0)

AUTONOMY screen auto_049_ETHUSDT_15m_volatility_indicators_v1 tier=0 proxy_skill=1.4515439898981315 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:32:07 UTC (tier 0)

START gen=auto_050_ETHUSDT_15m_volatility_pivot_v1 ETHUSDT 15m target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:32:12 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.522563765822611e-10, 'circular_shift': 8.522563765822611e-10, 'fourier_phase': 8.52256465400103e-10, 'row_shuffle': 8.522563765822611e-10} passed=False

## [INFO] 2026-08-02 10:32:47 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:32:47 UTC (tier 0)

trial `49cafab7-3458-42cf-b60e-a7feda39aee5` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:32:48 UTC (tier 0)

trial `3786bb44-20bb-4e1c-8106-7f268959baaf` model=ridge tier=0 target=volatility skill=0.993 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:32:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00878 skill_surrogate=-0.00476

## [INFO] 2026-08-02 10:32:58 UTC (tier 0)

trial `2bfc137d-7043-454a-9a8f-ae5a63cd82c7` model=lgbm_regressor tier=0 target=volatility skill=0.998 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:33:00 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-71.75393 skill_surrogate=-71.75393

## [INFO] 2026-08-02 10:33:00 UTC (tier 0)

trial `5d6efa9b-0d6c-4012-af3f-e5ad6ab16f2f` model=lgbm_classifier tier=0 target=volatility skill=0.017 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:33:00 UTC (tier 0)

Hunt complete: {"generation_id": "auto_050_ETHUSDT_15m_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:33:00 UTC (tier 0)

AUTONOMY screen auto_050_ETHUSDT_15m_volatility_pivot_v1 tier=0 proxy_skill=1.0 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:33:00 UTC (tier 0)

START gen=auto_051_SOLUSDT_15m_volatility_ohlcv_v1 SOLUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-02 10:33:09 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 7.270442026197088e-10, 'circular_shift': 7.270442026197088e-10, 'fourier_phase': 7.270442026197088e-10, 'row_shuffle': 7.270442026197088e-10} passed=False

## [INFO] 2026-08-02 10:33:24 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:33:24 UTC (tier 0)

trial `e503025b-ecb2-40dc-b924-ec2c4bb0bdc9` model=hist_mean tier=0 target=volatility skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:33:25 UTC (tier 0)

trial `d876f30c-6dcd-4fcb-8001-27bd2a5b97e1` model=ridge tier=0 target=volatility skill=1.703 n=131421 gates=UNKNOWN

## [INFO] 2026-08-02 10:33:38 UTC (tier 0)

trial `dda20845-fadb-400f-bfd4-5123b4501a5e` model=lgbm_regressor tier=0 target=volatility skill=1.748 n=131421 gates=UNKNOWN

## [INFO] 2026-08-02 10:33:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-44.76189 skill_surrogate=-44.76189

## [INFO] 2026-08-02 10:33:43 UTC (tier 0)

trial `dbfd1170-c856-45ef-8700-4d123d958abd` model=lgbm_classifier tier=0 target=volatility skill=0.027 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:33:43 UTC (tier 0)

Hunt complete: {"generation_id": "auto_051_SOLUSDT_15m_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:33:43 UTC (tier 0)

AUTONOMY screen auto_051_SOLUSDT_15m_volatility_ohlcv_v1 tier=0 proxy_skill=1.7483994545637311 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:33:43 UTC (tier 0)

START gen=auto_052_SOLUSDT_15m_volatility_indicators_v1 SOLUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-02 10:33:54 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 7.268854407271874e-10, 'circular_shift': 7.268854407271874e-10, 'fourier_phase': 7.268854407271874e-10, 'row_shuffle': 7.268854407271874e-10} passed=False

## [INFO] 2026-08-02 10:34:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:34:05 UTC (tier 0)

trial `b30bcb93-d494-459c-9195-c6aa95adf761` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:34:07 UTC (tier 0)

trial `74703584-f48a-4694-8a86-c7a8ff5a2811` model=ridge tier=0 target=volatility skill=1.717 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:34:20 UTC (tier 0)

trial `ebaf45ed-09c2-494c-a1fb-a3b6e7bb16f7` model=lgbm_regressor tier=0 target=volatility skill=1.490 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:34:24 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-44.75800 skill_surrogate=-44.75800

## [INFO] 2026-08-02 10:34:24 UTC (tier 0)

trial `bcc5d3dd-eb65-4fc2-bc38-f6a7efa85fb7` model=lgbm_classifier tier=0 target=volatility skill=0.027 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:34:24 UTC (tier 0)

Hunt complete: {"generation_id": "auto_052_SOLUSDT_15m_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:34:24 UTC (tier 0)

AUTONOMY screen auto_052_SOLUSDT_15m_volatility_indicators_v1 tier=0 proxy_skill=1.7174687138471694 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:34:24 UTC (tier 0)

START gen=auto_053_SOLUSDT_15m_volatility_pivot_v1 SOLUSDT 15m target=volatility space=pivot_v1

## [INFO] 2026-08-02 10:34:29 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 7.264303603093936e-10, 'circular_shift': 7.264303603093936e-10, 'fourier_phase': 7.264303603093936e-10, 'row_shuffle': 7.264303603093936e-10} passed=False

## [INFO] 2026-08-02 10:34:34 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:34:34 UTC (tier 0)

trial `ae99130e-3536-49d0-a019-13bfb1328856` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:34:35 UTC (tier 0)

trial `1744ad19-c5f4-49fc-8b33-fb7f90ffd544` model=ridge tier=0 target=volatility skill=1.007 n=131424 gates=UNKNOWN

## [INFO] 2026-08-02 10:34:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00184 skill_surrogate=-0.00093

## [INFO] 2026-08-02 10:34:43 UTC (tier 0)

trial `d6359c96-4a93-40ca-98bc-773bbba6f74d` model=lgbm_regressor tier=0 target=volatility skill=1.006 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:34:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-44.74830 skill_surrogate=-44.74830

## [INFO] 2026-08-02 10:34:45 UTC (tier 0)

trial `a9ed81b3-6895-436a-b16b-4e6c28e79d5d` model=lgbm_classifier tier=0 target=volatility skill=0.027 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:34:45 UTC (tier 0)

Hunt complete: {"generation_id": "auto_053_SOLUSDT_15m_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:34:45 UTC (tier 0)

AUTONOMY screen auto_053_SOLUSDT_15m_volatility_pivot_v1 tier=0 proxy_skill=1.0072194885277623 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:34:45 UTC (tier 0)

START gen=auto_054_BTCUSDT_1h_xs_rank_xs_v1 BTCUSDT 1h target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:35:02 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3747336602421001e-11, 'circular_shift': 1.3747336602421001e-11, 'fourier_phase': 1.3747336602421001e-11, 'row_shuffle': 1.3747336602421001e-11} passed=False

## [INFO] 2026-08-02 10:35:21 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:35:21 UTC (tier 0)

trial `c9b1c805-0c4b-4f4f-8621-d845d918ccf0` model=hist_mean tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:35:22 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00033 skill_surrogate=-0.00026

## [INFO] 2026-08-02 10:35:22 UTC (tier 0)

trial `12abbc30-34d9-4da8-b4bb-61069c7965f2` model=ridge tier=0 target=xs_rank pf=0.732 n=29894 gates=FAIL

## [INFO] 2026-08-02 10:35:36 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00322 skill_surrogate=-0.00161

## [INFO] 2026-08-02 10:35:36 UTC (tier 0)

trial `964e3493-2c32-44be-a666-a51f1f57abd2` model=lgbm_regressor tier=0 target=xs_rank pf=0.716 n=29258 gates=FAIL

## [INFO] 2026-08-02 10:35:37 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.68212 skill_surrogate=-0.68212

## [INFO] 2026-08-02 10:35:37 UTC (tier 0)

trial `954685ea-df79-47fb-b65e-9f98ba6224ab` model=lgbm_classifier tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:35:37 UTC (tier 0)

Hunt complete: {"generation_id": "auto_054_BTCUSDT_1h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:35:37 UTC (tier 0)

AUTONOMY screen auto_054_BTCUSDT_1h_xs_rank_xs_v1 tier=0 proxy_pf=0.7319728202993308 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:35:37 UTC (tier 0)

START gen=auto_055_BTCUSDT_1h_xs_rank_crosspair_v1 BTCUSDT 1h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:35:39 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3857581748766279e-11, 'circular_shift': 1.3857581748766279e-11, 'fourier_phase': 1.3857581748766279e-11, 'row_shuffle': 1.3857581748766279e-11} passed=False

## [INFO] 2026-08-02 10:35:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:35:44 UTC (tier 0)

trial `eb917dc8-9d4e-4fd6-be20-ee8b35b20e5a` model=hist_mean tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:35:44 UTC (tier 0)

trial `466315be-7699-4a15-aa21-4507a49d98b5` model=ridge tier=0 target=xs_rank pf=0.723 n=32826 gates=FAIL

## [INFO] 2026-08-02 10:35:49 UTC (tier 0)

trial `b850785e-646d-4442-9148-d4bc5dc479d8` model=lgbm_regressor tier=0 target=xs_rank pf=0.712 n=29858 gates=FAIL

## [INFO] 2026-08-02 10:35:50 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.68034 skill_surrogate=-0.68034

## [INFO] 2026-08-02 10:35:50 UTC (tier 0)

trial `b2312047-071a-4531-ba7c-63a41beeb46e` model=lgbm_classifier tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:35:50 UTC (tier 0)

Hunt complete: {"generation_id": "auto_055_BTCUSDT_1h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:35:50 UTC (tier 0)

AUTONOMY screen auto_055_BTCUSDT_1h_xs_rank_crosspair_v1 tier=0 proxy_pf=0.7228965935014684 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:35:50 UTC (tier 0)

START gen=auto_056_BTCUSDT_1h_xs_rank_ohlcv_v1 BTCUSDT 1h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:35:52 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3075096561010469e-11, 'circular_shift': 1.3075096561010469e-11, 'fourier_phase': 1.3075096561010469e-11, 'row_shuffle': 1.3075096561010469e-11} passed=False

## [INFO] 2026-08-02 10:36:00 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:36:00 UTC (tier 0)

trial `7fb585b2-139d-4131-8385-889c2581ab00` model=hist_mean tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:36:00 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00348 skill_surrogate=-0.00074

## [INFO] 2026-08-02 10:36:00 UTC (tier 0)

trial `f452b2dd-afa7-45bb-8c14-11917ce82dbe` model=ridge tier=0 target=xs_rank pf=0.712 n=32394 gates=FAIL

## [INFO] 2026-08-02 10:36:20 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00746 skill_surrogate=-0.00208

## [INFO] 2026-08-02 10:36:20 UTC (tier 0)

trial `08e73a6c-299b-4bdc-9678-3625fcb8bbc3` model=lgbm_regressor tier=0 target=xs_rank pf=0.700 n=30150 gates=FAIL

## [INFO] 2026-08-02 10:36:22 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.68594 skill_surrogate=-0.68594

## [INFO] 2026-08-02 10:36:22 UTC (tier 0)

trial `03528a96-0b1e-4e01-9c6f-bb57a3131958` model=lgbm_classifier tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:36:22 UTC (tier 0)

Hunt complete: {"generation_id": "auto_056_BTCUSDT_1h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:36:22 UTC (tier 0)

AUTONOMY screen auto_056_BTCUSDT_1h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.7228965935014684 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:36:22 UTC (tier 0)

START gen=auto_057_ETHUSDT_1h_xs_rank_xs_v1 ETHUSDT 1h target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:36:26 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.6435741656550817e-11, 'circular_shift': 1.6435741656550817e-11, 'fourier_phase': 1.6435741656550817e-11, 'row_shuffle': 1.6435741656550817e-11} passed=False

## [INFO] 2026-08-02 10:36:32 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:36:32 UTC (tier 0)

trial `e3c20e10-bbe9-4deb-925b-a6f9951042c6` model=hist_mean tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:36:32 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00372 skill_surrogate=-0.00018

## [INFO] 2026-08-02 10:36:32 UTC (tier 0)

trial `565409fe-32d3-4dd5-a8f3-dfefadbbff75` model=ridge tier=0 target=xs_rank pf=0.767 n=29494 gates=FAIL

## [INFO] 2026-08-02 10:36:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00155 skill_surrogate=+0.00121

## [INFO] 2026-08-02 10:36:44 UTC (tier 0)

trial `a647327d-2114-4173-96bd-c0250d3ea7db` model=lgbm_regressor tier=0 target=xs_rank pf=0.754 n=29296 gates=FAIL

## [INFO] 2026-08-02 10:36:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.87043 skill_surrogate=-0.87043

## [INFO] 2026-08-02 10:36:45 UTC (tier 0)

trial `a6fba00b-da1f-414d-81c1-e58d36f58f15` model=lgbm_classifier tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:36:45 UTC (tier 0)

Hunt complete: {"generation_id": "auto_057_ETHUSDT_1h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:36:45 UTC (tier 0)

AUTONOMY screen auto_057_ETHUSDT_1h_xs_rank_xs_v1 tier=0 proxy_pf=0.7674134926733643 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:36:45 UTC (tier 0)

START gen=auto_058_ETHUSDT_1h_xs_rank_crosspair_v1 ETHUSDT 1h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:36:48 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.6632584198816858e-11, 'circular_shift': 1.6632584198816858e-11, 'fourier_phase': 1.6632584198816858e-11, 'row_shuffle': 1.6632584198816858e-11} passed=False

## [INFO] 2026-08-02 10:36:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:36:57 UTC (tier 0)

trial `dfbb9568-943c-4c7b-a47f-8c0f51b5a2a1` model=hist_mean tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:36:57 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00027 skill_surrogate=-0.00013

## [INFO] 2026-08-02 10:36:57 UTC (tier 0)

trial `4dcb049b-ea47-4a06-a6d6-d78b7fb18ba9` model=ridge tier=0 target=xs_rank pf=0.763 n=32771 gates=FAIL

## [INFO] 2026-08-02 10:37:14 UTC (tier 0)

trial `973c4cc1-d3af-4ee0-8174-01481721514c` model=lgbm_regressor tier=0 target=xs_rank pf=0.761 n=30310 gates=FAIL

## [INFO] 2026-08-02 10:37:15 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.86324 skill_surrogate=-0.86324

## [INFO] 2026-08-02 10:37:15 UTC (tier 0)

trial `2302b6ae-cf13-44e9-aa05-85f7f75babcb` model=lgbm_classifier tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:37:15 UTC (tier 0)

Hunt complete: {"generation_id": "auto_058_ETHUSDT_1h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:37:15 UTC (tier 0)

AUTONOMY screen auto_058_ETHUSDT_1h_xs_rank_crosspair_v1 tier=0 proxy_pf=0.7642285849544566 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:37:15 UTC (tier 0)

START gen=auto_059_ETHUSDT_1h_xs_rank_ohlcv_v1 ETHUSDT 1h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:37:18 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.6435741656550817e-11, 'circular_shift': 1.6435741656550817e-11, 'fourier_phase': 1.6435741656550817e-11, 'row_shuffle': 1.6435741656550817e-11} passed=False

## [INFO] 2026-08-02 10:37:23 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:37:23 UTC (tier 0)

trial `ccc93507-b518-4660-8de1-22a1fdae85a5` model=hist_mean tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:37:23 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00281 skill_surrogate=+0.00066

## [INFO] 2026-08-02 10:37:23 UTC (tier 0)

trial `9f12e096-8bc3-44aa-a5ea-62e6f9babb41` model=ridge tier=0 target=xs_rank pf=0.749 n=31287 gates=FAIL

## [INFO] 2026-08-02 10:37:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00137 skill_surrogate=-0.00042

## [INFO] 2026-08-02 10:37:32 UTC (tier 0)

trial `bd699bdb-a991-425f-ad26-1e3062f44172` model=lgbm_regressor tier=0 target=xs_rank pf=0.750 n=29417 gates=FAIL

## [INFO] 2026-08-02 10:37:33 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.87043 skill_surrogate=-0.87043

## [INFO] 2026-08-02 10:37:33 UTC (tier 0)

trial `a9f95f20-44d3-4cda-80ae-6c0fe41bd221` model=lgbm_classifier tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:37:33 UTC (tier 0)

Hunt complete: {"generation_id": "auto_059_ETHUSDT_1h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:37:33 UTC (tier 0)

AUTONOMY screen auto_059_ETHUSDT_1h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.7642285849544566 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:37:33 UTC (tier 0)

START gen=auto_060_SOLUSDT_1h_xs_rank_xs_v1 SOLUSDT 1h target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:37:37 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.629630426388758e-12, 'circular_shift': 9.629630426388758e-12, 'fourier_phase': 9.629630426388758e-12, 'row_shuffle': 9.629630426388758e-12} passed=False

## [INFO] 2026-08-02 10:37:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:37:42 UTC (tier 0)

trial `a48e135f-92f5-440b-9b87-611e58337fcf` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:37:42 UTC (tier 0)

trial `3117da12-6d52-435d-82c3-b093fbb41c79` model=ridge tier=0 target=xs_rank pf=0.846 n=11524 gates=FAIL

## [INFO] 2026-08-02 10:37:46 UTC (tier 0)

trial `0682e9f8-00dc-40cc-9792-b24aefe7085e` model=lgbm_regressor tier=0 target=xs_rank pf=0.877 n=9592 gates=FAIL

## [INFO] 2026-08-02 10:37:46 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.77286 skill_surrogate=-0.77286

## [INFO] 2026-08-02 10:37:46 UTC (tier 0)

trial `10c278f7-e145-4d64-8f25-65f694864f91` model=lgbm_classifier tier=0 target=xs_rank pf=0.848 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:37:46 UTC (tier 0)

Hunt complete: {"generation_id": "auto_060_SOLUSDT_1h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:37:46 UTC (tier 0)

AUTONOMY screen auto_060_SOLUSDT_1h_xs_rank_xs_v1 tier=0 proxy_pf=0.8768375096847943 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:37:47 UTC (tier 0)

START gen=auto_061_SOLUSDT_1h_xs_rank_crosspair_v1 SOLUSDT 1h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:37:48 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.629630426388758e-12, 'circular_shift': 9.629630426388758e-12, 'fourier_phase': 9.629630426388758e-12, 'row_shuffle': 9.629630426388758e-12} passed=False

## [INFO] 2026-08-02 10:37:52 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:37:52 UTC (tier 0)

trial `632b5416-8436-4bd8-8e1d-25d30e948ec9` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:37:52 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=+0.00004 skill_surrogate=+0.00016

## [INFO] 2026-08-02 10:37:52 UTC (tier 0)

trial `02e91d7f-6280-4e22-8d59-5e38b5bcfe5f` model=ridge tier=0 target=xs_rank pf=0.925 n=3509 gates=FAIL

## [INFO] 2026-08-02 10:37:56 UTC (tier 0)

trial `61b01ab9-8466-4d18-9d7c-c2b191e81fac` model=lgbm_regressor tier=0 target=xs_rank pf=0.929 n=7397 gates=FAIL

## [INFO] 2026-08-02 10:37:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.77286 skill_surrogate=-0.77286

## [INFO] 2026-08-02 10:37:57 UTC (tier 0)

trial `1ecb6d38-c77c-4c4f-a8aa-6c70b2f6fe9b` model=lgbm_classifier tier=0 target=xs_rank pf=0.848 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:37:57 UTC (tier 0)

Hunt complete: {"generation_id": "auto_061_SOLUSDT_1h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:37:57 UTC (tier 0)

AUTONOMY screen auto_061_SOLUSDT_1h_xs_rank_crosspair_v1 tier=0 proxy_pf=0.9292943930471456 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:37:57 UTC (tier 0)

START gen=auto_062_SOLUSDT_1h_xs_rank_ohlcv_v1 SOLUSDT 1h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:37:59 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.629630426388758e-12, 'circular_shift': 9.629630426388758e-12, 'fourier_phase': 9.629630426388758e-12, 'row_shuffle': 9.629630426388758e-12} passed=False

## [INFO] 2026-08-02 10:38:03 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:38:03 UTC (tier 0)

trial `0df27dda-adbe-45fb-86e7-aa0f3025479c` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:38:04 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00124 skill_surrogate=+0.00072

## [INFO] 2026-08-02 10:38:04 UTC (tier 0)

trial `75897d65-2922-47a4-9194-a280aef545e6` model=ridge tier=0 target=xs_rank pf=0.899 n=9983 gates=FAIL

## [INFO] 2026-08-02 10:38:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00232 skill_surrogate=+0.00068

## [INFO] 2026-08-02 10:38:10 UTC (tier 0)

trial `ac289ef7-8ac1-45d4-acf9-8573c21424e7` model=lgbm_regressor tier=0 target=xs_rank pf=0.897 n=13536 gates=FAIL

## [INFO] 2026-08-02 10:38:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.77286 skill_surrogate=-0.77286

## [INFO] 2026-08-02 10:38:11 UTC (tier 0)

trial `72b0aebe-360a-4aab-b0b9-0fc108269b9f` model=lgbm_classifier tier=0 target=xs_rank pf=0.848 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:38:11 UTC (tier 0)

Hunt complete: {"generation_id": "auto_062_SOLUSDT_1h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:38:11 UTC (tier 0)

AUTONOMY screen auto_062_SOLUSDT_1h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.8987394146822163 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:38:11 UTC (tier 0)

START gen=auto_063_BTCUSDT_4h_xs_rank_xs_v1 BTCUSDT 4h target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:38:15 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3778533869412968e-11, 'circular_shift': 1.3778533869412968e-11, 'fourier_phase': 1.377864489171543e-11, 'row_shuffle': 1.3778533869412968e-11} passed=False

## [INFO] 2026-08-02 10:38:19 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:38:19 UTC (tier 0)

trial `783eb087-efb7-4231-a917-ca94dbd5a601` model=hist_mean tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:19 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00643 skill_surrogate=-0.00120

## [INFO] 2026-08-02 10:38:19 UTC (tier 0)

trial `b50f5b96-cc9b-40a4-b752-fbaed9c9c499` model=ridge tier=0 target=xs_rank pf=0.939 n=7797 gates=FAIL

## [INFO] 2026-08-02 10:38:22 UTC (tier 0)

trial `67a250ac-667e-4392-a1a1-02ee48c537f8` model=lgbm_regressor tier=0 target=xs_rank pf=0.896 n=7124 gates=FAIL

## [INFO] 2026-08-02 10:38:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.57357 skill_surrogate=-0.57357

## [INFO] 2026-08-02 10:38:23 UTC (tier 0)

trial `b7fbfa43-3bea-47b7-8040-6ed50b69132e` model=lgbm_classifier tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:23 UTC (tier 0)

Hunt complete: {"generation_id": "auto_063_BTCUSDT_4h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:38:23 UTC (tier 0)

AUTONOMY screen auto_063_BTCUSDT_4h_xs_rank_xs_v1 tier=0 proxy_pf=0.948482148877497 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:38:23 UTC (tier 0)

START gen=auto_064_BTCUSDT_4h_xs_rank_crosspair_v1 BTCUSDT 4h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:38:23 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.40059075448562e-11, 'circular_shift': 1.40059075448562e-11, 'fourier_phase': 1.4006151793921617e-11, 'row_shuffle': 1.40059075448562e-11} passed=False

## [INFO] 2026-08-02 10:38:25 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:38:25 UTC (tier 0)

trial `cf5a37b1-e73b-4738-b2bd-1f2edd1cff49` model=hist_mean tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:25 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00500 skill_surrogate=-0.00137

## [INFO] 2026-08-02 10:38:25 UTC (tier 0)

trial `189a5a4f-0c7e-4b6c-b9e1-1c8a157f6e7e` model=ridge tier=0 target=xs_rank pf=0.951 n=8106 gates=FAIL

## [INFO] 2026-08-02 10:38:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00484 skill_surrogate=-0.00254

## [INFO] 2026-08-02 10:38:27 UTC (tier 0)

trial `790c2c4b-591c-457f-9e8c-b77a594d33b8` model=lgbm_regressor tier=0 target=xs_rank pf=0.943 n=6967 gates=FAIL

## [INFO] 2026-08-02 10:38:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.57454 skill_surrogate=-0.57454

## [INFO] 2026-08-02 10:38:27 UTC (tier 0)

trial `fb099caf-c6ef-40fc-a5ff-70e1046b20b8` model=lgbm_classifier tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:27 UTC (tier 0)

Hunt complete: {"generation_id": "auto_064_BTCUSDT_4h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:38:27 UTC (tier 0)

AUTONOMY screen auto_064_BTCUSDT_4h_xs_rank_crosspair_v1 tier=0 proxy_pf=0.9510713636379153 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:38:27 UTC (tier 0)

START gen=auto_065_BTCUSDT_4h_xs_rank_ohlcv_v1 BTCUSDT 4h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:38:28 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3234191520439254e-11, 'circular_shift': 1.3234191520439254e-11, 'fourier_phase': 1.3234213724899746e-11, 'row_shuffle': 1.3234191520439254e-11} passed=False

## [INFO] 2026-08-02 10:38:30 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:38:30 UTC (tier 0)

trial `1a1cf966-9909-49e0-9b06-27516cabce7b` model=hist_mean tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:30 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00266 skill_surrogate=+0.00029

## [INFO] 2026-08-02 10:38:30 UTC (tier 0)

trial `fc37bf92-b61d-483e-aba0-db7b4544a6ab` model=ridge tier=0 target=xs_rank pf=0.925 n=8084 gates=FAIL

## [INFO] 2026-08-02 10:38:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00897 skill_surrogate=+0.00086

## [INFO] 2026-08-02 10:38:34 UTC (tier 0)

trial `858fd8ad-eeca-43b3-9165-958541cf72fe` model=lgbm_regressor tier=0 target=xs_rank pf=0.943 n=7468 gates=FAIL

## [INFO] 2026-08-02 10:38:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.56815 skill_surrogate=-0.56815

## [INFO] 2026-08-02 10:38:35 UTC (tier 0)

trial `9f036fc3-b8c5-438b-b814-c0801d7ab38c` model=lgbm_classifier tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:35 UTC (tier 0)

Hunt complete: {"generation_id": "auto_065_BTCUSDT_4h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:38:35 UTC (tier 0)

AUTONOMY screen auto_065_BTCUSDT_4h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.948482148877497 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:38:35 UTC (tier 0)

START gen=auto_066_ETHUSDT_4h_xs_rank_xs_v1 ETHUSDT 4h target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:38:36 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.6669665647839338e-11, 'circular_shift': 1.6669665647839338e-11, 'fourier_phase': 1.6669665647839338e-11, 'row_shuffle': 1.6669665647839338e-11} passed=False

## [INFO] 2026-08-02 10:38:38 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:38:38 UTC (tier 0)

trial `8e995788-c4ee-4464-8591-f8b11a87f0fa` model=hist_mean tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:38 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00460 skill_surrogate=-0.00310

## [INFO] 2026-08-02 10:38:38 UTC (tier 0)

trial `f682687a-9e32-4972-8516-0ef80401a0fc` model=ridge tier=0 target=xs_rank pf=0.922 n=8174 gates=FAIL

## [INFO] 2026-08-02 10:38:42 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00458 skill_surrogate=-0.00565

## [INFO] 2026-08-02 10:38:42 UTC (tier 0)

trial `3a98410a-6213-4148-a517-1e1392263f4c` model=lgbm_regressor tier=0 target=xs_rank pf=0.898 n=7404 gates=FAIL

## [INFO] 2026-08-02 10:38:42 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.85370 skill_surrogate=-0.85370

## [INFO] 2026-08-02 10:38:42 UTC (tier 0)

trial `e1fae436-ee54-4bec-b282-afd14e8d0f40` model=lgbm_classifier tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:42 UTC (tier 0)

Hunt complete: {"generation_id": "auto_066_ETHUSDT_4h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:38:42 UTC (tier 0)

AUTONOMY screen auto_066_ETHUSDT_4h_xs_rank_xs_v1 tier=0 proxy_pf=0.9215764347940009 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:38:42 UTC (tier 0)

START gen=auto_067_ETHUSDT_4h_xs_rank_crosspair_v1 ETHUSDT 4h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:38:43 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.6767920385518664e-11, 'circular_shift': 1.6767920385518664e-11, 'fourier_phase': 1.6768164634584083e-11, 'row_shuffle': 1.6767920385518664e-11} passed=False

## [INFO] 2026-08-02 10:38:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:38:44 UTC (tier 0)

trial `afa0ce13-aba6-42ab-bcf1-cbfcd39e7c46` model=hist_mean tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:44 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00008 skill_surrogate=-0.00129

## [INFO] 2026-08-02 10:38:44 UTC (tier 0)

trial `f2b78bc4-2532-4c37-8dfe-c26013f7183b` model=ridge tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:47 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01119 skill_surrogate=-0.00497

## [INFO] 2026-08-02 10:38:47 UTC (tier 0)

trial `aad071fe-9e1b-4960-a5e1-b3f90a4ec924` model=lgbm_regressor tier=0 target=xs_rank pf=0.942 n=7191 gates=FAIL

## [INFO] 2026-08-02 10:38:47 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.84376 skill_surrogate=-0.84376

## [INFO] 2026-08-02 10:38:47 UTC (tier 0)

trial `7b192b49-2f23-4fa6-bf4f-1b5b73ed5fff` model=lgbm_classifier tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:47 UTC (tier 0)

Hunt complete: {"generation_id": "auto_067_ETHUSDT_4h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:38:47 UTC (tier 0)

AUTONOMY screen auto_067_ETHUSDT_4h_xs_rank_crosspair_v1 tier=0 proxy_pf=0.9415470386990968 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:38:47 UTC (tier 0)

START gen=auto_068_ETHUSDT_4h_xs_rank_ohlcv_v1 ETHUSDT 4h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:38:48 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.6669665647839338e-11, 'circular_shift': 1.6669665647839338e-11, 'fourier_phase': 1.6669665647839338e-11, 'row_shuffle': 1.6669665647839338e-11} passed=False

## [INFO] 2026-08-02 10:38:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:38:50 UTC (tier 0)

trial `dc7734a9-3014-4b6f-ac89-d739f75409d6` model=hist_mean tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:50 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00399 skill_surrogate=-0.00465

## [INFO] 2026-08-02 10:38:50 UTC (tier 0)

trial `8eda21ac-dfdc-46ea-b3af-282be45e2280` model=ridge tier=0 target=xs_rank pf=0.906 n=8088 gates=FAIL

## [INFO] 2026-08-02 10:38:55 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00772 skill_surrogate=-0.01135

## [INFO] 2026-08-02 10:38:55 UTC (tier 0)

trial `fe074ac7-9495-4433-87a8-06ea74f4c213` model=lgbm_regressor tier=0 target=xs_rank pf=0.895 n=7425 gates=FAIL

## [INFO] 2026-08-02 10:38:55 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.85370 skill_surrogate=-0.85370

## [INFO] 2026-08-02 10:38:55 UTC (tier 0)

trial `926b1745-3d67-48bc-b5af-404c0553b64e` model=lgbm_classifier tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:38:55 UTC (tier 0)

Hunt complete: {"generation_id": "auto_068_ETHUSDT_4h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:38:55 UTC (tier 0)

AUTONOMY screen auto_068_ETHUSDT_4h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.9200856060065038 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:38:55 UTC (tier 0)

START gen=auto_069_SOLUSDT_4h_xs_rank_xs_v1 SOLUSDT 4h target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:38:57 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.418021917895203e-12, 'circular_shift': 9.418021917895203e-12, 'fourier_phase': 9.418110735737173e-12, 'row_shuffle': 9.418021917895203e-12} passed=False

## [INFO] 2026-08-02 10:38:58 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 10:38:58 UTC (tier 0)

trial `dd7f6319-5a26-4461-b42d-07470ba2e41c` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:38:58 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00491 skill_surrogate=+0.00159

## [INFO] 2026-08-02 10:38:58 UTC (tier 0)

trial `f462c7c3-c355-49d1-a25a-ff481adb64c7` model=ridge tier=0 target=xs_rank pf=0.922 n=3257 gates=FAIL

## [INFO] 2026-08-02 10:39:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00903 skill_surrogate=+0.00072

## [INFO] 2026-08-02 10:39:02 UTC (tier 0)

trial `2e0ffa81-2e3f-4f65-8136-aede419ffba2` model=lgbm_regressor tier=0 target=xs_rank pf=0.950 n=4160 gates=FAIL

## [INFO] 2026-08-02 10:39:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.84700 skill_surrogate=-0.84700

## [INFO] 2026-08-02 10:39:02 UTC (tier 0)

trial `e9b8cf72-7783-4ed3-8215-c6d77da8e516` model=lgbm_classifier tier=0 target=xs_rank pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:39:02 UTC (tier 0)

Hunt complete: {"generation_id": "auto_069_SOLUSDT_4h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:39:02 UTC (tier 0)

AUTONOMY screen auto_069_SOLUSDT_4h_xs_rank_xs_v1 tier=0 proxy_pf=0.9701066640508432 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:39:02 UTC (tier 0)

START gen=auto_070_SOLUSDT_4h_xs_rank_crosspair_v1 SOLUSDT 4h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:39:03 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.418021917895203e-12, 'circular_shift': 9.418021917895203e-12, 'fourier_phase': 9.418110735737173e-12, 'row_shuffle': 9.418021917895203e-12} passed=False

## [INFO] 2026-08-02 10:39:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 10:39:04 UTC (tier 0)

trial `dc9a5090-2062-4567-a155-7717c091e2b0` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:39:04 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00056 skill_surrogate=+0.00092

## [INFO] 2026-08-02 10:39:04 UTC (tier 0)

trial `c9d5ee42-b025-4caf-b304-8c37eeee6187` model=ridge tier=0 target=xs_rank pf=1.021 n=585 gates=FAIL

## [INFO] 2026-08-02 10:39:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00132 skill_surrogate=+0.00102

## [INFO] 2026-08-02 10:39:07 UTC (tier 0)

trial `d68f785d-ebd2-4b38-97a5-5403393d4dfe` model=lgbm_regressor tier=0 target=xs_rank pf=1.124 n=3003 gates=FAIL

## [INFO] 2026-08-02 10:39:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.84700 skill_surrogate=-0.84700

## [INFO] 2026-08-02 10:39:07 UTC (tier 0)

trial `e82ad976-0459-48c6-8bce-c917545ca05f` model=lgbm_classifier tier=0 target=xs_rank pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:39:07 UTC (tier 0)

Hunt complete: {"generation_id": "auto_070_SOLUSDT_4h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:39:07 UTC (tier 0)

AUTONOMY screen auto_070_SOLUSDT_4h_xs_rank_crosspair_v1 tier=0 proxy_pf=1.1237433499382057 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:39:07 UTC (tier 0)

START gen=auto_071_SOLUSDT_4h_xs_rank_ohlcv_v1 SOLUSDT 4h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:39:08 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.418021917895203e-12, 'circular_shift': 9.418021917895203e-12, 'fourier_phase': 9.418110735737173e-12, 'row_shuffle': 9.418021917895203e-12} passed=False

## [INFO] 2026-08-02 10:39:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 10:39:09 UTC (tier 0)

trial `3c27b2c5-9e9e-46c5-93ef-d16acbb16f38` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:39:09 UTC (tier 0)

trial `274a6e6e-f5dd-402c-ba9a-18e80bb2b80a` model=ridge tier=0 target=xs_rank pf=1.164 n=2083 gates=FAIL

## [INFO] 2026-08-02 10:39:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02228 skill_surrogate=+0.00212

## [INFO] 2026-08-02 10:39:12 UTC (tier 0)

trial `abef456d-4c5d-4e27-9336-32ac06993e7b` model=lgbm_regressor tier=0 target=xs_rank pf=0.979 n=4726 gates=FAIL

## [INFO] 2026-08-02 10:39:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.84700 skill_surrogate=-0.84700

## [INFO] 2026-08-02 10:39:12 UTC (tier 0)

trial `11962163-1ce1-480a-a508-c441aa10c555` model=lgbm_classifier tier=0 target=xs_rank pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:39:12 UTC (tier 0)

Hunt complete: {"generation_id": "auto_071_SOLUSDT_4h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:39:12 UTC (tier 0)

AUTONOMY screen auto_071_SOLUSDT_4h_xs_rank_ohlcv_v1 tier=0 proxy_pf=1.1640774293306702 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:39:13 UTC (tier 0)

START gen=auto_072_BTCUSDT_15m_xs_rank_xs_v1 BTCUSDT 15m target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:39:42 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3757772698852477e-11, 'circular_shift': 1.3757772698852477e-11, 'fourier_phase': 1.3757772698852477e-11, 'row_shuffle': 1.3757772698852477e-11} passed=False

## [INFO] 2026-08-02 10:40:30 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:40:30 UTC (tier 0)

trial `ad74d157-f4dc-4e30-98b3-c4964b67fc6c` model=hist_mean tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:40:30 UTC (tier 0)

trial `ca6a156c-7350-4682-a58e-014d3cff470d` model=ridge tier=0 target=xs_rank pf=0.472 n=107826 gates=FAIL

## [INFO] 2026-08-02 10:40:38 UTC (tier 0)

trial `948b4322-1d8e-4650-bfb0-6a153bff10a3` model=lgbm_regressor tier=0 target=xs_rank pf=0.469 n=113074 gates=FAIL

## [INFO] 2026-08-02 10:40:40 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.67283 skill_surrogate=-0.67283

## [INFO] 2026-08-02 10:40:40 UTC (tier 0)

trial `bad504f2-2013-4692-9ed9-731f58f16e62` model=lgbm_classifier tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:40:40 UTC (tier 0)

Hunt complete: {"generation_id": "auto_072_BTCUSDT_15m_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:40:40 UTC (tier 0)

AUTONOMY screen auto_072_BTCUSDT_15m_xs_rank_xs_v1 tier=0 proxy_pf=0.47251179753828415 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:40:41 UTC (tier 0)

START gen=auto_073_BTCUSDT_15m_xs_rank_crosspair_v1 BTCUSDT 15m target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:40:47 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.375832781036479e-11, 'circular_shift': 1.375832781036479e-11, 'fourier_phase': 1.375832781036479e-11, 'row_shuffle': 1.375832781036479e-11} passed=False

## [INFO] 2026-08-02 10:41:31 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:41:31 UTC (tier 0)

trial `5304d6ba-84bd-4d71-8aca-53a35385932a` model=hist_mean tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:41:32 UTC (tier 0)

trial `3ccca3cd-9dd8-473a-8796-f47379042fed` model=ridge tier=0 target=xs_rank pf=0.469 n=128747 gates=FAIL

## [INFO] 2026-08-02 10:41:38 UTC (tier 0)

trial `edb428e0-9265-4908-9007-2ae85882235e` model=lgbm_regressor tier=0 target=xs_rank pf=0.456 n=117559 gates=FAIL

## [INFO] 2026-08-02 10:41:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.67100 skill_surrogate=-0.67100

## [INFO] 2026-08-02 10:41:39 UTC (tier 0)

trial `3abecca1-bcc4-4824-8a89-1fcefd2f1a49` model=lgbm_classifier tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:41:39 UTC (tier 0)

Hunt complete: {"generation_id": "auto_073_BTCUSDT_15m_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:41:39 UTC (tier 0)

AUTONOMY screen auto_073_BTCUSDT_15m_xs_rank_crosspair_v1 tier=0 proxy_pf=0.47251179753828415 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:41:39 UTC (tier 0)

START gen=auto_074_BTCUSDT_15m_xs_rank_ohlcv_v1 BTCUSDT 15m target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:41:49 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3025580614112187e-11, 'circular_shift': 1.3025580614112187e-11, 'fourier_phase': 1.3025580614112187e-11, 'row_shuffle': 1.3025580614112187e-11} passed=False

## [INFO] 2026-08-02 10:42:41 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:42:41 UTC (tier 0)

trial `7ff1f037-759e-4280-8c6e-7da3e651602c` model=hist_mean tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:42:42 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00014 skill_surrogate=-0.00037

## [INFO] 2026-08-02 10:42:42 UTC (tier 0)

trial `131e7a4d-cc21-40a6-9223-1b7ada0cc7c3` model=ridge tier=0 target=xs_rank pf=0.463 n=130075 gates=FAIL

## [INFO] 2026-08-02 10:42:55 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00192 skill_surrogate=-0.00014

## [INFO] 2026-08-02 10:42:55 UTC (tier 0)

trial `1a64bb9f-ed6a-4360-9510-1331c95e45b4` model=lgbm_regressor tier=0 target=xs_rank pf=0.458 n=124547 gates=FAIL

## [INFO] 2026-08-02 10:43:00 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.67680 skill_surrogate=-0.67680

## [INFO] 2026-08-02 10:43:00 UTC (tier 0)

trial `2edbda4e-c78a-4ea1-990d-04a242d5fba3` model=lgbm_classifier tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:43:00 UTC (tier 0)

Hunt complete: {"generation_id": "auto_074_BTCUSDT_15m_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:43:01 UTC (tier 0)

AUTONOMY screen auto_074_BTCUSDT_15m_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.47251179753828415 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:43:01 UTC (tier 0)

START gen=auto_075_ETHUSDT_15m_xs_rank_xs_v1 ETHUSDT 15m target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:43:16 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.628575052592396e-11, 'circular_shift': 1.628575052592396e-11, 'fourier_phase': 1.628575052592396e-11, 'row_shuffle': 1.628575052592396e-11} passed=False

## [INFO] 2026-08-02 10:44:14 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:44:14 UTC (tier 0)

trial `245bafaf-50a8-4f5c-ac97-de9122d780e9` model=hist_mean tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:44:15 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00093 skill_surrogate=-0.00038

## [INFO] 2026-08-02 10:44:15 UTC (tier 0)

trial `c62c543d-e8ea-4f0f-817f-08baec7ee237` model=ridge tier=0 target=xs_rank pf=0.557 n=102570 gates=FAIL

## [INFO] 2026-08-02 10:44:22 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00021 skill_surrogate=-0.00031

## [INFO] 2026-08-02 10:44:22 UTC (tier 0)

trial `721a8eb5-3e85-45c3-b26f-83bcac1fd0cb` model=lgbm_regressor tier=0 target=xs_rank pf=0.552 n=111900 gates=FAIL

## [INFO] 2026-08-02 10:44:25 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.95943 skill_surrogate=-0.95943

## [INFO] 2026-08-02 10:44:25 UTC (tier 0)

trial `ace8d7af-9022-41d3-8fcd-192d4b62c232` model=lgbm_classifier tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:44:25 UTC (tier 0)

Hunt complete: {"generation_id": "auto_075_ETHUSDT_15m_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:44:25 UTC (tier 0)

AUTONOMY screen auto_075_ETHUSDT_15m_xs_rank_xs_v1 tier=0 proxy_pf=0.5573349843833583 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:44:25 UTC (tier 0)

START gen=auto_076_ETHUSDT_15m_xs_rank_crosspair_v1 ETHUSDT 15m target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:44:31 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.6562751170567935e-11, 'circular_shift': 1.6562751170567935e-11, 'fourier_phase': 1.6562751170567935e-11, 'row_shuffle': 1.6562751170567935e-11} passed=False

## [INFO] 2026-08-02 10:44:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:44:50 UTC (tier 0)

trial `45a5380c-bed6-4477-9447-cdc6e311baa0` model=hist_mean tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:44:51 UTC (tier 0)

trial `2ed4736a-691d-49fd-aa0a-853ef0a4283b` model=ridge tier=0 target=xs_rank pf=0.554 n=129608 gates=FAIL

## [INFO] 2026-08-02 10:44:55 UTC (tier 0)

trial `d4bca97f-a157-42d1-b1ec-cea98f922b96` model=lgbm_regressor tier=0 target=xs_rank pf=0.552 n=114892 gates=FAIL

## [INFO] 2026-08-02 10:44:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.95412 skill_surrogate=-0.95412

## [INFO] 2026-08-02 10:44:57 UTC (tier 0)

trial `6409b69e-3931-495b-9a0f-bdb4c28c176d` model=lgbm_classifier tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:44:57 UTC (tier 0)

Hunt complete: {"generation_id": "auto_076_ETHUSDT_15m_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:44:57 UTC (tier 0)

AUTONOMY screen auto_076_ETHUSDT_15m_xs_rank_crosspair_v1 tier=0 proxy_pf=0.5551435152352238 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:44:57 UTC (tier 0)

START gen=auto_077_ETHUSDT_15m_xs_rank_ohlcv_v1 ETHUSDT 15m target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:45:01 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.6285639503621496e-11, 'circular_shift': 1.6285639503621496e-11, 'fourier_phase': 1.6285639503621496e-11, 'row_shuffle': 1.6285639503621496e-11} passed=False

## [INFO] 2026-08-02 10:45:22 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:45:22 UTC (tier 0)

trial `c52d01b3-dabd-4924-9fcc-c93afb7eabe0` model=hist_mean tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:45:24 UTC (tier 0)

trial `6b0caf4f-884e-4ac4-b64d-4e71e74c29d8` model=ridge tier=0 target=xs_rank pf=0.546 n=125836 gates=FAIL

## [INFO] 2026-08-02 10:45:34 UTC (tier 0)

trial `4b633ca9-138a-4f98-bc75-b0829652f0b3` model=lgbm_regressor tier=0 target=xs_rank pf=0.544 n=121498 gates=FAIL

## [INFO] 2026-08-02 10:45:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.95943 skill_surrogate=-0.95943

## [INFO] 2026-08-02 10:45:38 UTC (tier 0)

trial `436e3ed0-fa23-48c0-bc84-d9d50079304e` model=lgbm_classifier tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:45:38 UTC (tier 0)

Hunt complete: {"generation_id": "auto_077_ETHUSDT_15m_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:45:38 UTC (tier 0)

AUTONOMY screen auto_077_ETHUSDT_15m_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.5551435152352238 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:45:38 UTC (tier 0)

START gen=auto_078_SOLUSDT_15m_xs_rank_xs_v1 SOLUSDT 15m target=xs_rank space=xs_v1

## [INFO] 2026-08-02 10:45:51 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.69857527621798e-12, 'circular_shift': 9.69857527621798e-12, 'fourier_phase': 9.69857527621798e-12, 'row_shuffle': 9.69857527621798e-12} passed=False

## [INFO] 2026-08-02 10:46:01 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:46:01 UTC (tier 0)

trial `bbc71b02-d258-49cc-b076-72cb51b9b85a` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:46:02 UTC (tier 0)

trial `2f649bd0-fd7c-4afe-97a5-1c177ad31d4a` model=ridge tier=0 target=xs_rank pf=0.693 n=44219 gates=FAIL

## [INFO] 2026-08-02 10:46:08 UTC (tier 0)

trial `f10b7ef4-22af-432f-8a99-83e92418a25e` model=lgbm_regressor tier=0 target=xs_rank pf=0.697 n=40267 gates=FAIL

## [INFO] 2026-08-02 10:46:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.76759 skill_surrogate=-0.76759

## [INFO] 2026-08-02 10:46:10 UTC (tier 0)

trial `c0661afd-4c7d-4445-b8e5-591d0078528c` model=lgbm_classifier tier=0 target=xs_rank pf=0.692 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:46:10 UTC (tier 0)

Hunt complete: {"generation_id": "auto_078_SOLUSDT_15m_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:46:10 UTC (tier 0)

AUTONOMY screen auto_078_SOLUSDT_15m_xs_rank_xs_v1 tier=0 proxy_pf=0.6967328951023124 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:46:10 UTC (tier 0)

START gen=auto_079_SOLUSDT_15m_xs_rank_crosspair_v1 SOLUSDT 15m target=xs_rank space=crosspair_v1

## [INFO] 2026-08-02 10:46:14 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.69857527621798e-12, 'circular_shift': 9.69857527621798e-12, 'fourier_phase': 9.69857527621798e-12, 'row_shuffle': 9.69857527621798e-12} passed=False

## [INFO] 2026-08-02 10:46:22 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:46:22 UTC (tier 0)

trial `069e6657-077e-4c10-aa51-fe659b0910d2` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:46:22 UTC (tier 0)

trial `fa47ac94-85f3-4e3e-8924-7d49905a7c9c` model=ridge tier=0 target=xs_rank pf=0.718 n=26686 gates=FAIL

## [INFO] 2026-08-02 10:46:28 UTC (tier 0)

trial `39cd39d8-7267-40e8-a59b-6210eae7f172` model=lgbm_regressor tier=0 target=xs_rank pf=0.738 n=32429 gates=FAIL

## [INFO] 2026-08-02 10:46:30 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.76759 skill_surrogate=-0.76759

## [INFO] 2026-08-02 10:46:30 UTC (tier 0)

trial `a6dbd8c1-cfb7-4e86-89c5-630563d287f8` model=lgbm_classifier tier=0 target=xs_rank pf=0.692 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:46:30 UTC (tier 0)

Hunt complete: {"generation_id": "auto_079_SOLUSDT_15m_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:46:30 UTC (tier 0)

AUTONOMY screen auto_079_SOLUSDT_15m_xs_rank_crosspair_v1 tier=0 proxy_pf=0.7376375064539358 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:46:30 UTC (tier 0)

START gen=auto_080_SOLUSDT_15m_xs_rank_ohlcv_v1 SOLUSDT 15m target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-02 10:46:34 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.69857527621798e-12, 'circular_shift': 9.69857527621798e-12, 'fourier_phase': 9.69857527621798e-12, 'row_shuffle': 9.69857527621798e-12} passed=False

## [INFO] 2026-08-02 10:46:39 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:46:39 UTC (tier 0)

trial `4ecab431-90d6-4934-adfc-e330e1d922c6` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:46:40 UTC (tier 0)

trial `05d65b65-cd28-4a2a-939c-8e634747e0c4` model=ridge tier=0 target=xs_rank pf=0.740 n=35043 gates=FAIL

## [INFO] 2026-08-02 10:46:47 UTC (tier 0)

trial `8f20aea9-60df-400f-adb3-e229f209ea2f` model=lgbm_regressor tier=0 target=xs_rank pf=0.705 n=46551 gates=FAIL

## [INFO] 2026-08-02 10:46:51 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.76759 skill_surrogate=-0.76759

## [INFO] 2026-08-02 10:46:51 UTC (tier 0)

trial `6b8c6435-5e7b-4bbf-8744-245c85913c4b` model=lgbm_classifier tier=0 target=xs_rank pf=0.692 n=131421 gates=FAIL

## [INFO] 2026-08-02 10:46:51 UTC (tier 0)

Hunt complete: {"generation_id": "auto_080_SOLUSDT_15m_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:46:51 UTC (tier 0)

AUTONOMY screen auto_080_SOLUSDT_15m_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.7400009358868682 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:46:51 UTC (tier 0)

AUTONOMY non-directional block complete — draw conclusions only after reviewing xs_rank×xs_v1; predictability_passed=false across the board favours 'no edge in this feature/horizon space' over 'need a new model'

## [INFO] 2026-08-02 10:46:51 UTC (tier 0)

START gen=auto_081_BTCUSDT_1h_quantile_ohlcv_v1 BTCUSDT 1h target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:46:53 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.57226426217494e-09, 'circular_shift': 3.57226426217494e-09, 'fourier_phase': 3.57226426217494e-09, 'row_shuffle': 3.57226426217494e-09} passed=False

## [INFO] 2026-08-02 10:47:03 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:47:03 UTC (tier 0)

trial `ca87d7a2-e385-4c0e-a58f-d4f42b27e8ec` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:47:03 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00806 skill_surrogate=+0.00208

## [INFO] 2026-08-02 10:47:03 UTC (tier 0)

trial `a1c294be-0cec-423e-85bc-42054d7579eb` model=ridge tier=0 target=quantile pf=0.824 n=6802 gates=FAIL

## [INFO] 2026-08-02 10:47:09 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01158 skill_surrogate=-0.00797

## [INFO] 2026-08-02 10:47:09 UTC (tier 0)

trial `9c6674c7-e501-4f74-9541-46e218fbac0a` model=lgbm_regressor tier=0 target=quantile pf=0.769 n=4203 gates=FAIL

## [INFO] 2026-08-02 10:47:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.88126 skill_surrogate=-5.16850

## [INFO] 2026-08-02 10:47:28 UTC (tier 0)

trial `741b432c-dc47-40aa-aab2-bd9e7fec0f98` model=lgbm_classifier tier=0 target=quantile pf=0.713 n=32726 gates=FAIL

## [INFO] 2026-08-02 10:47:28 UTC (tier 0)

Hunt complete: {"generation_id": "auto_081_BTCUSDT_1h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:47:28 UTC (tier 0)

AUTONOMY screen auto_081_BTCUSDT_1h_quantile_ohlcv_v1 tier=0 proxy_pf=0.8241790932610158 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:47:28 UTC (tier 0)

START gen=auto_082_BTCUSDT_1h_quantile_indicators_v1 BTCUSDT 1h target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:47:30 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.5701032130575072e-09, 'circular_shift': 3.5701032130575072e-09, 'fourier_phase': 3.5701032130575072e-09, 'row_shuffle': 3.5701032130575072e-09} passed=False

## [INFO] 2026-08-02 10:47:35 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:47:35 UTC (tier 0)

trial `ad34a4e5-b118-4523-8898-b5fc2915ff32` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:47:35 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.03431 skill_surrogate=-0.00150

## [INFO] 2026-08-02 10:47:35 UTC (tier 0)

trial `7d5a8816-ee41-463a-9746-e5ffc3936e64` model=ridge tier=0 target=quantile pf=0.802 n=14771 gates=FAIL

## [INFO] 2026-08-02 10:47:40 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01395 skill_surrogate=-0.02015

## [INFO] 2026-08-02 10:47:40 UTC (tier 0)

trial `28c4d611-7803-4181-98d6-d29ae8c028cb` model=lgbm_regressor tier=0 target=quantile pf=0.729 n=12986 gates=FAIL

## [INFO] 2026-08-02 10:47:49 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-134.00153 skill_surrogate=-5.99580

## [INFO] 2026-08-02 10:47:49 UTC (tier 0)

trial `7b857e87-79be-4edd-aadd-6379b0c12cd6` model=lgbm_classifier tier=0 target=quantile pf=0.690 n=32709 gates=FAIL

## [INFO] 2026-08-02 10:47:49 UTC (tier 0)

Hunt complete: {"generation_id": "auto_082_BTCUSDT_1h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:47:49 UTC (tier 0)

AUTONOMY screen auto_082_BTCUSDT_1h_quantile_indicators_v1 tier=0 proxy_pf=0.8019564394607935 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:47:49 UTC (tier 0)

START gen=auto_083_BTCUSDT_1h_quantile_pivot_v1 BTCUSDT 1h target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:47:50 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.5743014104028248e-09, 'circular_shift': 3.5743014104028248e-09, 'fourier_phase': 3.5743014104028248e-09, 'row_shuffle': 3.5743014104028248e-09} passed=False

## [INFO] 2026-08-02 10:47:54 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:47:54 UTC (tier 0)

trial `2cc1ed66-3608-40a6-a493-dabdcb8ae838` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:47:55 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00596 skill_surrogate=-0.00093

## [INFO] 2026-08-02 10:47:55 UTC (tier 0)

trial `aafb1e62-6c15-4907-b977-87959971400d` model=ridge tier=0 target=quantile pf=0.782 n=2380 gates=FAIL

## [INFO] 2026-08-02 10:47:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02190 skill_surrogate=-0.00929

## [INFO] 2026-08-02 10:47:58 UTC (tier 0)

trial `2f9a184a-67d1-4c83-8e13-019ef464fcaa` model=lgbm_regressor tier=0 target=quantile pf=0.730 n=7895 gates=FAIL

## [INFO] 2026-08-02 10:48:08 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.89018 skill_surrogate=-5.26027

## [INFO] 2026-08-02 10:48:08 UTC (tier 0)

trial `84084e8c-0f20-4f41-88c1-09e23ed8e39c` model=lgbm_classifier tier=0 target=quantile pf=0.713 n=32840 gates=FAIL

## [INFO] 2026-08-02 10:48:08 UTC (tier 0)

Hunt complete: {"generation_id": "auto_083_BTCUSDT_1h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:48:08 UTC (tier 0)

AUTONOMY screen auto_083_BTCUSDT_1h_quantile_pivot_v1 tier=0 proxy_pf=0.7815190217194922 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:48:08 UTC (tier 0)

START gen=auto_084_ETHUSDT_1h_quantile_ohlcv_v1 ETHUSDT 1h target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:48:10 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.2880143335513026e-09, 'circular_shift': 2.2880143335513026e-09, 'fourier_phase': 2.2880143335513026e-09, 'row_shuffle': 2.2880143335513026e-09} passed=False

## [INFO] 2026-08-02 10:48:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:48:16 UTC (tier 0)

trial `674d0684-b821-4257-a757-03996dd20725` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:48:17 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00388 skill_surrogate=-0.00120

## [INFO] 2026-08-02 10:48:17 UTC (tier 0)

trial `995c8bf5-4c83-40ec-9703-62711305604b` model=ridge tier=0 target=quantile pf=0.836 n=11451 gates=FAIL

## [INFO] 2026-08-02 10:48:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00683 skill_surrogate=-0.00393

## [INFO] 2026-08-02 10:48:21 UTC (tier 0)

trial `81e866cf-a6fc-43e2-b664-cc35c286ddc0` model=lgbm_regressor tier=0 target=quantile pf=0.898 n=7192 gates=FAIL

## [INFO] 2026-08-02 10:48:29 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.69690 skill_surrogate=-2.37310

## [INFO] 2026-08-02 10:48:29 UTC (tier 0)

trial `029deaab-5a3d-4249-a00b-b9bcd5e26af8` model=lgbm_classifier tier=0 target=quantile pf=0.754 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:48:29 UTC (tier 0)

Hunt complete: {"generation_id": "auto_084_ETHUSDT_1h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:48:29 UTC (tier 0)

AUTONOMY screen auto_084_ETHUSDT_1h_quantile_ohlcv_v1 tier=0 proxy_pf=0.8983023017364945 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:48:29 UTC (tier 0)

START gen=auto_085_ETHUSDT_1h_quantile_indicators_v1 ETHUSDT 1h target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:48:30 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.2867210347499167e-09, 'circular_shift': 2.2867210347499167e-09, 'fourier_phase': 2.2867210347499167e-09, 'row_shuffle': 2.2867210347499167e-09} passed=False

## [INFO] 2026-08-02 10:48:33 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:48:33 UTC (tier 0)

trial `a0c9f068-3147-4522-82fe-582549effd4a` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:48:33 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00937 skill_surrogate=+0.00069

## [INFO] 2026-08-02 10:48:33 UTC (tier 0)

trial `b62eb97d-0b1f-411a-9d7d-505255a0e8f9` model=ridge tier=0 target=quantile pf=0.906 n=15512 gates=FAIL

## [INFO] 2026-08-02 10:48:37 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04618 skill_surrogate=-0.00491

## [INFO] 2026-08-02 10:48:37 UTC (tier 0)

trial `16a40fcc-326b-4faa-b311-ef8f019478d5` model=lgbm_regressor tier=0 target=quantile pf=0.844 n=19181 gates=FAIL

## [INFO] 2026-08-02 10:48:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.69431 skill_surrogate=-2.80776

## [INFO] 2026-08-02 10:48:44 UTC (tier 0)

trial `5bad3c17-7d32-45b0-a4ce-777dad26389c` model=lgbm_classifier tier=0 target=quantile pf=0.727 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:48:44 UTC (tier 0)

Hunt complete: {"generation_id": "auto_085_ETHUSDT_1h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:48:44 UTC (tier 0)

AUTONOMY screen auto_085_ETHUSDT_1h_quantile_indicators_v1 tier=0 proxy_pf=0.906214041880571 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:48:44 UTC (tier 0)

START gen=auto_086_ETHUSDT_1h_quantile_pivot_v1 ETHUSDT 1h target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:48:44 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.284545885800071e-09, 'circular_shift': 2.284545885800071e-09, 'fourier_phase': 2.284545885800071e-09, 'row_shuffle': 2.284545885800071e-09} passed=False

## [INFO] 2026-08-02 10:48:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:48:46 UTC (tier 0)

trial `cc73cae0-a921-4a7d-a6aa-221fef7cca30` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:48:46 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00410 skill_surrogate=-0.00087

## [INFO] 2026-08-02 10:48:46 UTC (tier 0)

trial `186f5c75-9ed4-481a-b362-bccd48533abe` model=ridge tier=0 target=quantile pf=0.732 n=4466 gates=FAIL

## [INFO] 2026-08-02 10:48:49 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01122 skill_surrogate=-0.00488

## [INFO] 2026-08-02 10:48:49 UTC (tier 0)

trial `f83191ea-44b3-42f4-98f5-0405219b10bb` model=lgbm_regressor tier=0 target=quantile pf=0.804 n=10953 gates=FAIL

## [INFO] 2026-08-02 10:48:54 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.71388 skill_surrogate=-2.33615

## [INFO] 2026-08-02 10:48:54 UTC (tier 0)

trial `87782326-df2a-425c-847d-a1f0c88f8918` model=lgbm_classifier tier=0 target=quantile pf=0.748 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:48:54 UTC (tier 0)

Hunt complete: {"generation_id": "auto_086_ETHUSDT_1h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:48:54 UTC (tier 0)

AUTONOMY screen auto_086_ETHUSDT_1h_quantile_pivot_v1 tier=0 proxy_pf=0.8044483162827601 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:48:55 UTC (tier 0)

START gen=auto_087_SOLUSDT_1h_quantile_ohlcv_v1 SOLUSDT 1h target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:48:56 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.33865651475685e-10, 'circular_shift': 9.33865651475685e-10, 'fourier_phase': 9.33865651475685e-10, 'row_shuffle': 9.33865651475685e-10} passed=False

## [INFO] 2026-08-02 10:48:59 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:48:59 UTC (tier 0)

trial `5e46c9b4-9562-45df-b4c6-27e5e2c65d6b` model=hist_mean tier=0 target=quantile pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-02 10:49:00 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00462 skill_surrogate=+0.00053

## [INFO] 2026-08-02 10:49:00 UTC (tier 0)

trial `59eb7fa2-d793-49d7-95e8-9c6c33dcc0bf` model=ridge tier=0 target=quantile pf=0.902 n=17004 gates=FAIL

## [INFO] 2026-08-02 10:49:03 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01179 skill_surrogate=-0.00431

## [INFO] 2026-08-02 10:49:03 UTC (tier 0)

trial `40dd24cd-61ba-47f1-8832-ef4d8968e65b` model=lgbm_regressor tier=0 target=quantile pf=0.846 n=12027 gates=FAIL

## [INFO] 2026-08-02 10:49:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.08167 skill_surrogate=-1.53531

## [INFO] 2026-08-02 10:49:14 UTC (tier 0)

trial `d6441919-252f-4709-b6e7-19cae5cd0613` model=lgbm_classifier tier=0 target=quantile pf=0.874 n=32854 gates=FAIL

## [INFO] 2026-08-02 10:49:14 UTC (tier 0)

Hunt complete: {"generation_id": "auto_087_SOLUSDT_1h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:49:14 UTC (tier 0)

AUTONOMY screen auto_087_SOLUSDT_1h_quantile_ohlcv_v1 tier=0 proxy_pf=0.9022273781710141 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:49:14 UTC (tier 0)

START gen=auto_088_SOLUSDT_1h_quantile_indicators_v1 SOLUSDT 1h target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:49:16 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.349697682736746e-10, 'circular_shift': 9.349697682736746e-10, 'fourier_phase': 9.349697682736746e-10, 'row_shuffle': 9.349697682736746e-10} passed=False

## [INFO] 2026-08-02 10:49:20 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:49:20 UTC (tier 0)

trial `a5ffbb8c-5a2a-445e-9add-18918ea0a327` model=hist_mean tier=0 target=quantile pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-02 10:49:20 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01219 skill_surrogate=-0.00289

## [INFO] 2026-08-02 10:49:20 UTC (tier 0)

trial `a4596ba6-a9ea-4d31-8afd-58bf3c9ecccb` model=ridge tier=0 target=quantile pf=0.884 n=22651 gates=FAIL

## [INFO] 2026-08-02 10:49:24 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01149 skill_surrogate=-0.00429

## [INFO] 2026-08-02 10:49:24 UTC (tier 0)

trial `d2394081-30b9-47f0-8fdc-7e51660d1f3c` model=lgbm_regressor tier=0 target=quantile pf=0.958 n=15633 gates=FAIL

## [INFO] 2026-08-02 10:49:33 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.05580 skill_surrogate=-1.93033

## [INFO] 2026-08-02 10:49:33 UTC (tier 0)

trial `2c817458-57bc-450b-86c9-fcd9c25f5451` model=lgbm_classifier tier=0 target=quantile pf=0.860 n=32699 gates=FAIL

## [INFO] 2026-08-02 10:49:33 UTC (tier 0)

Hunt complete: {"generation_id": "auto_088_SOLUSDT_1h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:49:33 UTC (tier 0)

AUTONOMY screen auto_088_SOLUSDT_1h_quantile_indicators_v1 tier=0 proxy_pf=0.958342346586077 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:49:33 UTC (tier 0)

START gen=auto_089_SOLUSDT_1h_quantile_pivot_v1 SOLUSDT 1h target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:49:33 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.31883903376729e-10, 'circular_shift': 9.31883903376729e-10, 'fourier_phase': 9.31883903376729e-10, 'row_shuffle': 9.31883903376729e-10} passed=False

## [INFO] 2026-08-02 10:49:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:49:36 UTC (tier 0)

trial `d26d22ca-9ed8-4b42-ac4c-e4dcf1ccf344` model=hist_mean tier=0 target=quantile pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-02 10:49:36 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00186 skill_surrogate=-0.00048

## [INFO] 2026-08-02 10:49:36 UTC (tier 0)

trial `6a347c08-2f93-4558-a8f5-230bc6cbdebc` model=ridge tier=0 target=quantile pf=0.745 n=8221 gates=FAIL

## [INFO] 2026-08-02 10:49:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01905 skill_surrogate=-0.00702

## [INFO] 2026-08-02 10:49:38 UTC (tier 0)

trial `520248c8-9ca0-4b7d-bd6b-fc9b11e51202` model=lgbm_regressor tier=0 target=quantile pf=0.890 n=17033 gates=FAIL

## [INFO] 2026-08-02 10:49:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.08766 skill_surrogate=-1.57613

## [INFO] 2026-08-02 10:49:43 UTC (tier 0)

trial `8f72312b-50ab-484f-92ad-b13180217bed` model=lgbm_classifier tier=0 target=quantile pf=0.840 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:49:43 UTC (tier 0)

Hunt complete: {"generation_id": "auto_089_SOLUSDT_1h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:49:43 UTC (tier 0)

AUTONOMY screen auto_089_SOLUSDT_1h_quantile_pivot_v1 tier=0 proxy_pf=0.8901217750441386 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:49:43 UTC (tier 0)

START gen=auto_090_BTCUSDT_4h_quantile_ohlcv_v1 BTCUSDT 4h target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:49:44 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.749191371393295e-10, 'circular_shift': 8.749191371393295e-10, 'fourier_phase': 8.749191371393295e-10, 'row_shuffle': 8.749191371393295e-10} passed=False

## [INFO] 2026-08-02 10:49:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:49:46 UTC (tier 0)

trial `fb0fc79e-8476-43fa-8301-b3561c78af17` model=hist_mean tier=0 target=quantile pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-02 10:49:46 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00342 skill_surrogate=-0.00882

## [INFO] 2026-08-02 10:49:46 UTC (tier 0)

trial `619c93d8-0014-423b-b38b-aeb8ed46bbea` model=ridge tier=0 target=quantile pf=1.018 n=5223 gates=FAIL

## [INFO] 2026-08-02 10:49:48 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04444 skill_surrogate=-0.02884

## [INFO] 2026-08-02 10:49:49 UTC (tier 0)

trial `475fc96b-1261-4073-a24d-58e4133ad227` model=lgbm_regressor tier=0 target=quantile pf=0.864 n=5565 gates=FAIL

## [INFO] 2026-08-02 10:49:53 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.22449 skill_surrogate=-4.36823

## [INFO] 2026-08-02 10:49:53 UTC (tier 0)

trial `f7b2d4d6-7631-4800-b0aa-a961fa0e643f` model=lgbm_classifier tier=0 target=quantile pf=0.834 n=8204 gates=FAIL

## [INFO] 2026-08-02 10:49:53 UTC (tier 0)

Hunt complete: {"generation_id": "auto_090_BTCUSDT_4h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:49:53 UTC (tier 0)

AUTONOMY screen auto_090_BTCUSDT_4h_quantile_ohlcv_v1 tier=0 proxy_pf=1.0176857259100298 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:49:53 UTC (tier 0)

START gen=auto_091_BTCUSDT_4h_quantile_indicators_v1 BTCUSDT 4h target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:49:54 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.808362927936741e-10, 'circular_shift': 8.808362927936741e-10, 'fourier_phase': 8.808362927936741e-10, 'row_shuffle': 8.808362927936741e-10} passed=False

## [INFO] 2026-08-02 10:49:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:49:55 UTC (tier 0)

trial `401e0142-3a1e-44cd-96b9-f6b6c706e406` model=hist_mean tier=0 target=quantile pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-02 10:49:55 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.04064 skill_surrogate=-0.00925

## [INFO] 2026-08-02 10:49:55 UTC (tier 0)

trial `3bbedd30-a2c4-46f1-904b-f35c0a80daea` model=ridge tier=0 target=quantile pf=0.827 n=6439 gates=FAIL

## [INFO] 2026-08-02 10:49:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.05483 skill_surrogate=-0.04181

## [INFO] 2026-08-02 10:49:59 UTC (tier 0)

trial `605e44e2-d622-4304-a3e7-503d4d8c3292` model=lgbm_regressor tier=0 target=quantile pf=0.800 n=7028 gates=FAIL

## [INFO] 2026-08-02 10:50:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16491 skill_surrogate=-6.95168

## [INFO] 2026-08-02 10:50:11 UTC (tier 0)

trial `f520223b-7f24-4495-8c32-d31b62f75d7c` model=lgbm_classifier tier=0 target=quantile pf=0.817 n=8213 gates=FAIL

## [INFO] 2026-08-02 10:50:11 UTC (tier 0)

Hunt complete: {"generation_id": "auto_091_BTCUSDT_4h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:50:11 UTC (tier 0)

AUTONOMY screen auto_091_BTCUSDT_4h_quantile_indicators_v1 tier=0 proxy_pf=0.8266177086033331 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:50:11 UTC (tier 0)

START gen=auto_092_BTCUSDT_4h_quantile_pivot_v1 BTCUSDT 4h target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:50:12 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.773649584625787e-10, 'circular_shift': 8.773649584625787e-10, 'fourier_phase': 8.773649584625787e-10, 'row_shuffle': 8.773649584625787e-10} passed=False

## [INFO] 2026-08-02 10:50:13 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:50:13 UTC (tier 0)

trial `d9d6c840-73d3-4d90-8086-8c96c720b852` model=hist_mean tier=0 target=quantile pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-02 10:50:13 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00530 skill_surrogate=+0.00020

## [INFO] 2026-08-02 10:50:13 UTC (tier 0)

trial `a4e06fd2-90e4-4a6d-890d-fc1606a7a1c8` model=ridge tier=0 target=quantile pf=0.842 n=2815 gates=FAIL

## [INFO] 2026-08-02 10:50:15 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03841 skill_surrogate=-0.00734

## [INFO] 2026-08-02 10:50:15 UTC (tier 0)

trial `849d57c5-444d-48bd-8a3e-f3b891f53ae2` model=lgbm_regressor tier=0 target=quantile pf=0.842 n=5743 gates=FAIL

## [INFO] 2026-08-02 10:50:20 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16893 skill_surrogate=-4.75857

## [INFO] 2026-08-02 10:50:20 UTC (tier 0)

trial `4095217b-9ea0-4e8e-ab81-d3efd59495d7` model=lgbm_classifier tier=0 target=quantile pf=0.846 n=8210 gates=FAIL

## [INFO] 2026-08-02 10:50:20 UTC (tier 0)

Hunt complete: {"generation_id": "auto_092_BTCUSDT_4h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:50:21 UTC (tier 0)

AUTONOMY screen auto_092_BTCUSDT_4h_quantile_pivot_v1 tier=0 proxy_pf=0.8464266512174518 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:50:21 UTC (tier 0)

START gen=auto_093_ETHUSDT_4h_quantile_ohlcv_v1 ETHUSDT 4h target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:50:21 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 5.530373936579736e-10, 'circular_shift': 5.530373936579736e-10, 'fourier_phase': 5.530373936579736e-10, 'row_shuffle': 5.530373936579736e-10} passed=False

## [INFO] 2026-08-02 10:50:22 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:50:22 UTC (tier 0)

trial `1a679421-64d0-4ea9-9407-5e9c00a762dc` model=hist_mean tier=0 target=quantile pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:22 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00136 skill_surrogate=-0.00007

## [INFO] 2026-08-02 10:50:22 UTC (tier 0)

trial `ea06f8d3-23c2-4a4f-902b-5aacaa6fe9ee` model=ridge tier=0 target=quantile pf=0.946 n=6072 gates=FAIL

## [INFO] 2026-08-02 10:50:24 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02168 skill_surrogate=-0.00761

## [INFO] 2026-08-02 10:50:24 UTC (tier 0)

trial `e62bfe2a-a749-45f0-8377-02d08e409f03` model=lgbm_regressor tier=0 target=quantile pf=0.930 n=6253 gates=FAIL

## [INFO] 2026-08-02 10:50:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.11179 skill_surrogate=-2.38091

## [INFO] 2026-08-02 10:50:32 UTC (tier 0)

trial `bd59a44f-2e0c-47a9-863b-d166b73d4499` model=lgbm_classifier tier=0 target=quantile pf=0.903 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:32 UTC (tier 0)

Hunt complete: {"generation_id": "auto_093_ETHUSDT_4h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:50:32 UTC (tier 0)

AUTONOMY screen auto_093_ETHUSDT_4h_quantile_ohlcv_v1 tier=0 proxy_pf=0.9460121773106233 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:50:32 UTC (tier 0)

START gen=auto_094_ETHUSDT_4h_quantile_indicators_v1 ETHUSDT 4h target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:50:33 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 5.509456224572773e-10, 'circular_shift': 5.509456224572773e-10, 'fourier_phase': 5.509456224572773e-10, 'row_shuffle': 5.509456224572773e-10} passed=False

## [INFO] 2026-08-02 10:50:34 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:50:34 UTC (tier 0)

trial `32079495-9597-4eff-86df-b7b444e51e90` model=hist_mean tier=0 target=quantile pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:34 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00167 skill_surrogate=-0.00523

## [INFO] 2026-08-02 10:50:34 UTC (tier 0)

trial `6878f44b-172b-4900-8281-d9fbac553807` model=ridge tier=0 target=quantile pf=0.888 n=6885 gates=FAIL

## [INFO] 2026-08-02 10:50:36 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03816 skill_surrogate=-0.01158

## [INFO] 2026-08-02 10:50:36 UTC (tier 0)

trial `053859b9-98d0-4989-8a71-755fbd595cbc` model=lgbm_regressor tier=0 target=quantile pf=0.918 n=7147 gates=FAIL

## [INFO] 2026-08-02 10:50:41 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.01013 skill_surrogate=-2.65853

## [INFO] 2026-08-02 10:50:41 UTC (tier 0)

trial `6aee7dab-6915-4617-8628-0a4cf26a3e7d` model=lgbm_classifier tier=0 target=quantile pf=0.915 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:41 UTC (tier 0)

Hunt complete: {"generation_id": "auto_094_ETHUSDT_4h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:50:41 UTC (tier 0)

AUTONOMY screen auto_094_ETHUSDT_4h_quantile_indicators_v1 tier=0 proxy_pf=0.9200856060065038 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:50:41 UTC (tier 0)

START gen=auto_095_ETHUSDT_4h_quantile_pivot_v1 ETHUSDT 4h target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:50:41 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 5.546206827133915e-10, 'circular_shift': 5.546206827133915e-10, 'fourier_phase': 5.546206827133915e-10, 'row_shuffle': 5.546206827133915e-10} passed=False

## [INFO] 2026-08-02 10:50:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:50:42 UTC (tier 0)

trial `cfe6dc3d-9af3-4f67-835d-c0ab19396ea5` model=hist_mean tier=0 target=quantile pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:42 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00295 skill_surrogate=+0.00031

## [INFO] 2026-08-02 10:50:42 UTC (tier 0)

trial `588122f6-445f-4d4d-9d3e-393862b4d4d8` model=ridge tier=0 target=quantile pf=0.951 n=6014 gates=FAIL

## [INFO] 2026-08-02 10:50:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01431 skill_surrogate=-0.01088

## [INFO] 2026-08-02 10:50:44 UTC (tier 0)

trial `4a6b067d-0a8d-417a-8aeb-ad9200b83c89` model=lgbm_regressor tier=0 target=quantile pf=0.930 n=6824 gates=FAIL

## [INFO] 2026-08-02 10:50:47 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.01322 skill_surrogate=-2.68694

## [INFO] 2026-08-02 10:50:47 UTC (tier 0)

trial `5f3fb4ed-0979-44db-85d4-b7e8fd7874b6` model=lgbm_classifier tier=0 target=quantile pf=0.905 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:47 UTC (tier 0)

Hunt complete: {"generation_id": "auto_095_ETHUSDT_4h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:50:47 UTC (tier 0)

AUTONOMY screen auto_095_ETHUSDT_4h_quantile_pivot_v1 tier=0 proxy_pf=0.9510175596610267 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:50:47 UTC (tier 0)

START gen=auto_096_SOLUSDT_4h_quantile_ohlcv_v1 SOLUSDT 4h target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:50:47 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.3751911548686166e-10, 'circular_shift': 2.3751911548686166e-10, 'fourier_phase': 2.3751911548686166e-10, 'row_shuffle': 2.3751911548686166e-10} passed=False

## [INFO] 2026-08-02 10:50:48 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:50:48 UTC (tier 0)

trial `59d4a0f9-9674-4e7a-afc9-de88ee206872` model=hist_mean tier=0 target=quantile pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:48 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01743 skill_surrogate=-0.00753

## [INFO] 2026-08-02 10:50:48 UTC (tier 0)

trial `72cf045e-78e5-494d-a7bc-69be47c6cca5` model=ridge tier=0 target=quantile pf=0.997 n=7292 gates=FAIL

## [INFO] 2026-08-02 10:50:49 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02577 skill_surrogate=-0.02091

## [INFO] 2026-08-02 10:50:49 UTC (tier 0)

trial `fb19e93c-12f7-4ed4-b495-9957c8c418f4` model=lgbm_regressor tier=0 target=quantile pf=0.958 n=7161 gates=FAIL

## [INFO] 2026-08-02 10:50:54 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.52165 skill_surrogate=-1.47638

## [INFO] 2026-08-02 10:50:54 UTC (tier 0)

trial `af70d4ee-7180-4cee-a4cc-fd511651af7f` model=lgbm_classifier tier=0 target=quantile pf=0.989 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:54 UTC (tier 0)

Hunt complete: {"generation_id": "auto_096_SOLUSDT_4h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:50:54 UTC (tier 0)

AUTONOMY screen auto_096_SOLUSDT_4h_quantile_ohlcv_v1 tier=0 proxy_pf=0.9965702191452582 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:50:54 UTC (tier 0)

START gen=auto_097_SOLUSDT_4h_quantile_indicators_v1 SOLUSDT 4h target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:50:55 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.3690038819523807e-10, 'circular_shift': 2.3690038819523807e-10, 'fourier_phase': 2.3690038819523807e-10, 'row_shuffle': 2.3690038819523807e-10} passed=False

## [INFO] 2026-08-02 10:50:56 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 10:50:56 UTC (tier 0)

trial `8fb1be62-9c4b-4b0e-b2f5-529e835bab7b` model=hist_mean tier=0 target=quantile pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:50:56 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00250 skill_surrogate=-0.01403

## [INFO] 2026-08-02 10:50:56 UTC (tier 0)

trial `c4fe3afb-7d4b-424f-95b6-deec4c57744c` model=ridge tier=0 target=quantile pf=1.042 n=7405 gates=FAIL

## [INFO] 2026-08-02 10:50:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01843 skill_surrogate=-0.01847

## [INFO] 2026-08-02 10:50:59 UTC (tier 0)

trial `c775d100-0544-4476-8843-694c02e93a01` model=lgbm_regressor tier=0 target=quantile pf=0.951 n=7318 gates=FAIL

## [INFO] 2026-08-02 10:51:05 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.44360 skill_surrogate=-2.74855

## [INFO] 2026-08-02 10:51:05 UTC (tier 0)

trial `09e03107-0837-406a-b9a0-dbcb3ca446c9` model=lgbm_classifier tier=0 target=quantile pf=0.918 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:51:05 UTC (tier 0)

Hunt complete: {"generation_id": "auto_097_SOLUSDT_4h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:51:05 UTC (tier 0)

AUTONOMY screen auto_097_SOLUSDT_4h_quantile_indicators_v1 tier=0 proxy_pf=1.0422191080060303 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:51:05 UTC (tier 0)

START gen=auto_098_SOLUSDT_4h_quantile_pivot_v1 SOLUSDT 4h target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:51:05 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.358924167111809e-10, 'circular_shift': 2.358924167111809e-10, 'fourier_phase': 2.358924167111809e-10, 'row_shuffle': 2.358924167111809e-10} passed=False

## [INFO] 2026-08-02 10:51:07 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:51:07 UTC (tier 0)

trial `974ed7ee-4319-48c1-8f7b-587a4b8c5a83` model=hist_mean tier=0 target=quantile pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:51:07 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00757 skill_surrogate=-0.00052

## [INFO] 2026-08-02 10:51:07 UTC (tier 0)

trial `56f5101a-fcb2-417d-820f-e2d10c3ea925` model=ridge tier=0 target=quantile pf=0.975 n=6843 gates=FAIL

## [INFO] 2026-08-02 10:51:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04768 skill_surrogate=-0.01214

## [INFO] 2026-08-02 10:51:10 UTC (tier 0)

trial `81912137-fb96-4913-b92f-6004164c8ac8` model=lgbm_regressor tier=0 target=quantile pf=0.987 n=7360 gates=FAIL

## [INFO] 2026-08-02 10:51:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.44952 skill_surrogate=-2.25744

## [INFO] 2026-08-02 10:51:18 UTC (tier 0)

trial `3d5fdec4-7c37-4842-b0da-c57be7a1bddf` model=lgbm_classifier tier=0 target=quantile pf=0.921 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:51:18 UTC (tier 0)

Hunt complete: {"generation_id": "auto_098_SOLUSDT_4h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:51:18 UTC (tier 0)

AUTONOMY screen auto_098_SOLUSDT_4h_quantile_pivot_v1 tier=0 proxy_pf=0.9868588821857988 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:51:18 UTC (tier 0)

START gen=auto_099_BTCUSDT_15m_quantile_ohlcv_v1 BTCUSDT 15m target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:51:21 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3483151373172575e-08, 'circular_shift': 1.3483151373172575e-08, 'fourier_phase': 1.3483151373172575e-08, 'row_shuffle': 1.3483151373172575e-08} passed=False

## [INFO] 2026-08-02 10:51:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:51:57 UTC (tier 0)

trial `cfa97665-28d0-4555-92be-679771dce6d6` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:51:58 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00863 skill_surrogate=+0.00078

## [INFO] 2026-08-02 10:51:58 UTC (tier 0)

trial `a14c66b5-9169-452c-958a-f70a09ddd81e` model=ridge tier=0 target=quantile pf=1.045 n=790 gates=FAIL

## [INFO] 2026-08-02 10:52:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00290 skill_surrogate=-0.00196

## [INFO] 2026-08-02 10:52:06 UTC (tier 0)

trial `52ae6f68-63b6-4e94-bd45-1efe2910ea0b` model=lgbm_regressor tier=0 target=quantile pf=0.810 n=2069 gates=FAIL

## [INFO] 2026-08-02 10:52:19 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-278.14698 skill_surrogate=-5.70952

## [INFO] 2026-08-02 10:52:19 UTC (tier 0)

trial `004f51e4-e535-4f17-ad4c-5d2126a3b8e1` model=lgbm_classifier tier=0 target=quantile pf=0.467 n=130835 gates=FAIL

## [INFO] 2026-08-02 10:52:19 UTC (tier 0)

Hunt complete: {"generation_id": "auto_099_BTCUSDT_15m_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:52:19 UTC (tier 0)

AUTONOMY screen auto_099_BTCUSDT_15m_quantile_ohlcv_v1 tier=0 proxy_pf=1.0445968814778723 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:52:19 UTC (tier 0)

START gen=auto_100_BTCUSDT_15m_quantile_indicators_v1 BTCUSDT 15m target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:52:22 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3484098726479488e-08, 'circular_shift': 1.3484098726479488e-08, 'fourier_phase': 1.348409877088841e-08, 'row_shuffle': 1.3484098726479488e-08} passed=False

## [INFO] 2026-08-02 10:52:34 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:52:34 UTC (tier 0)

trial `e05e0aee-74ef-4630-a799-95f62ea4be86` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:52:35 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01350 skill_surrogate=-0.00078

## [INFO] 2026-08-02 10:52:35 UTC (tier 0)

trial `4f2605a3-8cb5-46c6-bd21-34e83cc6a5d5` model=ridge tier=0 target=quantile pf=0.765 n=4559 gates=FAIL

## [INFO] 2026-08-02 10:52:41 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00271 skill_surrogate=-0.00586

## [INFO] 2026-08-02 10:52:41 UTC (tier 0)

trial `d0570bef-cd04-484a-9588-595e3c2266fd` model=lgbm_regressor tier=0 target=quantile pf=0.511 n=11633 gates=FAIL

## [INFO] 2026-08-02 10:52:53 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-277.38180 skill_surrogate=-7.46693

## [INFO] 2026-08-02 10:52:53 UTC (tier 0)

trial `54effab6-7032-4e0d-9034-9a18e9f9cbbd` model=lgbm_classifier tier=0 target=quantile pf=0.462 n=130999 gates=FAIL

## [INFO] 2026-08-02 10:52:53 UTC (tier 0)

Hunt complete: {"generation_id": "auto_100_BTCUSDT_15m_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:52:53 UTC (tier 0)

AUTONOMY screen auto_100_BTCUSDT_15m_quantile_indicators_v1 tier=0 proxy_pf=0.7654162061547987 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:52:53 UTC (tier 0)

START gen=auto_101_BTCUSDT_15m_quantile_pivot_v1 BTCUSDT 15m target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:52:56 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.348536438072756e-08, 'circular_shift': 1.348536438072756e-08, 'fourier_phase': 1.348536438072756e-08, 'row_shuffle': 1.348536438072756e-08} passed=False

## [INFO] 2026-08-02 10:53:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:53:08 UTC (tier 0)

trial `750e7442-f7e1-4111-95dd-bba1b725f6b6` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:53:09 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00154 skill_surrogate=-0.00009

## [INFO] 2026-08-02 10:53:09 UTC (tier 0)

trial `73effd78-8289-4e81-b532-bd0b86f320da` model=ridge tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:53:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00626 skill_surrogate=-0.00212

## [INFO] 2026-08-02 10:53:12 UTC (tier 0)

trial `8db87de9-ebee-4871-bb76-697015a248fc` model=lgbm_regressor tier=0 target=quantile pf=0.598 n=3861 gates=FAIL

## [INFO] 2026-08-02 10:53:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-278.16756 skill_surrogate=-6.05904

## [INFO] 2026-08-02 10:53:21 UTC (tier 0)

trial `b22ea14d-1143-4a83-b319-097f2925439a` model=lgbm_classifier tier=0 target=quantile pf=0.466 n=131317 gates=FAIL

## [INFO] 2026-08-02 10:53:21 UTC (tier 0)

Hunt complete: {"generation_id": "auto_101_BTCUSDT_15m_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:53:21 UTC (tier 0)

AUTONOMY screen auto_101_BTCUSDT_15m_quantile_pivot_v1 tier=0 proxy_pf=0.5975835294509682 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:53:21 UTC (tier 0)

START gen=auto_102_ETHUSDT_15m_quantile_ohlcv_v1 ETHUSDT 15m target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:53:23 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.470337320432009e-09, 'circular_shift': 8.470337320432009e-09, 'fourier_phase': 8.470337320432009e-09, 'row_shuffle': 8.470337320432009e-09} passed=False

## [INFO] 2026-08-02 10:53:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:53:36 UTC (tier 0)

trial `760eabba-823a-4f89-987c-e364b56d0f00` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:53:37 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00542 skill_surrogate=-0.00009

## [INFO] 2026-08-02 10:53:37 UTC (tier 0)

trial `056c1d28-7cf5-4808-8b99-1d6a7e1b650c` model=ridge tier=0 target=quantile pf=0.881 n=3512 gates=FAIL

## [INFO] 2026-08-02 10:53:42 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00470 skill_surrogate=-0.00053

## [INFO] 2026-08-02 10:53:42 UTC (tier 0)

trial `945b8a2d-d3fb-44cf-bffa-98afeb9bf213` model=lgbm_regressor tier=0 target=quantile pf=1.022 n=2467 gates=FAIL

## [INFO] 2026-08-02 10:53:55 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.36925 skill_surrogate=-3.44623

## [INFO] 2026-08-02 10:53:55 UTC (tier 0)

trial `e426b01c-256c-415e-9ed7-6fd394927ff9` model=lgbm_classifier tier=0 target=quantile pf=0.545 n=131409 gates=FAIL

## [INFO] 2026-08-02 10:53:55 UTC (tier 0)

Hunt complete: {"generation_id": "auto_102_ETHUSDT_15m_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:53:55 UTC (tier 0)

AUTONOMY screen auto_102_ETHUSDT_15m_quantile_ohlcv_v1 tier=0 proxy_pf=1.022178284329403 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:53:55 UTC (tier 0)

START gen=auto_103_ETHUSDT_15m_quantile_indicators_v1 ETHUSDT 15m target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:53:59 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.471199297588328e-09, 'circular_shift': 8.471199297588328e-09, 'fourier_phase': 8.471199297588328e-09, 'row_shuffle': 8.471199297588328e-09} passed=False

## [INFO] 2026-08-02 10:54:11 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:54:11 UTC (tier 0)

trial `dfddbbbf-a651-4345-bed4-bb1d1a540bf8` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:54:12 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00595 skill_surrogate=-0.00037

## [INFO] 2026-08-02 10:54:12 UTC (tier 0)

trial `4f815a86-e98f-4885-a993-c81b2870597b` model=ridge tier=0 target=quantile pf=0.743 n=14768 gates=FAIL

## [INFO] 2026-08-02 10:54:16 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00380 skill_surrogate=-0.00330

## [INFO] 2026-08-02 10:54:16 UTC (tier 0)

trial `4dece99b-7116-4b96-b9fb-30c02f38e661` model=lgbm_regressor tier=0 target=quantile pf=0.689 n=20360 gates=FAIL

## [INFO] 2026-08-02 10:54:29 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.35786 skill_surrogate=-3.25835

## [INFO] 2026-08-02 10:54:29 UTC (tier 0)

trial `3f0c8ee6-a579-4cf9-b95e-86d7d8f2ca4a` model=lgbm_classifier tier=0 target=quantile pf=0.540 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:54:29 UTC (tier 0)

Hunt complete: {"generation_id": "auto_103_ETHUSDT_15m_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:54:29 UTC (tier 0)

AUTONOMY screen auto_103_ETHUSDT_15m_quantile_indicators_v1 tier=0 proxy_pf=0.7433357706857794 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:54:29 UTC (tier 0)

START gen=auto_104_ETHUSDT_15m_quantile_pivot_v1 ETHUSDT 15m target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:54:31 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.446917609816751e-09, 'circular_shift': 8.446917609816751e-09, 'fourier_phase': 8.446917720839053e-09, 'row_shuffle': 8.446917609816751e-09} passed=False

## [INFO] 2026-08-02 10:54:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:54:42 UTC (tier 0)

trial `b04f83ce-6931-4202-a7b3-5db1fa028658` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:54:42 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00074 skill_surrogate=-0.00017

## [INFO] 2026-08-02 10:54:42 UTC (tier 0)

trial `38712f56-3d98-4a01-b331-ffc39361227a` model=ridge tier=0 target=quantile pf=0.714 n=216 gates=FAIL

## [INFO] 2026-08-02 10:54:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00242 skill_surrogate=-0.00063

## [INFO] 2026-08-02 10:54:45 UTC (tier 0)

trial `8b36170c-d0c2-4686-a227-871aa1a94afe` model=lgbm_regressor tier=0 target=quantile pf=0.609 n=4625 gates=FAIL

## [INFO] 2026-08-02 10:54:51 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.38200 skill_surrogate=-3.43643

## [INFO] 2026-08-02 10:54:51 UTC (tier 0)

trial `8505315e-094c-45d9-9fca-9db5ac728ec8` model=lgbm_classifier tier=0 target=quantile pf=0.538 n=131424 gates=FAIL

## [INFO] 2026-08-02 10:54:51 UTC (tier 0)

Hunt complete: {"generation_id": "auto_104_ETHUSDT_15m_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:54:51 UTC (tier 0)

AUTONOMY screen auto_104_ETHUSDT_15m_quantile_pivot_v1 tier=0 proxy_pf=0.7137730515448887 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:54:51 UTC (tier 0)

START gen=auto_105_SOLUSDT_15m_quantile_ohlcv_v1 SOLUSDT 15m target=quantile space=ohlcv_v1

## [INFO] 2026-08-02 10:54:53 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.4974860785297324e-09, 'circular_shift': 3.4974860785297324e-09, 'fourier_phase': 3.4974860785297324e-09, 'row_shuffle': 3.4974860785297324e-09} passed=False

## [INFO] 2026-08-02 10:54:56 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:54:56 UTC (tier 0)

trial `a4272acb-23af-4154-83fb-77add2cd4803` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:54:57 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00469 skill_surrogate=-0.00019

## [INFO] 2026-08-02 10:54:57 UTC (tier 0)

trial `ed98b847-5abb-4ba4-b954-311e96ae48ed` model=ridge tier=0 target=quantile pf=0.830 n=17256 gates=FAIL

## [INFO] 2026-08-02 10:55:03 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00193 skill_surrogate=-0.00245

## [INFO] 2026-08-02 10:55:03 UTC (tier 0)

trial `d8661114-eff8-448a-b962-11df27753910` model=lgbm_regressor tier=0 target=quantile pf=1.030 n=5137 gates=FAIL

## [INFO] 2026-08-02 10:55:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.25482 skill_surrogate=-1.47565

## [INFO] 2026-08-02 10:55:14 UTC (tier 0)

trial `ac2c4f3c-530f-422a-b8f8-83abc5f31d6d` model=lgbm_classifier tier=0 target=quantile pf=0.698 n=131420 gates=FAIL

## [INFO] 2026-08-02 10:55:14 UTC (tier 0)

Hunt complete: {"generation_id": "auto_105_SOLUSDT_15m_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:55:14 UTC (tier 0)

AUTONOMY screen auto_105_SOLUSDT_15m_quantile_ohlcv_v1 tier=0 proxy_pf=1.0303105414187936 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:55:14 UTC (tier 0)

START gen=auto_106_SOLUSDT_15m_quantile_indicators_v1 SOLUSDT 15m target=quantile space=indicators_v1

## [INFO] 2026-08-02 10:55:16 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.4967430062593508e-09, 'circular_shift': 3.4967430062593508e-09, 'fourier_phase': 3.4967430062593508e-09, 'row_shuffle': 3.4967430062593508e-09} passed=False

## [INFO] 2026-08-02 10:55:19 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:55:19 UTC (tier 0)

trial `3e64d497-9a33-4e71-9da1-c5423b12fd44` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:55:20 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00278 skill_surrogate=-0.00123

## [INFO] 2026-08-02 10:55:20 UTC (tier 0)

trial `cffdea0b-17f1-4a92-9348-e694b494843d` model=ridge tier=0 target=quantile pf=0.805 n=27631 gates=FAIL

## [INFO] 2026-08-02 10:55:24 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01027 skill_surrogate=-0.00022

## [INFO] 2026-08-02 10:55:24 UTC (tier 0)

trial `c85a7103-c25e-4037-8b11-a6450de32c1a` model=lgbm_regressor tier=0 target=quantile pf=0.774 n=30223 gates=FAIL

## [INFO] 2026-08-02 10:55:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.25741 skill_surrogate=-1.58664

## [INFO] 2026-08-02 10:55:38 UTC (tier 0)

trial `2aa53a6a-5250-40be-a2d3-c41cff8d7166` model=lgbm_classifier tier=0 target=quantile pf=0.687 n=129756 gates=FAIL

## [INFO] 2026-08-02 10:55:38 UTC (tier 0)

Hunt complete: {"generation_id": "auto_106_SOLUSDT_15m_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:55:38 UTC (tier 0)

AUTONOMY screen auto_106_SOLUSDT_15m_quantile_indicators_v1 tier=0 proxy_pf=0.8048929656613859 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:55:38 UTC (tier 0)

START gen=auto_107_SOLUSDT_15m_quantile_pivot_v1 SOLUSDT 15m target=quantile space=pivot_v1

## [INFO] 2026-08-02 10:55:39 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.4959626304953417e-09, 'circular_shift': 3.4959626304953417e-09, 'fourier_phase': 3.4959626304953417e-09, 'row_shuffle': 3.4959626304953417e-09} passed=False

## [INFO] 2026-08-02 10:55:41 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:55:41 UTC (tier 0)

trial `0c7e2ac4-8447-4b1b-9b22-b049994c6390` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:55:41 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00062 skill_surrogate=-0.00002

## [INFO] 2026-08-02 10:55:41 UTC (tier 0)

trial `6ca670b7-3c73-4394-bf00-d353b02f1d83` model=ridge tier=0 target=quantile pf=0.749 n=4755 gates=FAIL

## [INFO] 2026-08-02 10:55:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00177 skill_surrogate=-0.00257

## [INFO] 2026-08-02 10:55:44 UTC (tier 0)

trial `bcc4134b-dbb2-4dac-9089-f92754d4ab0c` model=lgbm_regressor tier=0 target=quantile pf=0.741 n=10958 gates=FAIL

## [INFO] 2026-08-02 10:55:50 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.27253 skill_surrogate=-1.60802

## [INFO] 2026-08-02 10:55:50 UTC (tier 0)

trial `e29c8a3c-779e-446b-82d7-3cfb2a4a1ce6` model=lgbm_classifier tier=0 target=quantile pf=0.697 n=131423 gates=FAIL

## [INFO] 2026-08-02 10:55:50 UTC (tier 0)

Hunt complete: {"generation_id": "auto_107_SOLUSDT_15m_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:55:50 UTC (tier 0)

AUTONOMY screen auto_107_SOLUSDT_15m_quantile_pivot_v1 tier=0 proxy_pf=0.749015333263043 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:55:50 UTC (tier 0)

START gen=auto_108_BTCUSDT_1h_fwd_return_ohlcv_v1 BTCUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 10:55:51 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.57226426217494e-09, 'circular_shift': 3.57226426217494e-09, 'fourier_phase': 3.57226426217494e-09, 'row_shuffle': 3.57226426217494e-09} passed=False

## [INFO] 2026-08-02 10:55:53 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:55:53 UTC (tier 0)

trial `9630eafa-6109-4481-993d-1e5a71c78dcf` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:55:53 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00806 skill_surrogate=+0.00208

## [INFO] 2026-08-02 10:55:53 UTC (tier 0)

trial `42cff9a8-9b50-4f3f-9673-42f9b313b094` model=ridge tier=0 target=fwd_return pf=0.824 n=6802 gates=FAIL

## [INFO] 2026-08-02 10:55:56 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01158 skill_surrogate=-0.00797

## [INFO] 2026-08-02 10:55:56 UTC (tier 0)

trial `c351de93-2037-4f2e-a7b6-6aeba4dd99d7` model=lgbm_regressor tier=0 target=fwd_return pf=0.769 n=4203 gates=FAIL

## [INFO] 2026-08-02 10:56:05 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.88126 skill_surrogate=-5.16850

## [INFO] 2026-08-02 10:56:05 UTC (tier 0)

trial `150b86a1-90fb-4510-b610-afb575a76f70` model=lgbm_classifier tier=0 target=fwd_return pf=0.713 n=32726 gates=FAIL

## [INFO] 2026-08-02 10:56:05 UTC (tier 0)

Hunt complete: {"generation_id": "auto_108_BTCUSDT_1h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:56:05 UTC (tier 0)

AUTONOMY screen auto_108_BTCUSDT_1h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.8241790932610158 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:56:05 UTC (tier 0)

START gen=auto_109_BTCUSDT_1h_fwd_return_indicators_v1 BTCUSDT 1h target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 10:56:06 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.5701032130575072e-09, 'circular_shift': 3.5701032130575072e-09, 'fourier_phase': 3.5701032130575072e-09, 'row_shuffle': 3.5701032130575072e-09} passed=False

## [INFO] 2026-08-02 10:56:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:56:09 UTC (tier 0)

trial `4b99b576-c10c-4476-b35c-dcba87694265` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:56:09 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.03431 skill_surrogate=-0.00150

## [INFO] 2026-08-02 10:56:09 UTC (tier 0)

trial `f22ae67d-db1d-4463-94ed-021f1ff36509` model=ridge tier=0 target=fwd_return pf=0.802 n=14771 gates=FAIL

## [INFO] 2026-08-02 10:56:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01395 skill_surrogate=-0.02015

## [INFO] 2026-08-02 10:56:11 UTC (tier 0)

trial `52985385-1493-443d-b105-6eed2707bde1` model=lgbm_regressor tier=0 target=fwd_return pf=0.729 n=12986 gates=FAIL

## [INFO] 2026-08-02 10:56:17 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-134.00153 skill_surrogate=-5.99580

## [INFO] 2026-08-02 10:56:17 UTC (tier 0)

trial `0be01345-5fec-46b5-9c63-b72394ab3e0e` model=lgbm_classifier tier=0 target=fwd_return pf=0.690 n=32709 gates=FAIL

## [INFO] 2026-08-02 10:56:17 UTC (tier 0)

Hunt complete: {"generation_id": "auto_109_BTCUSDT_1h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:56:17 UTC (tier 0)

AUTONOMY screen auto_109_BTCUSDT_1h_fwd_return_indicators_v1 tier=0 proxy_pf=0.8019564394607935 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:56:17 UTC (tier 0)

START gen=auto_110_BTCUSDT_1h_fwd_return_pivot_v1 BTCUSDT 1h target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 10:56:17 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 3.5743014104028248e-09, 'circular_shift': 3.5743014104028248e-09, 'fourier_phase': 3.5743014104028248e-09, 'row_shuffle': 3.5743014104028248e-09} passed=False

## [INFO] 2026-08-02 10:56:19 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:56:19 UTC (tier 0)

trial `266a5c2d-3ee7-4168-9554-48067ea0ad1c` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:56:19 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00596 skill_surrogate=-0.00093

## [INFO] 2026-08-02 10:56:19 UTC (tier 0)

trial `a17ab4c6-aea4-4ff1-b397-c65f2f0dc586` model=ridge tier=0 target=fwd_return pf=0.782 n=2380 gates=FAIL

## [INFO] 2026-08-02 10:56:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02190 skill_surrogate=-0.00929

## [INFO] 2026-08-02 10:56:21 UTC (tier 0)

trial `b755e294-eaa4-4951-bb98-38e16d0f75b5` model=lgbm_regressor tier=0 target=fwd_return pf=0.730 n=7895 gates=FAIL

## [INFO] 2026-08-02 10:56:29 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.89018 skill_surrogate=-5.26027

## [INFO] 2026-08-02 10:56:29 UTC (tier 0)

trial `161111f1-7e2f-437b-bc01-614fa54e8383` model=lgbm_classifier tier=0 target=fwd_return pf=0.713 n=32840 gates=FAIL

## [INFO] 2026-08-02 10:56:29 UTC (tier 0)

Hunt complete: {"generation_id": "auto_110_BTCUSDT_1h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:56:29 UTC (tier 0)

AUTONOMY screen auto_110_BTCUSDT_1h_fwd_return_pivot_v1 tier=0 proxy_pf=0.7815190217194922 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:56:29 UTC (tier 0)

START gen=auto_111_ETHUSDT_1h_fwd_return_ohlcv_v1 ETHUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 10:56:30 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.2880143335513026e-09, 'circular_shift': 2.2880143335513026e-09, 'fourier_phase': 2.2880143335513026e-09, 'row_shuffle': 2.2880143335513026e-09} passed=False

## [INFO] 2026-08-02 10:56:35 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:56:35 UTC (tier 0)

trial `690a3c55-1452-4fa7-b66e-63659a907dc0` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:56:35 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00388 skill_surrogate=-0.00120

## [INFO] 2026-08-02 10:56:35 UTC (tier 0)

trial `e407c825-458e-4ac9-90bf-f56e77b717c2` model=ridge tier=0 target=fwd_return pf=0.836 n=11451 gates=FAIL

## [INFO] 2026-08-02 10:56:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00683 skill_surrogate=-0.00393

## [INFO] 2026-08-02 10:56:39 UTC (tier 0)

trial `12681602-89d6-4851-8678-fcd1e0fce15f` model=lgbm_regressor tier=0 target=fwd_return pf=0.898 n=7192 gates=FAIL

## [INFO] 2026-08-02 10:56:47 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.69690 skill_surrogate=-2.37310

## [INFO] 2026-08-02 10:56:47 UTC (tier 0)

trial `96ba8bb9-cd89-4de2-bfe6-06429b70e9b9` model=lgbm_classifier tier=0 target=fwd_return pf=0.754 n=32855 gates=FAIL

## [INFO] 2026-08-02 10:56:47 UTC (tier 0)

Hunt complete: {"generation_id": "auto_111_ETHUSDT_1h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:56:47 UTC (tier 0)

AUTONOMY screen auto_111_ETHUSDT_1h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.8983023017364945 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:56:47 UTC (tier 0)

START gen=auto_112_ETHUSDT_1h_fwd_return_indicators_v1 ETHUSDT 1h target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 10:56:48 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.2867210347499167e-09, 'circular_shift': 2.2867210347499167e-09, 'fourier_phase': 2.2867210347499167e-09, 'row_shuffle': 2.2867210347499167e-09} passed=False

## [INFO] 2026-08-02 10:56:52 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:56:52 UTC (tier 0)

trial `664b85f6-25a4-4bf6-a09e-3b4d3242f916` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:56:52 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00937 skill_surrogate=+0.00069

## [INFO] 2026-08-02 10:56:52 UTC (tier 0)

trial `9de32122-e86e-4c4a-bf6a-f5ab30b91f90` model=ridge tier=0 target=fwd_return pf=0.906 n=15512 gates=FAIL

## [INFO] 2026-08-02 10:56:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04618 skill_surrogate=-0.00491

## [INFO] 2026-08-02 10:56:58 UTC (tier 0)

trial `c1c90f9a-2c91-4425-a8f9-3e1adb41152e` model=lgbm_regressor tier=0 target=fwd_return pf=0.844 n=19181 gates=FAIL

## [INFO] 2026-08-02 10:57:08 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.69431 skill_surrogate=-2.80776

## [INFO] 2026-08-02 10:57:08 UTC (tier 0)

trial `60190e7d-5088-49b3-bb84-b906d220d1e7` model=lgbm_classifier tier=0 target=fwd_return pf=0.727 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:57:08 UTC (tier 0)

Hunt complete: {"generation_id": "auto_112_ETHUSDT_1h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:57:08 UTC (tier 0)

AUTONOMY screen auto_112_ETHUSDT_1h_fwd_return_indicators_v1 tier=0 proxy_pf=0.906214041880571 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:57:08 UTC (tier 0)

START gen=auto_113_ETHUSDT_1h_fwd_return_pivot_v1 ETHUSDT 1h target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 10:57:08 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.284545885800071e-09, 'circular_shift': 2.284545885800071e-09, 'fourier_phase': 2.284545885800071e-09, 'row_shuffle': 2.284545885800071e-09} passed=False

## [INFO] 2026-08-02 10:57:10 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:57:10 UTC (tier 0)

trial `c13d78a9-458b-41ab-82ed-a421942c9db5` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:57:10 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00410 skill_surrogate=-0.00087

## [INFO] 2026-08-02 10:57:10 UTC (tier 0)

trial `f975d187-46a5-44a9-aeec-6699989eaa03` model=ridge tier=0 target=fwd_return pf=0.732 n=4466 gates=FAIL

## [INFO] 2026-08-02 10:57:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01122 skill_surrogate=-0.00488

## [INFO] 2026-08-02 10:57:12 UTC (tier 0)

trial `8be775a8-8c95-4689-87e9-d75dfac1a5ea` model=lgbm_regressor tier=0 target=fwd_return pf=0.804 n=10953 gates=FAIL

## [INFO] 2026-08-02 10:57:15 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.71388 skill_surrogate=-2.33615

## [INFO] 2026-08-02 10:57:15 UTC (tier 0)

trial `31c632ea-1bd0-4809-9605-914cc74f336c` model=lgbm_classifier tier=0 target=fwd_return pf=0.748 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:57:15 UTC (tier 0)

Hunt complete: {"generation_id": "auto_113_ETHUSDT_1h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:57:15 UTC (tier 0)

AUTONOMY screen auto_113_ETHUSDT_1h_fwd_return_pivot_v1 tier=0 proxy_pf=0.8044483162827601 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:57:15 UTC (tier 0)

START gen=auto_114_SOLUSDT_1h_fwd_return_ohlcv_v1 SOLUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 10:57:16 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.33865651475685e-10, 'circular_shift': 9.33865651475685e-10, 'fourier_phase': 9.33865651475685e-10, 'row_shuffle': 9.33865651475685e-10} passed=False

## [INFO] 2026-08-02 10:57:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:57:17 UTC (tier 0)

trial `b466317a-d93a-4861-afd3-e24ce050c24d` model=hist_mean tier=0 target=fwd_return pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-02 10:57:18 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00462 skill_surrogate=+0.00053

## [INFO] 2026-08-02 10:57:18 UTC (tier 0)

trial `a6d01e1d-0685-4e7d-a2da-d49c20e0a60e` model=ridge tier=0 target=fwd_return pf=0.902 n=17004 gates=FAIL

## [INFO] 2026-08-02 10:57:20 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01179 skill_surrogate=-0.00431

## [INFO] 2026-08-02 10:57:20 UTC (tier 0)

trial `47849821-6bad-4c85-8642-42a95d848128` model=lgbm_regressor tier=0 target=fwd_return pf=0.846 n=12027 gates=FAIL

## [INFO] 2026-08-02 10:57:25 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.08167 skill_surrogate=-1.53531

## [INFO] 2026-08-02 10:57:25 UTC (tier 0)

trial `a48498f2-5db0-4d6b-b8a7-cb28e278d3df` model=lgbm_classifier tier=0 target=fwd_return pf=0.874 n=32854 gates=FAIL

## [INFO] 2026-08-02 10:57:25 UTC (tier 0)

Hunt complete: {"generation_id": "auto_114_SOLUSDT_1h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:57:25 UTC (tier 0)

AUTONOMY screen auto_114_SOLUSDT_1h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.9022273781710141 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:57:25 UTC (tier 0)

START gen=auto_115_SOLUSDT_1h_fwd_return_indicators_v1 SOLUSDT 1h target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 10:57:27 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.349697682736746e-10, 'circular_shift': 9.349697682736746e-10, 'fourier_phase': 9.349697682736746e-10, 'row_shuffle': 9.349697682736746e-10} passed=False

## [INFO] 2026-08-02 10:57:31 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:57:31 UTC (tier 0)

trial `856fcc17-7906-4acb-be88-961596f0c42c` model=hist_mean tier=0 target=fwd_return pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-02 10:57:31 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01219 skill_surrogate=-0.00289

## [INFO] 2026-08-02 10:57:31 UTC (tier 0)

trial `fbfffc12-2691-4482-b614-85fc0a75a609` model=ridge tier=0 target=fwd_return pf=0.884 n=22651 gates=FAIL

## [INFO] 2026-08-02 10:57:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01149 skill_surrogate=-0.00429

## [INFO] 2026-08-02 10:57:34 UTC (tier 0)

trial `52c688e6-45d1-4b9d-b8ff-393ed3dd2fb3` model=lgbm_regressor tier=0 target=fwd_return pf=0.958 n=15633 gates=FAIL

## [INFO] 2026-08-02 10:57:41 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.05580 skill_surrogate=-1.93033

## [INFO] 2026-08-02 10:57:41 UTC (tier 0)

trial `8114e00d-fe78-469f-8ed2-c7fec0d9f552` model=lgbm_classifier tier=0 target=fwd_return pf=0.860 n=32699 gates=FAIL

## [INFO] 2026-08-02 10:57:41 UTC (tier 0)

Hunt complete: {"generation_id": "auto_115_SOLUSDT_1h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:57:41 UTC (tier 0)

AUTONOMY screen auto_115_SOLUSDT_1h_fwd_return_indicators_v1 tier=0 proxy_pf=0.958342346586077 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:57:41 UTC (tier 0)

START gen=auto_116_SOLUSDT_1h_fwd_return_pivot_v1 SOLUSDT 1h target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 10:57:41 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.31883903376729e-10, 'circular_shift': 9.31883903376729e-10, 'fourier_phase': 9.31883903376729e-10, 'row_shuffle': 9.31883903376729e-10} passed=False

## [INFO] 2026-08-02 10:57:43 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:57:43 UTC (tier 0)

trial `182425b3-6066-4058-8203-3b899f8e022e` model=hist_mean tier=0 target=fwd_return pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-02 10:57:43 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00186 skill_surrogate=-0.00048

## [INFO] 2026-08-02 10:57:43 UTC (tier 0)

trial `d579452c-abac-4f6b-be13-348a641ea589` model=ridge tier=0 target=fwd_return pf=0.745 n=8221 gates=FAIL

## [INFO] 2026-08-02 10:57:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01905 skill_surrogate=-0.00702

## [INFO] 2026-08-02 10:57:44 UTC (tier 0)

trial `b912fbbd-a2b7-4d71-a95c-8ff62c1ff0d2` model=lgbm_regressor tier=0 target=fwd_return pf=0.890 n=17033 gates=FAIL

## [INFO] 2026-08-02 10:57:48 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.08766 skill_surrogate=-1.57613

## [INFO] 2026-08-02 10:57:48 UTC (tier 0)

trial `7f8febeb-42b6-4260-875e-d1b02a0fc564` model=lgbm_classifier tier=0 target=fwd_return pf=0.840 n=32856 gates=FAIL

## [INFO] 2026-08-02 10:57:48 UTC (tier 0)

Hunt complete: {"generation_id": "auto_116_SOLUSDT_1h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:57:48 UTC (tier 0)

AUTONOMY screen auto_116_SOLUSDT_1h_fwd_return_pivot_v1 tier=0 proxy_pf=0.8901217750441386 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:57:48 UTC (tier 0)

START gen=auto_117_BTCUSDT_4h_fwd_return_ohlcv_v1 BTCUSDT 4h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 10:57:48 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.749191371393295e-10, 'circular_shift': 8.749191371393295e-10, 'fourier_phase': 8.749191371393295e-10, 'row_shuffle': 8.749191371393295e-10} passed=False

## [INFO] 2026-08-02 10:57:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:57:49 UTC (tier 0)

trial `1ac3c317-abc9-4016-b532-659a23278e0c` model=hist_mean tier=0 target=fwd_return pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-02 10:57:49 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00342 skill_surrogate=-0.00882

## [INFO] 2026-08-02 10:57:49 UTC (tier 0)

trial `c0322e92-8b7f-4a77-88f4-c329fc8c6836` model=ridge tier=0 target=fwd_return pf=1.018 n=5223 gates=FAIL

## [INFO] 2026-08-02 10:57:51 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04444 skill_surrogate=-0.02884

## [INFO] 2026-08-02 10:57:51 UTC (tier 0)

trial `d9311e8a-46d9-4a0b-932e-06cdc3795a12` model=lgbm_regressor tier=0 target=fwd_return pf=0.864 n=5565 gates=FAIL

## [INFO] 2026-08-02 10:57:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.22449 skill_surrogate=-4.36823

## [INFO] 2026-08-02 10:57:57 UTC (tier 0)

trial `ae9a8611-f30c-44e5-87a1-ad3c9e7c5ea5` model=lgbm_classifier tier=0 target=fwd_return pf=0.834 n=8204 gates=FAIL

## [INFO] 2026-08-02 10:57:57 UTC (tier 0)

Hunt complete: {"generation_id": "auto_117_BTCUSDT_4h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:57:57 UTC (tier 0)

AUTONOMY screen auto_117_BTCUSDT_4h_fwd_return_ohlcv_v1 tier=0 proxy_pf=1.0176857259100298 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:57:57 UTC (tier 0)

START gen=auto_118_BTCUSDT_4h_fwd_return_indicators_v1 BTCUSDT 4h target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 10:57:58 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.808362927936741e-10, 'circular_shift': 8.808362927936741e-10, 'fourier_phase': 8.808362927936741e-10, 'row_shuffle': 8.808362927936741e-10} passed=False

## [INFO] 2026-08-02 10:57:59 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:57:59 UTC (tier 0)

trial `419f74ba-fb56-40c8-9a51-a2f526277d08` model=hist_mean tier=0 target=fwd_return pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-02 10:57:59 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.04064 skill_surrogate=-0.00925

## [INFO] 2026-08-02 10:57:59 UTC (tier 0)

trial `d4abecdc-7aed-4c0a-a46e-4693b3bfcdf6` model=ridge tier=0 target=fwd_return pf=0.827 n=6439 gates=FAIL

## [INFO] 2026-08-02 10:58:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.05483 skill_surrogate=-0.04181

## [INFO] 2026-08-02 10:58:02 UTC (tier 0)

trial `480bddc9-7304-434c-963e-f7ee7a7642ce` model=lgbm_regressor tier=0 target=fwd_return pf=0.800 n=7028 gates=FAIL

## [INFO] 2026-08-02 10:58:09 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16491 skill_surrogate=-6.95168

## [INFO] 2026-08-02 10:58:09 UTC (tier 0)

trial `30dc1a39-f9c7-48d1-8f6f-9bd01a1ee6bd` model=lgbm_classifier tier=0 target=fwd_return pf=0.817 n=8213 gates=FAIL

## [INFO] 2026-08-02 10:58:09 UTC (tier 0)

Hunt complete: {"generation_id": "auto_118_BTCUSDT_4h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:58:09 UTC (tier 0)

AUTONOMY screen auto_118_BTCUSDT_4h_fwd_return_indicators_v1 tier=0 proxy_pf=0.8266177086033331 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:58:09 UTC (tier 0)

START gen=auto_119_BTCUSDT_4h_fwd_return_pivot_v1 BTCUSDT 4h target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 10:58:09 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.773649584625787e-10, 'circular_shift': 8.773649584625787e-10, 'fourier_phase': 8.773649584625787e-10, 'row_shuffle': 8.773649584625787e-10} passed=False

## [INFO] 2026-08-02 10:58:10 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:58:10 UTC (tier 0)

trial `054a35bd-178c-4dd1-b533-83efdbb3e043` model=hist_mean tier=0 target=fwd_return pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-02 10:58:10 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00530 skill_surrogate=+0.00020

## [INFO] 2026-08-02 10:58:10 UTC (tier 0)

trial `f401dd81-f870-4e7b-803b-e3781237342f` model=ridge tier=0 target=fwd_return pf=0.842 n=2815 gates=FAIL

## [INFO] 2026-08-02 10:58:13 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03841 skill_surrogate=-0.00734

## [INFO] 2026-08-02 10:58:13 UTC (tier 0)

trial `56f38c86-74fd-4b96-83f6-7e29a6b7ef84` model=lgbm_regressor tier=0 target=fwd_return pf=0.842 n=5743 gates=FAIL

## [INFO] 2026-08-02 10:58:16 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16893 skill_surrogate=-4.75857

## [INFO] 2026-08-02 10:58:16 UTC (tier 0)

trial `594ed009-5911-4382-8be1-eb986145efb6` model=lgbm_classifier tier=0 target=fwd_return pf=0.846 n=8210 gates=FAIL

## [INFO] 2026-08-02 10:58:16 UTC (tier 0)

Hunt complete: {"generation_id": "auto_119_BTCUSDT_4h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:58:16 UTC (tier 0)

AUTONOMY screen auto_119_BTCUSDT_4h_fwd_return_pivot_v1 tier=0 proxy_pf=0.8464266512174518 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:58:16 UTC (tier 0)

START gen=auto_120_ETHUSDT_4h_fwd_return_ohlcv_v1 ETHUSDT 4h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 10:58:17 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 5.530373936579736e-10, 'circular_shift': 5.530373936579736e-10, 'fourier_phase': 5.530373936579736e-10, 'row_shuffle': 5.530373936579736e-10} passed=False

## [INFO] 2026-08-02 10:58:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:58:17 UTC (tier 0)

trial `cb2f43f3-73f2-44ee-b395-f53d6cc5eac9` model=hist_mean tier=0 target=fwd_return pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:17 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00136 skill_surrogate=-0.00007

## [INFO] 2026-08-02 10:58:18 UTC (tier 0)

trial `16a93826-0499-4ed6-b4ef-020ae25a18d0` model=ridge tier=0 target=fwd_return pf=0.946 n=6072 gates=FAIL

## [INFO] 2026-08-02 10:58:19 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02168 skill_surrogate=-0.00761

## [INFO] 2026-08-02 10:58:19 UTC (tier 0)

trial `6ac1f5a4-8f4f-4153-80c3-8a067df6ced5` model=lgbm_regressor tier=0 target=fwd_return pf=0.930 n=6253 gates=FAIL

## [INFO] 2026-08-02 10:58:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.11179 skill_surrogate=-2.38091

## [INFO] 2026-08-02 10:58:23 UTC (tier 0)

trial `45dd91f8-5647-4fc8-b83d-9099e7f3761e` model=lgbm_classifier tier=0 target=fwd_return pf=0.903 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:23 UTC (tier 0)

Hunt complete: {"generation_id": "auto_120_ETHUSDT_4h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:58:23 UTC (tier 0)

AUTONOMY screen auto_120_ETHUSDT_4h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.9460121773106233 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:58:23 UTC (tier 0)

START gen=auto_121_ETHUSDT_4h_fwd_return_indicators_v1 ETHUSDT 4h target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 10:58:23 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 5.509456224572773e-10, 'circular_shift': 5.509456224572773e-10, 'fourier_phase': 5.509456224572773e-10, 'row_shuffle': 5.509456224572773e-10} passed=False

## [INFO] 2026-08-02 10:58:25 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:58:25 UTC (tier 0)

trial `27d0374d-fac5-4b2b-87d7-1aab3c52ca47` model=hist_mean tier=0 target=fwd_return pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:25 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00167 skill_surrogate=-0.00523

## [INFO] 2026-08-02 10:58:25 UTC (tier 0)

trial `4a5b4e5f-1a23-4a77-8248-409221ac6012` model=ridge tier=0 target=fwd_return pf=0.888 n=6885 gates=FAIL

## [INFO] 2026-08-02 10:58:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03816 skill_surrogate=-0.01158

## [INFO] 2026-08-02 10:58:27 UTC (tier 0)

trial `d300d1cd-e9f0-4f60-b25a-e1b71ea816af` model=lgbm_regressor tier=0 target=fwd_return pf=0.918 n=7147 gates=FAIL

## [INFO] 2026-08-02 10:58:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.01013 skill_surrogate=-2.65853

## [INFO] 2026-08-02 10:58:34 UTC (tier 0)

trial `cf1d0c09-7a99-48aa-a5c7-eb9aff3dca55` model=lgbm_classifier tier=0 target=fwd_return pf=0.915 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:34 UTC (tier 0)

Hunt complete: {"generation_id": "auto_121_ETHUSDT_4h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:58:34 UTC (tier 0)

AUTONOMY screen auto_121_ETHUSDT_4h_fwd_return_indicators_v1 tier=0 proxy_pf=0.9200856060065038 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:58:34 UTC (tier 0)

START gen=auto_122_ETHUSDT_4h_fwd_return_pivot_v1 ETHUSDT 4h target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 10:58:35 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 5.546206827133915e-10, 'circular_shift': 5.546206827133915e-10, 'fourier_phase': 5.546206827133915e-10, 'row_shuffle': 5.546206827133915e-10} passed=False

## [INFO] 2026-08-02 10:58:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:58:36 UTC (tier 0)

trial `f96e7589-c793-4b8e-91e0-468ebbd2f249` model=hist_mean tier=0 target=fwd_return pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:36 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00295 skill_surrogate=+0.00031

## [INFO] 2026-08-02 10:58:36 UTC (tier 0)

trial `2d42336a-34b3-4401-b551-375ed51d64f7` model=ridge tier=0 target=fwd_return pf=0.951 n=6014 gates=FAIL

## [INFO] 2026-08-02 10:58:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01431 skill_surrogate=-0.01088

## [INFO] 2026-08-02 10:58:38 UTC (tier 0)

trial `983f1e1e-46a9-470d-82cb-b9bcdf6854ea` model=lgbm_regressor tier=0 target=fwd_return pf=0.930 n=6824 gates=FAIL

## [INFO] 2026-08-02 10:58:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.01322 skill_surrogate=-2.68694

## [INFO] 2026-08-02 10:58:44 UTC (tier 0)

trial `1bda4966-8a95-4040-b1c4-bbd9ff19fcd7` model=lgbm_classifier tier=0 target=fwd_return pf=0.905 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:44 UTC (tier 0)

Hunt complete: {"generation_id": "auto_122_ETHUSDT_4h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:58:44 UTC (tier 0)

AUTONOMY screen auto_122_ETHUSDT_4h_fwd_return_pivot_v1 tier=0 proxy_pf=0.9510175596610267 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:58:44 UTC (tier 0)

START gen=auto_123_SOLUSDT_4h_fwd_return_ohlcv_v1 SOLUSDT 4h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 10:58:44 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.3751911548686166e-10, 'circular_shift': 2.3751911548686166e-10, 'fourier_phase': 2.3751911548686166e-10, 'row_shuffle': 2.3751911548686166e-10} passed=False

## [INFO] 2026-08-02 10:58:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:58:46 UTC (tier 0)

trial `6c190c3b-b968-4470-b4f0-b0db09f07f1f` model=hist_mean tier=0 target=fwd_return pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:46 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01743 skill_surrogate=-0.00753

## [INFO] 2026-08-02 10:58:46 UTC (tier 0)

trial `e68ea7d6-032b-42b1-a730-5d5db496c255` model=ridge tier=0 target=fwd_return pf=0.997 n=7292 gates=FAIL

## [INFO] 2026-08-02 10:58:49 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02577 skill_surrogate=-0.02091

## [INFO] 2026-08-02 10:58:49 UTC (tier 0)

trial `f84c5e81-79f9-437c-b132-baf96dfc3810` model=lgbm_regressor tier=0 target=fwd_return pf=0.958 n=7161 gates=FAIL

## [INFO] 2026-08-02 10:58:54 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.52165 skill_surrogate=-1.47638

## [INFO] 2026-08-02 10:58:54 UTC (tier 0)

trial `a60c46fa-2a79-4a94-ae9a-eca1f38d50e9` model=lgbm_classifier tier=0 target=fwd_return pf=0.989 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:54 UTC (tier 0)

Hunt complete: {"generation_id": "auto_123_SOLUSDT_4h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:58:54 UTC (tier 0)

AUTONOMY screen auto_123_SOLUSDT_4h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.9965702191452582 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:58:54 UTC (tier 0)

START gen=auto_124_SOLUSDT_4h_fwd_return_indicators_v1 SOLUSDT 4h target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 10:58:55 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.3690038819523807e-10, 'circular_shift': 2.3690038819523807e-10, 'fourier_phase': 2.3690038819523807e-10, 'row_shuffle': 2.3690038819523807e-10} passed=False

## [INFO] 2026-08-02 10:58:56 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-02 10:58:56 UTC (tier 0)

trial `a4050e88-c1e9-41d2-a46d-f4347177d9e1` model=hist_mean tier=0 target=fwd_return pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:58:56 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00250 skill_surrogate=-0.01403

## [INFO] 2026-08-02 10:58:56 UTC (tier 0)

trial `6eda6a59-4a8c-4b73-be25-4a2b51154335` model=ridge tier=0 target=fwd_return pf=1.042 n=7405 gates=FAIL

## [INFO] 2026-08-02 10:58:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01843 skill_surrogate=-0.01847

## [INFO] 2026-08-02 10:58:58 UTC (tier 0)

trial `8f2c6600-111c-4260-8166-e9816de556bc` model=lgbm_regressor tier=0 target=fwd_return pf=0.951 n=7318 gates=FAIL

## [INFO] 2026-08-02 10:59:04 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.44360 skill_surrogate=-2.74855

## [INFO] 2026-08-02 10:59:04 UTC (tier 0)

trial `2bb37972-eeb7-4660-a93a-5634ceb49765` model=lgbm_classifier tier=0 target=fwd_return pf=0.918 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:59:04 UTC (tier 0)

Hunt complete: {"generation_id": "auto_124_SOLUSDT_4h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:59:04 UTC (tier 0)

AUTONOMY screen auto_124_SOLUSDT_4h_fwd_return_indicators_v1 tier=0 proxy_pf=1.0422191080060303 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:59:04 UTC (tier 0)

START gen=auto_125_SOLUSDT_4h_fwd_return_pivot_v1 SOLUSDT 4h target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 10:59:05 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 2.358924167111809e-10, 'circular_shift': 2.358924167111809e-10, 'fourier_phase': 2.358924167111809e-10, 'row_shuffle': 2.358924167111809e-10} passed=False

## [INFO] 2026-08-02 10:59:05 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:59:05 UTC (tier 0)

trial `68a79533-d8af-412d-b70d-4d6b97846c37` model=hist_mean tier=0 target=fwd_return pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:59:05 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00757 skill_surrogate=-0.00052

## [INFO] 2026-08-02 10:59:05 UTC (tier 0)

trial `9c166b5b-2dfa-4768-a48f-fbb80b1d0a42` model=ridge tier=0 target=fwd_return pf=0.975 n=6843 gates=FAIL

## [INFO] 2026-08-02 10:59:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04768 skill_surrogate=-0.01214

## [INFO] 2026-08-02 10:59:07 UTC (tier 0)

trial `6ed0a505-7d72-4846-ac78-77718d49d906` model=lgbm_regressor tier=0 target=fwd_return pf=0.987 n=7360 gates=FAIL

## [INFO] 2026-08-02 10:59:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.44952 skill_surrogate=-2.25744

## [INFO] 2026-08-02 10:59:10 UTC (tier 0)

trial `a24e3ae3-130f-46a0-aaf5-72f05c903c8b` model=lgbm_classifier tier=0 target=fwd_return pf=0.921 n=8214 gates=FAIL

## [INFO] 2026-08-02 10:59:10 UTC (tier 0)

Hunt complete: {"generation_id": "auto_125_SOLUSDT_4h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:59:10 UTC (tier 0)

AUTONOMY screen auto_125_SOLUSDT_4h_fwd_return_pivot_v1 tier=0 proxy_pf=0.9868588821857988 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:59:10 UTC (tier 0)

START gen=auto_126_BTCUSDT_15m_fwd_return_ohlcv_v1 BTCUSDT 15m target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 10:59:13 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3483151373172575e-08, 'circular_shift': 1.3483151373172575e-08, 'fourier_phase': 1.3483151373172575e-08, 'row_shuffle': 1.3483151373172575e-08} passed=False

## [INFO] 2026-08-02 10:59:25 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 10:59:25 UTC (tier 0)

trial `27095d6e-f13d-4df5-8e2d-bc619cc74b01` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 10:59:26 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00863 skill_surrogate=+0.00078

## [INFO] 2026-08-02 10:59:26 UTC (tier 0)

trial `ff3a4175-d648-42d3-b6e7-aa7bfba1ea3c` model=ridge tier=0 target=fwd_return pf=1.045 n=790 gates=FAIL

## [INFO] 2026-08-02 10:59:33 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00290 skill_surrogate=-0.00196

## [INFO] 2026-08-02 10:59:33 UTC (tier 0)

trial `c4f036b6-8fba-4e1d-a660-71535f70c9fe` model=lgbm_regressor tier=0 target=fwd_return pf=0.810 n=2069 gates=FAIL

## [INFO] 2026-08-02 10:59:51 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-278.14698 skill_surrogate=-5.70952

## [INFO] 2026-08-02 10:59:51 UTC (tier 0)

trial `332f8998-9b0f-4acf-9c9c-48c3a0bcca27` model=lgbm_classifier tier=0 target=fwd_return pf=0.467 n=130835 gates=FAIL

## [INFO] 2026-08-02 10:59:51 UTC (tier 0)

Hunt complete: {"generation_id": "auto_126_BTCUSDT_15m_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 10:59:51 UTC (tier 0)

AUTONOMY screen auto_126_BTCUSDT_15m_fwd_return_ohlcv_v1 tier=0 proxy_pf=1.0445968814778723 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 10:59:52 UTC (tier 0)

START gen=auto_127_BTCUSDT_15m_fwd_return_indicators_v1 BTCUSDT 15m target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 10:59:56 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.3484098726479488e-08, 'circular_shift': 1.3484098726479488e-08, 'fourier_phase': 1.348409877088841e-08, 'row_shuffle': 1.3484098726479488e-08} passed=False

## [INFO] 2026-08-02 11:00:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 11:00:16 UTC (tier 0)

trial `3277a959-2490-4d32-b32d-42d213ed4c16` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 11:00:18 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01350 skill_surrogate=-0.00078

## [INFO] 2026-08-02 11:00:18 UTC (tier 0)

trial `10f126ae-30cc-4418-8a44-e3cbd6876194` model=ridge tier=0 target=fwd_return pf=0.765 n=4559 gates=FAIL

## [INFO] 2026-08-02 11:00:26 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00271 skill_surrogate=-0.00586

## [INFO] 2026-08-02 11:00:26 UTC (tier 0)

trial `b59f42e1-6f13-495a-8af7-4d625038531d` model=lgbm_regressor tier=0 target=fwd_return pf=0.511 n=11633 gates=FAIL

## [INFO] 2026-08-02 11:00:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-277.38180 skill_surrogate=-7.46693

## [INFO] 2026-08-02 11:00:43 UTC (tier 0)

trial `aed1df3c-1426-4e38-b522-5080a4d006a3` model=lgbm_classifier tier=0 target=fwd_return pf=0.462 n=130999 gates=FAIL

## [INFO] 2026-08-02 11:00:43 UTC (tier 0)

Hunt complete: {"generation_id": "auto_127_BTCUSDT_15m_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 11:00:43 UTC (tier 0)

AUTONOMY screen auto_127_BTCUSDT_15m_fwd_return_indicators_v1 tier=0 proxy_pf=0.7654162061547987 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 11:00:43 UTC (tier 0)

START gen=auto_128_BTCUSDT_15m_fwd_return_pivot_v1 BTCUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 11:00:45 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.348536438072756e-08, 'circular_shift': 1.348536438072756e-08, 'fourier_phase': 1.348536438072756e-08, 'row_shuffle': 1.348536438072756e-08} passed=False

## [INFO] 2026-08-02 11:00:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 11:00:55 UTC (tier 0)

trial `c9fd0d7e-e270-4c6b-a413-49156cf60fc6` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 11:00:55 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00154 skill_surrogate=-0.00009

## [INFO] 2026-08-02 11:00:55 UTC (tier 0)

trial `7dbfcd9f-2763-4026-8758-96116a7db14e` model=ridge tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 11:00:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00626 skill_surrogate=-0.00212

## [INFO] 2026-08-02 11:00:59 UTC (tier 0)

trial `ed5901f4-8002-46a0-8508-2112c86b8159` model=lgbm_regressor tier=0 target=fwd_return pf=0.598 n=3861 gates=FAIL

## [INFO] 2026-08-02 11:01:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-278.16756 skill_surrogate=-6.05904

## [INFO] 2026-08-02 11:01:11 UTC (tier 0)

trial `479383d0-7214-4c86-bdc1-4287bfa88eb3` model=lgbm_classifier tier=0 target=fwd_return pf=0.466 n=131317 gates=FAIL

## [INFO] 2026-08-02 11:01:11 UTC (tier 0)

Hunt complete: {"generation_id": "auto_128_BTCUSDT_15m_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 11:01:11 UTC (tier 0)

AUTONOMY screen auto_128_BTCUSDT_15m_fwd_return_pivot_v1 tier=0 proxy_pf=0.5975835294509682 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 11:01:11 UTC (tier 0)

START gen=auto_129_ETHUSDT_15m_fwd_return_ohlcv_v1 ETHUSDT 15m target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-02 11:01:14 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.470337320432009e-09, 'circular_shift': 8.470337320432009e-09, 'fourier_phase': 8.470337320432009e-09, 'row_shuffle': 8.470337320432009e-09} passed=False

## [INFO] 2026-08-02 11:01:29 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 11:01:29 UTC (tier 0)

trial `5ada6337-231c-4213-8bf6-2ae2bd0eb3f1` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 11:01:30 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00542 skill_surrogate=-0.00009

## [INFO] 2026-08-02 11:01:30 UTC (tier 0)

trial `eb129ea3-5ee3-4291-b282-9329bcfd5d26` model=ridge tier=0 target=fwd_return pf=0.881 n=3512 gates=FAIL

## [INFO] 2026-08-02 11:01:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00470 skill_surrogate=-0.00053

## [INFO] 2026-08-02 11:01:39 UTC (tier 0)

trial `f811cb1a-f470-46ef-9189-95e5b885f9b5` model=lgbm_regressor tier=0 target=fwd_return pf=1.022 n=2467 gates=FAIL

## [INFO] 2026-08-02 11:02:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.36925 skill_surrogate=-3.44623

## [INFO] 2026-08-02 11:02:02 UTC (tier 0)

trial `8c471f56-d15d-41c1-89a8-b2d5b113d2d4` model=lgbm_classifier tier=0 target=fwd_return pf=0.545 n=131409 gates=FAIL

## [INFO] 2026-08-02 11:02:02 UTC (tier 0)

Hunt complete: {"generation_id": "auto_129_ETHUSDT_15m_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 11:02:02 UTC (tier 0)

AUTONOMY screen auto_129_ETHUSDT_15m_fwd_return_ohlcv_v1 tier=0 proxy_pf=1.022178284329403 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 11:02:02 UTC (tier 0)

START gen=auto_130_ETHUSDT_15m_fwd_return_indicators_v1 ETHUSDT 15m target=fwd_return space=indicators_v1

## [INFO] 2026-08-02 11:02:08 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.471199297588328e-09, 'circular_shift': 8.471199297588328e-09, 'fourier_phase': 8.471199297588328e-09, 'row_shuffle': 8.471199297588328e-09} passed=False

## [INFO] 2026-08-02 11:02:38 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 11:02:38 UTC (tier 0)

trial `ac5e67e4-0b9f-4918-bef3-5f73286852dc` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-02 11:02:39 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00595 skill_surrogate=-0.00037

## [INFO] 2026-08-02 11:02:39 UTC (tier 0)

trial `dd4026d8-dd3c-4b2e-af94-c7ac770176ec` model=ridge tier=0 target=fwd_return pf=0.743 n=14768 gates=FAIL

## [INFO] 2026-08-02 11:02:47 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00380 skill_surrogate=-0.00330

## [INFO] 2026-08-02 11:02:47 UTC (tier 0)

trial `f6001522-9dfd-4d97-bc00-39fda42992bd` model=lgbm_regressor tier=0 target=fwd_return pf=0.689 n=20360 gates=FAIL

## [INFO] 2026-08-02 11:03:13 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.35786 skill_surrogate=-3.25835

## [INFO] 2026-08-02 11:03:13 UTC (tier 0)

trial `f117efc6-0ee7-45cf-bcdd-f13d9c56164a` model=lgbm_classifier tier=0 target=fwd_return pf=0.540 n=131424 gates=FAIL

## [INFO] 2026-08-02 11:03:13 UTC (tier 0)

Hunt complete: {"generation_id": "auto_130_ETHUSDT_15m_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 11:03:13 UTC (tier 0)

AUTONOMY screen auto_130_ETHUSDT_15m_fwd_return_indicators_v1 tier=0 proxy_pf=0.7433357706857794 (proxy is a filter, not evidence)

## [INFO] 2026-08-02 11:03:13 UTC (tier 0)

START gen=auto_131_ETHUSDT_15m_fwd_return_pivot_v1 ETHUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-02 11:03:17 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 8.446917609816751e-09, 'circular_shift': 8.446917609816751e-09, 'fourier_phase': 8.446917720839053e-09, 'row_shuffle': 8.446917609816751e-09} passed=False

## [INFO] 2026-08-02 11:04:23 UTC (tier 0)

GO/NO-GO non-directional block: NO-GO. max_tier=0 including xs_rank x xs_v1; predictability_passed=false throughout. Frozen out: fwd_return, direction. Skill>1 without predictability will not escalate. No tier2_review (no Tier>=1). botsgeneral push: nothing to push (even with origin/main at 3e7eb30).

## [INFO] 2026-08-02 11:04:38 UTC (tier 0)

AUTONOMY start 108 combos; frozen_out=['direction', 'fwd_return']; active=['vol_ratio', 'volatility', 'xs_rank', 'quantile']

## [INFO] 2026-08-02 11:04:38 UTC (tier 0)

START gen=auto_000_BTCUSDT_1h_vol_ratio_ohlcv_v1 BTCUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 11:04:39 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.795497746267756e-13, 'circular_shift': 9.795497746267756e-13, 'fourier_phase': 9.795497746267756e-13, 'row_shuffle': 9.795497746267756e-13} passed=False

## [INFO] 2026-08-02 11:04:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 11:04:42 UTC (tier 0)

trial `556e5404-6e24-40fb-8ec3-71937ea20ee0` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-02 11:04:42 UTC (tier 0)

trial `02e2d59e-a7ae-476e-8795-e9cd47626d20` model=ridge tier=0 target=vol_ratio skill=1.063 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 11:04:49 UTC (tier 0)

trial `b476f118-24da-4dcf-be24-a232592a4a3f` model=lgbm_regressor tier=0 target=vol_ratio skill=1.129 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 11:04:51 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06290 skill_surrogate=+0.06290

## [INFO] 2026-08-02 11:04:51 UTC (tier 0)

trial `224deee0-e91f-4e42-9bf2-c85d42926c1a` model=lgbm_classifier tier=0 target=vol_ratio skill=1.060 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 11:04:51 UTC (tier 0)

Hunt complete: {"generation_id": "auto_000_BTCUSDT_1h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 11:04:51 UTC (tier 0)

AUTONOMY screen auto_000_BTCUSDT_1h_vol_ratio_ohlcv_v1 tier=0 proxy_skill=1.1287881645516609 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-02 11:04:51 UTC (tier 0)

START gen=auto_001_BTCUSDT_1h_vol_ratio_indicators_v1 BTCUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 11:04:53 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.788836408120005e-13, 'circular_shift': 9.788836408120005e-13, 'fourier_phase': 9.788836408120005e-13, 'row_shuffle': 9.788836408120005e-13} passed=False

## [INFO] 2026-08-02 11:04:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 11:04:57 UTC (tier 0)

trial `41983f61-e5ac-4de3-8276-a9b144fd0b8c` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 11:04:57 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01111 skill_surrogate=-0.01347

## [INFO] 2026-08-02 11:04:57 UTC (tier 0)

trial `aa9deec8-2a40-4af7-98f5-8c2b5d0acf58` model=ridge tier=0 target=vol_ratio skill=1.065 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 11:05:03 UTC (tier 0)

trial `4fdcc8cd-3907-4e43-936e-90569ce0a1c9` model=lgbm_regressor tier=0 target=vol_ratio skill=1.002 n=32856 gates=FAIL

## [INFO] 2026-08-02 11:05:04 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06305 skill_surrogate=+0.06305

## [INFO] 2026-08-02 11:05:04 UTC (tier 0)

trial `d974145e-5423-4315-a632-89c8e89eacc1` model=lgbm_classifier tier=0 target=vol_ratio skill=1.060 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 11:05:04 UTC (tier 0)

Hunt complete: {"generation_id": "auto_001_BTCUSDT_1h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 11:05:04 UTC (tier 0)

AUTONOMY screen auto_001_BTCUSDT_1h_vol_ratio_indicators_v1 tier=0 proxy_skill=1.0654752580145348 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-02 11:05:04 UTC (tier 0)

START gen=auto_002_BTCUSDT_1h_vol_ratio_pivot_v1 BTCUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-02 11:05:05 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 9.802159084415507e-13, 'circular_shift': 9.802159084415507e-13, 'fourier_phase': 9.802159084415507e-13, 'row_shuffle': 9.802159084415507e-13} passed=False

## [INFO] 2026-08-02 11:05:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 11:05:09 UTC (tier 0)

trial `f09ffa15-e30c-4ee4-a670-0a6d5347bc39` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-02 11:05:09 UTC (tier 0)

trial `e4371625-e910-4bb2-b5e6-4636a3d1ed88` model=ridge tier=0 target=vol_ratio skill=1.107 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 11:05:11 UTC (tier 0)

trial `0640270d-2fe4-4d0a-9c33-e97b1655ae56` model=lgbm_regressor tier=0 target=vol_ratio skill=1.116 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 11:05:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06281 skill_surrogate=+0.06281

## [INFO] 2026-08-02 11:05:12 UTC (tier 0)

trial `91624de9-b407-4361-bf4e-a48dbe0d5b73` model=lgbm_classifier tier=0 target=vol_ratio skill=1.059 n=32856 gates=UNKNOWN

## [INFO] 2026-08-02 11:05:12 UTC (tier 0)

Hunt complete: {"generation_id": "auto_002_BTCUSDT_1h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 11:05:12 UTC (tier 0)

AUTONOMY screen auto_002_BTCUSDT_1h_vol_ratio_pivot_v1 tier=0 proxy_skill=1.116215847766803 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-02 11:05:12 UTC (tier 0)

START gen=auto_003_ETHUSDT_1h_vol_ratio_ohlcv_v1 ETHUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-02 11:05:13 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.472044708350495e-12, 'circular_shift': 1.472044708350495e-12, 'fourier_phase': 1.472044708350495e-12, 'row_shuffle': 1.472044708350495e-12} passed=False

## [INFO] 2026-08-02 11:05:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-02 11:05:16 UTC (tier 0)

trial `61805c6f-ee2a-4b49-ad15-2f5aea1489bc` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-02 11:05:16 UTC (tier 0)

trial `78380444-65f1-4372-9f6a-b77c77e7bfae` model=ridge tier=0 target=vol_ratio skill=1.053 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 11:05:22 UTC (tier 0)

trial `7e1a1c89-11f8-4625-9364-5a5b023a028e` model=lgbm_regressor tier=0 target=vol_ratio skill=1.103 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 11:05:24 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05804 skill_surrogate=+0.05804

## [INFO] 2026-08-02 11:05:24 UTC (tier 0)

trial `5864f9d0-8df9-4366-82c6-e3b2b02e3614` model=lgbm_classifier tier=0 target=vol_ratio skill=1.054 n=32855 gates=UNKNOWN

## [INFO] 2026-08-02 11:05:24 UTC (tier 0)

Hunt complete: {"generation_id": "auto_003_ETHUSDT_1h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-02 11:05:24 UTC (tier 0)

AUTONOMY screen auto_003_ETHUSDT_1h_vol_ratio_ohlcv_v1 tier=0 proxy_skill=1.103409254981764 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-02 11:05:24 UTC (tier 0)

START gen=auto_004_ETHUSDT_1h_vol_ratio_indicators_v1 ETHUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-02 11:05:29 UTC (tier 0)

PREDICTABILITY real=0.0000 surrogates={'block_shuffle': 1.4707124407209449e-12, 'circular_shift': 1.4707124407209449e-12, 'fourier_phase': 1.4707124407209449e-12, 'row_shuffle': 1.4707124407209449e-12} passed=False

## [INFO] 2026-08-02 11:05:40 UTC (tier 0)

AUTONOMY start 108 combos; frozen_out=['direction', 'fwd_return']; active=['vol_ratio', 'volatility', 'xs_rank', 'quantile']

## [INFO] 2026-08-02 11:05:40 UTC (tier 0)

AUTONOMY sweep complete — no tier>=2 candidate

## [INFO] 2026-08-02 11:15:58 UTC (tier 0)

PREREG volfilter_001_BTCUSDT_1h sha256=f968eed84abd37b9 path=D:\projects\LLM2\configs\preregister\volfilter_001.yaml — vol forecast is filter_input_only; never emits side

## [INFO] 2026-08-02 11:16:01 UTC (tier 1)

FILTER_BEATS_CONTROL volfilter_001_BTCUSDT_1h: filtered_pf=0.9140 ctrl_pf=0.8636 filtered_pnl=-22.919812 ctrl_pnl=-43.583689 n_filt=26522 n_ctrl=29862 skip_more=True no_vol_side=True

## [INFO] 2026-08-02 11:17:20 UTC (tier 0)

PREREG volfilter_001_BTCUSDT_1h sha256=f968eed84abd37b9 path=D:\projects\LLM2\configs\preregister\volfilter_001.yaml — vol forecast is filter_input_only; never emits side

## [INFO] 2026-08-02 11:17:22 UTC (tier 1)

FILTER_BEATS_CONTROL volfilter_001_BTCUSDT_1h: filtered_pf=0.9140 ctrl_pf=0.8636 filtered_pnl=-22.919812 ctrl_pnl=-43.583689 n_filt=26522 n_ctrl=29862 skip_more=True no_vol_side=True

## [INFO] 2026-08-02 11:17:54 UTC (tier 1)

TRADESIM_FILTER_BEATS_CONTROL volfilter_001_BTCUSDT_1h_ts: filt_pf=0.8933 ctrl_pf=0.8201 filt_pnl=-42.9643 ctrl_pnl=-115.5528 n_filt=982 n_ctrl=1239 (max_signals_per_fold=800)

## [INFO] 2026-08-02 11:18:08 UTC (tier 0)

VOL-FILTER VERDICT volfilter_001: beats always-on on proxy and tradesim (skip-more, no side from vol) but both arms PF<1 — filter is a useful gate on a losing momentum rule, not an edge. Do not expand filter grid. RESEARCH_ONLY; no Tier-2.

## [INFO] 2026-08-02 11:33:36 UTC (tier 0)

PREREG volfilter_002_BTCUSDT_1h_meanrev status=PREREGISTERED entry=meanrev_24_cost_gate sha256=265787ae6e7c0c31 — vol filter_input_only; never emits side; percentile frozen at 75

## [INFO] 2026-08-02 11:33:37 UTC (tier 0)

FILTER_FAILS_vs_CONTROL volfilter_002_BTCUSDT_1h_meanrev: filtered_pf=0.7549 ctrl_pf=0.8251 filtered_pnl=-61.950588 ctrl_pnl=-51.974711 n_filt=26522 n_ctrl=29862 skip_more=True no_vol_side=True

## [INFO] 2026-08-02 11:33:50 UTC (tier 0)

VOL-FILTER POLICY LOCK: percentile frozen at 75; magnitude blocked from sides; skip-more only. volfilter_001 FROZEN (momentum: filter beats control, both PF<1 = methodology win). volfilter_002 FROZEN (meanrev: FILTER_FAILS_vs_CONTROL — filter is entry-rule-specific). RESEARCH_ONLY; no Finplot/live from vol-filter alone.

## [INFO] 2026-08-03 09:11:20 UTC (tier 0)

AUTONOMY start 162 combos; frozen_out=[]; active=['vol_ratio', 'volatility', 'xs_rank', 'quantile', 'fwd_return', 'direction']

## [INFO] 2026-08-03 09:11:20 UTC (tier 0)

START gen=auto_131_ETHUSDT_15m_fwd_return_pivot_v1 ETHUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 09:12:14 UTC (tier 0)

PREDICTABILITY real=-0.00081 p=0.9524 surr_q95=+0.00024 surr_max=+0.00026 draws=20 passed=False

## [INFO] 2026-08-03 09:12:16 UTC (tier 0)

AUTONOMY error auto_131_ETHUSDT_15m_fwd_return_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:12:16 UTC (tier 0)

START gen=auto_132_SOLUSDT_15m_fwd_return_ohlcv_v1 SOLUSDT 15m target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 09:14:04 UTC (tier 0)

PREDICTABILITY real=+0.00050 p=0.0476 surr_q95=-0.00003 surr_max=+0.00013 draws=20 passed=True

## [INFO] 2026-08-03 09:14:05 UTC (tier 0)

AUTONOMY error auto_132_SOLUSDT_15m_fwd_return_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:14:05 UTC (tier 0)

START gen=auto_133_SOLUSDT_15m_fwd_return_indicators_v1 SOLUSDT 15m target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 09:15:17 UTC (tier 0)

PREDICTABILITY real=-0.00304 p=0.9524 surr_q95=+0.00012 surr_max=+0.00053 draws=20 passed=False

## [INFO] 2026-08-03 09:15:19 UTC (tier 0)

AUTONOMY error auto_133_SOLUSDT_15m_fwd_return_indicators_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:15:19 UTC (tier 0)

START gen=auto_134_SOLUSDT_15m_fwd_return_pivot_v1 SOLUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 09:15:51 UTC (tier 0)

PREDICTABILITY real=-0.00106 p=1.0000 surr_q95=+0.00007 surr_max=+0.00009 draws=20 passed=False

## [INFO] 2026-08-03 09:15:53 UTC (tier 0)

AUTONOMY error auto_134_SOLUSDT_15m_fwd_return_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:15:53 UTC (tier 0)

START gen=auto_135_BTCUSDT_1h_direction_ohlcv_v1 BTCUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:16:08 UTC (tier 0)

PREDICTABILITY real=+0.00789 p=0.0476 surr_q95=-0.00021 surr_max=-0.00007 draws=20 passed=True

## [INFO] 2026-08-03 09:16:09 UTC (tier 0)

AUTONOMY error auto_135_BTCUSDT_1h_direction_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:16:09 UTC (tier 0)

START gen=auto_136_BTCUSDT_1h_direction_indicators_v1 BTCUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 09:16:24 UTC (tier 0)

PREDICTABILITY real=-0.00281 p=0.7619 surr_q95=+0.00097 surr_max=+0.00103 draws=20 passed=False

## [INFO] 2026-08-03 09:16:25 UTC (tier 0)

AUTONOMY error auto_136_BTCUSDT_1h_direction_indicators_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:16:25 UTC (tier 0)

START gen=auto_137_BTCUSDT_1h_direction_pivot_v1 BTCUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 09:16:31 UTC (tier 0)

PREDICTABILITY real=+0.00829 p=0.0476 surr_q95=+0.00090 surr_max=+0.00094 draws=20 passed=True

## [INFO] 2026-08-03 09:16:32 UTC (tier 0)

AUTONOMY error auto_137_BTCUSDT_1h_direction_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:16:33 UTC (tier 0)

START gen=auto_138_ETHUSDT_1h_direction_ohlcv_v1 ETHUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:16:44 UTC (tier 0)

PREDICTABILITY real=+0.00392 p=0.0476 surr_q95=-0.00007 surr_max=-0.00003 draws=20 passed=True

## [INFO] 2026-08-03 09:16:45 UTC (tier 0)

AUTONOMY error auto_138_ETHUSDT_1h_direction_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:16:45 UTC (tier 0)

START gen=auto_139_ETHUSDT_1h_direction_indicators_v1 ETHUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 09:16:59 UTC (tier 0)

PREDICTABILITY real=+0.00459 p=0.0476 surr_q95=+0.00036 surr_max=+0.00108 draws=20 passed=True

## [INFO] 2026-08-03 09:17:00 UTC (tier 0)

AUTONOMY error auto_139_ETHUSDT_1h_direction_indicators_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:17:00 UTC (tier 0)

START gen=auto_140_ETHUSDT_1h_direction_pivot_v1 ETHUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 09:17:08 UTC (tier 0)

PREDICTABILITY real=+0.00190 p=0.0476 surr_q95=+0.00011 surr_max=+0.00121 draws=20 passed=True

## [INFO] 2026-08-03 09:17:09 UTC (tier 0)

AUTONOMY error auto_140_ETHUSDT_1h_direction_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:17:09 UTC (tier 0)

START gen=auto_141_SOLUSDT_1h_direction_ohlcv_v1 SOLUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:17:19 UTC (tier 0)

PREDICTABILITY real=+0.00058 p=0.0952 surr_q95=+0.00029 surr_max=+0.00067 draws=20 passed=False

## [INFO] 2026-08-03 09:17:20 UTC (tier 0)

AUTONOMY error auto_141_SOLUSDT_1h_direction_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:17:20 UTC (tier 0)

START gen=auto_142_SOLUSDT_1h_direction_indicators_v1 SOLUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 09:17:31 UTC (tier 0)

PREDICTABILITY real=-0.00553 p=0.8095 surr_q95=+0.00075 surr_max=+0.00312 draws=20 passed=False

## [INFO] 2026-08-03 09:17:33 UTC (tier 0)

AUTONOMY error auto_142_SOLUSDT_1h_direction_indicators_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:17:33 UTC (tier 0)

START gen=auto_143_SOLUSDT_1h_direction_pivot_v1 SOLUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 09:17:39 UTC (tier 0)

PREDICTABILITY real=-0.00256 p=0.9048 surr_q95=+0.00118 surr_max=+0.00127 draws=20 passed=False

## [INFO] 2026-08-03 09:17:40 UTC (tier 0)

AUTONOMY error auto_143_SOLUSDT_1h_direction_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:17:40 UTC (tier 0)

START gen=auto_144_BTCUSDT_4h_direction_ohlcv_v1 BTCUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:17:44 UTC (tier 0)

PREDICTABILITY real=+0.00571 p=0.0476 surr_q95=+0.00297 surr_max=+0.00351 draws=20 passed=True

## [INFO] 2026-08-03 09:17:45 UTC (tier 0)

AUTONOMY error auto_144_BTCUSDT_4h_direction_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:17:45 UTC (tier 0)

START gen=auto_145_BTCUSDT_4h_direction_indicators_v1 BTCUSDT 4h target=direction space=indicators_v1

## [INFO] 2026-08-03 09:17:51 UTC (tier 0)

PREDICTABILITY real=-0.01554 p=0.6190 surr_q95=-0.00120 surr_max=+0.00292 draws=20 passed=False

## [INFO] 2026-08-03 09:17:52 UTC (tier 0)

AUTONOMY error auto_145_BTCUSDT_4h_direction_indicators_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:17:52 UTC (tier 0)

START gen=auto_146_BTCUSDT_4h_direction_pivot_v1 BTCUSDT 4h target=direction space=pivot_v1

## [INFO] 2026-08-03 09:17:54 UTC (tier 0)

PREDICTABILITY real=-0.00009 p=0.1429 surr_q95=+0.00024 surr_max=+0.00443 draws=20 passed=False

## [INFO] 2026-08-03 09:17:55 UTC (tier 0)

AUTONOMY error auto_146_BTCUSDT_4h_direction_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:17:55 UTC (tier 0)

START gen=auto_147_ETHUSDT_4h_direction_ohlcv_v1 ETHUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:18:04 UTC (tier 0)

PREDICTABILITY real=+0.00359 p=0.0476 surr_q95=-0.00075 surr_max=+0.00030 draws=20 passed=True

## [INFO] 2026-08-03 09:18:05 UTC (tier 0)

AUTONOMY error auto_147_ETHUSDT_4h_direction_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:18:05 UTC (tier 0)

START gen=auto_148_ETHUSDT_4h_direction_indicators_v1 ETHUSDT 4h target=direction space=indicators_v1

## [INFO] 2026-08-03 09:18:11 UTC (tier 0)

PREDICTABILITY real=-0.01466 p=0.8095 surr_q95=-0.00081 surr_max=+0.00570 draws=20 passed=False

## [INFO] 2026-08-03 09:18:12 UTC (tier 0)

AUTONOMY error auto_148_ETHUSDT_4h_direction_indicators_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:18:12 UTC (tier 0)

START gen=auto_149_ETHUSDT_4h_direction_pivot_v1 ETHUSDT 4h target=direction space=pivot_v1

## [INFO] 2026-08-03 09:18:15 UTC (tier 0)

PREDICTABILITY real=-0.00215 p=0.3810 surr_q95=+0.00087 surr_max=+0.00130 draws=20 passed=False

## [INFO] 2026-08-03 09:18:16 UTC (tier 0)

AUTONOMY error auto_149_ETHUSDT_4h_direction_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:18:16 UTC (tier 0)

START gen=auto_150_SOLUSDT_4h_direction_ohlcv_v1 SOLUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:18:20 UTC (tier 0)

PREDICTABILITY real=+0.00339 p=0.0476 surr_q95=-0.00013 surr_max=+0.00033 draws=20 passed=True

## [INFO] 2026-08-03 09:18:21 UTC (tier 0)

AUTONOMY error auto_150_SOLUSDT_4h_direction_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:18:21 UTC (tier 0)

START gen=auto_151_SOLUSDT_4h_direction_indicators_v1 SOLUSDT 4h target=direction space=indicators_v1

## [INFO] 2026-08-03 09:18:26 UTC (tier 0)

PREDICTABILITY real=+0.00113 p=0.0476 surr_q95=-0.00297 surr_max=-0.00164 draws=20 passed=True

## [INFO] 2026-08-03 09:18:27 UTC (tier 0)

AUTONOMY error auto_151_SOLUSDT_4h_direction_indicators_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:18:27 UTC (tier 0)

START gen=auto_152_SOLUSDT_4h_direction_pivot_v1 SOLUSDT 4h target=direction space=pivot_v1

## [INFO] 2026-08-03 09:18:30 UTC (tier 0)

PREDICTABILITY real=-0.00838 p=0.9048 surr_q95=+0.00217 surr_max=+0.00439 draws=20 passed=False

## [INFO] 2026-08-03 09:18:31 UTC (tier 0)

AUTONOMY error auto_152_SOLUSDT_4h_direction_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:18:31 UTC (tier 0)

START gen=auto_153_BTCUSDT_15m_direction_ohlcv_v1 BTCUSDT 15m target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:19:31 UTC (tier 0)

PREDICTABILITY real=+0.00985 p=0.0476 surr_q95=-0.00003 surr_max=+0.00004 draws=20 passed=True

## [INFO] 2026-08-03 09:19:32 UTC (tier 0)

AUTONOMY error auto_153_BTCUSDT_15m_direction_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:19:32 UTC (tier 0)

START gen=auto_154_BTCUSDT_15m_direction_indicators_v1 BTCUSDT 15m target=direction space=indicators_v1

## [INFO] 2026-08-03 09:20:31 UTC (tier 0)

PREDICTABILITY real=+0.00323 p=0.0476 surr_q95=+0.00008 surr_max=+0.00016 draws=20 passed=True

## [INFO] 2026-08-03 09:20:33 UTC (tier 0)

AUTONOMY error auto_154_BTCUSDT_15m_direction_indicators_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:20:33 UTC (tier 0)

START gen=auto_155_BTCUSDT_15m_direction_pivot_v1 BTCUSDT 15m target=direction space=pivot_v1

## [INFO] 2026-08-03 09:21:03 UTC (tier 0)

PREDICTABILITY real=+0.00617 p=0.0476 surr_q95=+0.00010 surr_max=+0.00022 draws=20 passed=True

## [INFO] 2026-08-03 09:21:04 UTC (tier 0)

AUTONOMY error auto_155_BTCUSDT_15m_direction_pivot_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:21:04 UTC (tier 0)

START gen=auto_156_ETHUSDT_15m_direction_ohlcv_v1 ETHUSDT 15m target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:22:08 UTC (tier 0)

PREDICTABILITY real=+0.00820 p=0.0476 surr_q95=+0.00002 surr_max=+0.00036 draws=20 passed=True

## [INFO] 2026-08-03 09:22:10 UTC (tier 0)

AUTONOMY error auto_156_ETHUSDT_15m_direction_ohlcv_v1: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'.
A suitable version of pyarrow or fastparquet is required for parquet support.
Trying to import the above resulted in these errors:
 - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
 - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.

## [INFO] 2026-08-03 09:22:10 UTC (tier 0)

START gen=auto_157_ETHUSDT_15m_direction_indicators_v1 ETHUSDT 15m target=direction space=indicators_v1

## [INFO] 2026-08-03 09:23:18 UTC (tier 0)

AUTONOMY start 162 combos; frozen_out=[]; active=['vol_ratio', 'volatility', 'xs_rank', 'quantile', 'fwd_return', 'direction']

## [INFO] 2026-08-03 09:23:19 UTC (tier 0)

START gen=auto_131_ETHUSDT_15m_fwd_return_pivot_v1 ETHUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 09:23:31 UTC (tier 0)

PREDICTABILITY real=+0.00498 p=0.0476 surr_q95=-0.00020 surr_max=-0.00013 draws=20 passed=True

## [INFO] 2026-08-03 09:23:33 UTC (tier 0)

AUTONOMY error auto_157_ETHUSDT_15m_direction_indicators_v1: No type extension with name arrow.py_extension_type found

## [INFO] 2026-08-03 09:23:51 UTC (tier 0)

PREDICTABILITY real=-0.00081 p=0.9524 surr_q95=+0.00024 surr_max=+0.00026 draws=20 passed=False

## [INFO] 2026-08-03 09:23:51 UTC (tier 0)

AUTONOMY error auto_131_ETHUSDT_15m_fwd_return_pivot_v1: No type extension with name arrow.py_extension_type found

## [INFO] 2026-08-03 09:23:51 UTC (tier 0)

START gen=auto_132_SOLUSDT_15m_fwd_return_ohlcv_v1 SOLUSDT 15m target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 09:24:24 UTC (tier 0)

PREDICTABILITY real=+0.00050 p=0.0476 surr_q95=-0.00003 surr_max=+0.00013 draws=20 passed=True

## [INFO] 2026-08-03 09:24:24 UTC (tier 0)

AUTONOMY error auto_132_SOLUSDT_15m_fwd_return_ohlcv_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:24:24 UTC (tier 0)

START gen=auto_133_SOLUSDT_15m_fwd_return_indicators_v1 SOLUSDT 15m target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 09:25:00 UTC (tier 0)

PREDICTABILITY real=-0.00304 p=0.9524 surr_q95=+0.00012 surr_max=+0.00053 draws=20 passed=False

## [INFO] 2026-08-03 09:25:00 UTC (tier 0)

AUTONOMY error auto_133_SOLUSDT_15m_fwd_return_indicators_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:25:00 UTC (tier 0)

START gen=auto_134_SOLUSDT_15m_fwd_return_pivot_v1 SOLUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 09:25:21 UTC (tier 0)

PREDICTABILITY real=-0.00106 p=1.0000 surr_q95=+0.00007 surr_max=+0.00009 draws=20 passed=False

## [INFO] 2026-08-03 09:25:21 UTC (tier 0)

AUTONOMY error auto_134_SOLUSDT_15m_fwd_return_pivot_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:25:21 UTC (tier 0)

START gen=auto_135_BTCUSDT_1h_direction_ohlcv_v1 BTCUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:25:34 UTC (tier 0)

PREDICTABILITY real=+0.00789 p=0.0476 surr_q95=-0.00021 surr_max=-0.00007 draws=20 passed=True

## [INFO] 2026-08-03 09:25:34 UTC (tier 0)

AUTONOMY error auto_135_BTCUSDT_1h_direction_ohlcv_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:25:34 UTC (tier 0)

START gen=auto_136_BTCUSDT_1h_direction_indicators_v1 BTCUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 09:25:47 UTC (tier 0)

PREDICTABILITY real=-0.00281 p=0.7619 surr_q95=+0.00097 surr_max=+0.00103 draws=20 passed=False

## [INFO] 2026-08-03 09:25:47 UTC (tier 0)

AUTONOMY error auto_136_BTCUSDT_1h_direction_indicators_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:25:47 UTC (tier 0)

START gen=auto_137_BTCUSDT_1h_direction_pivot_v1 BTCUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 09:25:54 UTC (tier 0)

PREDICTABILITY real=+0.00829 p=0.0476 surr_q95=+0.00090 surr_max=+0.00094 draws=20 passed=True

## [INFO] 2026-08-03 09:25:54 UTC (tier 0)

AUTONOMY error auto_137_BTCUSDT_1h_direction_pivot_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:25:54 UTC (tier 0)

START gen=auto_138_ETHUSDT_1h_direction_ohlcv_v1 ETHUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:26:05 UTC (tier 0)

PREDICTABILITY real=+0.00392 p=0.0476 surr_q95=-0.00007 surr_max=-0.00003 draws=20 passed=True

## [INFO] 2026-08-03 09:26:05 UTC (tier 0)

AUTONOMY error auto_138_ETHUSDT_1h_direction_ohlcv_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:26:05 UTC (tier 0)

START gen=auto_139_ETHUSDT_1h_direction_indicators_v1 ETHUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 09:26:19 UTC (tier 0)

PREDICTABILITY real=+0.00459 p=0.0476 surr_q95=+0.00036 surr_max=+0.00108 draws=20 passed=True

## [INFO] 2026-08-03 09:26:19 UTC (tier 0)

AUTONOMY error auto_139_ETHUSDT_1h_direction_indicators_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:26:19 UTC (tier 0)

START gen=auto_140_ETHUSDT_1h_direction_pivot_v1 ETHUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 09:26:25 UTC (tier 0)

PREDICTABILITY real=+0.00190 p=0.0476 surr_q95=+0.00011 surr_max=+0.00121 draws=20 passed=True

## [INFO] 2026-08-03 09:26:25 UTC (tier 0)

AUTONOMY error auto_140_ETHUSDT_1h_direction_pivot_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:26:25 UTC (tier 0)

START gen=auto_141_SOLUSDT_1h_direction_ohlcv_v1 SOLUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 09:26:46 UTC (tier 0)

PREDICTABILITY real=+0.00058 p=0.0952 surr_q95=+0.00029 surr_max=+0.00067 draws=20 passed=False

## [INFO] 2026-08-03 09:26:46 UTC (tier 0)

AUTONOMY error auto_141_SOLUSDT_1h_direction_ohlcv_v1: A type extension with name pandas.period already defined

## [INFO] 2026-08-03 09:27:46 UTC (tier 0)

AUTONOMY start 162 combos; gate_revision=g2; parquet_engine=pyarrow; frozen_out=[]; active=['vol_ratio', 'volatility', 'xs_rank', 'quantile', 'fwd_return', 'direction']

## [INFO] 2026-08-03 09:27:46 UTC (tier 0)

START gen=autog2_000_BTCUSDT_1h_vol_ratio_ohlcv_v1 BTCUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:28:08 UTC (tier 0)

PREDICTABILITY real=+0.24591 p=0.0476 surr_q95=+0.06646 surr_max=+0.08202 draws=20 passed=True

## [INFO] 2026-08-03 09:28:11 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:28:11 UTC (tier 0)

trial `4ad9aba8-7b82-4b03-a254-0a751717e170` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-03 09:28:11 UTC (tier 1)

trial `97759e35-32f8-4833-9d80-00ae1bd3e2e8` model=ridge tier=1 target=vol_ratio skill=1.063 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:28:20 UTC (tier 1)

trial `6c18643a-2a14-4f50-88b6-bee3c057d926` model=lgbm_regressor tier=1 target=vol_ratio skill=1.129 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:28:22 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06290 skill_surrogate=+0.06290

## [INFO] 2026-08-03 09:28:22 UTC (tier 0)

trial `c2701389-50cc-432b-ab85-ad03dab0ba48` model=lgbm_classifier tier=0 target=vol_ratio skill=1.060 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:28:22 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_000_BTCUSDT_1h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:28:22 UTC (tier 1)

AUTONOMY screen autog2_000_BTCUSDT_1h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.1287881645516609 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:28:22 UTC (tier 0)

START gen=autog2_000_BTCUSDT_1h_vol_ratio_ohlcv_v1_ts BTCUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:28:46 UTC (tier 0)

PREDICTABILITY real=+0.24591 p=0.0476 surr_q95=+0.06646 surr_max=+0.08202 draws=20 passed=True

## [INFO] 2026-08-03 09:28:54 UTC (tier 1)

trial `ba9c8505-2adb-4726-a7b8-d14bf13d7c4b` model=lgbm_regressor tier=1 target=vol_ratio skill=1.129 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:28:54 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_000_BTCUSDT_1h_vol_ratio_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:28:54 UTC (tier 1)

AUTONOMY tradesim autog2_000_BTCUSDT_1h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.1287881645516609

## [INFO] 2026-08-03 09:28:54 UTC (tier 0)

START gen=autog2_001_BTCUSDT_1h_vol_ratio_indicators_v1 BTCUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:29:28 UTC (tier 0)

PREDICTABILITY real=+0.11278 p=0.0476 surr_q95=+0.00041 surr_max=+0.00331 draws=20 passed=True

## [INFO] 2026-08-03 09:29:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:29:36 UTC (tier 0)

trial `cd8bf202-ee7a-4653-b1af-20376a1b2b52` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:29:36 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01111 skill_surrogate=-0.01347

## [INFO] 2026-08-03 09:29:36 UTC (tier 0)

trial `b9d5f7ee-1559-4f60-bd8e-9bd1b0d1c77f` model=ridge tier=0 target=vol_ratio skill=1.065 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:29:44 UTC (tier 1)

trial `82a9fe23-8240-485b-95f5-102f93089e5d` model=lgbm_regressor tier=1 target=vol_ratio skill=1.002 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:29:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06305 skill_surrogate=+0.06305

## [INFO] 2026-08-03 09:29:45 UTC (tier 0)

trial `2751cd59-6296-40cf-b3df-efbb4b0f6104` model=lgbm_classifier tier=0 target=vol_ratio skill=1.060 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:29:45 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_001_BTCUSDT_1h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:29:45 UTC (tier 1)

AUTONOMY screen autog2_001_BTCUSDT_1h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0018871600620736 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:29:45 UTC (tier 0)

START gen=autog2_001_BTCUSDT_1h_vol_ratio_indicators_v1_ts BTCUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:30:06 UTC (tier 0)

PREDICTABILITY real=+0.11278 p=0.0476 surr_q95=+0.00041 surr_max=+0.00331 draws=20 passed=True

## [INFO] 2026-08-03 09:30:12 UTC (tier 1)

trial `098d748f-3f09-4076-a954-88e2760bbccd` model=lgbm_regressor tier=1 target=vol_ratio skill=1.002 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:30:12 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_001_BTCUSDT_1h_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:30:12 UTC (tier 1)

AUTONOMY tradesim autog2_001_BTCUSDT_1h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0018871600620736

## [INFO] 2026-08-03 09:30:12 UTC (tier 0)

START gen=autog2_002_BTCUSDT_1h_vol_ratio_pivot_v1 BTCUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:30:22 UTC (tier 0)

PREDICTABILITY real=+0.13377 p=0.0476 surr_q95=+0.00648 surr_max=+0.00754 draws=20 passed=True

## [INFO] 2026-08-03 09:30:25 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:30:25 UTC (tier 0)

trial `933bfe65-8832-49e1-8bcd-aaa9a00570fd` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:30:25 UTC (tier 1)

trial `00f35732-47c2-4873-82ee-526ab07a8bd4` model=ridge tier=1 target=vol_ratio skill=1.107 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:30:27 UTC (tier 1)

trial `12f5d5c4-53a9-4667-bcee-d55c60ddc269` model=lgbm_regressor tier=1 target=vol_ratio skill=1.116 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:30:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06281 skill_surrogate=+0.06281

## [INFO] 2026-08-03 09:30:28 UTC (tier 0)

trial `172090a4-8cb0-4cd5-8dcc-3033eca24554` model=lgbm_classifier tier=0 target=vol_ratio skill=1.059 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:30:28 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_002_BTCUSDT_1h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:30:28 UTC (tier 1)

AUTONOMY screen autog2_002_BTCUSDT_1h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.116215847766803 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:30:28 UTC (tier 0)

START gen=autog2_002_BTCUSDT_1h_vol_ratio_pivot_v1_ts BTCUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:30:37 UTC (tier 0)

PREDICTABILITY real=+0.13377 p=0.0476 surr_q95=+0.00648 surr_max=+0.00754 draws=20 passed=True

## [INFO] 2026-08-03 09:30:42 UTC (tier 1)

trial `a3d2b056-41a0-4229-b5e4-fe9404475bec` model=lgbm_regressor tier=1 target=vol_ratio skill=1.116 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:30:42 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_002_BTCUSDT_1h_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:30:42 UTC (tier 1)

AUTONOMY tradesim autog2_002_BTCUSDT_1h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.116215847766803

## [INFO] 2026-08-03 09:30:42 UTC (tier 0)

START gen=autog2_003_ETHUSDT_1h_vol_ratio_ohlcv_v1 ETHUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:31:01 UTC (tier 0)

PREDICTABILITY real=+0.20795 p=0.0476 surr_q95=+0.03655 surr_max=+0.06994 draws=20 passed=True

## [INFO] 2026-08-03 09:31:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:31:09 UTC (tier 0)

trial `a17301bb-9ffc-4d15-8e1d-6dbb5622afd6` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-03 09:31:09 UTC (tier 1)

trial `c5a4c107-ecdf-4d31-9379-e7a3a7fc0172` model=ridge tier=1 target=vol_ratio skill=1.053 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:31:12 UTC (tier 1)

trial `4f5aa699-520f-4f55-ab46-462306ae2826` model=lgbm_regressor tier=1 target=vol_ratio skill=1.103 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:31:13 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05804 skill_surrogate=+0.05804

## [INFO] 2026-08-03 09:31:13 UTC (tier 0)

trial `e571ee94-6990-4e9c-83a1-048e914593fc` model=lgbm_classifier tier=0 target=vol_ratio skill=1.054 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:31:13 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_003_ETHUSDT_1h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:31:13 UTC (tier 1)

AUTONOMY screen autog2_003_ETHUSDT_1h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.103409254981764 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:31:13 UTC (tier 0)

START gen=autog2_003_ETHUSDT_1h_vol_ratio_ohlcv_v1_ts ETHUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:31:33 UTC (tier 0)

PREDICTABILITY real=+0.20795 p=0.0476 surr_q95=+0.03655 surr_max=+0.06994 draws=20 passed=True

## [INFO] 2026-08-03 09:31:43 UTC (tier 1)

trial `be7c7658-c21b-44b9-8599-a4d058a52929` model=lgbm_regressor tier=1 target=vol_ratio skill=1.103 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:31:43 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_003_ETHUSDT_1h_vol_ratio_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:31:43 UTC (tier 1)

AUTONOMY tradesim autog2_003_ETHUSDT_1h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.103409254981764

## [INFO] 2026-08-03 09:31:43 UTC (tier 0)

START gen=autog2_004_ETHUSDT_1h_vol_ratio_indicators_v1 ETHUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:32:01 UTC (tier 0)

PREDICTABILITY real=+0.09526 p=0.0476 surr_q95=-0.00010 surr_max=+0.00512 draws=20 passed=True

## [INFO] 2026-08-03 09:32:05 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:32:05 UTC (tier 0)

trial `b22860e0-1b00-47be-b6c5-c9ee9d68014b` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:32:05 UTC (tier 1)

trial `32e4468a-72a4-43fe-9786-4aadf2aa0496` model=ridge tier=1 target=vol_ratio skill=1.089 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:32:09 UTC (tier 1)

trial `cdc77238-b98c-4777-9da2-af0967a05e3e` model=lgbm_regressor tier=1 target=vol_ratio skill=0.978 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:32:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05813 skill_surrogate=+0.05813

## [INFO] 2026-08-03 09:32:10 UTC (tier 0)

trial `6ed112d8-4482-42a0-9aaa-f45cb60ec3cb` model=lgbm_classifier tier=0 target=vol_ratio skill=1.054 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:32:10 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_004_ETHUSDT_1h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:32:10 UTC (tier 1)

AUTONOMY screen autog2_004_ETHUSDT_1h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0890694563877426 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:32:10 UTC (tier 0)

START gen=autog2_004_ETHUSDT_1h_vol_ratio_indicators_v1_ts ETHUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:32:36 UTC (tier 0)

PREDICTABILITY real=+0.09526 p=0.0476 surr_q95=-0.00010 surr_max=+0.00512 draws=20 passed=True

## [INFO] 2026-08-03 09:32:42 UTC (tier 1)

trial `2cedbca7-ae42-46c7-b871-40da79a554be` model=ridge tier=1 target=vol_ratio skill=1.089 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:32:42 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_004_ETHUSDT_1h_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:32:42 UTC (tier 1)

AUTONOMY tradesim autog2_004_ETHUSDT_1h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0890694563877426

## [INFO] 2026-08-03 09:32:42 UTC (tier 0)

START gen=autog2_005_ETHUSDT_1h_vol_ratio_pivot_v1 ETHUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:32:53 UTC (tier 0)

PREDICTABILITY real=+0.16805 p=0.0476 surr_q95=+0.00338 surr_max=+0.00952 draws=20 passed=True

## [INFO] 2026-08-03 09:32:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 09:32:55 UTC (tier 0)

trial `6a86516e-6953-4314-8bf5-5aa5723a06cc` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:32:55 UTC (tier 1)

trial `6a0d2da2-ef55-4c63-ae18-3467e4e7348c` model=ridge tier=1 target=vol_ratio skill=1.109 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:32:57 UTC (tier 1)

trial `0fcb6ff2-581f-4eaa-838e-4de33ac7c5a2` model=lgbm_regressor tier=1 target=vol_ratio skill=1.121 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:32:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05777 skill_surrogate=+0.05777

## [INFO] 2026-08-03 09:32:58 UTC (tier 0)

trial `f1930b34-f0ff-4033-aef3-38a79bdb4ef6` model=lgbm_classifier tier=0 target=vol_ratio skill=1.053 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:32:58 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_005_ETHUSDT_1h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:32:58 UTC (tier 1)

AUTONOMY screen autog2_005_ETHUSDT_1h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.1207453579891 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:32:58 UTC (tier 0)

START gen=autog2_005_ETHUSDT_1h_vol_ratio_pivot_v1_ts ETHUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:33:24 UTC (tier 0)

PREDICTABILITY real=+0.16805 p=0.0476 surr_q95=+0.00338 surr_max=+0.00952 draws=20 passed=True

## [INFO] 2026-08-03 09:33:35 UTC (tier 1)

trial `804e9128-f924-40e8-aae4-3e5f2844f52b` model=lgbm_regressor tier=1 target=vol_ratio skill=1.121 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:33:35 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_005_ETHUSDT_1h_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:33:35 UTC (tier 1)

AUTONOMY tradesim autog2_005_ETHUSDT_1h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.1207453579891

## [INFO] 2026-08-03 09:33:35 UTC (tier 0)

START gen=autog2_006_SOLUSDT_1h_vol_ratio_ohlcv_v1 SOLUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:34:13 UTC (tier 0)

PREDICTABILITY real=+0.22200 p=0.0476 surr_q95=+0.02085 surr_max=+0.02379 draws=20 passed=True

## [INFO] 2026-08-03 09:34:24 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:34:24 UTC (tier 0)

trial `577f364e-2f79-45b7-bb2e-7086da09bc1e` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-03 09:34:24 UTC (tier 1)

trial `d52d3913-9a90-49c9-a578-010d4f63400f` model=ridge tier=1 target=vol_ratio skill=1.033 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:34:30 UTC (tier 1)

trial `526f5352-eb41-4447-8699-005b3e97ed51` model=lgbm_regressor tier=1 target=vol_ratio skill=1.028 n=32855 gates=FAIL

## [INFO] 2026-08-03 09:34:31 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04932 skill_surrogate=+0.04932

## [INFO] 2026-08-03 09:34:31 UTC (tier 0)

trial `e60b8abb-900f-4be2-b049-7066d51bff00` model=lgbm_classifier tier=0 target=vol_ratio skill=1.046 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:34:31 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_006_SOLUSDT_1h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:34:31 UTC (tier 1)

AUTONOMY screen autog2_006_SOLUSDT_1h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.0329651928325683 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:34:31 UTC (tier 0)

START gen=autog2_006_SOLUSDT_1h_vol_ratio_ohlcv_v1_ts SOLUSDT 1h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:35:07 UTC (tier 0)

PREDICTABILITY real=+0.22200 p=0.0476 surr_q95=+0.02085 surr_max=+0.02379 draws=20 passed=True

## [INFO] 2026-08-03 09:35:13 UTC (tier 1)

trial `c53fa36a-5f8f-4b71-bc59-f700171a3701` model=ridge tier=1 target=vol_ratio skill=1.033 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 09:35:13 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_006_SOLUSDT_1h_vol_ratio_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:35:13 UTC (tier 1)

AUTONOMY tradesim autog2_006_SOLUSDT_1h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.0329651928325683

## [INFO] 2026-08-03 09:35:13 UTC (tier 0)

START gen=autog2_007_SOLUSDT_1h_vol_ratio_indicators_v1 SOLUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:35:52 UTC (tier 0)

PREDICTABILITY real=+0.11116 p=0.0476 surr_q95=-0.00083 surr_max=-0.00020 draws=20 passed=True

## [INFO] 2026-08-03 09:35:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 09:35:57 UTC (tier 0)

trial `02495724-cc95-4e73-b948-a59f2a065d59` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:35:58 UTC (tier 1)

trial `72923365-95e3-4dba-a0e9-3430e645589b` model=ridge tier=1 target=vol_ratio skill=1.044 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:36:04 UTC (tier 1)

trial `0d91ac98-4875-4368-a3fb-2924f630d416` model=lgbm_regressor tier=1 target=vol_ratio skill=0.890 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:36:05 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04937 skill_surrogate=+0.04937

## [INFO] 2026-08-03 09:36:05 UTC (tier 0)

trial `08081641-0d44-45f9-bcb0-6ef125cc6b58` model=lgbm_classifier tier=0 target=vol_ratio skill=1.046 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:36:05 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_007_SOLUSDT_1h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:36:05 UTC (tier 1)

AUTONOMY screen autog2_007_SOLUSDT_1h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0442374820055766 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:36:05 UTC (tier 0)

START gen=autog2_007_SOLUSDT_1h_vol_ratio_indicators_v1_ts SOLUSDT 1h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:36:51 UTC (tier 0)

PREDICTABILITY real=+0.11116 p=0.0476 surr_q95=-0.00083 surr_max=-0.00020 draws=20 passed=True

## [INFO] 2026-08-03 09:36:57 UTC (tier 1)

trial `a04c240a-7101-404f-8e19-92e35a2f8f34` model=ridge tier=1 target=vol_ratio skill=1.044 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:36:57 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_007_SOLUSDT_1h_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:36:57 UTC (tier 1)

AUTONOMY tradesim autog2_007_SOLUSDT_1h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0442374820055766

## [INFO] 2026-08-03 09:36:57 UTC (tier 0)

START gen=autog2_008_SOLUSDT_1h_vol_ratio_pivot_v1 SOLUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:37:20 UTC (tier 0)

PREDICTABILITY real=+0.16605 p=0.0476 surr_q95=+0.00321 surr_max=+0.00499 draws=20 passed=True

## [INFO] 2026-08-03 09:37:26 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:37:26 UTC (tier 0)

trial `f1a3c480-f560-47f2-9c22-a7a112ad330b` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 09:37:26 UTC (tier 1)

trial `ca1af089-f5a9-45d7-89da-637468b19fb7` model=ridge tier=1 target=vol_ratio skill=1.089 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:37:30 UTC (tier 1)

trial `fcb273af-2355-44b6-b68a-afaab4f79031` model=lgbm_regressor tier=1 target=vol_ratio skill=1.104 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:37:31 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04920 skill_surrogate=+0.04920

## [INFO] 2026-08-03 09:37:32 UTC (tier 0)

trial `90ec8f17-7956-4468-8bfe-59ba1d436fbe` model=lgbm_classifier tier=0 target=vol_ratio skill=1.046 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:37:32 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_008_SOLUSDT_1h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:37:32 UTC (tier 1)

AUTONOMY screen autog2_008_SOLUSDT_1h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.1038453941790123 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:37:32 UTC (tier 0)

START gen=autog2_008_SOLUSDT_1h_vol_ratio_pivot_v1_ts SOLUSDT 1h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:37:53 UTC (tier 0)

PREDICTABILITY real=+0.16605 p=0.0476 surr_q95=+0.00321 surr_max=+0.00499 draws=20 passed=True

## [INFO] 2026-08-03 09:38:06 UTC (tier 1)

trial `cf1c5bcf-11e7-4889-8837-f1142e0ef0dd` model=lgbm_regressor tier=1 target=vol_ratio skill=1.104 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 09:38:06 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_008_SOLUSDT_1h_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:38:06 UTC (tier 1)

AUTONOMY tradesim autog2_008_SOLUSDT_1h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.1038453941790123

## [INFO] 2026-08-03 09:38:06 UTC (tier 0)

START gen=autog2_009_BTCUSDT_4h_vol_ratio_ohlcv_v1 BTCUSDT 4h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:38:26 UTC (tier 0)

PREDICTABILITY real=+0.15969 p=0.0476 surr_q95=+0.05268 surr_max=+0.05519 draws=20 passed=True

## [INFO] 2026-08-03 09:38:28 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:38:28 UTC (tier 0)

trial `94a9aa32-5efe-4437-b360-f635597a334a` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:38:28 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00585 skill_surrogate=-0.00060

## [INFO] 2026-08-03 09:38:28 UTC (tier 0)

trial `4d2bdca2-199c-494b-b046-f0eb28f67a76` model=ridge tier=0 target=vol_ratio skill=1.021 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:38:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01273 skill_surrogate=-0.00969

## [INFO] 2026-08-03 09:38:34 UTC (tier 0)

trial `bb47edfa-d3bc-4509-9f1e-9f1869ecc93c` model=lgbm_regressor tier=0 target=vol_ratio skill=1.041 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:38:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05352 skill_surrogate=+0.05352

## [INFO] 2026-08-03 09:38:34 UTC (tier 0)

trial `2746293f-b391-4bd5-9a1c-a47dd9cb7f82` model=lgbm_classifier tier=0 target=vol_ratio skill=1.059 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:38:34 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_009_BTCUSDT_4h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:38:34 UTC (tier 0)

AUTONOMY screen autog2_009_BTCUSDT_4h_vol_ratio_ohlcv_v1 tier=0 proxy_skill=1.058917175717542 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:38:34 UTC (tier 0)

START gen=autog2_010_BTCUSDT_4h_vol_ratio_indicators_v1 BTCUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:38:49 UTC (tier 0)

PREDICTABILITY real=+0.13001 p=0.0476 surr_q95=-0.00122 surr_max=+0.00041 draws=20 passed=True

## [INFO] 2026-08-03 09:38:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:38:50 UTC (tier 0)

trial `cfd8f30a-ea2e-4557-b761-9e7a70e804ea` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:38:50 UTC (tier 1)

trial `d63983e7-a914-4237-9a19-94d93270d6d3` model=ridge tier=1 target=vol_ratio skill=1.056 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:38:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.71588 skill_surrogate=-0.03184

## [INFO] 2026-08-03 09:38:57 UTC (tier 0)

trial `4b66c842-8bc3-4da8-8a47-17069a942fab` model=lgbm_regressor tier=0 target=vol_ratio skill=0.707 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:38:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05113 skill_surrogate=+0.05113

## [INFO] 2026-08-03 09:38:57 UTC (tier 0)

trial `497eb3a0-5382-4e1d-a641-6ca8b6682898` model=lgbm_classifier tier=0 target=vol_ratio skill=1.056 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:38:57 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_010_BTCUSDT_4h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:38:57 UTC (tier 1)

AUTONOMY screen autog2_010_BTCUSDT_4h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0555832731547092 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:38:57 UTC (tier 0)

START gen=autog2_010_BTCUSDT_4h_vol_ratio_indicators_v1_ts BTCUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:39:05 UTC (tier 0)

PREDICTABILITY real=+0.13001 p=0.0476 surr_q95=-0.00122 surr_max=+0.00041 draws=20 passed=True

## [INFO] 2026-08-03 09:39:07 UTC (tier 1)

trial `a1b78824-7d8b-4332-b2ea-53bf7f24a6aa` model=ridge tier=1 target=vol_ratio skill=1.056 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:07 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_010_BTCUSDT_4h_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:39:07 UTC (tier 1)

AUTONOMY tradesim autog2_010_BTCUSDT_4h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0555832731547092

## [INFO] 2026-08-03 09:39:07 UTC (tier 0)

START gen=autog2_011_BTCUSDT_4h_vol_ratio_pivot_v1 BTCUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:39:14 UTC (tier 0)

PREDICTABILITY real=+0.04582 p=0.0476 surr_q95=+0.00415 surr_max=+0.01784 draws=20 passed=True

## [INFO] 2026-08-03 09:39:15 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:39:15 UTC (tier 0)

trial `865bc98f-e7a9-4e05-aae3-d2b0c69638c4` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:39:15 UTC (tier 1)

trial `37573e45-0d9e-4834-9348-d98d07595168` model=ridge tier=1 target=vol_ratio skill=1.037 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:16 UTC (tier 0)

PREREG diag001_pulse_continuation_BTCUSDT_1h status=PREREGISTERED sha256=aa8a75d88c89e63a fold_design=6c52076664e2fe64 hold=96 sl=0.1 lev=9.0 engine_stamp=9a037b290c8a

## [INFO] 2026-08-03 09:39:17 UTC (tier 1)

trial `abc6d1a9-3662-425b-98e3-311d244f6449` model=lgbm_regressor tier=1 target=vol_ratio skill=1.018 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:17 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05321 skill_surrogate=+0.05321

## [INFO] 2026-08-03 09:39:17 UTC (tier 0)

trial `45770024-111c-4cf7-a2ab-4e6d3f2cde75` model=lgbm_classifier tier=0 target=vol_ratio skill=1.058 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:17 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_011_BTCUSDT_4h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:39:17 UTC (tier 1)

AUTONOMY screen autog2_011_BTCUSDT_4h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.0373287131346058 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:39:17 UTC (tier 0)

START gen=autog2_011_BTCUSDT_4h_vol_ratio_pivot_v1_ts BTCUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:39:21 UTC (tier 0)

PREDICTABILITY real=+0.04582 p=0.0476 surr_q95=+0.00415 surr_max=+0.01784 draws=20 passed=True

## [INFO] 2026-08-03 09:39:22 UTC (tier 1)

trial `684ee3f1-f923-4fe0-a708-63e8054f7729` model=ridge tier=1 target=vol_ratio skill=1.037 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:22 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_011_BTCUSDT_4h_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:39:22 UTC (tier 1)

AUTONOMY tradesim autog2_011_BTCUSDT_4h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.0373287131346058

## [INFO] 2026-08-03 09:39:22 UTC (tier 0)

START gen=autog2_012_ETHUSDT_4h_vol_ratio_ohlcv_v1 ETHUSDT 4h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:39:32 UTC (tier 0)

PREDICTABILITY real=+0.12339 p=0.0476 surr_q95=+0.03657 surr_max=+0.04006 draws=20 passed=True

## [INFO] 2026-08-03 09:39:33 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 09:39:33 UTC (tier 0)

trial `077e5475-b784-4c9e-9a21-a68646e722a6` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:39:33 UTC (tier 1)

trial `384b52f8-8555-4610-a9ff-a8e6920e3779` model=ridge tier=1 target=vol_ratio skill=1.058 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:35 UTC (tier 1)

trial `beab7869-9e87-4676-a94d-ba025e44fce3` model=lgbm_regressor tier=1 target=vol_ratio skill=0.993 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:39:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06059 skill_surrogate=+0.06059

## [INFO] 2026-08-03 09:39:35 UTC (tier 0)

trial `5b262f66-91de-4442-838d-0d23844dbe77` model=lgbm_classifier tier=0 target=vol_ratio skill=1.058 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:35 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_012_ETHUSDT_4h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:39:35 UTC (tier 1)

AUTONOMY screen autog2_012_ETHUSDT_4h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.0580094881335798 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:39:35 UTC (tier 0)

START gen=autog2_012_ETHUSDT_4h_vol_ratio_ohlcv_v1_ts ETHUSDT 4h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:39:45 UTC (tier 0)

PREDICTABILITY real=+0.12339 p=0.0476 surr_q95=+0.03657 surr_max=+0.04006 draws=20 passed=True

## [INFO] 2026-08-03 09:39:46 UTC (tier 1)

trial `c582c694-d695-4c1d-8aea-bf2c55386270` model=ridge tier=1 target=vol_ratio skill=1.058 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:46 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_012_ETHUSDT_4h_vol_ratio_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:39:46 UTC (tier 1)

AUTONOMY tradesim autog2_012_ETHUSDT_4h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.0580094881335798

## [INFO] 2026-08-03 09:39:46 UTC (tier 0)

START gen=autog2_013_ETHUSDT_4h_vol_ratio_indicators_v1 ETHUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:39:54 UTC (tier 0)

PREDICTABILITY real=+0.12055 p=0.0476 surr_q95=+0.00121 surr_max=+0.00445 draws=20 passed=True

## [INFO] 2026-08-03 09:39:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:39:55 UTC (tier 0)

trial `5ca79cdd-fb5e-4b0b-8c07-df99f9a8f073` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:39:55 UTC (tier 1)

trial `0b08c965-6a10-4dbc-8754-3b6470c2bbda` model=ridge tier=1 target=vol_ratio skill=1.105 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:57 UTC (tier 1)

trial `81523201-e83e-4894-98f6-27cc3a805f2a` model=lgbm_regressor tier=1 target=vol_ratio skill=0.922 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:39:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06086 skill_surrogate=+0.06086

## [INFO] 2026-08-03 09:39:57 UTC (tier 0)

trial `0fcb14f5-8aa4-4bd1-b628-d3892e7edea5` model=lgbm_classifier tier=0 target=vol_ratio skill=1.058 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:39:57 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_013_ETHUSDT_4h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:39:57 UTC (tier 1)

AUTONOMY screen autog2_013_ETHUSDT_4h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.105217771789115 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:39:57 UTC (tier 0)

START gen=autog2_013_ETHUSDT_4h_vol_ratio_indicators_v1_ts ETHUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:40:07 UTC (tier 0)

PREDICTABILITY real=+0.12055 p=0.0476 surr_q95=+0.00121 surr_max=+0.00445 draws=20 passed=True

## [INFO] 2026-08-03 09:40:08 UTC (tier 1)

trial `f6886d54-fac9-4f8f-a6bc-ebe779b53834` model=ridge tier=1 target=vol_ratio skill=1.105 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:40:08 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_013_ETHUSDT_4h_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:40:08 UTC (tier 1)

AUTONOMY tradesim autog2_013_ETHUSDT_4h_vol_ratio_indicators_v1 tier=1 proxy_skill=1.105217771789115

## [INFO] 2026-08-03 09:40:08 UTC (tier 0)

START gen=autog2_014_ETHUSDT_4h_vol_ratio_pivot_v1 ETHUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:40:13 UTC (tier 0)

PREDICTABILITY real=+0.08177 p=0.0476 surr_q95=+0.00052 surr_max=+0.00484 draws=20 passed=True

## [INFO] 2026-08-03 09:40:14 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:40:14 UTC (tier 0)

trial `cc6c0a66-cc6e-43f2-b926-f58a2845a98b` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:40:14 UTC (tier 1)

trial `7347ce0f-3796-493d-be84-7ca701f3b362` model=ridge tier=1 target=vol_ratio skill=1.081 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:40:14 UTC (tier 0)

PREREG diag001_pulse_continuation_BTCUSDT_1h status=PREREGISTERED sha256=aa8a75d88c89e63a fold_design=6c52076664e2fe64 hold=96 sl=0.1 lev=9.0 engine_stamp=9a037b290c8a

## [INFO] 2026-08-03 09:40:16 UTC (tier 1)

trial `026bea35-13f2-4b8f-8815-a64fb2f82f7a` model=lgbm_regressor tier=1 target=vol_ratio skill=1.058 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:40:16 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05969 skill_surrogate=+0.05969

## [INFO] 2026-08-03 09:40:16 UTC (tier 0)

trial `e678cd78-bad8-4cc0-aa5a-481cf28037d7` model=lgbm_classifier tier=0 target=vol_ratio skill=1.056 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:40:16 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_014_ETHUSDT_4h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:40:16 UTC (tier 1)

AUTONOMY screen autog2_014_ETHUSDT_4h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.0812966863479607 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:40:16 UTC (tier 0)

START gen=autog2_014_ETHUSDT_4h_vol_ratio_pivot_v1_ts ETHUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:40:20 UTC (tier 0)

PREDICTABILITY real=+0.08177 p=0.0476 surr_q95=+0.00052 surr_max=+0.00484 draws=20 passed=True

## [INFO] 2026-08-03 09:40:21 UTC (tier 1)

trial `c978ad44-00a5-4a78-978f-eea6e0edcc1a` model=ridge tier=1 target=vol_ratio skill=1.081 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:40:21 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_014_ETHUSDT_4h_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:40:21 UTC (tier 1)

AUTONOMY tradesim autog2_014_ETHUSDT_4h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.0812966863479607

## [INFO] 2026-08-03 09:40:21 UTC (tier 0)

START gen=autog2_015_SOLUSDT_4h_vol_ratio_ohlcv_v1 SOLUSDT 4h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:40:25 UTC (tier 0)

PULSE_FAILS_ON_COST diag001_pulse_continuation_BTCUSDT_1h: pulse_pf=1.1176 pnl=10.85 n=92 | ctrl_pf=1.1168 pnl=6.82 n=82 | down_pf=0.8100 n=90 | entry_bar_stops=0 liq=0 folds_ok=True

## [INFO] 2026-08-03 09:40:31 UTC (tier 0)

PREDICTABILITY real=+0.03855 p=0.0476 surr_q95=-0.00103 surr_max=+0.00517 draws=20 passed=True

## [INFO] 2026-08-03 09:40:32 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:40:32 UTC (tier 0)

trial `261ac4a3-f23b-4cbd-b2b9-a1784c30f203` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:40:32 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01402 skill_surrogate=+0.00193

## [INFO] 2026-08-03 09:40:32 UTC (tier 0)

trial `b0715e8e-14a0-4f72-b20c-1244bba40d6d` model=ridge tier=0 target=vol_ratio skill=0.992 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:40:34 UTC (tier 1)

trial `10940c6c-a0a2-4c5e-82e8-0c0157234e90` model=lgbm_regressor tier=1 target=vol_ratio skill=0.955 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:40:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05371 skill_surrogate=+0.05371

## [INFO] 2026-08-03 09:40:35 UTC (tier 0)

trial `8cec2178-e260-4acd-8c11-97756df2a43b` model=lgbm_classifier tier=0 target=vol_ratio skill=1.068 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:40:35 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_015_SOLUSDT_4h_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:40:35 UTC (tier 1)

AUTONOMY screen autog2_015_SOLUSDT_4h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=0.9551776908167203 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:40:35 UTC (tier 0)

START gen=autog2_015_SOLUSDT_4h_vol_ratio_ohlcv_v1_ts SOLUSDT 4h target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:40:41 UTC (tier 0)

PREDICTABILITY real=+0.03855 p=0.0476 surr_q95=-0.00103 surr_max=+0.00517 draws=20 passed=True

## [INFO] 2026-08-03 09:40:44 UTC (tier 1)

trial `6eb88a64-87e0-4469-bb68-7ee32c963ab9` model=lgbm_regressor tier=1 target=vol_ratio skill=0.955 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:40:44 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_015_SOLUSDT_4h_vol_ratio_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:40:44 UTC (tier 1)

AUTONOMY tradesim autog2_015_SOLUSDT_4h_vol_ratio_ohlcv_v1 tier=1 proxy_skill=0.9551776908167203

## [INFO] 2026-08-03 09:40:44 UTC (tier 0)

START gen=autog2_016_SOLUSDT_4h_vol_ratio_indicators_v1 SOLUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:40:54 UTC (tier 0)

PREDICTABILITY real=+0.04468 p=0.0476 surr_q95=-0.00152 surr_max=+0.01127 draws=20 passed=True

## [INFO] 2026-08-03 09:40:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:40:55 UTC (tier 0)

trial `f5f75fbc-d0d0-4f59-82b9-7eeb4539851a` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:40:55 UTC (tier 1)

trial `e39aaa16-edb3-41d7-a2a7-34cf2fc2799b` model=ridge tier=1 target=vol_ratio skill=0.988 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:40:57 UTC (tier 1)

trial `154a3f3b-02a5-4330-b4a0-ff737ab0de9a` model=lgbm_regressor tier=1 target=vol_ratio skill=0.912 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:40:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05435 skill_surrogate=+0.05435

## [INFO] 2026-08-03 09:40:58 UTC (tier 0)

trial `02b2e255-3b97-4eed-8909-01b697366974` model=lgbm_classifier tier=0 target=vol_ratio skill=1.069 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:40:58 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_016_SOLUSDT_4h_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:40:58 UTC (tier 1)

AUTONOMY screen autog2_016_SOLUSDT_4h_vol_ratio_indicators_v1 tier=1 proxy_skill=0.988003429195714 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:40:58 UTC (tier 0)

START gen=autog2_016_SOLUSDT_4h_vol_ratio_indicators_v1_ts SOLUSDT 4h target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:41:06 UTC (tier 0)

PREDICTABILITY real=+0.04468 p=0.0476 surr_q95=-0.00152 surr_max=+0.01127 draws=20 passed=True

## [INFO] 2026-08-03 09:41:06 UTC (tier 1)

trial `9339231f-cb94-4d56-8df5-6a3e0d01b02a` model=ridge tier=1 target=vol_ratio skill=0.988 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:41:06 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_016_SOLUSDT_4h_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:41:06 UTC (tier 1)

AUTONOMY tradesim autog2_016_SOLUSDT_4h_vol_ratio_indicators_v1 tier=1 proxy_skill=0.988003429195714

## [INFO] 2026-08-03 09:41:06 UTC (tier 0)

START gen=autog2_017_SOLUSDT_4h_vol_ratio_pivot_v1 SOLUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:41:10 UTC (tier 0)

PREDICTABILITY real=+0.09786 p=0.0476 surr_q95=+0.00837 surr_max=+0.01211 draws=20 passed=True

## [INFO] 2026-08-03 09:41:10 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:41:10 UTC (tier 0)

trial `c0991981-d301-4c82-903d-1e13915d7acf` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 09:41:10 UTC (tier 1)

trial `3830e842-269f-40e4-83bd-1fe45e041474` model=ridge tier=1 target=vol_ratio skill=1.048 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:41:13 UTC (tier 1)

trial `08540b6e-17c5-43bb-830c-6689191b3c23` model=lgbm_regressor tier=1 target=vol_ratio skill=1.037 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:41:13 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.05235 skill_surrogate=+0.05235

## [INFO] 2026-08-03 09:41:13 UTC (tier 0)

trial `557dfe91-3019-4317-b6b1-7a2f4b84b5ae` model=lgbm_classifier tier=0 target=vol_ratio skill=1.065 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:41:13 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_017_SOLUSDT_4h_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:41:13 UTC (tier 1)

AUTONOMY screen autog2_017_SOLUSDT_4h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.0480994467541367 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:41:13 UTC (tier 0)

START gen=autog2_017_SOLUSDT_4h_vol_ratio_pivot_v1_ts SOLUSDT 4h target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:41:17 UTC (tier 0)

PREDICTABILITY real=+0.09786 p=0.0476 surr_q95=+0.00837 surr_max=+0.01211 draws=20 passed=True

## [INFO] 2026-08-03 09:41:18 UTC (tier 1)

trial `87eb896f-66fe-4cba-971a-0e7c50223599` model=ridge tier=1 target=vol_ratio skill=1.048 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 09:41:18 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_017_SOLUSDT_4h_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:41:18 UTC (tier 1)

AUTONOMY tradesim autog2_017_SOLUSDT_4h_vol_ratio_pivot_v1 tier=1 proxy_skill=1.0480994467541367

## [INFO] 2026-08-03 09:41:18 UTC (tier 0)

START gen=autog2_018_BTCUSDT_15m_vol_ratio_ohlcv_v1 BTCUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:41:31 UTC (tier 0)

PREREG diag001_pulse_continuation_BTCUSDT_1h status=PREREGISTERED sha256=aa8a75d88c89e63a fold_design=6c52076664e2fe64 hold=96 sl=0.1 lev=9.0 engine_stamp=9a037b290c8a

## [INFO] 2026-08-03 09:41:47 UTC (tier 0)

PULSE_FAILS_ON_COST diag001_pulse_continuation_BTCUSDT_1h: pulse_pf=1.0667 pnl=6.27 n=92 | ctrl_pf=1.0491 pnl=2.96 n=82 | down_pf=0.7790 n=90 | entry_bar_stops=0 liq=0 folds_ok=True

## [INFO] 2026-08-03 09:42:27 UTC (tier 0)

PREDICTABILITY real=+0.25197 p=0.0476 surr_q95=+0.03114 surr_max=+0.08185 draws=20 passed=True

## [INFO] 2026-08-03 09:43:23 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 09:43:23 UTC (tier 0)

trial `c7609345-bb32-46f8-af7d-39d0d34c99fb` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-03 09:43:24 UTC (tier 1)

trial `6ef7485f-fb9a-454b-90b9-ba4a711eb3a1` model=ridge tier=1 target=vol_ratio skill=1.073 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:43:34 UTC (tier 1)

trial `5cd6a806-27bf-454f-a0a0-21417e176df7` model=lgbm_regressor tier=1 target=vol_ratio skill=1.151 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:43:37 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.07156 skill_surrogate=+0.07156

## [INFO] 2026-08-03 09:43:37 UTC (tier 0)

trial `c28a02cd-0f92-4eaa-a23a-1a0931c50df8` model=lgbm_classifier tier=0 target=vol_ratio skill=1.069 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:43:37 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_018_BTCUSDT_15m_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:43:37 UTC (tier 1)

AUTONOMY screen autog2_018_BTCUSDT_15m_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.1510304051943747 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:43:37 UTC (tier 0)

START gen=autog2_018_BTCUSDT_15m_vol_ratio_ohlcv_v1_ts BTCUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:44:45 UTC (tier 0)

PREDICTABILITY real=+0.25197 p=0.0476 surr_q95=+0.03114 surr_max=+0.08185 draws=20 passed=True

## [INFO] 2026-08-03 09:45:06 UTC (tier 1)

trial `ba6a0a18-3cff-447d-9a10-254e25079409` model=lgbm_regressor tier=1 target=vol_ratio skill=1.151 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:45:06 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_018_BTCUSDT_15m_vol_ratio_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:45:06 UTC (tier 1)

AUTONOMY tradesim autog2_018_BTCUSDT_15m_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.1510304051943747

## [INFO] 2026-08-03 09:45:06 UTC (tier 0)

START gen=autog2_019_BTCUSDT_15m_vol_ratio_indicators_v1 BTCUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:45:50 UTC (tier 0)

PREDICTABILITY real=+0.08107 p=0.0476 surr_q95=+0.00325 surr_max=+0.00359 draws=20 passed=True

## [INFO] 2026-08-03 09:45:58 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:45:58 UTC (tier 0)

trial `30e9666b-b36e-48ef-a4ce-73ae1d16eccc` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 09:45:58 UTC (tier 1)

trial `8be523c6-bb69-4f6c-920d-5bd785169aa7` model=ridge tier=1 target=vol_ratio skill=1.055 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:46:04 UTC (tier 1)

trial `4cd55cee-4370-4de9-9690-585960f5e93e` model=lgbm_regressor tier=1 target=vol_ratio skill=0.988 n=131424 gates=FAIL

## [INFO] 2026-08-03 09:46:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.07156 skill_surrogate=+0.07156

## [INFO] 2026-08-03 09:46:07 UTC (tier 0)

trial `efc9499d-4fc2-4dc5-95ae-ffc9506f6ba3` model=lgbm_classifier tier=0 target=vol_ratio skill=1.069 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:46:07 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_019_BTCUSDT_15m_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:46:07 UTC (tier 1)

AUTONOMY screen autog2_019_BTCUSDT_15m_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0550255825182597 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:46:07 UTC (tier 0)

START gen=autog2_019_BTCUSDT_15m_vol_ratio_indicators_v1_ts BTCUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:47:04 UTC (tier 0)

PREDICTABILITY real=+0.08107 p=0.0476 surr_q95=+0.00325 surr_max=+0.00359 draws=20 passed=True

## [INFO] 2026-08-03 09:47:15 UTC (tier 1)

trial `1e2c7276-2e4a-4460-b23e-319065c31f22` model=ridge tier=1 target=vol_ratio skill=1.055 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:47:15 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_019_BTCUSDT_15m_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:47:15 UTC (tier 1)

AUTONOMY tradesim autog2_019_BTCUSDT_15m_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0550255825182597

## [INFO] 2026-08-03 09:47:15 UTC (tier 0)

START gen=autog2_020_BTCUSDT_15m_vol_ratio_pivot_v1 BTCUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:47:40 UTC (tier 0)

PREDICTABILITY real=+0.13141 p=0.0476 surr_q95=+0.00244 surr_max=+0.00417 draws=20 passed=True

## [INFO] 2026-08-03 09:47:53 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:47:53 UTC (tier 0)

trial `a07c09d1-c6c5-4961-9526-0b8752f6a622` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 09:47:53 UTC (tier 1)

trial `29ac07cb-6003-4362-bcac-3722f921a4c0` model=ridge tier=1 target=vol_ratio skill=1.098 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:47:57 UTC (tier 1)

trial `b769c8ae-f996-45d3-8c1c-0ca158594dcd` model=lgbm_regressor tier=1 target=vol_ratio skill=1.125 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:47:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.07154 skill_surrogate=+0.07154

## [INFO] 2026-08-03 09:47:58 UTC (tier 0)

trial `8e0c2224-8859-4ec8-a2a1-a07ca235a860` model=lgbm_classifier tier=0 target=vol_ratio skill=1.069 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:47:58 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_020_BTCUSDT_15m_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:47:58 UTC (tier 1)

AUTONOMY screen autog2_020_BTCUSDT_15m_vol_ratio_pivot_v1 tier=1 proxy_skill=1.124786825423441 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:47:58 UTC (tier 0)

START gen=autog2_020_BTCUSDT_15m_vol_ratio_pivot_v1_ts BTCUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:48:38 UTC (tier 0)

PREDICTABILITY real=+0.13141 p=0.0476 surr_q95=+0.00244 surr_max=+0.00417 draws=20 passed=True

## [INFO] 2026-08-03 09:49:03 UTC (tier 1)

trial `5f2dbf18-193c-47c6-b089-b3e8b3345c1b` model=lgbm_regressor tier=1 target=vol_ratio skill=1.125 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:49:03 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_020_BTCUSDT_15m_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:49:03 UTC (tier 1)

AUTONOMY tradesim autog2_020_BTCUSDT_15m_vol_ratio_pivot_v1 tier=1 proxy_skill=1.124786825423441

## [INFO] 2026-08-03 09:49:03 UTC (tier 0)

START gen=autog2_021_ETHUSDT_15m_vol_ratio_ohlcv_v1 ETHUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:50:30 UTC (tier 0)

PREDICTABILITY real=+0.21440 p=0.0476 surr_q95=+0.04475 surr_max=+0.06196 draws=20 passed=True

## [INFO] 2026-08-03 09:51:38 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:51:38 UTC (tier 0)

trial `72de29e2-f573-4c41-8034-26f242ea52e9` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-03 09:51:39 UTC (tier 1)

trial `49825a48-de81-4409-876b-5c4522b1d8af` model=ridge tier=1 target=vol_ratio skill=1.074 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:51:47 UTC (tier 1)

trial `2df92a2a-678b-469d-b647-808efbb056c0` model=lgbm_regressor tier=1 target=vol_ratio skill=1.134 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:51:50 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06668 skill_surrogate=+0.06668

## [INFO] 2026-08-03 09:51:50 UTC (tier 0)

trial `89676293-f886-48c5-9b28-80156255aa8c` model=lgbm_classifier tier=0 target=vol_ratio skill=1.057 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:51:50 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_021_ETHUSDT_15m_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:51:50 UTC (tier 1)

AUTONOMY screen autog2_021_ETHUSDT_15m_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.1342657671980088 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:51:50 UTC (tier 0)

START gen=autog2_021_ETHUSDT_15m_vol_ratio_ohlcv_v1_ts ETHUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:52:45 UTC (tier 0)

PREDICTABILITY real=+0.21440 p=0.0476 surr_q95=+0.04475 surr_max=+0.06196 draws=20 passed=True

## [INFO] 2026-08-03 09:52:58 UTC (tier 1)

trial `cfdcd5c5-5b77-4f29-99cd-cee8a7ad31f5` model=lgbm_regressor tier=1 target=vol_ratio skill=1.134 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:52:58 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_021_ETHUSDT_15m_vol_ratio_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:52:58 UTC (tier 1)

AUTONOMY tradesim autog2_021_ETHUSDT_15m_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.1342657671980088

## [INFO] 2026-08-03 09:52:58 UTC (tier 0)

START gen=autog2_022_ETHUSDT_15m_vol_ratio_indicators_v1 ETHUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:53:42 UTC (tier 0)

PREDICTABILITY real=+0.08987 p=0.0476 surr_q95=-0.00026 surr_max=+0.00008 draws=20 passed=True

## [INFO] 2026-08-03 09:53:54 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:53:54 UTC (tier 0)

trial `f17a9e81-ef5c-4d9d-af28-7beb8504255c` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 09:53:55 UTC (tier 1)

trial `125e859c-7555-46bf-a6d2-cbc2b6a3df85` model=ridge tier=1 target=vol_ratio skill=1.091 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:54:01 UTC (tier 1)

trial `518b0362-010d-47a2-81d1-23e7ba24d152` model=lgbm_regressor tier=1 target=vol_ratio skill=1.012 n=131424 gates=FAIL

## [INFO] 2026-08-03 09:54:04 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06670 skill_surrogate=+0.06670

## [INFO] 2026-08-03 09:54:04 UTC (tier 0)

trial `4b9cc5ec-bebd-4d4b-b5ca-9bb537f5d0c6` model=lgbm_classifier tier=0 target=vol_ratio skill=1.057 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:54:04 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_022_ETHUSDT_15m_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:54:04 UTC (tier 1)

AUTONOMY screen autog2_022_ETHUSDT_15m_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0907317885110825 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:54:04 UTC (tier 0)

START gen=autog2_022_ETHUSDT_15m_vol_ratio_indicators_v1_ts ETHUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 09:55:24 UTC (tier 0)

PREDICTABILITY real=+0.08987 p=0.0476 surr_q95=-0.00026 surr_max=+0.00008 draws=20 passed=True

## [INFO] 2026-08-03 09:55:39 UTC (tier 1)

trial `ef102fda-7cb7-4e1c-8290-d1f9d5a17c46` model=ridge tier=1 target=vol_ratio skill=1.091 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:55:39 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_022_ETHUSDT_15m_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:55:39 UTC (tier 1)

AUTONOMY tradesim autog2_022_ETHUSDT_15m_vol_ratio_indicators_v1 tier=1 proxy_skill=1.0907317885110825

## [INFO] 2026-08-03 09:55:39 UTC (tier 0)

START gen=autog2_023_ETHUSDT_15m_vol_ratio_pivot_v1 ETHUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:56:22 UTC (tier 0)

PREDICTABILITY real=+0.14932 p=0.0476 surr_q95=+0.00341 surr_max=+0.00542 draws=20 passed=True

## [INFO] 2026-08-03 09:56:37 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:56:37 UTC (tier 0)

trial `23cf0276-4708-4c69-9be8-5ee5b14b12ef` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 09:56:38 UTC (tier 1)

trial `0b63cb5e-016e-434e-9a07-fd323eaaf8e4` model=ridge tier=1 target=vol_ratio skill=1.113 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:56:42 UTC (tier 1)

trial `cd29541a-4dce-4f1a-8cf7-6d8ed33b0a9c` model=lgbm_regressor tier=1 target=vol_ratio skill=1.141 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:56:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.06660 skill_surrogate=+0.06660

## [INFO] 2026-08-03 09:56:43 UTC (tier 0)

trial `57535c31-e740-48ad-a062-e2b19b2f2853` model=lgbm_classifier tier=0 target=vol_ratio skill=1.057 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:56:43 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_023_ETHUSDT_15m_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:56:43 UTC (tier 1)

AUTONOMY screen autog2_023_ETHUSDT_15m_vol_ratio_pivot_v1 tier=1 proxy_skill=1.1409015723741756 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:56:43 UTC (tier 0)

START gen=autog2_023_ETHUSDT_15m_vol_ratio_pivot_v1_ts ETHUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 09:57:17 UTC (tier 0)

PREDICTABILITY real=+0.14932 p=0.0476 surr_q95=+0.00341 surr_max=+0.00542 draws=20 passed=True

## [INFO] 2026-08-03 09:57:40 UTC (tier 1)

trial `1869f45c-59c2-4a24-bffc-bbadc9eaa3d2` model=lgbm_regressor tier=1 target=vol_ratio skill=1.141 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 09:57:40 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_023_ETHUSDT_15m_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:57:40 UTC (tier 1)

AUTONOMY tradesim autog2_023_ETHUSDT_15m_vol_ratio_pivot_v1 tier=1 proxy_skill=1.1409015723741756

## [INFO] 2026-08-03 09:57:40 UTC (tier 0)

START gen=autog2_024_SOLUSDT_15m_vol_ratio_ohlcv_v1 SOLUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:58:45 UTC (tier 0)

PREDICTABILITY real=+0.21685 p=0.0476 surr_q95=+0.04042 surr_max=+0.06827 draws=20 passed=True

## [INFO] 2026-08-03 09:58:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 09:58:49 UTC (tier 0)

trial `9e191076-be05-4117-8cd0-cda76d9324b3` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-03 09:58:50 UTC (tier 1)

trial `61cb9489-2663-46f1-8244-8411a37bf3a5` model=ridge tier=1 target=vol_ratio skill=1.052 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:58:59 UTC (tier 1)

trial `d2ca736e-6d24-4877-ac50-fc0d7d269c57` model=lgbm_regressor tier=1 target=vol_ratio skill=1.100 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:59:01 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04518 skill_surrogate=+0.04518

## [INFO] 2026-08-03 09:59:01 UTC (tier 0)

trial `94857b8f-3b02-4166-b9b9-efd7b405f361` model=lgbm_classifier tier=0 target=vol_ratio skill=1.045 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 09:59:01 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_024_SOLUSDT_15m_vol_ratio_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 09:59:01 UTC (tier 1)

AUTONOMY screen autog2_024_SOLUSDT_15m_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.1004484724326358 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 09:59:01 UTC (tier 0)

START gen=autog2_024_SOLUSDT_15m_vol_ratio_ohlcv_v1_ts SOLUSDT 15m target=vol_ratio space=ohlcv_v1

## [INFO] 2026-08-03 09:59:19 UTC (tier 0)

TE_FALSIFY BTCUSDT 1h: NONLINEAR_CROSSASSET_PARTIAL pairs=31 all3=0 any=16 closed=15

## [INFO] 2026-08-03 10:00:28 UTC (tier 0)

PREDICTABILITY real=+0.21685 p=0.0476 surr_q95=+0.04042 surr_max=+0.06827 draws=20 passed=True

## [INFO] 2026-08-03 10:00:36 UTC (tier 1)

trial `127209ba-caff-4298-946f-a7242faf24c3` model=lgbm_regressor tier=1 target=vol_ratio skill=1.100 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:00:36 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_024_SOLUSDT_15m_vol_ratio_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:00:36 UTC (tier 1)

AUTONOMY tradesim autog2_024_SOLUSDT_15m_vol_ratio_ohlcv_v1 tier=1 proxy_skill=1.1004484724326358

## [INFO] 2026-08-03 10:00:36 UTC (tier 0)

START gen=autog2_025_SOLUSDT_15m_vol_ratio_indicators_v1 SOLUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 10:01:44 UTC (tier 0)

PREDICTABILITY real=+0.13577 p=0.0476 surr_q95=+0.00009 surr_max=+0.00016 draws=20 passed=True

## [INFO] 2026-08-03 10:01:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 10:01:46 UTC (tier 0)

trial `117e960c-475f-4d7f-96dd-5df343e13eca` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:01:47 UTC (tier 1)

trial `fd198516-f142-4529-a984-6bc4677f61da` model=ridge tier=1 target=vol_ratio skill=1.076 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:01:52 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.15270 skill_surrogate=-0.01579

## [INFO] 2026-08-03 10:01:52 UTC (tier 0)

trial `ec2efb96-eb01-4136-bcd4-c97d18280cd0` model=lgbm_regressor tier=0 target=vol_ratio skill=0.966 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:01:54 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04519 skill_surrogate=+0.04519

## [INFO] 2026-08-03 10:01:54 UTC (tier 0)

trial `2d7a12b7-4c58-490b-bcbb-e20074f9ce34` model=lgbm_classifier tier=0 target=vol_ratio skill=1.045 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:01:54 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_025_SOLUSDT_15m_vol_ratio_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:01:54 UTC (tier 1)

AUTONOMY screen autog2_025_SOLUSDT_15m_vol_ratio_indicators_v1 tier=1 proxy_skill=1.075884630587128 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:01:54 UTC (tier 0)

START gen=autog2_025_SOLUSDT_15m_vol_ratio_indicators_v1_ts SOLUSDT 15m target=vol_ratio space=indicators_v1

## [INFO] 2026-08-03 10:02:38 UTC (tier 0)

TE_FALSIFY BTCUSDT 1h: NONLINEAR_CROSSASSET_PARTIAL pairs=31 all3=0 any=9 closed=22

## [INFO] 2026-08-03 10:03:03 UTC (tier 0)

PREDICTABILITY real=+0.13577 p=0.0476 surr_q95=+0.00009 surr_max=+0.00016 draws=20 passed=True

## [INFO] 2026-08-03 10:03:08 UTC (tier 1)

trial `4cb127e1-1fc0-4592-8dd7-fb2e31d0b139` model=ridge tier=1 target=vol_ratio skill=1.076 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:03:08 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_025_SOLUSDT_15m_vol_ratio_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:03:08 UTC (tier 1)

AUTONOMY tradesim autog2_025_SOLUSDT_15m_vol_ratio_indicators_v1 tier=1 proxy_skill=1.075884630587128

## [INFO] 2026-08-03 10:03:08 UTC (tier 0)

START gen=autog2_026_SOLUSDT_15m_vol_ratio_pivot_v1 SOLUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 10:03:43 UTC (tier 0)

PREDICTABILITY real=+0.15715 p=0.0476 surr_q95=+0.00074 surr_max=+0.00114 draws=20 passed=True

## [INFO] 2026-08-03 10:03:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:03:46 UTC (tier 0)

trial `bbfc5508-2882-4bad-9762-fc390a102d9a` model=hist_mean tier=0 target=vol_ratio skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:03:46 UTC (tier 1)

trial `cabc1882-5e5a-49c0-af8c-3a723791b6e1` model=ridge tier=1 target=vol_ratio skill=1.100 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:03:49 UTC (tier 1)

trial `17da8844-ead1-4af2-8bd7-00ca3622dad9` model=lgbm_regressor tier=1 target=vol_ratio skill=1.123 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:03:50 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=+0.04509 skill_surrogate=+0.04509

## [INFO] 2026-08-03 10:03:50 UTC (tier 0)

trial `b856e660-1b9c-4687-9366-a42f1a3ce841` model=lgbm_classifier tier=0 target=vol_ratio skill=1.045 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:03:50 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_026_SOLUSDT_15m_vol_ratio_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:03:50 UTC (tier 1)

AUTONOMY screen autog2_026_SOLUSDT_15m_vol_ratio_pivot_v1 tier=1 proxy_skill=1.1231874658307415 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:03:50 UTC (tier 0)

START gen=autog2_026_SOLUSDT_15m_vol_ratio_pivot_v1_ts SOLUSDT 15m target=vol_ratio space=pivot_v1

## [INFO] 2026-08-03 10:04:13 UTC (tier 0)

PREDICTABILITY real=+0.15715 p=0.0476 surr_q95=+0.00074 surr_max=+0.00114 draws=20 passed=True

## [INFO] 2026-08-03 10:04:18 UTC (tier 1)

trial `a53d145b-2be0-4579-86d7-021e9e1e0cb2` model=lgbm_regressor tier=1 target=vol_ratio skill=1.123 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:04:18 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_026_SOLUSDT_15m_vol_ratio_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:04:18 UTC (tier 1)

AUTONOMY tradesim autog2_026_SOLUSDT_15m_vol_ratio_pivot_v1 tier=1 proxy_skill=1.1231874658307415

## [INFO] 2026-08-03 10:04:18 UTC (tier 0)

START gen=autog2_027_BTCUSDT_1h_volatility_ohlcv_v1 BTCUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:04:34 UTC (tier 0)

PREDICTABILITY real=+0.43163 p=0.0476 surr_q95=+0.09610 surr_max=+0.16644 draws=20 passed=True

## [INFO] 2026-08-03 10:04:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:04:36 UTC (tier 0)

trial `a245b5a7-8c87-404a-92b7-9177488b3d60` model=hist_mean tier=0 target=volatility skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:04:36 UTC (tier 1)

trial `19de0713-9ba8-42f1-a30a-d28c59b177fd` model=ridge tier=1 target=volatility skill=1.366 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:04:38 UTC (tier 1)

trial `9b41eb42-6139-4304-9e8b-cc12c6e6513d` model=lgbm_regressor tier=1 target=volatility skill=1.485 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:04:40 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-40.83757 skill_surrogate=-40.83757

## [INFO] 2026-08-03 10:04:40 UTC (tier 0)

trial `6d720c69-8649-4240-950d-898467495d5e` model=lgbm_classifier tier=0 target=volatility skill=0.025 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:04:40 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_027_BTCUSDT_1h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:04:40 UTC (tier 1)

AUTONOMY screen autog2_027_BTCUSDT_1h_volatility_ohlcv_v1 tier=1 proxy_skill=1.4853096764285245 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:04:40 UTC (tier 0)

START gen=autog2_027_BTCUSDT_1h_volatility_ohlcv_v1_ts BTCUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:04:57 UTC (tier 0)

PREDICTABILITY real=+0.43163 p=0.0476 surr_q95=+0.09610 surr_max=+0.16644 draws=20 passed=True

## [INFO] 2026-08-03 10:05:01 UTC (tier 1)

trial `324e79f2-7d0e-49b9-a378-20276674a4eb` model=lgbm_regressor tier=1 target=volatility skill=1.485 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:05:01 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_027_BTCUSDT_1h_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:05:01 UTC (tier 1)

AUTONOMY tradesim autog2_027_BTCUSDT_1h_volatility_ohlcv_v1 tier=1 proxy_skill=1.4853096764285245

## [INFO] 2026-08-03 10:05:01 UTC (tier 0)

START gen=autog2_028_BTCUSDT_1h_volatility_indicators_v1 BTCUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:05:14 UTC (tier 0)

PREDICTABILITY real=+0.37457 p=0.0476 surr_q95=+0.09653 surr_max=+0.17873 draws=20 passed=True

## [INFO] 2026-08-03 10:05:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:05:16 UTC (tier 0)

trial `14371a0b-983b-4e33-a348-2dd034f71df6` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:05:16 UTC (tier 1)

trial `5e949075-32e8-4379-9df8-3cb26a876739` model=ridge tier=1 target=volatility skill=1.466 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:05:18 UTC (tier 1)

trial `af222b98-43b7-437b-be9a-ace52ecdc212` model=lgbm_regressor tier=1 target=volatility skill=1.279 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:05:19 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-40.81540 skill_surrogate=-40.81540

## [INFO] 2026-08-03 10:05:19 UTC (tier 0)

trial `b07cdc14-e678-4ade-bf54-2261335da5e4` model=lgbm_classifier tier=0 target=volatility skill=0.025 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:05:19 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_028_BTCUSDT_1h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:05:19 UTC (tier 1)

AUTONOMY screen autog2_028_BTCUSDT_1h_volatility_indicators_v1 tier=1 proxy_skill=1.4659121912133612 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:05:19 UTC (tier 0)

START gen=autog2_028_BTCUSDT_1h_volatility_indicators_v1_ts BTCUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:05:31 UTC (tier 0)

PREDICTABILITY real=+0.37457 p=0.0476 surr_q95=+0.09653 surr_max=+0.17873 draws=20 passed=True

## [INFO] 2026-08-03 10:05:35 UTC (tier 1)

trial `b5e333ea-985f-446a-b668-002ab62dae2a` model=ridge tier=1 target=volatility skill=1.466 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:05:35 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_028_BTCUSDT_1h_volatility_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:05:35 UTC (tier 1)

AUTONOMY tradesim autog2_028_BTCUSDT_1h_volatility_indicators_v1 tier=1 proxy_skill=1.4659121912133612

## [INFO] 2026-08-03 10:05:35 UTC (tier 0)

START gen=autog2_029_BTCUSDT_1h_volatility_pivot_v1 BTCUSDT 1h target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:05:42 UTC (tier 0)

PREDICTABILITY real=+0.05935 p=0.0476 surr_q95=+0.00264 surr_max=+0.00478 draws=20 passed=True

## [INFO] 2026-08-03 10:05:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:05:44 UTC (tier 0)

trial `ec1331bc-4d1f-4ef4-8159-8ce1929c49e4` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:05:44 UTC (tier 1)

trial `03881178-343f-4d86-a462-b204829cf97b` model=ridge tier=1 target=volatility skill=1.008 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:05:46 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01818 skill_surrogate=-0.00445

## [INFO] 2026-08-03 10:05:46 UTC (tier 0)

trial `b1f70566-e95d-4456-bfdf-ef23b64ad4f2` model=lgbm_regressor tier=0 target=volatility skill=1.018 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:05:46 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-40.85346 skill_surrogate=-40.85346

## [INFO] 2026-08-03 10:05:46 UTC (tier 0)

trial `8ce2acbe-85e6-4827-9643-72c486308335` model=lgbm_classifier tier=0 target=volatility skill=0.025 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:05:46 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_029_BTCUSDT_1h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:05:46 UTC (tier 1)

AUTONOMY screen autog2_029_BTCUSDT_1h_volatility_pivot_v1 tier=1 proxy_skill=1.0076614253911855 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:05:46 UTC (tier 0)

START gen=autog2_029_BTCUSDT_1h_volatility_pivot_v1_ts BTCUSDT 1h target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:05:53 UTC (tier 0)

PREDICTABILITY real=+0.05935 p=0.0476 surr_q95=+0.00264 surr_max=+0.00478 draws=20 passed=True

## [INFO] 2026-08-03 10:05:55 UTC (tier 1)

trial `c0bc3e94-9f24-4ba0-8146-a47a1a4c0a99` model=ridge tier=1 target=volatility skill=1.008 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:05:55 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_029_BTCUSDT_1h_volatility_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:05:55 UTC (tier 1)

AUTONOMY tradesim autog2_029_BTCUSDT_1h_volatility_pivot_v1 tier=1 proxy_skill=1.0076614253911855

## [INFO] 2026-08-03 10:05:55 UTC (tier 0)

START gen=autog2_030_ETHUSDT_1h_volatility_ohlcv_v1 ETHUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:06:05 UTC (tier 0)

PREDICTABILITY real=+0.52761 p=0.0476 surr_q95=+0.08854 surr_max=+0.40906 draws=20 passed=True

## [INFO] 2026-08-03 10:06:07 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 10:06:07 UTC (tier 0)

trial `09bc502e-e488-4602-aa04-59ada751536c` model=hist_mean tier=0 target=volatility skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:06:07 UTC (tier 1)

trial `697404b2-3268-4b17-865c-c6c5848e7f5e` model=ridge tier=1 target=volatility skill=1.408 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:06:09 UTC (tier 1)

trial `e03b5207-458c-4d2d-b9ee-aaa9eb79244d` model=lgbm_regressor tier=1 target=volatility skill=1.505 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:06:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.42057 skill_surrogate=-35.42057

## [INFO] 2026-08-03 10:06:10 UTC (tier 0)

trial `99d2ab61-67ed-4fea-a021-188c631497c0` model=lgbm_classifier tier=0 target=volatility skill=0.033 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:06:10 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_030_ETHUSDT_1h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:06:10 UTC (tier 1)

AUTONOMY screen autog2_030_ETHUSDT_1h_volatility_ohlcv_v1 tier=1 proxy_skill=1.5051713954550512 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:06:10 UTC (tier 0)

START gen=autog2_030_ETHUSDT_1h_volatility_ohlcv_v1_ts ETHUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:06:22 UTC (tier 0)

PREDICTABILITY real=+0.52761 p=0.0476 surr_q95=+0.08854 surr_max=+0.40906 draws=20 passed=True

## [INFO] 2026-08-03 10:06:26 UTC (tier 1)

trial `326369e1-2204-415e-970e-c3e9db9637d9` model=lgbm_regressor tier=1 target=volatility skill=1.505 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:06:26 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_030_ETHUSDT_1h_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:06:26 UTC (tier 1)

AUTONOMY tradesim autog2_030_ETHUSDT_1h_volatility_ohlcv_v1 tier=1 proxy_skill=1.5051713954550512

## [INFO] 2026-08-03 10:06:26 UTC (tier 0)

START gen=autog2_031_ETHUSDT_1h_volatility_indicators_v1 ETHUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:06:38 UTC (tier 0)

PREDICTABILITY real=+0.44968 p=0.0476 surr_q95=+0.09020 surr_max=+0.35623 draws=20 passed=True

## [INFO] 2026-08-03 10:06:40 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:06:40 UTC (tier 0)

trial `bbc5df9d-0818-4e13-96b1-e456ac52e155` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:06:40 UTC (tier 1)

trial `a13401bf-f157-456e-bc46-c4d63f53deb2` model=ridge tier=1 target=volatility skill=1.490 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:06:42 UTC (tier 1)

trial `e3767827-ff5b-4eb5-8a1f-f186c24a325a` model=lgbm_regressor tier=1 target=volatility skill=1.308 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:06:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.41141 skill_surrogate=-35.41141

## [INFO] 2026-08-03 10:06:43 UTC (tier 0)

trial `4b464e3f-8d07-4e27-85ac-34692dd54169` model=lgbm_classifier tier=0 target=volatility skill=0.033 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:06:43 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_031_ETHUSDT_1h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:06:43 UTC (tier 1)

AUTONOMY screen autog2_031_ETHUSDT_1h_volatility_indicators_v1 tier=1 proxy_skill=1.4899209735588588 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:06:43 UTC (tier 0)

START gen=autog2_031_ETHUSDT_1h_volatility_indicators_v1_ts ETHUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:06:56 UTC (tier 0)

PREDICTABILITY real=+0.44968 p=0.0476 surr_q95=+0.09020 surr_max=+0.35623 draws=20 passed=True

## [INFO] 2026-08-03 10:06:58 UTC (tier 1)

trial `f081c286-e372-469f-9970-b98891e753c2` model=ridge tier=1 target=volatility skill=1.490 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:06:58 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_031_ETHUSDT_1h_volatility_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:06:58 UTC (tier 1)

AUTONOMY tradesim autog2_031_ETHUSDT_1h_volatility_indicators_v1 tier=1 proxy_skill=1.4899209735588588

## [INFO] 2026-08-03 10:06:58 UTC (tier 0)

START gen=autog2_032_ETHUSDT_1h_volatility_pivot_v1 ETHUSDT 1h target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:07:06 UTC (tier 0)

PREDICTABILITY real=-0.00835 p=0.8095 surr_q95=+0.00180 surr_max=+0.00241 draws=20 passed=False

## [INFO] 2026-08-03 10:07:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:07:08 UTC (tier 0)

trial `0d372c4b-cf3f-49e3-869c-e9aec3fb0b21` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:07:08 UTC (tier 0)

trial `d99b6e34-67ea-4520-9a99-aa90119ab93d` model=ridge tier=0 target=volatility skill=0.992 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:07:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01743 skill_surrogate=-0.00568

## [INFO] 2026-08-03 10:07:10 UTC (tier 0)

trial `817e4edd-0897-4848-a1cd-5bda48534d7f` model=lgbm_regressor tier=0 target=volatility skill=0.988 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:07:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.42126 skill_surrogate=-35.42126

## [INFO] 2026-08-03 10:07:10 UTC (tier 0)

trial `84288ed4-58b3-4bba-ac68-784a2a7c8f92` model=lgbm_classifier tier=0 target=volatility skill=0.033 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:07:10 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_032_ETHUSDT_1h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:07:10 UTC (tier 0)

AUTONOMY screen autog2_032_ETHUSDT_1h_volatility_pivot_v1 tier=0 proxy_skill=1.0 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:07:10 UTC (tier 0)

START gen=autog2_033_SOLUSDT_1h_volatility_ohlcv_v1 SOLUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:07:22 UTC (tier 0)

PREDICTABILITY real=+0.45640 p=0.0476 surr_q95=+0.06798 surr_max=+0.09995 draws=20 passed=True

## [INFO] 2026-08-03 10:07:23 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:07:23 UTC (tier 0)

trial `225c39a8-31d4-4254-830d-7783731d3af2` model=hist_mean tier=0 target=volatility skill=1.000 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:07:23 UTC (tier 1)

trial `95b39cc0-9638-4d73-a8ad-5eeec9b2e1f2` model=ridge tier=1 target=volatility skill=1.580 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:07:25 UTC (tier 1)

trial `423861fe-552d-4422-95bc-63043a165212` model=lgbm_regressor tier=1 target=volatility skill=1.596 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:07:26 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-22.15869 skill_surrogate=-22.15869

## [INFO] 2026-08-03 10:07:26 UTC (tier 0)

trial `2bab6b7a-8576-46b1-8ba9-83f46b1d7fa5` model=lgbm_classifier tier=0 target=volatility skill=0.054 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:07:26 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_033_SOLUSDT_1h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:07:26 UTC (tier 1)

AUTONOMY screen autog2_033_SOLUSDT_1h_volatility_ohlcv_v1 tier=1 proxy_skill=1.595746376466047 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:07:26 UTC (tier 0)

START gen=autog2_033_SOLUSDT_1h_volatility_ohlcv_v1_ts SOLUSDT 1h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:07:35 UTC (tier 0)

PREDICTABILITY real=+0.45640 p=0.0476 surr_q95=+0.06798 surr_max=+0.09995 draws=20 passed=True

## [INFO] 2026-08-03 10:07:38 UTC (tier 1)

trial `a0c7b7b1-b955-496b-b8b6-dd3b5c59863c` model=lgbm_regressor tier=1 target=volatility skill=1.596 n=32855 gates=UNKNOWN

## [INFO] 2026-08-03 10:07:38 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_033_SOLUSDT_1h_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:07:38 UTC (tier 1)

AUTONOMY tradesim autog2_033_SOLUSDT_1h_volatility_ohlcv_v1 tier=1 proxy_skill=1.595746376466047

## [INFO] 2026-08-03 10:07:39 UTC (tier 0)

START gen=autog2_034_SOLUSDT_1h_volatility_indicators_v1 SOLUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:07:49 UTC (tier 0)

PREDICTABILITY real=+0.41432 p=0.0476 surr_q95=+0.09457 surr_max=+0.11613 draws=20 passed=True

## [INFO] 2026-08-03 10:07:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:07:50 UTC (tier 0)

trial `0ed5741a-956c-428c-85ba-2b6f4e356b77` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:07:50 UTC (tier 1)

trial `5f70c1c2-5ad4-4a1a-904d-d28c76fa07f8` model=ridge tier=1 target=volatility skill=1.569 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:07:52 UTC (tier 1)

trial `608ebe5c-fd71-426b-bbe2-1ed39c64453a` model=lgbm_regressor tier=1 target=volatility skill=1.246 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:07:53 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-22.20659 skill_surrogate=-22.20659

## [INFO] 2026-08-03 10:07:53 UTC (tier 0)

trial `61d5c6b6-9e25-4471-9115-db7fcead9e3a` model=lgbm_classifier tier=0 target=volatility skill=0.054 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:07:53 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_034_SOLUSDT_1h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:07:53 UTC (tier 1)

AUTONOMY screen autog2_034_SOLUSDT_1h_volatility_indicators_v1 tier=1 proxy_skill=1.5693395431819315 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:07:53 UTC (tier 0)

START gen=autog2_034_SOLUSDT_1h_volatility_indicators_v1_ts SOLUSDT 1h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:08:03 UTC (tier 0)

PREDICTABILITY real=+0.41432 p=0.0476 surr_q95=+0.09457 surr_max=+0.11613 draws=20 passed=True

## [INFO] 2026-08-03 10:08:04 UTC (tier 1)

trial `f25da1b0-9b57-4d8c-a713-2a85189f1433` model=ridge tier=1 target=volatility skill=1.569 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:04 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_034_SOLUSDT_1h_volatility_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:04 UTC (tier 1)

AUTONOMY tradesim autog2_034_SOLUSDT_1h_volatility_indicators_v1 tier=1 proxy_skill=1.5693395431819315

## [INFO] 2026-08-03 10:08:04 UTC (tier 0)

START gen=autog2_035_SOLUSDT_1h_volatility_pivot_v1 SOLUSDT 1h target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:08:10 UTC (tier 0)

PREDICTABILITY real=-0.00233 p=0.6667 surr_q95=+0.00319 surr_max=+0.00506 draws=20 passed=False

## [INFO] 2026-08-03 10:08:11 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:08:11 UTC (tier 0)

trial `f804f3ac-d7d3-4cff-b89f-9a64107fbe2f` model=hist_mean tier=0 target=volatility skill=1.000 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:08:11 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00323 skill_surrogate=-0.00203

## [INFO] 2026-08-03 10:08:11 UTC (tier 0)

trial `47197352-d1e2-4e94-8f32-baf6ad08a375` model=ridge tier=0 target=volatility skill=1.005 n=32856 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02000 skill_surrogate=-0.00177

## [INFO] 2026-08-03 10:08:12 UTC (tier 0)

trial `f9e6df0e-da0d-480c-9450-1315371fd313` model=lgbm_regressor tier=0 target=volatility skill=0.997 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:08:13 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-22.11338 skill_surrogate=-22.11338

## [INFO] 2026-08-03 10:08:13 UTC (tier 0)

trial `f758dafa-64c6-463b-9a5e-b0b12b94ed71` model=lgbm_classifier tier=0 target=volatility skill=0.054 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:08:13 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_035_SOLUSDT_1h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:13 UTC (tier 0)

AUTONOMY screen autog2_035_SOLUSDT_1h_volatility_pivot_v1 tier=0 proxy_skill=1.004751764657602 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:08:13 UTC (tier 0)

START gen=autog2_036_BTCUSDT_4h_volatility_ohlcv_v1 BTCUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:08:17 UTC (tier 0)

PREDICTABILITY real=+0.36327 p=0.0476 surr_q95=+0.09482 surr_max=+0.13644 draws=20 passed=True

## [INFO] 2026-08-03 10:08:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:08:18 UTC (tier 0)

trial `3c51556e-9d49-4678-b268-2c6b4917f5d4` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:18 UTC (tier 1)

trial `d1075a01-9c72-4ae2-8a92-a9bf27173902` model=ridge tier=1 target=volatility skill=1.265 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:19 UTC (tier 1)

trial `6498bb20-21dc-4019-885e-7221dd3a1490` model=lgbm_regressor tier=1 target=volatility skill=1.285 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:19 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-20.13682 skill_surrogate=-20.13682

## [INFO] 2026-08-03 10:08:19 UTC (tier 0)

trial `6f1f0845-509a-4b45-a442-4a15aba27895` model=lgbm_classifier tier=0 target=volatility skill=0.049 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:19 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_036_BTCUSDT_4h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:19 UTC (tier 1)

AUTONOMY screen autog2_036_BTCUSDT_4h_volatility_ohlcv_v1 tier=1 proxy_skill=1.2845413152826792 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:08:19 UTC (tier 0)

START gen=autog2_036_BTCUSDT_4h_volatility_ohlcv_v1_ts BTCUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:08:24 UTC (tier 0)

PREDICTABILITY real=+0.36327 p=0.0476 surr_q95=+0.09482 surr_max=+0.13644 draws=20 passed=True

## [INFO] 2026-08-03 10:08:26 UTC (tier 1)

trial `aec5b5fa-3f03-4650-a7ae-7f30237a04ad` model=lgbm_regressor tier=1 target=volatility skill=1.285 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:26 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_036_BTCUSDT_4h_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:26 UTC (tier 1)

AUTONOMY tradesim autog2_036_BTCUSDT_4h_volatility_ohlcv_v1 tier=1 proxy_skill=1.2845413152826792

## [INFO] 2026-08-03 10:08:26 UTC (tier 0)

START gen=autog2_037_BTCUSDT_4h_volatility_indicators_v1 BTCUSDT 4h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:08:30 UTC (tier 0)

PREDICTABILITY real=+0.30075 p=0.0476 surr_q95=+0.04620 surr_max=+0.06853 draws=20 passed=True

## [INFO] 2026-08-03 10:08:31 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:08:31 UTC (tier 0)

trial `c422d52a-e831-46ed-9f42-08e28670aaad` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:31 UTC (tier 1)

trial `093c84ff-f725-4749-a29c-a0102e0c4bb6` model=ridge tier=1 target=volatility skill=1.422 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.12206 skill_surrogate=-0.06321

## [INFO] 2026-08-03 10:08:32 UTC (tier 0)

trial `0598a3f4-c8d8-4b8d-b8a5-81fc77ce1bea` model=lgbm_regressor tier=0 target=volatility skill=0.785 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:33 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-20.18784 skill_surrogate=-20.18784

## [INFO] 2026-08-03 10:08:33 UTC (tier 0)

trial `08acdee1-b8b4-4e1b-9bf4-5a0018b0dd9f` model=lgbm_classifier tier=0 target=volatility skill=0.049 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:33 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_037_BTCUSDT_4h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:33 UTC (tier 1)

AUTONOMY screen autog2_037_BTCUSDT_4h_volatility_indicators_v1 tier=1 proxy_skill=1.422183366648676 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:08:33 UTC (tier 0)

START gen=autog2_037_BTCUSDT_4h_volatility_indicators_v1_ts BTCUSDT 4h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:08:37 UTC (tier 0)

PREDICTABILITY real=+0.30075 p=0.0476 surr_q95=+0.04620 surr_max=+0.06853 draws=20 passed=True

## [INFO] 2026-08-03 10:08:38 UTC (tier 1)

trial `c67b6f08-54c7-4fb1-b1c0-afad8cfbdc62` model=ridge tier=1 target=volatility skill=1.422 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:38 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_037_BTCUSDT_4h_volatility_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:38 UTC (tier 1)

AUTONOMY tradesim autog2_037_BTCUSDT_4h_volatility_indicators_v1 tier=1 proxy_skill=1.422183366648676

## [INFO] 2026-08-03 10:08:38 UTC (tier 0)

START gen=autog2_038_BTCUSDT_4h_volatility_pivot_v1 BTCUSDT 4h target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:08:41 UTC (tier 0)

PREDICTABILITY real=-0.05135 p=0.9048 surr_q95=+0.00631 surr_max=+0.01410 draws=20 passed=False

## [INFO] 2026-08-03 10:08:41 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:08:41 UTC (tier 0)

trial `b17d883c-3069-4371-9a58-2996377e8c65` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:41 UTC (tier 0)

trial `efeba4cb-d80f-4ea9-b431-f43c3f78ead0` model=ridge tier=0 target=volatility skill=0.994 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:42 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02062 skill_surrogate=-0.01398

## [INFO] 2026-08-03 10:08:42 UTC (tier 0)

trial `17b56682-f891-468c-aceb-3ad6cedf9259` model=lgbm_regressor tier=0 target=volatility skill=0.980 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-20.20560 skill_surrogate=-20.20560

## [INFO] 2026-08-03 10:08:43 UTC (tier 0)

trial `3078bbcd-8dde-4812-bbcc-6c469eeb99be` model=lgbm_classifier tier=0 target=volatility skill=0.049 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:43 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_038_BTCUSDT_4h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:43 UTC (tier 0)

AUTONOMY screen autog2_038_BTCUSDT_4h_volatility_pivot_v1 tier=0 proxy_skill=1.0 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:08:43 UTC (tier 0)

START gen=autog2_039_ETHUSDT_4h_volatility_ohlcv_v1 ETHUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:08:48 UTC (tier 0)

PREDICTABILITY real=+0.48480 p=0.0476 surr_q95=+0.08989 surr_max=+0.09691 draws=20 passed=True

## [INFO] 2026-08-03 10:08:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:08:49 UTC (tier 0)

trial `964ea593-87ee-46ef-b8bb-833199539297` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:49 UTC (tier 1)

trial `3ccbfec0-785f-483b-b44a-49adeec468a3` model=ridge tier=1 target=volatility skill=1.298 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:50 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.08621 skill_surrogate=-0.01717

## [INFO] 2026-08-03 10:08:50 UTC (tier 0)

trial `75885831-ace8-4898-a2c9-82b75544eb33` model=lgbm_regressor tier=0 target=volatility skill=1.276 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:50 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-17.23510 skill_surrogate=-17.23510

## [INFO] 2026-08-03 10:08:50 UTC (tier 0)

trial `2518a5d1-d1bf-471a-ad10-4035d6e5545a` model=lgbm_classifier tier=0 target=volatility skill=0.068 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:08:50 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_039_ETHUSDT_4h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:50 UTC (tier 1)

AUTONOMY screen autog2_039_ETHUSDT_4h_volatility_ohlcv_v1 tier=1 proxy_skill=1.2978023057047012 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:08:50 UTC (tier 0)

START gen=autog2_039_ETHUSDT_4h_volatility_ohlcv_v1_ts ETHUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:08:56 UTC (tier 0)

PREDICTABILITY real=+0.48480 p=0.0476 surr_q95=+0.08989 surr_max=+0.09691 draws=20 passed=True

## [INFO] 2026-08-03 10:08:56 UTC (tier 1)

trial `1b2c3e9f-b65b-40c6-b020-b35ee9da76bb` model=ridge tier=1 target=volatility skill=1.298 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:08:56 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_039_ETHUSDT_4h_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:08:56 UTC (tier 1)

AUTONOMY tradesim autog2_039_ETHUSDT_4h_volatility_ohlcv_v1 tier=1 proxy_skill=1.2978023057047012

## [INFO] 2026-08-03 10:08:57 UTC (tier 0)

START gen=autog2_040_ETHUSDT_4h_volatility_indicators_v1 ETHUSDT 4h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:09:03 UTC (tier 0)

PREDICTABILITY real=+0.39543 p=0.0476 surr_q95=+0.07097 surr_max=+0.39368 draws=20 passed=True

## [INFO] 2026-08-03 10:09:03 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:09:03 UTC (tier 0)

trial `c84d4522-84eb-4189-8764-232cc4617b6a` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:03 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01814 skill_surrogate=-0.00512

## [INFO] 2026-08-03 10:09:03 UTC (tier 0)

trial `62fd23e4-70c7-4f6f-aede-5f65dbe0f919` model=ridge tier=0 target=volatility skill=1.316 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:09:05 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.15671 skill_surrogate=-0.04793

## [INFO] 2026-08-03 10:09:05 UTC (tier 0)

trial `c7c2ea9a-381b-4e63-8286-36490d030507` model=lgbm_regressor tier=0 target=volatility skill=1.084 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:05 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-17.19931 skill_surrogate=-17.19931

## [INFO] 2026-08-03 10:09:05 UTC (tier 0)

trial `606f0bd5-7d52-474e-bc17-6aa565b956c4` model=lgbm_classifier tier=0 target=volatility skill=0.068 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:05 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_040_ETHUSDT_4h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:09:05 UTC (tier 0)

AUTONOMY screen autog2_040_ETHUSDT_4h_volatility_indicators_v1 tier=0 proxy_skill=1.3159898277040334 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:09:05 UTC (tier 0)

START gen=autog2_041_ETHUSDT_4h_volatility_pivot_v1 ETHUSDT 4h target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:09:08 UTC (tier 0)

PREDICTABILITY real=-0.07400 p=1.0000 surr_q95=+0.00659 surr_max=+0.02094 draws=20 passed=False

## [INFO] 2026-08-03 10:09:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:09:09 UTC (tier 0)

trial `bfb3b05c-d86c-40e9-b81c-eeca90bb1e5d` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:09 UTC (tier 0)

trial `bb8272fe-639b-4358-84c7-abf182883989` model=ridge tier=0 target=volatility skill=0.989 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03446 skill_surrogate=-0.01364

## [INFO] 2026-08-03 10:09:10 UTC (tier 0)

trial `8ad48530-f017-4b02-bcf5-607475a9b5dc` model=lgbm_regressor tier=0 target=volatility skill=0.939 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-17.26916 skill_surrogate=-17.26916

## [INFO] 2026-08-03 10:09:10 UTC (tier 0)

trial `64c97471-5bbc-43f0-bca7-82a276bbb007` model=lgbm_classifier tier=0 target=volatility skill=0.067 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:10 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_041_ETHUSDT_4h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:09:10 UTC (tier 0)

AUTONOMY screen autog2_041_ETHUSDT_4h_volatility_pivot_v1 tier=0 proxy_skill=1.0 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:09:10 UTC (tier 0)

START gen=autog2_042_SOLUSDT_4h_volatility_ohlcv_v1 SOLUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:09:15 UTC (tier 0)

PREDICTABILITY real=+0.24259 p=0.0476 surr_q95=+0.04341 surr_max=+0.08758 draws=20 passed=True

## [INFO] 2026-08-03 10:09:15 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:09:15 UTC (tier 0)

trial `cb25c5de-b515-40b4-b4d5-e8717d780699` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:15 UTC (tier 1)

trial `d5a2cbb4-0bdc-4ebf-83ba-ba7008f1ce55` model=ridge tier=1 target=volatility skill=1.400 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:09:17 UTC (tier 1)

trial `5184fcea-8e60-4165-ad99-29e8ffd8dc3c` model=lgbm_regressor tier=1 target=volatility skill=1.360 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:09:17 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-10.23145 skill_surrogate=-10.23145

## [INFO] 2026-08-03 10:09:17 UTC (tier 0)

trial `591dba2c-ea99-4916-a16b-43e893ee0360` model=lgbm_classifier tier=0 target=volatility skill=0.117 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:17 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_042_SOLUSDT_4h_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:09:17 UTC (tier 1)

AUTONOMY screen autog2_042_SOLUSDT_4h_volatility_ohlcv_v1 tier=1 proxy_skill=1.4004070131362052 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:09:17 UTC (tier 0)

START gen=autog2_042_SOLUSDT_4h_volatility_ohlcv_v1_ts SOLUSDT 4h target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:09:22 UTC (tier 0)

PREDICTABILITY real=+0.24259 p=0.0476 surr_q95=+0.04341 surr_max=+0.08758 draws=20 passed=True

## [INFO] 2026-08-03 10:09:22 UTC (tier 1)

trial `1f688545-9ba6-44b6-a55a-f05249c4637c` model=ridge tier=1 target=volatility skill=1.400 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:09:22 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_042_SOLUSDT_4h_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:09:22 UTC (tier 1)

AUTONOMY tradesim autog2_042_SOLUSDT_4h_volatility_ohlcv_v1 tier=1 proxy_skill=1.4004070131362052

## [INFO] 2026-08-03 10:09:22 UTC (tier 0)

START gen=autog2_043_SOLUSDT_4h_volatility_indicators_v1 SOLUSDT 4h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:09:28 UTC (tier 0)

PREDICTABILITY real=+0.24331 p=0.0476 surr_q95=+0.09154 surr_max=+0.17614 draws=20 passed=True

## [INFO] 2026-08-03 10:09:29 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:09:29 UTC (tier 0)

trial `92feeaa1-18dc-4254-aef2-230feca3ecc8` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:29 UTC (tier 1)

trial `285235e8-a3b8-4f81-a748-813a76329b7f` model=ridge tier=1 target=volatility skill=1.313 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:09:30 UTC (tier 1)

trial `067d7a8c-20e0-4edd-a5d3-229d3a07e372` model=lgbm_regressor tier=1 target=volatility skill=1.090 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:30 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-10.21190 skill_surrogate=-10.21190

## [INFO] 2026-08-03 10:09:30 UTC (tier 0)

trial `2f5ed10a-9f0b-4257-add7-ec8ca7e23173` model=lgbm_classifier tier=0 target=volatility skill=0.117 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:30 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_043_SOLUSDT_4h_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:09:30 UTC (tier 1)

AUTONOMY screen autog2_043_SOLUSDT_4h_volatility_indicators_v1 tier=1 proxy_skill=1.3132728154456093 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:09:30 UTC (tier 0)

START gen=autog2_043_SOLUSDT_4h_volatility_indicators_v1_ts SOLUSDT 4h target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:09:35 UTC (tier 0)

PREDICTABILITY real=+0.24331 p=0.0476 surr_q95=+0.09154 surr_max=+0.17614 draws=20 passed=True

## [INFO] 2026-08-03 10:09:35 UTC (tier 1)

trial `6fcd0387-d5dd-4db9-8e47-edf16de1bc26` model=ridge tier=1 target=volatility skill=1.313 n=8214 gates=UNKNOWN

## [INFO] 2026-08-03 10:09:35 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_043_SOLUSDT_4h_volatility_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:09:35 UTC (tier 1)

AUTONOMY tradesim autog2_043_SOLUSDT_4h_volatility_indicators_v1 tier=1 proxy_skill=1.3132728154456093

## [INFO] 2026-08-03 10:09:35 UTC (tier 0)

START gen=autog2_044_SOLUSDT_4h_volatility_pivot_v1 SOLUSDT 4h target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:09:37 UTC (tier 0)

PREDICTABILITY real=-0.07170 p=1.0000 surr_q95=+0.00250 surr_max=+0.01022 draws=20 passed=False

## [INFO] 2026-08-03 10:09:38 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 10:09:38 UTC (tier 0)

trial `3c0e16c9-152b-4e0c-8570-d4413ca5896f` model=hist_mean tier=0 target=volatility skill=1.000 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:38 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.05379 skill_surrogate=+0.00687

## [INFO] 2026-08-03 10:09:38 UTC (tier 0)

trial `a63a34c5-c0c9-48a3-93f9-2d55054d49f9` model=ridge tier=0 target=volatility skill=0.997 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.07073 skill_surrogate=-0.01793

## [INFO] 2026-08-03 10:09:39 UTC (tier 0)

trial `bfe50f97-a6de-4fe4-a02e-1ed5baca775c` model=lgbm_regressor tier=0 target=volatility skill=0.993 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-10.18045 skill_surrogate=-10.18045

## [INFO] 2026-08-03 10:09:39 UTC (tier 0)

trial `765897d6-6ae0-4693-b4e9-4ef0e51bbb64` model=lgbm_classifier tier=0 target=volatility skill=0.117 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:09:39 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_044_SOLUSDT_4h_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:09:39 UTC (tier 0)

AUTONOMY screen autog2_044_SOLUSDT_4h_volatility_pivot_v1 tier=0 proxy_skill=1.0 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:09:39 UTC (tier 0)

START gen=autog2_045_BTCUSDT_15m_volatility_ohlcv_v1 BTCUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:10:23 UTC (tier 0)

PREDICTABILITY real=+0.49764 p=0.0476 surr_q95=+0.05002 surr_max=+0.11285 draws=20 passed=True

## [INFO] 2026-08-03 10:10:41 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:10:41 UTC (tier 0)

trial `51c3da07-03ef-457b-8237-979832237c35` model=hist_mean tier=0 target=volatility skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:10:42 UTC (tier 1)

trial `e3ed229a-9236-43ee-b4b4-3448ae1394b4` model=ridge tier=1 target=volatility skill=1.510 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:10:48 UTC (tier 1)

trial `84238a62-749c-47fd-a5bf-566a528d25a7` model=lgbm_regressor tier=1 target=volatility skill=1.658 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:10:51 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-80.87244 skill_surrogate=-80.87244

## [INFO] 2026-08-03 10:10:51 UTC (tier 0)

trial `3e02013a-882e-4c16-b0a7-17db4821e7ee` model=lgbm_classifier tier=0 target=volatility skill=0.013 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:10:51 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_045_BTCUSDT_15m_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:10:51 UTC (tier 1)

AUTONOMY screen autog2_045_BTCUSDT_15m_volatility_ohlcv_v1 tier=1 proxy_skill=1.65788100618668 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:10:51 UTC (tier 0)

START gen=autog2_045_BTCUSDT_15m_volatility_ohlcv_v1_ts BTCUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:11:47 UTC (tier 0)

PREDICTABILITY real=+0.49764 p=0.0476 surr_q95=+0.05002 surr_max=+0.11285 draws=20 passed=True

## [INFO] 2026-08-03 10:12:01 UTC (tier 1)

trial `1c0cd7cc-1d89-4315-a1b4-81c82e67fcd6` model=lgbm_regressor tier=1 target=volatility skill=1.658 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:12:01 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_045_BTCUSDT_15m_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:12:01 UTC (tier 1)

AUTONOMY tradesim autog2_045_BTCUSDT_15m_volatility_ohlcv_v1 tier=1 proxy_skill=1.65788100618668

## [INFO] 2026-08-03 10:12:01 UTC (tier 0)

START gen=autog2_046_BTCUSDT_15m_volatility_indicators_v1 BTCUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:12:42 UTC (tier 0)

PREDICTABILITY real=+0.40995 p=0.0476 surr_q95=+0.00251 surr_max=+0.04611 draws=20 passed=True

## [INFO] 2026-08-03 10:12:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:12:50 UTC (tier 0)

trial `fc37ec18-61cf-4dd0-9b63-5a31db68366d` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:12:51 UTC (tier 1)

trial `c0bf1d99-6a2a-49a8-932f-ebe9d7c47555` model=ridge tier=1 target=volatility skill=1.501 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:12:56 UTC (tier 1)

trial `2bad7611-e601-4f3b-aeb0-d5c390a1e893` model=lgbm_regressor tier=1 target=volatility skill=1.382 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:12:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-80.87717 skill_surrogate=-80.87717

## [INFO] 2026-08-03 10:12:59 UTC (tier 0)

trial `6e6ac48a-7edd-49a5-afd1-35d53cc39a75` model=lgbm_classifier tier=0 target=volatility skill=0.013 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:12:59 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_046_BTCUSDT_15m_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:12:59 UTC (tier 1)

AUTONOMY screen autog2_046_BTCUSDT_15m_volatility_indicators_v1 tier=1 proxy_skill=1.5006966284139462 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:12:59 UTC (tier 0)

START gen=autog2_046_BTCUSDT_15m_volatility_indicators_v1_ts BTCUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:13:40 UTC (tier 0)

PREDICTABILITY real=+0.40995 p=0.0476 surr_q95=+0.00251 surr_max=+0.04611 draws=20 passed=True

## [INFO] 2026-08-03 10:13:48 UTC (tier 1)

trial `db5c8b75-86e6-4629-83fd-ae7beca20842` model=ridge tier=1 target=volatility skill=1.501 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:13:48 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_046_BTCUSDT_15m_volatility_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:13:48 UTC (tier 1)

AUTONOMY tradesim autog2_046_BTCUSDT_15m_volatility_indicators_v1 tier=1 proxy_skill=1.5006966284139462

## [INFO] 2026-08-03 10:13:48 UTC (tier 0)

START gen=autog2_047_BTCUSDT_15m_volatility_pivot_v1 BTCUSDT 15m target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:14:09 UTC (tier 0)

PREDICTABILITY real=+0.01019 p=0.0476 surr_q95=+0.00539 surr_max=+0.00840 draws=20 passed=True

## [INFO] 2026-08-03 10:14:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:14:16 UTC (tier 0)

trial `9488b851-5105-4752-a038-e3ff3e114edd` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:14:16 UTC (tier 1)

trial `edb8a46d-a5db-4572-80ff-6c4daf717482` model=ridge tier=1 target=volatility skill=1.001 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:14:20 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02497 skill_surrogate=-0.00079

## [INFO] 2026-08-03 10:14:20 UTC (tier 0)

trial `629ea160-88aa-4f26-b00b-d275f0f18ceb` model=lgbm_regressor tier=0 target=volatility skill=1.005 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:14:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-80.87991 skill_surrogate=-80.87991

## [INFO] 2026-08-03 10:14:21 UTC (tier 0)

trial `1259e2b0-057c-45c4-a770-35d36f35ced5` model=lgbm_classifier tier=0 target=volatility skill=0.013 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:14:21 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_047_BTCUSDT_15m_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:14:21 UTC (tier 1)

AUTONOMY screen autog2_047_BTCUSDT_15m_volatility_pivot_v1 tier=1 proxy_skill=1.0013425710724406 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:14:21 UTC (tier 0)

START gen=autog2_047_BTCUSDT_15m_volatility_pivot_v1_ts BTCUSDT 15m target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:14:42 UTC (tier 0)

PREDICTABILITY real=+0.01019 p=0.0476 surr_q95=+0.00539 surr_max=+0.00840 draws=20 passed=True

## [INFO] 2026-08-03 10:14:50 UTC (tier 1)

trial `0d6b5792-21c5-4bcf-9515-97a11ee46316` model=ridge tier=1 target=volatility skill=1.001 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:14:50 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_047_BTCUSDT_15m_volatility_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:14:50 UTC (tier 1)

AUTONOMY tradesim autog2_047_BTCUSDT_15m_volatility_pivot_v1 tier=1 proxy_skill=1.0013425710724406

## [INFO] 2026-08-03 10:14:50 UTC (tier 0)

START gen=autog2_048_ETHUSDT_15m_volatility_ohlcv_v1 ETHUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:15:38 UTC (tier 0)

PREDICTABILITY real=+0.52332 p=0.0476 surr_q95=+0.05062 surr_max=+0.09738 draws=20 passed=True

## [INFO] 2026-08-03 10:15:48 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:15:48 UTC (tier 0)

trial `fed06fca-fd50-46a5-8d62-0f1a5e17026c` model=hist_mean tier=0 target=volatility skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:15:49 UTC (tier 1)

trial `bc464926-228f-4f0a-8190-86dc4c289d7f` model=ridge tier=1 target=volatility skill=1.549 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:15:55 UTC (tier 1)

trial `f8088fce-f8b5-4d14-abf9-10050287515b` model=lgbm_regressor tier=1 target=volatility skill=1.631 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:15:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-71.77345 skill_surrogate=-71.77345

## [INFO] 2026-08-03 10:15:57 UTC (tier 0)

trial `efc630d0-5037-4c0b-b613-abbef5e6c1af` model=lgbm_classifier tier=0 target=volatility skill=0.017 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:15:57 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_048_ETHUSDT_15m_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:15:57 UTC (tier 1)

AUTONOMY screen autog2_048_ETHUSDT_15m_volatility_ohlcv_v1 tier=1 proxy_skill=1.6306570921647627 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:15:57 UTC (tier 0)

START gen=autog2_048_ETHUSDT_15m_volatility_ohlcv_v1_ts ETHUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:16:49 UTC (tier 0)

PREDICTABILITY real=+0.52332 p=0.0476 surr_q95=+0.05062 surr_max=+0.09738 draws=20 passed=True

## [INFO] 2026-08-03 10:17:05 UTC (tier 1)

trial `0c5d88de-7b55-4ca7-ba42-df799d754e07` model=lgbm_regressor tier=1 target=volatility skill=1.631 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:17:05 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_048_ETHUSDT_15m_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:17:05 UTC (tier 1)

AUTONOMY tradesim autog2_048_ETHUSDT_15m_volatility_ohlcv_v1 tier=1 proxy_skill=1.6306570921647627

## [INFO] 2026-08-03 10:17:05 UTC (tier 0)

START gen=autog2_049_ETHUSDT_15m_volatility_indicators_v1 ETHUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:17:55 UTC (tier 0)

PREDICTABILITY real=+0.48057 p=0.0476 surr_q95=+0.01355 surr_max=+0.22330 draws=20 passed=True

## [INFO] 2026-08-03 10:18:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:18:09 UTC (tier 0)

trial `326a890c-cefe-465d-8812-21d5eef941de` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:18:10 UTC (tier 1)

trial `33bce117-01a6-41df-a314-b06cd17ea949` model=ridge tier=1 target=volatility skill=1.435 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:18:16 UTC (tier 1)

trial `ee1a17bd-1271-43db-93e0-d01617ca47c0` model=lgbm_regressor tier=1 target=volatility skill=1.452 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:18:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-71.78078 skill_surrogate=-71.78078

## [INFO] 2026-08-03 10:18:18 UTC (tier 0)

trial `f25cb66f-6f35-405c-845d-5957f145eadf` model=lgbm_classifier tier=0 target=volatility skill=0.017 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:18:18 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_049_ETHUSDT_15m_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:18:18 UTC (tier 1)

AUTONOMY screen autog2_049_ETHUSDT_15m_volatility_indicators_v1 tier=1 proxy_skill=1.4515439898981315 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:18:18 UTC (tier 0)

START gen=autog2_049_ETHUSDT_15m_volatility_indicators_v1_ts ETHUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:19:17 UTC (tier 0)

PREDICTABILITY real=+0.48057 p=0.0476 surr_q95=+0.01355 surr_max=+0.22330 draws=20 passed=True

## [INFO] 2026-08-03 10:19:34 UTC (tier 1)

trial `4d11c322-dee1-48e5-babe-7235b90e94d4` model=lgbm_regressor tier=1 target=volatility skill=1.452 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:19:34 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_049_ETHUSDT_15m_volatility_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:19:34 UTC (tier 1)

AUTONOMY tradesim autog2_049_ETHUSDT_15m_volatility_indicators_v1 tier=1 proxy_skill=1.4515439898981315

## [INFO] 2026-08-03 10:19:34 UTC (tier 0)

START gen=autog2_050_ETHUSDT_15m_volatility_pivot_v1 ETHUSDT 15m target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:19:58 UTC (tier 0)

PREDICTABILITY real=-0.00800 p=1.0000 surr_q95=+0.00183 surr_max=+0.00524 draws=20 passed=False

## [INFO] 2026-08-03 10:20:05 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:20:05 UTC (tier 0)

trial `d30d13d8-1458-4623-af12-a664a84bda18` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:20:05 UTC (tier 0)

trial `2f6a7234-69e5-40e3-bc41-c856e73f91e0` model=ridge tier=0 target=volatility skill=0.993 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:20:08 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00878 skill_surrogate=-0.00476

## [INFO] 2026-08-03 10:20:08 UTC (tier 0)

trial `fc1cd923-8fc7-4677-8281-3246509d5079` model=lgbm_regressor tier=0 target=volatility skill=0.998 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:20:09 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-71.75393 skill_surrogate=-71.75393

## [INFO] 2026-08-03 10:20:09 UTC (tier 0)

trial `ce4e7660-f691-48df-9b25-f95b6122b1ec` model=lgbm_classifier tier=0 target=volatility skill=0.017 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:20:09 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_050_ETHUSDT_15m_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:20:09 UTC (tier 0)

AUTONOMY screen autog2_050_ETHUSDT_15m_volatility_pivot_v1 tier=0 proxy_skill=1.0 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:20:09 UTC (tier 0)

START gen=autog2_051_SOLUSDT_15m_volatility_ohlcv_v1 SOLUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:20:56 UTC (tier 0)

PREDICTABILITY real=+0.47112 p=0.0476 surr_q95=+0.05343 surr_max=+0.08194 draws=20 passed=True

## [INFO] 2026-08-03 10:20:59 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:20:59 UTC (tier 0)

trial `8e97d659-699e-409a-ac8c-fb9e07f635a0` model=hist_mean tier=0 target=volatility skill=1.000 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:21:01 UTC (tier 1)

trial `7d95e262-eb16-4bd8-abe2-6f10f05703c2` model=ridge tier=1 target=volatility skill=1.703 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:21:09 UTC (tier 1)

trial `b4aa20ed-fd2a-4b7e-b0e6-c33bdedc5861` model=lgbm_regressor tier=1 target=volatility skill=1.748 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:21:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-44.76189 skill_surrogate=-44.76189

## [INFO] 2026-08-03 10:21:11 UTC (tier 0)

trial `6819636a-370b-440c-87f0-33f4de99e174` model=lgbm_classifier tier=0 target=volatility skill=0.027 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:21:11 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_051_SOLUSDT_15m_volatility_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:21:11 UTC (tier 1)

AUTONOMY screen autog2_051_SOLUSDT_15m_volatility_ohlcv_v1 tier=1 proxy_skill=1.7483994545637311 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:21:11 UTC (tier 0)

START gen=autog2_051_SOLUSDT_15m_volatility_ohlcv_v1_ts SOLUSDT 15m target=volatility space=ohlcv_v1

## [INFO] 2026-08-03 10:21:54 UTC (tier 0)

PREDICTABILITY real=+0.47112 p=0.0476 surr_q95=+0.05343 surr_max=+0.08194 draws=20 passed=True

## [INFO] 2026-08-03 10:22:01 UTC (tier 1)

trial `89adf6ec-f1bd-4a31-9fb5-adde3cc4b41f` model=lgbm_regressor tier=1 target=volatility skill=1.748 n=131421 gates=UNKNOWN

## [INFO] 2026-08-03 10:22:01 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_051_SOLUSDT_15m_volatility_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:22:01 UTC (tier 1)

AUTONOMY tradesim autog2_051_SOLUSDT_15m_volatility_ohlcv_v1 tier=1 proxy_skill=1.7483994545637311

## [INFO] 2026-08-03 10:22:01 UTC (tier 0)

START gen=autog2_052_SOLUSDT_15m_volatility_indicators_v1 SOLUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:22:42 UTC (tier 0)

PREDICTABILITY real=+0.44941 p=0.0476 surr_q95=+0.01625 surr_max=+0.11214 draws=20 passed=True

## [INFO] 2026-08-03 10:22:45 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:22:45 UTC (tier 0)

trial `e84210a3-e7cb-49df-801b-106259d05fd4` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:22:46 UTC (tier 1)

trial `09d81afd-4a55-4fea-b3ec-37ebe811afa8` model=ridge tier=1 target=volatility skill=1.717 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:22:51 UTC (tier 1)

trial `19b9ca37-c3f7-40a3-8601-e943641aff02` model=lgbm_regressor tier=1 target=volatility skill=1.490 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:22:53 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-44.75800 skill_surrogate=-44.75800

## [INFO] 2026-08-03 10:22:53 UTC (tier 0)

trial `47c22edb-f8bb-4a28-be5f-c1f354f65bb4` model=lgbm_classifier tier=0 target=volatility skill=0.027 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:22:53 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_052_SOLUSDT_15m_volatility_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:22:53 UTC (tier 1)

AUTONOMY screen autog2_052_SOLUSDT_15m_volatility_indicators_v1 tier=1 proxy_skill=1.7174687138471694 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:22:53 UTC (tier 0)

START gen=autog2_052_SOLUSDT_15m_volatility_indicators_v1_ts SOLUSDT 15m target=volatility space=indicators_v1

## [INFO] 2026-08-03 10:23:46 UTC (tier 0)

PREDICTABILITY real=+0.44941 p=0.0476 surr_q95=+0.01625 surr_max=+0.11214 draws=20 passed=True

## [INFO] 2026-08-03 10:23:49 UTC (tier 1)

trial `3ee0df08-ebbe-4173-82e3-c0b7c445b6b2` model=ridge tier=1 target=volatility skill=1.717 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:23:49 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_052_SOLUSDT_15m_volatility_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:23:49 UTC (tier 1)

AUTONOMY tradesim autog2_052_SOLUSDT_15m_volatility_indicators_v1 tier=1 proxy_skill=1.7174687138471694

## [INFO] 2026-08-03 10:23:49 UTC (tier 0)

START gen=autog2_053_SOLUSDT_15m_volatility_pivot_v1 SOLUSDT 15m target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:24:18 UTC (tier 0)

PREDICTABILITY real=+0.01252 p=0.0476 surr_q95=+0.00091 surr_max=+0.00387 draws=20 passed=True

## [INFO] 2026-08-03 10:24:21 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:24:21 UTC (tier 0)

trial `3635b9f1-9109-4eac-a2cb-aef2ff3775a0` model=hist_mean tier=0 target=volatility skill=1.000 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:24:21 UTC (tier 1)

trial `e9ada4e1-efa1-4ff3-842a-9038f193078d` model=ridge tier=1 target=volatility skill=1.007 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:24:26 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00184 skill_surrogate=-0.00093

## [INFO] 2026-08-03 10:24:26 UTC (tier 0)

trial `d212d691-a8ea-436a-b018-56ab81fe7ef8` model=lgbm_regressor tier=0 target=volatility skill=1.006 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:24:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-44.74830 skill_surrogate=-44.74830

## [INFO] 2026-08-03 10:24:27 UTC (tier 0)

trial `df595b4d-f41c-4c04-929f-43ab8b2fdaf0` model=lgbm_classifier tier=0 target=volatility skill=0.027 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:24:27 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_053_SOLUSDT_15m_volatility_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:24:27 UTC (tier 1)

AUTONOMY screen autog2_053_SOLUSDT_15m_volatility_pivot_v1 tier=1 proxy_skill=1.0072194885277623 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:24:27 UTC (tier 0)

START gen=autog2_053_SOLUSDT_15m_volatility_pivot_v1_ts SOLUSDT 15m target=volatility space=pivot_v1

## [INFO] 2026-08-03 10:24:58 UTC (tier 0)

PREDICTABILITY real=+0.01252 p=0.0476 surr_q95=+0.00091 surr_max=+0.00387 draws=20 passed=True

## [INFO] 2026-08-03 10:25:00 UTC (tier 1)

trial `cb270c92-ec04-49a6-9876-c2e7259571e0` model=ridge tier=1 target=volatility skill=1.007 n=131424 gates=UNKNOWN

## [INFO] 2026-08-03 10:25:00 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_053_SOLUSDT_15m_volatility_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:25:00 UTC (tier 1)

AUTONOMY tradesim autog2_053_SOLUSDT_15m_volatility_pivot_v1 tier=1 proxy_skill=1.0072194885277623

## [INFO] 2026-08-03 10:25:00 UTC (tier 0)

START gen=autog2_054_BTCUSDT_1h_xs_rank_xs_v1 BTCUSDT 1h target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:25:10 UTC (tier 0)

PREDICTABILITY real=+0.00438 p=0.0476 surr_q95=+0.00067 surr_max=+0.00217 draws=20 passed=True

## [INFO] 2026-08-03 10:25:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:25:12 UTC (tier 0)

trial `58b93474-0b6e-4739-9d0a-a2fb40990698` model=hist_mean tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:25:12 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00033 skill_surrogate=-0.00026

## [INFO] 2026-08-03 10:25:12 UTC (tier 0)

trial `c5df1b49-0517-42cb-a929-02f67c46d7f2` model=ridge tier=0 target=xs_rank pf=0.732 n=29894 gates=FAIL

## [INFO] 2026-08-03 10:25:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00322 skill_surrogate=-0.00161

## [INFO] 2026-08-03 10:25:14 UTC (tier 0)

trial `a45b6be6-e1b5-4940-a77b-182ee2a40834` model=lgbm_regressor tier=0 target=xs_rank pf=0.716 n=29258 gates=FAIL

## [INFO] 2026-08-03 10:25:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.68212 skill_surrogate=-0.68212

## [INFO] 2026-08-03 10:25:14 UTC (tier 0)

trial `91d4090a-4706-47ac-8695-cb4dc6164066` model=lgbm_classifier tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:25:14 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_054_BTCUSDT_1h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:25:14 UTC (tier 0)

AUTONOMY screen autog2_054_BTCUSDT_1h_xs_rank_xs_v1 tier=0 proxy_pf=0.7319728202993308 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:25:14 UTC (tier 0)

START gen=autog2_055_BTCUSDT_1h_xs_rank_crosspair_v1 BTCUSDT 1h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:25:21 UTC (tier 0)

PREDICTABILITY real=+0.00197 p=0.0476 surr_q95=+0.00061 surr_max=+0.00108 draws=20 passed=True

## [INFO] 2026-08-03 10:25:23 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:25:23 UTC (tier 0)

trial `73de6b51-e8a0-4037-a4eb-e26f2d7812e0` model=hist_mean tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:25:24 UTC (tier 1)

trial `2c507031-6ec9-4f9b-af5c-33da7cb6a8e0` model=ridge tier=1 target=xs_rank pf=0.723 n=32826 gates=FAIL

## [INFO] 2026-08-03 10:25:25 UTC (tier 1)

trial `6f311529-37b0-40fd-ab3c-3afd016ac4a5` model=lgbm_regressor tier=1 target=xs_rank pf=0.712 n=29858 gates=FAIL

## [INFO] 2026-08-03 10:25:25 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.68034 skill_surrogate=-0.68034

## [INFO] 2026-08-03 10:25:25 UTC (tier 0)

trial `e5eaff21-c8a4-419d-af58-8c9881fe04a3` model=lgbm_classifier tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:25:25 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_055_BTCUSDT_1h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:25:25 UTC (tier 1)

AUTONOMY screen autog2_055_BTCUSDT_1h_xs_rank_crosspair_v1 tier=1 proxy_pf=0.7225304798248219 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:25:25 UTC (tier 0)

START gen=autog2_055_BTCUSDT_1h_xs_rank_crosspair_v1_ts BTCUSDT 1h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:25:32 UTC (tier 0)

PREDICTABILITY real=+0.00197 p=0.0476 surr_q95=+0.00061 surr_max=+0.00108 draws=20 passed=True

## [INFO] 2026-08-03 10:25:42 UTC (tier 1)

trial `2ce3841e-f835-40e3-b32e-4522c80fbf8f` model=ridge tier=1 target=xs_rank pf=0.810 n=3760 gates=FAIL

## [INFO] 2026-08-03 10:25:42 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_055_BTCUSDT_1h_xs_rank_crosspair_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:25:42 UTC (tier 1)

AUTONOMY tradesim autog2_055_BTCUSDT_1h_xs_rank_crosspair_v1 tier=1 proxy_pf=0.8095944309000572

## [INFO] 2026-08-03 10:25:42 UTC (tier 0)

START gen=autog2_056_BTCUSDT_1h_xs_rank_ohlcv_v1 BTCUSDT 1h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:25:55 UTC (tier 0)

PREDICTABILITY real=-0.00118 p=0.7143 surr_q95=+0.00954 surr_max=+0.01867 draws=20 passed=False

## [INFO] 2026-08-03 10:25:58 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:25:58 UTC (tier 0)

trial `b711f68d-1058-4f81-80a5-b2e6c9a47c90` model=hist_mean tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:25:58 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00348 skill_surrogate=-0.00074

## [INFO] 2026-08-03 10:25:58 UTC (tier 0)

trial `5af9476f-b3c0-4345-a2e6-f1ddf0702f16` model=ridge tier=0 target=xs_rank pf=0.712 n=32394 gates=FAIL

## [INFO] 2026-08-03 10:26:00 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00746 skill_surrogate=-0.00208

## [INFO] 2026-08-03 10:26:00 UTC (tier 0)

trial `3cf12082-cf52-4277-bcd9-92c0351811f7` model=lgbm_regressor tier=0 target=xs_rank pf=0.700 n=30150 gates=FAIL

## [INFO] 2026-08-03 10:26:01 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.68594 skill_surrogate=-0.68594

## [INFO] 2026-08-03 10:26:01 UTC (tier 0)

trial `25155b17-1d4d-45d7-93d4-6abbc818a5c5` model=lgbm_classifier tier=0 target=xs_rank pf=0.723 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:26:01 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_056_BTCUSDT_1h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:26:01 UTC (tier 0)

AUTONOMY screen autog2_056_BTCUSDT_1h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.7228965935014684 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:26:01 UTC (tier 0)

START gen=autog2_057_ETHUSDT_1h_xs_rank_xs_v1 ETHUSDT 1h target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:26:10 UTC (tier 0)

PREDICTABILITY real=-0.00177 p=0.8095 surr_q95=+0.00051 surr_max=+0.00558 draws=20 passed=False

## [INFO] 2026-08-03 10:26:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:26:12 UTC (tier 0)

trial `3677bf0b-565c-49f2-9f01-678c5569fb93` model=hist_mean tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:26:12 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00372 skill_surrogate=-0.00018

## [INFO] 2026-08-03 10:26:12 UTC (tier 0)

trial `e5aedd18-4fca-43c5-a50f-548f4cc53f38` model=ridge tier=0 target=xs_rank pf=0.767 n=29494 gates=FAIL

## [INFO] 2026-08-03 10:26:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00155 skill_surrogate=+0.00121

## [INFO] 2026-08-03 10:26:14 UTC (tier 0)

trial `42fe4aee-3786-4fe2-bffc-d4bc9e1703de` model=lgbm_regressor tier=0 target=xs_rank pf=0.754 n=29296 gates=FAIL

## [INFO] 2026-08-03 10:26:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.87043 skill_surrogate=-0.87043

## [INFO] 2026-08-03 10:26:14 UTC (tier 0)

trial `3140cd8a-6109-4f38-acd1-5f62071711bc` model=lgbm_classifier tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:26:14 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_057_ETHUSDT_1h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:26:14 UTC (tier 0)

AUTONOMY screen autog2_057_ETHUSDT_1h_xs_rank_xs_v1 tier=0 proxy_pf=0.7674134926733643 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:26:14 UTC (tier 0)

START gen=autog2_058_ETHUSDT_1h_xs_rank_crosspair_v1 ETHUSDT 1h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:26:20 UTC (tier 0)

PREDICTABILITY real=-0.00095 p=0.7619 surr_q95=+0.00084 surr_max=+0.00096 draws=20 passed=False

## [INFO] 2026-08-03 10:26:23 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:26:23 UTC (tier 0)

trial `7e776a97-b84d-4caa-85a0-ed97d1622aca` model=hist_mean tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:26:23 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00027 skill_surrogate=-0.00013

## [INFO] 2026-08-03 10:26:23 UTC (tier 0)

trial `0841189d-9d06-4c16-b04e-629dce3d7abc` model=ridge tier=0 target=xs_rank pf=0.763 n=32771 gates=FAIL

## [INFO] 2026-08-03 10:26:24 UTC (tier 0)

trial `52b3fd38-10bc-4310-8ec8-7675d111e704` model=lgbm_regressor tier=0 target=xs_rank pf=0.761 n=30310 gates=FAIL

## [INFO] 2026-08-03 10:26:24 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.86324 skill_surrogate=-0.86324

## [INFO] 2026-08-03 10:26:24 UTC (tier 0)

trial `c4763919-b89b-4a4b-bbf8-c31bfb719e37` model=lgbm_classifier tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:26:24 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_058_ETHUSDT_1h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:26:24 UTC (tier 0)

AUTONOMY screen autog2_058_ETHUSDT_1h_xs_rank_crosspair_v1 tier=0 proxy_pf=0.7642285849544566 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:26:24 UTC (tier 0)

START gen=autog2_059_ETHUSDT_1h_xs_rank_ohlcv_v1 ETHUSDT 1h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:26:37 UTC (tier 0)

PREDICTABILITY real=-0.01830 p=1.0000 surr_q95=+0.00393 surr_max=+0.00508 draws=20 passed=False

## [INFO] 2026-08-03 10:26:40 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:26:40 UTC (tier 0)

trial `a25c679e-2f3d-4c63-904a-94b81beabc72` model=hist_mean tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:26:40 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00281 skill_surrogate=+0.00066

## [INFO] 2026-08-03 10:26:40 UTC (tier 0)

trial `363ad268-7c44-4c3f-be3d-4a18c77ed247` model=ridge tier=0 target=xs_rank pf=0.749 n=31287 gates=FAIL

## [INFO] 2026-08-03 10:26:42 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00137 skill_surrogate=-0.00042

## [INFO] 2026-08-03 10:26:42 UTC (tier 0)

trial `4f20b7a4-1655-4894-9c2c-2b542c024bb8` model=lgbm_regressor tier=0 target=xs_rank pf=0.750 n=29417 gates=FAIL

## [INFO] 2026-08-03 10:26:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.87043 skill_surrogate=-0.87043

## [INFO] 2026-08-03 10:26:43 UTC (tier 0)

trial `ee3a6752-1b02-4e8f-b1d3-ce06a23c09f7` model=lgbm_classifier tier=0 target=xs_rank pf=0.764 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:26:43 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_059_ETHUSDT_1h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:26:43 UTC (tier 0)

AUTONOMY screen autog2_059_ETHUSDT_1h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.7642285849544566 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:26:43 UTC (tier 0)

START gen=autog2_060_SOLUSDT_1h_xs_rank_xs_v1 SOLUSDT 1h target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:26:52 UTC (tier 0)

PREDICTABILITY real=-0.00071 p=0.5714 surr_q95=+0.00037 surr_max=+0.00062 draws=20 passed=False

## [INFO] 2026-08-03 10:26:54 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:26:54 UTC (tier 0)

trial `a59d5cb4-730b-49c4-99af-8de133a6820b` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:26:54 UTC (tier 0)

trial `8357fa55-54d8-4adf-896c-21f76a3614ab` model=ridge tier=0 target=xs_rank pf=0.846 n=11524 gates=FAIL

## [INFO] 2026-08-03 10:26:56 UTC (tier 0)

trial `b2a5e9b2-bf9f-4b26-964e-d060875b922f` model=lgbm_regressor tier=0 target=xs_rank pf=0.877 n=9592 gates=FAIL

## [INFO] 2026-08-03 10:26:56 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.77286 skill_surrogate=-0.77286

## [INFO] 2026-08-03 10:26:56 UTC (tier 0)

trial `8675eb43-2075-4410-982c-e30f9c6c1ff6` model=lgbm_classifier tier=0 target=xs_rank pf=0.848 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:26:56 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_060_SOLUSDT_1h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:26:56 UTC (tier 0)

AUTONOMY screen autog2_060_SOLUSDT_1h_xs_rank_xs_v1 tier=0 proxy_pf=0.8768375096847943 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:26:56 UTC (tier 0)

START gen=autog2_061_SOLUSDT_1h_xs_rank_crosspair_v1 SOLUSDT 1h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:27:02 UTC (tier 0)

PREDICTABILITY real=+0.00113 p=0.0476 surr_q95=+0.00043 surr_max=+0.00069 draws=20 passed=True

## [INFO] 2026-08-03 10:27:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:27:04 UTC (tier 0)

trial `281e1b9c-06f4-4beb-80ac-80b01d2a0c27` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:27:04 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=+0.00004 skill_surrogate=+0.00016

## [INFO] 2026-08-03 10:27:04 UTC (tier 0)

trial `86eaff98-cc27-44eb-9592-2195ea18ea5e` model=ridge tier=0 target=xs_rank pf=0.925 n=3509 gates=FAIL

## [INFO] 2026-08-03 10:27:06 UTC (tier 1)

trial `0dbac0c9-9cb1-4a1f-8b08-289ead5fcd6e` model=lgbm_regressor tier=1 target=xs_rank pf=0.929 n=7397 gates=FAIL

## [INFO] 2026-08-03 10:27:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.77286 skill_surrogate=-0.77286

## [INFO] 2026-08-03 10:27:06 UTC (tier 0)

trial `8dc64a9e-d826-4408-9098-61ff31253bc6` model=lgbm_classifier tier=0 target=xs_rank pf=0.848 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:27:06 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_061_SOLUSDT_1h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:27:06 UTC (tier 1)

AUTONOMY screen autog2_061_SOLUSDT_1h_xs_rank_crosspair_v1 tier=1 proxy_pf=0.9292943930471456 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:27:06 UTC (tier 0)

START gen=autog2_061_SOLUSDT_1h_xs_rank_crosspair_v1_ts SOLUSDT 1h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:27:12 UTC (tier 0)

PREDICTABILITY real=+0.00113 p=0.0476 surr_q95=+0.00043 surr_max=+0.00069 draws=20 passed=True

## [INFO] 2026-08-03 10:27:20 UTC (tier 1)

trial `e152aad7-e820-47cd-b1e1-866712c70cee` model=lgbm_regressor tier=1 target=xs_rank pf=0.785 n=4055 gates=FAIL

## [INFO] 2026-08-03 10:27:20 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_061_SOLUSDT_1h_xs_rank_crosspair_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:27:20 UTC (tier 1)

AUTONOMY tradesim autog2_061_SOLUSDT_1h_xs_rank_crosspair_v1 tier=1 proxy_pf=0.7845204185561809

## [INFO] 2026-08-03 10:27:21 UTC (tier 0)

START gen=autog2_062_SOLUSDT_1h_xs_rank_ohlcv_v1 SOLUSDT 1h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:27:33 UTC (tier 0)

PREDICTABILITY real=-0.00112 p=0.4286 surr_q95=+0.00016 surr_max=+0.00069 draws=20 passed=False

## [INFO] 2026-08-03 10:27:35 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:27:35 UTC (tier 0)

trial `ce9f9eba-b83a-4b25-92a9-f139537f4c45` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:27:35 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00124 skill_surrogate=+0.00072

## [INFO] 2026-08-03 10:27:35 UTC (tier 0)

trial `5fada8b4-c3c3-4dcf-9415-9a47608e4164` model=ridge tier=0 target=xs_rank pf=0.899 n=9983 gates=FAIL

## [INFO] 2026-08-03 10:27:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00232 skill_surrogate=+0.00068

## [INFO] 2026-08-03 10:27:38 UTC (tier 0)

trial `ecf0edce-19fc-4cf3-aaf9-61414549d6f2` model=lgbm_regressor tier=0 target=xs_rank pf=0.897 n=13536 gates=FAIL

## [INFO] 2026-08-03 10:27:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.77286 skill_surrogate=-0.77286

## [INFO] 2026-08-03 10:27:38 UTC (tier 0)

trial `9e1821bb-667f-48b0-9142-2361a78b402a` model=lgbm_classifier tier=0 target=xs_rank pf=0.848 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:27:38 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_062_SOLUSDT_1h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:27:38 UTC (tier 0)

AUTONOMY screen autog2_062_SOLUSDT_1h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.8987394146822163 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:27:38 UTC (tier 0)

START gen=autog2_063_BTCUSDT_4h_xs_rank_xs_v1 BTCUSDT 4h target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:27:44 UTC (tier 0)

PREDICTABILITY real=-0.01465 p=1.0000 surr_q95=-0.00012 surr_max=+0.00008 draws=20 passed=False

## [INFO] 2026-08-03 10:27:45 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:27:45 UTC (tier 0)

trial `01ff2537-f4e5-40c8-949e-c2239c2671a3` model=hist_mean tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:27:45 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00643 skill_surrogate=-0.00120

## [INFO] 2026-08-03 10:27:45 UTC (tier 0)

trial `b0c6dde1-4adc-4c3b-9034-f8d9340e41a2` model=ridge tier=0 target=xs_rank pf=0.939 n=7797 gates=FAIL

## [INFO] 2026-08-03 10:27:46 UTC (tier 0)

trial `ea40d2c7-a1ac-405c-94b2-543013f89f21` model=lgbm_regressor tier=0 target=xs_rank pf=0.896 n=7124 gates=FAIL

## [INFO] 2026-08-03 10:27:46 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.57357 skill_surrogate=-0.57357

## [INFO] 2026-08-03 10:27:46 UTC (tier 0)

trial `9ccd53eb-9476-4a9a-8dc6-525fc25807cf` model=lgbm_classifier tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:27:46 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_063_BTCUSDT_4h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:27:46 UTC (tier 0)

AUTONOMY screen autog2_063_BTCUSDT_4h_xs_rank_xs_v1 tier=0 proxy_pf=0.948482148877497 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:27:46 UTC (tier 0)

START gen=autog2_064_BTCUSDT_4h_xs_rank_crosspair_v1 BTCUSDT 4h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:27:50 UTC (tier 0)

PREDICTABILITY real=+0.01127 p=0.0476 surr_q95=+0.00413 surr_max=+0.00476 draws=20 passed=True

## [INFO] 2026-08-03 10:27:51 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:27:51 UTC (tier 0)

trial `f7ee8216-acb3-4830-adeb-4fb0c43506c3` model=hist_mean tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:27:51 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00500 skill_surrogate=-0.00137

## [INFO] 2026-08-03 10:27:51 UTC (tier 0)

trial `e3036acf-d73f-4cf8-9aaa-a873009e3ad2` model=ridge tier=0 target=xs_rank pf=0.951 n=8106 gates=FAIL

## [INFO] 2026-08-03 10:27:52 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00484 skill_surrogate=-0.00254

## [INFO] 2026-08-03 10:27:52 UTC (tier 0)

trial `725ac6f4-4de8-43d4-9b58-7caa73d3349c` model=lgbm_regressor tier=0 target=xs_rank pf=0.943 n=6967 gates=FAIL

## [INFO] 2026-08-03 10:27:52 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.57454 skill_surrogate=-0.57454

## [INFO] 2026-08-03 10:27:52 UTC (tier 0)

trial `80aedb9f-b251-497a-a53d-85d7cb53bd6c` model=lgbm_classifier tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:27:52 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_064_BTCUSDT_4h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:27:52 UTC (tier 0)

AUTONOMY screen autog2_064_BTCUSDT_4h_xs_rank_crosspair_v1 tier=0 proxy_pf=0.9510713636379153 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:27:52 UTC (tier 0)

START gen=autog2_065_BTCUSDT_4h_xs_rank_ohlcv_v1 BTCUSDT 4h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:27:59 UTC (tier 0)

PREDICTABILITY real=-0.00521 p=0.4762 surr_q95=+0.00782 surr_max=+0.01029 draws=20 passed=False

## [INFO] 2026-08-03 10:28:00 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:28:00 UTC (tier 0)

trial `9dc86e00-216e-4e8c-aec2-cc745c602024` model=hist_mean tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:00 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00266 skill_surrogate=+0.00029

## [INFO] 2026-08-03 10:28:00 UTC (tier 0)

trial `4bb38e8f-f263-400a-84e7-b3aa2059433c` model=ridge tier=0 target=xs_rank pf=0.925 n=8084 gates=FAIL

## [INFO] 2026-08-03 10:28:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00897 skill_surrogate=+0.00086

## [INFO] 2026-08-03 10:28:02 UTC (tier 0)

trial `670c0a27-eb97-414c-9f03-e17711b0408a` model=lgbm_regressor tier=0 target=xs_rank pf=0.943 n=7468 gates=FAIL

## [INFO] 2026-08-03 10:28:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.56815 skill_surrogate=-0.56815

## [INFO] 2026-08-03 10:28:02 UTC (tier 0)

trial `c5dd468b-a690-46f3-8fca-0ad34225c21c` model=lgbm_classifier tier=0 target=xs_rank pf=0.948 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:02 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_065_BTCUSDT_4h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:28:02 UTC (tier 0)

AUTONOMY screen autog2_065_BTCUSDT_4h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.948482148877497 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:28:02 UTC (tier 0)

START gen=autog2_066_ETHUSDT_4h_xs_rank_xs_v1 ETHUSDT 4h target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:28:06 UTC (tier 0)

PREDICTABILITY real=+0.00290 p=0.0952 surr_q95=+0.00149 surr_max=+0.00327 draws=20 passed=False

## [INFO] 2026-08-03 10:28:07 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:28:07 UTC (tier 0)

trial `08c65ecd-26af-47e8-9121-853ac804f64b` model=hist_mean tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:07 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00460 skill_surrogate=-0.00310

## [INFO] 2026-08-03 10:28:07 UTC (tier 0)

trial `21b2d761-a2e0-42e4-ab5a-670929a481a8` model=ridge tier=0 target=xs_rank pf=0.922 n=8174 gates=FAIL

## [INFO] 2026-08-03 10:28:08 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00458 skill_surrogate=-0.00565

## [INFO] 2026-08-03 10:28:08 UTC (tier 0)

trial `2542c5a9-694c-4122-9d17-dcc1153fcbb5` model=lgbm_regressor tier=0 target=xs_rank pf=0.898 n=7404 gates=FAIL

## [INFO] 2026-08-03 10:28:09 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.85370 skill_surrogate=-0.85370

## [INFO] 2026-08-03 10:28:09 UTC (tier 0)

trial `023aa645-50c5-454a-b23b-fe18db50bf1b` model=lgbm_classifier tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:09 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_066_ETHUSDT_4h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:28:09 UTC (tier 0)

AUTONOMY screen autog2_066_ETHUSDT_4h_xs_rank_xs_v1 tier=0 proxy_pf=0.9215764347940009 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:28:09 UTC (tier 0)

START gen=autog2_067_ETHUSDT_4h_xs_rank_crosspair_v1 ETHUSDT 4h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:28:12 UTC (tier 0)

PREDICTABILITY real=-0.00387 p=0.8571 surr_q95=+0.00323 surr_max=+0.01086 draws=20 passed=False

## [INFO] 2026-08-03 10:28:13 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:28:13 UTC (tier 0)

trial `a4244598-a28a-454e-9710-72ed01dbb2ef` model=hist_mean tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:13 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00008 skill_surrogate=-0.00129

## [INFO] 2026-08-03 10:28:13 UTC (tier 0)

trial `7ad8903e-3819-4890-ab1d-eeb78f0b72e9` model=ridge tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01119 skill_surrogate=-0.00497

## [INFO] 2026-08-03 10:28:14 UTC (tier 0)

trial `0e0b6655-b70a-46ed-bf34-68a729db2abd` model=lgbm_regressor tier=0 target=xs_rank pf=0.942 n=7191 gates=FAIL

## [INFO] 2026-08-03 10:28:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.84376 skill_surrogate=-0.84376

## [INFO] 2026-08-03 10:28:14 UTC (tier 0)

trial `0820e111-d5d3-494b-a7ef-a68afe0a0c27` model=lgbm_classifier tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:14 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_067_ETHUSDT_4h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:28:14 UTC (tier 0)

AUTONOMY screen autog2_067_ETHUSDT_4h_xs_rank_crosspair_v1 tier=0 proxy_pf=0.9415470386990968 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:28:14 UTC (tier 0)

START gen=autog2_068_ETHUSDT_4h_xs_rank_ohlcv_v1 ETHUSDT 4h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:28:20 UTC (tier 0)

PREDICTABILITY real=-0.01729 p=0.8571 surr_q95=-0.00101 surr_max=-0.00044 draws=20 passed=False

## [INFO] 2026-08-03 10:28:22 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:28:22 UTC (tier 0)

trial `18e0a3ac-5fbb-4157-a367-add6833d2fec` model=hist_mean tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:22 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00399 skill_surrogate=-0.00465

## [INFO] 2026-08-03 10:28:22 UTC (tier 0)

trial `6e7923a5-a11d-4672-a097-c74107ff9382` model=ridge tier=0 target=xs_rank pf=0.906 n=8088 gates=FAIL

## [INFO] 2026-08-03 10:28:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00772 skill_surrogate=-0.01135

## [INFO] 2026-08-03 10:28:23 UTC (tier 0)

trial `f1ce8a0b-909a-47f6-a53f-b893fc273fc1` model=lgbm_regressor tier=0 target=xs_rank pf=0.895 n=7425 gates=FAIL

## [INFO] 2026-08-03 10:28:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.85370 skill_surrogate=-0.85370

## [INFO] 2026-08-03 10:28:23 UTC (tier 0)

trial `d92a7162-5f72-43dd-bb5f-dde28641ff18` model=lgbm_classifier tier=0 target=xs_rank pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:23 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_068_ETHUSDT_4h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:28:23 UTC (tier 0)

AUTONOMY screen autog2_068_ETHUSDT_4h_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.9200856060065038 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:28:23 UTC (tier 0)

START gen=autog2_069_SOLUSDT_4h_xs_rank_xs_v1 SOLUSDT 4h target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:28:26 UTC (tier 0)

PREDICTABILITY real=-0.00388 p=0.6190 surr_q95=+0.00177 surr_max=+0.00293 draws=20 passed=False

## [INFO] 2026-08-03 10:28:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 10:28:27 UTC (tier 0)

trial `20e28cdc-40d5-4131-a411-fa9080f522d5` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:28:27 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00491 skill_surrogate=+0.00159

## [INFO] 2026-08-03 10:28:27 UTC (tier 0)

trial `c2083b9b-6a34-4cf2-b46e-b825a7ea78d4` model=ridge tier=0 target=xs_rank pf=0.922 n=3257 gates=FAIL

## [INFO] 2026-08-03 10:28:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00903 skill_surrogate=+0.00072

## [INFO] 2026-08-03 10:28:28 UTC (tier 0)

trial `7e6affc1-79ba-47b6-8e7b-25d9d085b7c3` model=lgbm_regressor tier=0 target=xs_rank pf=0.950 n=4160 gates=FAIL

## [INFO] 2026-08-03 10:28:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.84700 skill_surrogate=-0.84700

## [INFO] 2026-08-03 10:28:28 UTC (tier 0)

trial `0089022c-046a-4c2f-b1d7-4471e28d1ec6` model=lgbm_classifier tier=0 target=xs_rank pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:28 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_069_SOLUSDT_4h_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:28:28 UTC (tier 0)

AUTONOMY screen autog2_069_SOLUSDT_4h_xs_rank_xs_v1 tier=0 proxy_pf=0.9701066640508432 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:28:28 UTC (tier 0)

START gen=autog2_070_SOLUSDT_4h_xs_rank_crosspair_v1 SOLUSDT 4h target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:28:30 UTC (tier 0)

PREDICTABILITY real=+0.00220 p=0.2381 surr_q95=+0.00416 surr_max=+0.00636 draws=20 passed=False

## [INFO] 2026-08-03 10:28:31 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 10:28:31 UTC (tier 0)

trial `6dda1b2b-81cb-4801-8098-7fbe64c11438` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:28:31 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00056 skill_surrogate=+0.00092

## [INFO] 2026-08-03 10:28:31 UTC (tier 0)

trial `314e7a4a-c68a-452f-b819-b76b986f3500` model=ridge tier=0 target=xs_rank pf=1.021 n=585 gates=FAIL

## [INFO] 2026-08-03 10:28:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00132 skill_surrogate=+0.00102

## [INFO] 2026-08-03 10:28:32 UTC (tier 0)

trial `e6b8af3e-ce5e-4d68-b286-e1942af5b652` model=lgbm_regressor tier=0 target=xs_rank pf=1.124 n=3003 gates=FAIL

## [INFO] 2026-08-03 10:28:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.84700 skill_surrogate=-0.84700

## [INFO] 2026-08-03 10:28:32 UTC (tier 0)

trial `601a7d99-dba3-4a5c-a703-1cf62efa48b4` model=lgbm_classifier tier=0 target=xs_rank pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:32 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_070_SOLUSDT_4h_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:28:32 UTC (tier 0)

AUTONOMY screen autog2_070_SOLUSDT_4h_xs_rank_crosspair_v1 tier=0 proxy_pf=1.1237433499382057 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:28:32 UTC (tier 0)

START gen=autog2_071_SOLUSDT_4h_xs_rank_ohlcv_v1 SOLUSDT 4h target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:28:36 UTC (tier 0)

PREDICTABILITY real=-0.00162 p=0.2857 surr_q95=+0.00310 surr_max=+0.00613 draws=20 passed=False

## [INFO] 2026-08-03 10:28:37 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 10:28:37 UTC (tier 0)

trial `9e102e6a-2d9d-4e6b-85c2-11fb569e73a4` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:28:37 UTC (tier 0)

trial `1b01f294-9036-4187-b162-37d2ca5b852b` model=ridge tier=0 target=xs_rank pf=1.164 n=2083 gates=FAIL

## [INFO] 2026-08-03 10:28:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02228 skill_surrogate=+0.00212

## [INFO] 2026-08-03 10:28:38 UTC (tier 0)

trial `e6331acd-3bc7-4de3-b7f1-0df54bf7d61d` model=lgbm_regressor tier=0 target=xs_rank pf=0.979 n=4726 gates=FAIL

## [INFO] 2026-08-03 10:28:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.84700 skill_surrogate=-0.84700

## [INFO] 2026-08-03 10:28:38 UTC (tier 0)

trial `4c9c1d6a-052f-4beb-928a-14f5eb4bfacb` model=lgbm_classifier tier=0 target=xs_rank pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:28:38 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_071_SOLUSDT_4h_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:28:38 UTC (tier 0)

AUTONOMY screen autog2_071_SOLUSDT_4h_xs_rank_ohlcv_v1 tier=0 proxy_pf=1.1640774293306702 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:28:39 UTC (tier 0)

START gen=autog2_072_BTCUSDT_15m_xs_rank_xs_v1 BTCUSDT 15m target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:29:43 UTC (tier 0)

PREDICTABILITY real=+0.00855 p=0.0476 surr_q95=+0.00006 surr_max=+0.00036 draws=20 passed=True

## [INFO] 2026-08-03 10:30:02 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:30:02 UTC (tier 0)

trial `af3f7343-4d81-499d-b860-31d95e42058a` model=hist_mean tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:30:02 UTC (tier 1)

trial `c0af9159-4aa9-4ad1-bf53-3de55321aea6` model=ridge tier=1 target=xs_rank pf=0.472 n=107826 gates=FAIL

## [INFO] 2026-08-03 10:30:08 UTC (tier 1)

trial `aa065d31-0526-403a-b130-d3711c405a39` model=lgbm_regressor tier=1 target=xs_rank pf=0.469 n=113074 gates=FAIL

## [INFO] 2026-08-03 10:30:09 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.67283 skill_surrogate=-0.67283

## [INFO] 2026-08-03 10:30:09 UTC (tier 0)

trial `fff2067c-3573-4e40-a396-d08a05ed6c36` model=lgbm_classifier tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:30:09 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_072_BTCUSDT_15m_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:30:09 UTC (tier 1)

AUTONOMY screen autog2_072_BTCUSDT_15m_xs_rank_xs_v1 tier=1 proxy_pf=0.47224957496344816 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:30:09 UTC (tier 0)

START gen=autog2_072_BTCUSDT_15m_xs_rank_xs_v1_ts BTCUSDT 15m target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:30:53 UTC (tier 0)

PREDICTABILITY real=+0.00855 p=0.0476 surr_q95=+0.00006 surr_max=+0.00036 draws=20 passed=True

## [INFO] 2026-08-03 10:31:31 UTC (tier 1)

trial `a9d4d9a7-b39f-4eee-9468-940cd71ecc4c` model=ridge tier=1 target=xs_rank pf=0.809 n=4174 gates=FAIL

## [INFO] 2026-08-03 10:31:31 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_072_BTCUSDT_15m_xs_rank_xs_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:31:31 UTC (tier 1)

AUTONOMY tradesim autog2_072_BTCUSDT_15m_xs_rank_xs_v1 tier=1 proxy_pf=0.8092891662197864

## [INFO] 2026-08-03 10:31:31 UTC (tier 0)

START gen=autog2_073_BTCUSDT_15m_xs_rank_crosspair_v1 BTCUSDT 15m target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:32:00 UTC (tier 0)

PREDICTABILITY real=+0.00476 p=0.0476 surr_q95=+0.00010 surr_max=+0.00011 draws=20 passed=True

## [INFO] 2026-08-03 10:32:13 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:32:13 UTC (tier 0)

trial `17343ffc-4881-4cc2-9d75-fbee9c93f861` model=hist_mean tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:32:13 UTC (tier 1)

trial `7ba51a35-23ef-4b31-b310-8823caec8f13` model=ridge tier=1 target=xs_rank pf=0.469 n=128747 gates=FAIL

## [INFO] 2026-08-03 10:32:20 UTC (tier 1)

trial `58395f43-783d-4b41-83be-43a255db44dc` model=lgbm_regressor tier=1 target=xs_rank pf=0.456 n=117559 gates=FAIL

## [INFO] 2026-08-03 10:32:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.67100 skill_surrogate=-0.67100

## [INFO] 2026-08-03 10:32:21 UTC (tier 0)

trial `da9d2915-a3a7-4c7f-952d-cc77545ccc38` model=lgbm_classifier tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:32:21 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_073_BTCUSDT_15m_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:32:21 UTC (tier 1)

AUTONOMY screen autog2_073_BTCUSDT_15m_xs_rank_crosspair_v1 tier=1 proxy_pf=0.4687574733048152 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:32:21 UTC (tier 0)

START gen=autog2_073_BTCUSDT_15m_xs_rank_crosspair_v1_ts BTCUSDT 15m target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:32:46 UTC (tier 0)

PREDICTABILITY real=+0.00476 p=0.0476 surr_q95=+0.00010 surr_max=+0.00011 draws=20 passed=True

## [INFO] 2026-08-03 10:33:14 UTC (tier 1)

trial `6b80a953-0fd0-4258-a60a-bf0ecdafe7a6` model=ridge tier=1 target=xs_rank pf=0.803 n=4451 gates=FAIL

## [INFO] 2026-08-03 10:33:14 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_073_BTCUSDT_15m_xs_rank_crosspair_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:33:14 UTC (tier 1)

AUTONOMY tradesim autog2_073_BTCUSDT_15m_xs_rank_crosspair_v1 tier=1 proxy_pf=0.8026444042596377

## [INFO] 2026-08-03 10:33:14 UTC (tier 0)

START gen=autog2_074_BTCUSDT_15m_xs_rank_ohlcv_v1 BTCUSDT 15m target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:34:02 UTC (tier 0)

PREDICTABILITY real=-0.00398 p=0.8571 surr_q95=+0.00844 surr_max=+0.01065 draws=20 passed=False

## [INFO] 2026-08-03 10:34:14 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:34:14 UTC (tier 0)

trial `14671bcc-822f-45ea-af2a-f9fab2849288` model=hist_mean tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:34:15 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00014 skill_surrogate=-0.00037

## [INFO] 2026-08-03 10:34:15 UTC (tier 0)

trial `eec17c52-ec81-4728-956e-6ee76aefd5a4` model=ridge tier=0 target=xs_rank pf=0.463 n=130075 gates=FAIL

## [INFO] 2026-08-03 10:34:20 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00192 skill_surrogate=-0.00014

## [INFO] 2026-08-03 10:34:20 UTC (tier 0)

trial `28e2e35b-870e-45d4-a200-2f11d3eb6d1a` model=lgbm_regressor tier=0 target=xs_rank pf=0.458 n=124547 gates=FAIL

## [INFO] 2026-08-03 10:34:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.67680 skill_surrogate=-0.67680

## [INFO] 2026-08-03 10:34:23 UTC (tier 0)

trial `9e50d362-e1cf-4865-bb00-bc01f230a225` model=lgbm_classifier tier=0 target=xs_rank pf=0.473 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:34:23 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_074_BTCUSDT_15m_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:34:23 UTC (tier 0)

AUTONOMY screen autog2_074_BTCUSDT_15m_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.47251179753828415 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:34:23 UTC (tier 0)

START gen=autog2_075_ETHUSDT_15m_xs_rank_xs_v1 ETHUSDT 15m target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:34:56 UTC (tier 0)

PREDICTABILITY real=+0.00317 p=0.0476 surr_q95=+0.00012 surr_max=+0.00020 draws=20 passed=True

## [INFO] 2026-08-03 10:35:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:35:08 UTC (tier 0)

trial `c5c8b33c-44f5-4805-8f88-6274408377e3` model=hist_mean tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:35:08 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00093 skill_surrogate=-0.00038

## [INFO] 2026-08-03 10:35:08 UTC (tier 0)

trial `dd99a28e-6c3d-45e2-80b2-f3e3e38efe9b` model=ridge tier=0 target=xs_rank pf=0.557 n=102570 gates=FAIL

## [INFO] 2026-08-03 10:35:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00021 skill_surrogate=-0.00031

## [INFO] 2026-08-03 10:35:12 UTC (tier 0)

trial `b4c5c97e-c1b7-4632-8c88-6ccddb62d089` model=lgbm_regressor tier=0 target=xs_rank pf=0.552 n=111900 gates=FAIL

## [INFO] 2026-08-03 10:35:13 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.95943 skill_surrogate=-0.95943

## [INFO] 2026-08-03 10:35:13 UTC (tier 0)

trial `d214151b-1261-4a58-8378-cd83e7608cd8` model=lgbm_classifier tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:35:13 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_075_ETHUSDT_15m_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:35:14 UTC (tier 0)

AUTONOMY screen autog2_075_ETHUSDT_15m_xs_rank_xs_v1 tier=0 proxy_pf=0.5573349843833583 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:35:14 UTC (tier 0)

START gen=autog2_076_ETHUSDT_15m_xs_rank_crosspair_v1 ETHUSDT 15m target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:35:33 UTC (tier 0)

PREDICTABILITY real=-0.00042 p=0.9048 surr_q95=+0.00012 surr_max=+0.00020 draws=20 passed=False

## [INFO] 2026-08-03 10:35:43 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:35:43 UTC (tier 0)

trial `000f89ac-303d-4866-a2af-52a055107ba6` model=hist_mean tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:35:44 UTC (tier 0)

trial `69b9c315-9d3f-4291-981c-273071c48ce9` model=ridge tier=0 target=xs_rank pf=0.554 n=129608 gates=FAIL

## [INFO] 2026-08-03 10:35:46 UTC (tier 0)

trial `ebddec81-d892-4122-8b7b-e34dc79bc7de` model=lgbm_regressor tier=0 target=xs_rank pf=0.552 n=114892 gates=FAIL

## [INFO] 2026-08-03 10:35:47 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.95412 skill_surrogate=-0.95412

## [INFO] 2026-08-03 10:35:47 UTC (tier 0)

trial `a90a8224-ed08-4b4e-b8c8-b92134b48268` model=lgbm_classifier tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:35:47 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_076_ETHUSDT_15m_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:35:47 UTC (tier 0)

AUTONOMY screen autog2_076_ETHUSDT_15m_xs_rank_crosspair_v1 tier=0 proxy_pf=0.5551435152352238 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:35:47 UTC (tier 0)

START gen=autog2_077_ETHUSDT_15m_xs_rank_ohlcv_v1 ETHUSDT 15m target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:36:37 UTC (tier 0)

PREDICTABILITY real=-0.00426 p=1.0000 surr_q95=+0.00225 surr_max=+0.00278 draws=20 passed=False

## [INFO] 2026-08-03 10:36:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:36:49 UTC (tier 0)

trial `a5944e33-f1a5-45bc-9f18-056069c65ca7` model=hist_mean tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:36:50 UTC (tier 0)

trial `5842f44c-35c1-4a20-ba96-8132b819cef9` model=ridge tier=0 target=xs_rank pf=0.546 n=125836 gates=FAIL

## [INFO] 2026-08-03 10:36:55 UTC (tier 0)

trial `2d1e71ad-abfd-414e-ae20-32e845f3d00b` model=lgbm_regressor tier=0 target=xs_rank pf=0.544 n=121498 gates=FAIL

## [INFO] 2026-08-03 10:36:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.95943 skill_surrogate=-0.95943

## [INFO] 2026-08-03 10:36:58 UTC (tier 0)

trial `d85c9d39-7d25-4d0c-8622-af7c3ff113f3` model=lgbm_classifier tier=0 target=xs_rank pf=0.555 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:36:58 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_077_ETHUSDT_15m_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:36:58 UTC (tier 0)

AUTONOMY screen autog2_077_ETHUSDT_15m_xs_rank_ohlcv_v1 tier=0 proxy_pf=0.5551435152352238 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:36:58 UTC (tier 0)

START gen=autog2_078_SOLUSDT_15m_xs_rank_xs_v1 SOLUSDT 15m target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:37:22 UTC (tier 0)

PREDICTABILITY real=+0.00092 p=0.0476 surr_q95=+0.00039 surr_max=+0.00055 draws=20 passed=True

## [INFO] 2026-08-03 10:37:26 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:37:26 UTC (tier 0)

trial `d434c950-fddf-43e6-bd3c-90e5e52121e5` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:37:26 UTC (tier 1)

trial `0001c3be-ec15-4407-92fc-f43fb2ff3c84` model=ridge tier=1 target=xs_rank pf=0.693 n=44219 gates=FAIL

## [INFO] 2026-08-03 10:37:29 UTC (tier 1)

trial `51fcd30c-d6eb-48da-b969-1a2a31a956f0` model=lgbm_regressor tier=1 target=xs_rank pf=0.697 n=40267 gates=FAIL

## [INFO] 2026-08-03 10:37:30 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.76759 skill_surrogate=-0.76759

## [INFO] 2026-08-03 10:37:30 UTC (tier 0)

trial `3b22c6d7-2909-4a81-adf6-6966bd1d75a2` model=lgbm_classifier tier=0 target=xs_rank pf=0.692 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:37:30 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_078_SOLUSDT_15m_xs_rank_xs_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:37:30 UTC (tier 1)

AUTONOMY screen autog2_078_SOLUSDT_15m_xs_rank_xs_v1 tier=1 proxy_pf=0.6967328951023124 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:37:30 UTC (tier 0)

START gen=autog2_078_SOLUSDT_15m_xs_rank_xs_v1_ts SOLUSDT 15m target=xs_rank space=xs_v1

## [INFO] 2026-08-03 10:37:56 UTC (tier 0)

PREDICTABILITY real=+0.00092 p=0.0476 surr_q95=+0.00039 surr_max=+0.00055 draws=20 passed=True

## [INFO] 2026-08-03 10:38:11 UTC (tier 1)

trial `d802e9e9-0a29-4a63-8566-edebbae9fa1c` model=lgbm_regressor tier=1 target=xs_rank pf=0.762 n=7719 gates=FAIL

## [INFO] 2026-08-03 10:38:11 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_078_SOLUSDT_15m_xs_rank_xs_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:38:11 UTC (tier 1)

AUTONOMY tradesim autog2_078_SOLUSDT_15m_xs_rank_xs_v1 tier=1 proxy_pf=0.761552343127849

## [INFO] 2026-08-03 10:38:11 UTC (tier 0)

START gen=autog2_079_SOLUSDT_15m_xs_rank_crosspair_v1 SOLUSDT 15m target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:38:30 UTC (tier 0)

PREDICTABILITY real=+0.00131 p=0.0476 surr_q95=+0.00012 surr_max=+0.00032 draws=20 passed=True

## [INFO] 2026-08-03 10:38:33 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:38:33 UTC (tier 0)

trial `e1650ae9-2cdf-459e-869c-96ef45e75007` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:38:33 UTC (tier 1)

trial `bc563b5f-01f6-461a-bf60-47cc213be815` model=ridge tier=1 target=xs_rank pf=0.718 n=26686 gates=FAIL

## [INFO] 2026-08-03 10:38:36 UTC (tier 1)

trial `6c782979-0c47-47b9-b27d-a290400a476a` model=lgbm_regressor tier=1 target=xs_rank pf=0.738 n=32429 gates=FAIL

## [INFO] 2026-08-03 10:38:37 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.76759 skill_surrogate=-0.76759

## [INFO] 2026-08-03 10:38:37 UTC (tier 0)

trial `68f26713-48b5-43e2-848a-7f1658f2dfa7` model=lgbm_classifier tier=0 target=xs_rank pf=0.692 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:38:37 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_079_SOLUSDT_15m_xs_rank_crosspair_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:38:37 UTC (tier 1)

AUTONOMY screen autog2_079_SOLUSDT_15m_xs_rank_crosspair_v1 tier=1 proxy_pf=0.7376375064539358 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:38:37 UTC (tier 0)

START gen=autog2_079_SOLUSDT_15m_xs_rank_crosspair_v1_ts SOLUSDT 15m target=xs_rank space=crosspair_v1

## [INFO] 2026-08-03 10:39:04 UTC (tier 0)

PREDICTABILITY real=+0.00131 p=0.0476 surr_q95=+0.00012 surr_max=+0.00032 draws=20 passed=True

## [INFO] 2026-08-03 10:39:16 UTC (tier 1)

trial `0100c288-ef0e-4614-b03b-1f3fb9128d58` model=lgbm_regressor tier=1 target=xs_rank pf=0.756 n=7707 gates=FAIL

## [INFO] 2026-08-03 10:39:16 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_079_SOLUSDT_15m_xs_rank_crosspair_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:39:16 UTC (tier 1)

AUTONOMY tradesim autog2_079_SOLUSDT_15m_xs_rank_crosspair_v1 tier=1 proxy_pf=0.7563555122194853

## [INFO] 2026-08-03 10:39:16 UTC (tier 0)

START gen=autog2_080_SOLUSDT_15m_xs_rank_ohlcv_v1 SOLUSDT 15m target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:40:03 UTC (tier 0)

PREDICTABILITY real=+0.00248 p=0.0476 surr_q95=-0.00002 surr_max=+0.00004 draws=20 passed=True

## [INFO] 2026-08-03 10:40:05 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:40:05 UTC (tier 0)

trial `b642d98e-3e2c-49f0-91f4-3cfd65a5e948` model=hist_mean tier=0 target=xs_rank pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:40:06 UTC (tier 1)

trial `72337374-269c-4b6c-97b5-a4e461d6672d` model=ridge tier=1 target=xs_rank pf=0.740 n=35043 gates=FAIL

## [INFO] 2026-08-03 10:40:10 UTC (tier 1)

trial `f05dfd63-0d8c-4179-82f4-c35ba1fe5aaa` model=lgbm_regressor tier=1 target=xs_rank pf=0.705 n=46551 gates=FAIL

## [INFO] 2026-08-03 10:40:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.76759 skill_surrogate=-0.76759

## [INFO] 2026-08-03 10:40:12 UTC (tier 0)

trial `80c8e735-95e2-4512-8a06-186faf16faef` model=lgbm_classifier tier=0 target=xs_rank pf=0.692 n=131421 gates=FAIL

## [INFO] 2026-08-03 10:40:12 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_080_SOLUSDT_15m_xs_rank_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:40:12 UTC (tier 1)

AUTONOMY screen autog2_080_SOLUSDT_15m_xs_rank_ohlcv_v1 tier=1 proxy_pf=0.7400009358868682 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:40:12 UTC (tier 0)

START gen=autog2_080_SOLUSDT_15m_xs_rank_ohlcv_v1_ts SOLUSDT 15m target=xs_rank space=ohlcv_v1

## [INFO] 2026-08-03 10:40:48 UTC (tier 0)

PREDICTABILITY real=+0.00248 p=0.0476 surr_q95=-0.00002 surr_max=+0.00004 draws=20 passed=True

## [INFO] 2026-08-03 10:40:56 UTC (tier 1)

trial `495658e3-68e5-4199-8c1c-74afa579594b` model=ridge tier=1 target=xs_rank pf=0.739 n=7091 gates=FAIL

## [INFO] 2026-08-03 10:40:56 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_080_SOLUSDT_15m_xs_rank_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:40:56 UTC (tier 1)

AUTONOMY tradesim autog2_080_SOLUSDT_15m_xs_rank_ohlcv_v1 tier=1 proxy_pf=0.7386369196635777

## [INFO] 2026-08-03 10:40:56 UTC (tier 0)

START gen=autog2_081_BTCUSDT_1h_quantile_ohlcv_v1 BTCUSDT 1h target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:41:06 UTC (tier 0)

PREDICTABILITY real=-0.01659 p=1.0000 surr_q95=-0.00002 surr_max=+0.00034 draws=20 passed=False

## [INFO] 2026-08-03 10:41:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:41:08 UTC (tier 0)

trial `ade3ac82-37a8-435c-a2d3-a215b310ef53` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:41:08 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00806 skill_surrogate=+0.00208

## [INFO] 2026-08-03 10:41:08 UTC (tier 0)

trial `0fcebb78-98dc-478d-ad63-c15c3e9ec967` model=ridge tier=0 target=quantile pf=0.824 n=6802 gates=FAIL

## [INFO] 2026-08-03 10:41:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01158 skill_surrogate=-0.00797

## [INFO] 2026-08-03 10:41:10 UTC (tier 0)

trial `1621ce28-edf7-471e-9a72-3e9f6ad31b93` model=lgbm_regressor tier=0 target=quantile pf=0.769 n=4203 gates=FAIL

## [INFO] 2026-08-03 10:41:15 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.88126 skill_surrogate=-5.16850

## [INFO] 2026-08-03 10:41:15 UTC (tier 0)

trial `b0898da0-8dfd-4615-aa4e-5fa376486ae0` model=lgbm_classifier tier=0 target=quantile pf=0.713 n=32726 gates=FAIL

## [INFO] 2026-08-03 10:41:15 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_081_BTCUSDT_1h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:41:15 UTC (tier 0)

AUTONOMY screen autog2_081_BTCUSDT_1h_quantile_ohlcv_v1 tier=0 proxy_pf=0.8241790932610158 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:41:15 UTC (tier 0)

START gen=autog2_082_BTCUSDT_1h_quantile_indicators_v1 BTCUSDT 1h target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:41:25 UTC (tier 0)

PREDICTABILITY real=-0.01816 p=1.0000 surr_q95=-0.00047 surr_max=-0.00008 draws=20 passed=False

## [INFO] 2026-08-03 10:41:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:41:27 UTC (tier 0)

trial `35131904-1656-4990-89e8-e7e6ed89d3ce` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:41:27 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.03431 skill_surrogate=-0.00150

## [INFO] 2026-08-03 10:41:27 UTC (tier 0)

trial `36e82c15-a3d1-4b2d-8acf-64264689c89f` model=ridge tier=0 target=quantile pf=0.802 n=14771 gates=FAIL

## [INFO] 2026-08-03 10:41:29 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01395 skill_surrogate=-0.02015

## [INFO] 2026-08-03 10:41:29 UTC (tier 0)

trial `52f6f2b9-9b9e-4236-9dc2-6555d5c66849` model=lgbm_regressor tier=0 target=quantile pf=0.729 n=12986 gates=FAIL

## [INFO] 2026-08-03 10:41:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-134.00153 skill_surrogate=-5.99580

## [INFO] 2026-08-03 10:41:34 UTC (tier 0)

trial `8794b8f6-be8c-43d1-8e1f-aa82b3f60b60` model=lgbm_classifier tier=0 target=quantile pf=0.690 n=32709 gates=FAIL

## [INFO] 2026-08-03 10:41:34 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_082_BTCUSDT_1h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:41:34 UTC (tier 0)

AUTONOMY screen autog2_082_BTCUSDT_1h_quantile_indicators_v1 tier=0 proxy_pf=0.8019564394607935 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:41:34 UTC (tier 0)

START gen=autog2_083_BTCUSDT_1h_quantile_pivot_v1 BTCUSDT 1h target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:41:40 UTC (tier 0)

PREDICTABILITY real=-0.00261 p=0.7619 surr_q95=+0.00125 surr_max=+0.00230 draws=20 passed=False

## [INFO] 2026-08-03 10:41:41 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:41:41 UTC (tier 0)

trial `afef4a53-8d6f-405c-8d6f-e84515ba4a55` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:41:41 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00596 skill_surrogate=-0.00093

## [INFO] 2026-08-03 10:41:41 UTC (tier 0)

trial `4130bdf5-f43a-4e12-b144-779bba3df293` model=ridge tier=0 target=quantile pf=0.782 n=2380 gates=FAIL

## [INFO] 2026-08-03 10:41:42 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02190 skill_surrogate=-0.00929

## [INFO] 2026-08-03 10:41:43 UTC (tier 0)

trial `103f1439-b54a-493f-80dd-d936d5ca0b58` model=lgbm_regressor tier=0 target=quantile pf=0.730 n=7895 gates=FAIL

## [INFO] 2026-08-03 10:41:46 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.89018 skill_surrogate=-5.26027

## [INFO] 2026-08-03 10:41:46 UTC (tier 0)

trial `ef748ec2-b53f-4a4a-9156-2436b6549c95` model=lgbm_classifier tier=0 target=quantile pf=0.713 n=32840 gates=FAIL

## [INFO] 2026-08-03 10:41:46 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_083_BTCUSDT_1h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:41:46 UTC (tier 0)

AUTONOMY screen autog2_083_BTCUSDT_1h_quantile_pivot_v1 tier=0 proxy_pf=0.7815190217194922 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:41:46 UTC (tier 0)

START gen=autog2_084_ETHUSDT_1h_quantile_ohlcv_v1 ETHUSDT 1h target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:41:55 UTC (tier 0)

PREDICTABILITY real=-0.00340 p=0.7143 surr_q95=-0.00016 surr_max=+0.00009 draws=20 passed=False

## [INFO] 2026-08-03 10:41:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:41:57 UTC (tier 0)

trial `388668ee-138e-4781-91a0-262dbf8e2381` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:41:57 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00388 skill_surrogate=-0.00120

## [INFO] 2026-08-03 10:41:57 UTC (tier 0)

trial `7e7bb10a-3c58-4014-8772-0c57e76d0e5d` model=ridge tier=0 target=quantile pf=0.836 n=11451 gates=FAIL

## [INFO] 2026-08-03 10:41:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00683 skill_surrogate=-0.00393

## [INFO] 2026-08-03 10:41:59 UTC (tier 0)

trial `45845481-2471-4758-a679-139c690c54d3` model=lgbm_regressor tier=0 target=quantile pf=0.898 n=7192 gates=FAIL

## [INFO] 2026-08-03 10:42:04 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.69690 skill_surrogate=-2.37310

## [INFO] 2026-08-03 10:42:04 UTC (tier 0)

trial `4271a5e4-e9b0-4550-803d-a8d91e4937a1` model=lgbm_classifier tier=0 target=quantile pf=0.754 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:42:04 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_084_ETHUSDT_1h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:42:04 UTC (tier 0)

AUTONOMY screen autog2_084_ETHUSDT_1h_quantile_ohlcv_v1 tier=0 proxy_pf=0.8983023017364945 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:42:04 UTC (tier 0)

START gen=autog2_085_ETHUSDT_1h_quantile_indicators_v1 ETHUSDT 1h target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:42:15 UTC (tier 0)

PREDICTABILITY real=-0.00963 p=0.8571 surr_q95=-0.00028 surr_max=+0.00103 draws=20 passed=False

## [INFO] 2026-08-03 10:42:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:42:16 UTC (tier 0)

trial `b45cc055-e0ba-43a6-b40b-cfc7ac6c7cd3` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:42:16 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00937 skill_surrogate=+0.00069

## [INFO] 2026-08-03 10:42:16 UTC (tier 0)

trial `dbbbdac2-134b-45a3-94fb-4a7ded7664ed` model=ridge tier=0 target=quantile pf=0.906 n=15512 gates=FAIL

## [INFO] 2026-08-03 10:42:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04618 skill_surrogate=-0.00491

## [INFO] 2026-08-03 10:42:18 UTC (tier 0)

trial `7e5a833d-e03c-460a-a90f-35ad9f8774e0` model=lgbm_regressor tier=0 target=quantile pf=0.844 n=19181 gates=FAIL

## [INFO] 2026-08-03 10:42:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.69431 skill_surrogate=-2.80776

## [INFO] 2026-08-03 10:42:23 UTC (tier 0)

trial `e378d9bb-b73a-44b2-9c27-849e4547ce6d` model=lgbm_classifier tier=0 target=quantile pf=0.727 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:42:23 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_085_ETHUSDT_1h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:42:23 UTC (tier 0)

AUTONOMY screen autog2_085_ETHUSDT_1h_quantile_indicators_v1 tier=0 proxy_pf=0.906214041880571 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:42:23 UTC (tier 0)

START gen=autog2_086_ETHUSDT_1h_quantile_pivot_v1 ETHUSDT 1h target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:42:29 UTC (tier 0)

PREDICTABILITY real=-0.00464 p=0.9524 surr_q95=+0.00101 surr_max=+0.00180 draws=20 passed=False

## [INFO] 2026-08-03 10:42:30 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:42:30 UTC (tier 0)

trial `3da25249-057c-4d8e-b3c0-edb0254d26e9` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:42:30 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00410 skill_surrogate=-0.00087

## [INFO] 2026-08-03 10:42:30 UTC (tier 0)

trial `dc304ce8-5437-4780-9614-f419f2326f8c` model=ridge tier=0 target=quantile pf=0.732 n=4466 gates=FAIL

## [INFO] 2026-08-03 10:42:31 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01122 skill_surrogate=-0.00488

## [INFO] 2026-08-03 10:42:31 UTC (tier 0)

trial `98ade9f2-8996-4dc5-bf42-0e18eb86e26b` model=lgbm_regressor tier=0 target=quantile pf=0.804 n=10953 gates=FAIL

## [INFO] 2026-08-03 10:42:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.71388 skill_surrogate=-2.33615

## [INFO] 2026-08-03 10:42:35 UTC (tier 0)

trial `26114654-27df-4624-b7db-820c88df2666` model=lgbm_classifier tier=0 target=quantile pf=0.748 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:42:35 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_086_ETHUSDT_1h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:42:35 UTC (tier 0)

AUTONOMY screen autog2_086_ETHUSDT_1h_quantile_pivot_v1 tier=0 proxy_pf=0.8044483162827601 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:42:35 UTC (tier 0)

START gen=autog2_087_SOLUSDT_1h_quantile_ohlcv_v1 SOLUSDT 1h target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:42:45 UTC (tier 0)

PREDICTABILITY real=-0.00647 p=1.0000 surr_q95=+0.00024 surr_max=+0.00228 draws=20 passed=False

## [INFO] 2026-08-03 10:42:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:42:46 UTC (tier 0)

trial `7452fe12-6c3f-4165-b397-0cbf614018b2` model=hist_mean tier=0 target=quantile pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-03 10:42:46 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00462 skill_surrogate=+0.00053

## [INFO] 2026-08-03 10:42:46 UTC (tier 0)

trial `cc62a6d3-c236-4e49-8ed5-a70684d54dd0` model=ridge tier=0 target=quantile pf=0.902 n=17004 gates=FAIL

## [INFO] 2026-08-03 10:42:48 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01179 skill_surrogate=-0.00431

## [INFO] 2026-08-03 10:42:48 UTC (tier 0)

trial `cdcece41-4fa4-4b90-8e50-616bdc4791a0` model=lgbm_regressor tier=0 target=quantile pf=0.846 n=12027 gates=FAIL

## [INFO] 2026-08-03 10:42:52 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.08167 skill_surrogate=-1.53531

## [INFO] 2026-08-03 10:42:52 UTC (tier 0)

trial `aff80020-a361-45c0-af17-215b7781b7d9` model=lgbm_classifier tier=0 target=quantile pf=0.874 n=32854 gates=FAIL

## [INFO] 2026-08-03 10:42:52 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_087_SOLUSDT_1h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:42:52 UTC (tier 0)

AUTONOMY screen autog2_087_SOLUSDT_1h_quantile_ohlcv_v1 tier=0 proxy_pf=0.9022273781710141 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:42:52 UTC (tier 0)

START gen=autog2_088_SOLUSDT_1h_quantile_indicators_v1 SOLUSDT 1h target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:43:02 UTC (tier 0)

PREDICTABILITY real=+0.00280 p=0.0952 surr_q95=-0.00028 surr_max=+0.00334 draws=20 passed=False

## [INFO] 2026-08-03 10:43:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:43:04 UTC (tier 0)

trial `4f047abb-64d9-425f-a3d1-a4f3bdd1b04f` model=hist_mean tier=0 target=quantile pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-03 10:43:04 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01219 skill_surrogate=-0.00289

## [INFO] 2026-08-03 10:43:04 UTC (tier 0)

trial `bf3a6f15-72e9-4d27-9499-db0eff4bf1f5` model=ridge tier=0 target=quantile pf=0.884 n=22651 gates=FAIL

## [INFO] 2026-08-03 10:43:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01149 skill_surrogate=-0.00429

## [INFO] 2026-08-03 10:43:06 UTC (tier 0)

trial `80fed4a2-e1b7-44b2-bb26-61785d0bda69` model=lgbm_regressor tier=0 target=quantile pf=0.958 n=15633 gates=FAIL

## [INFO] 2026-08-03 10:43:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.05580 skill_surrogate=-1.93033

## [INFO] 2026-08-03 10:43:10 UTC (tier 0)

trial `4e4adce1-2a36-4d10-9ff1-c51c50ad25b3` model=lgbm_classifier tier=0 target=quantile pf=0.860 n=32699 gates=FAIL

## [INFO] 2026-08-03 10:43:10 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_088_SOLUSDT_1h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:43:10 UTC (tier 0)

AUTONOMY screen autog2_088_SOLUSDT_1h_quantile_indicators_v1 tier=0 proxy_pf=0.958342346586077 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:43:10 UTC (tier 0)

START gen=autog2_089_SOLUSDT_1h_quantile_pivot_v1 SOLUSDT 1h target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:43:15 UTC (tier 0)

PREDICTABILITY real=-0.00184 p=0.7619 surr_q95=+0.00017 surr_max=+0.00126 draws=20 passed=False

## [INFO] 2026-08-03 10:43:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:43:16 UTC (tier 0)

trial `f8e854ff-fa3f-49ee-ae45-bffe90d846e6` model=hist_mean tier=0 target=quantile pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-03 10:43:16 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00186 skill_surrogate=-0.00048

## [INFO] 2026-08-03 10:43:17 UTC (tier 0)

trial `a105e3b0-d080-4dca-84b0-f1c54575db74` model=ridge tier=0 target=quantile pf=0.745 n=8221 gates=FAIL

## [INFO] 2026-08-03 10:43:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01905 skill_surrogate=-0.00702

## [INFO] 2026-08-03 10:43:18 UTC (tier 0)

trial `fabee8da-641e-4579-aab8-ecbcbee86c4f` model=lgbm_regressor tier=0 target=quantile pf=0.890 n=17033 gates=FAIL

## [INFO] 2026-08-03 10:43:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.08766 skill_surrogate=-1.57613

## [INFO] 2026-08-03 10:43:21 UTC (tier 0)

trial `520c1d09-e3ef-48fb-9c01-e47a91399c99` model=lgbm_classifier tier=0 target=quantile pf=0.840 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:43:21 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_089_SOLUSDT_1h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:43:21 UTC (tier 0)

AUTONOMY screen autog2_089_SOLUSDT_1h_quantile_pivot_v1 tier=0 proxy_pf=0.8901217750441386 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:43:21 UTC (tier 0)

START gen=autog2_090_BTCUSDT_4h_quantile_ohlcv_v1 BTCUSDT 4h target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:43:26 UTC (tier 0)

PREDICTABILITY real=-0.00524 p=0.6190 surr_q95=+0.00150 surr_max=+0.00420 draws=20 passed=False

## [INFO] 2026-08-03 10:43:26 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:43:26 UTC (tier 0)

trial `129f06df-c1bc-4dcb-bf14-44c2453ee7a7` model=hist_mean tier=0 target=quantile pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-03 10:43:26 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00342 skill_surrogate=-0.00882

## [INFO] 2026-08-03 10:43:26 UTC (tier 0)

trial `5f1021af-31c0-438f-be27-a5e372316bae` model=ridge tier=0 target=quantile pf=1.018 n=5223 gates=FAIL

## [INFO] 2026-08-03 10:43:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04444 skill_surrogate=-0.02884

## [INFO] 2026-08-03 10:43:27 UTC (tier 0)

trial `9b20fcb3-3cdd-41e2-9951-59f8da214c4e` model=lgbm_regressor tier=0 target=quantile pf=0.864 n=5565 gates=FAIL

## [INFO] 2026-08-03 10:43:31 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.22449 skill_surrogate=-4.36823

## [INFO] 2026-08-03 10:43:31 UTC (tier 0)

trial `474958f8-757c-4c0f-90ad-c09f8e3d3ef3` model=lgbm_classifier tier=0 target=quantile pf=0.834 n=8204 gates=FAIL

## [INFO] 2026-08-03 10:43:31 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_090_BTCUSDT_4h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:43:31 UTC (tier 0)

AUTONOMY screen autog2_090_BTCUSDT_4h_quantile_ohlcv_v1 tier=0 proxy_pf=1.0176857259100298 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:43:31 UTC (tier 0)

START gen=autog2_091_BTCUSDT_4h_quantile_indicators_v1 BTCUSDT 4h target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:43:35 UTC (tier 0)

PREDICTABILITY real=-0.05673 p=0.9524 surr_q95=-0.00099 surr_max=+0.00098 draws=20 passed=False

## [INFO] 2026-08-03 10:43:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:43:36 UTC (tier 0)

trial `3181d7ed-d07a-487e-b8fd-ec513454b7e0` model=hist_mean tier=0 target=quantile pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-03 10:43:36 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.04064 skill_surrogate=-0.00925

## [INFO] 2026-08-03 10:43:36 UTC (tier 0)

trial `935dfa5a-bc65-41a6-a7b3-c7443486211d` model=ridge tier=0 target=quantile pf=0.827 n=6439 gates=FAIL

## [INFO] 2026-08-03 10:43:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.05483 skill_surrogate=-0.04181

## [INFO] 2026-08-03 10:43:38 UTC (tier 0)

trial `de5a4b9a-8b40-4697-aa75-878ce5d1f7d1` model=lgbm_regressor tier=0 target=quantile pf=0.800 n=7028 gates=FAIL

## [INFO] 2026-08-03 10:43:41 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16491 skill_surrogate=-6.95168

## [INFO] 2026-08-03 10:43:41 UTC (tier 0)

trial `41194349-89b0-44f9-b500-9d4ed8291566` model=lgbm_classifier tier=0 target=quantile pf=0.817 n=8213 gates=FAIL

## [INFO] 2026-08-03 10:43:41 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_091_BTCUSDT_4h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:43:41 UTC (tier 0)

AUTONOMY screen autog2_091_BTCUSDT_4h_quantile_indicators_v1 tier=0 proxy_pf=0.8266177086033331 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:43:41 UTC (tier 0)

START gen=autog2_092_BTCUSDT_4h_quantile_pivot_v1 BTCUSDT 4h target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:43:43 UTC (tier 0)

PREDICTABILITY real=-0.00099 p=0.3333 surr_q95=+0.00322 surr_max=+0.00343 draws=20 passed=False

## [INFO] 2026-08-03 10:43:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:43:44 UTC (tier 0)

trial `2ed02234-9e41-46d5-8a10-0c29884022f7` model=hist_mean tier=0 target=quantile pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-03 10:43:44 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00530 skill_surrogate=+0.00020

## [INFO] 2026-08-03 10:43:44 UTC (tier 0)

trial `c6e375dd-16a8-407c-9e3f-86eed5f665b6` model=ridge tier=0 target=quantile pf=0.842 n=2815 gates=FAIL

## [INFO] 2026-08-03 10:43:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03841 skill_surrogate=-0.00734

## [INFO] 2026-08-03 10:43:45 UTC (tier 0)

trial `1d6dd2ee-da4a-427e-adee-560ea8ab78c7` model=lgbm_regressor tier=0 target=quantile pf=0.842 n=5743 gates=FAIL

## [INFO] 2026-08-03 10:43:47 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16893 skill_surrogate=-4.75857

## [INFO] 2026-08-03 10:43:47 UTC (tier 0)

trial `1e7613da-02f4-43fc-a8a1-e5b7266493fe` model=lgbm_classifier tier=0 target=quantile pf=0.846 n=8210 gates=FAIL

## [INFO] 2026-08-03 10:43:47 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_092_BTCUSDT_4h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:43:47 UTC (tier 0)

AUTONOMY screen autog2_092_BTCUSDT_4h_quantile_pivot_v1 tier=0 proxy_pf=0.8464266512174518 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:43:47 UTC (tier 0)

START gen=autog2_093_ETHUSDT_4h_quantile_ohlcv_v1 ETHUSDT 4h target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:43:51 UTC (tier 0)

PREDICTABILITY real=-0.00991 p=0.6190 surr_q95=+0.00728 surr_max=+0.00810 draws=20 passed=False

## [INFO] 2026-08-03 10:43:52 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:43:52 UTC (tier 0)

trial `608602da-c7fe-4c65-9bd8-f3ebfdc5b87a` model=hist_mean tier=0 target=quantile pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:43:52 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00136 skill_surrogate=-0.00007

## [INFO] 2026-08-03 10:43:52 UTC (tier 0)

trial `5dc9deed-18f0-443f-9d26-dd84e761c9e1` model=ridge tier=0 target=quantile pf=0.946 n=6072 gates=FAIL

## [INFO] 2026-08-03 10:43:53 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02168 skill_surrogate=-0.00761

## [INFO] 2026-08-03 10:43:53 UTC (tier 0)

trial `fe881ae1-59e3-49f2-8a88-bf1d8a5923d0` model=lgbm_regressor tier=0 target=quantile pf=0.930 n=6253 gates=FAIL

## [INFO] 2026-08-03 10:43:56 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.11179 skill_surrogate=-2.38091

## [INFO] 2026-08-03 10:43:56 UTC (tier 0)

trial `fe98c156-e367-4c5e-9570-cc0160286f23` model=lgbm_classifier tier=0 target=quantile pf=0.903 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:43:56 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_093_ETHUSDT_4h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:43:56 UTC (tier 0)

AUTONOMY screen autog2_093_ETHUSDT_4h_quantile_ohlcv_v1 tier=0 proxy_pf=0.9460121773106233 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:43:57 UTC (tier 0)

START gen=autog2_094_ETHUSDT_4h_quantile_indicators_v1 ETHUSDT 4h target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:44:01 UTC (tier 0)

PREDICTABILITY real=-0.07290 p=1.0000 surr_q95=-0.00201 surr_max=-0.00128 draws=20 passed=False

## [INFO] 2026-08-03 10:44:01 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:44:01 UTC (tier 0)

trial `cc4ec973-5d88-4232-86c7-8fd9094da727` model=hist_mean tier=0 target=quantile pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:01 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00167 skill_surrogate=-0.00523

## [INFO] 2026-08-03 10:44:01 UTC (tier 0)

trial `a01e10c6-a23b-4369-a4fe-0b1402f3210d` model=ridge tier=0 target=quantile pf=0.888 n=6885 gates=FAIL

## [INFO] 2026-08-03 10:44:03 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03816 skill_surrogate=-0.01158

## [INFO] 2026-08-03 10:44:03 UTC (tier 0)

trial `ca2734c2-59a0-44c2-8bf9-4f17459d4fb1` model=lgbm_regressor tier=0 target=quantile pf=0.918 n=7147 gates=FAIL

## [INFO] 2026-08-03 10:44:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.01013 skill_surrogate=-2.65853

## [INFO] 2026-08-03 10:44:06 UTC (tier 0)

trial `37e1c9ae-1b8a-44ed-8990-0559ac6285aa` model=lgbm_classifier tier=0 target=quantile pf=0.915 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:06 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_094_ETHUSDT_4h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:44:06 UTC (tier 0)

AUTONOMY screen autog2_094_ETHUSDT_4h_quantile_indicators_v1 tier=0 proxy_pf=0.9200856060065038 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:44:06 UTC (tier 0)

START gen=autog2_095_ETHUSDT_4h_quantile_pivot_v1 ETHUSDT 4h target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:44:08 UTC (tier 0)

PREDICTABILITY real=-0.00131 p=0.4286 surr_q95=+0.00145 surr_max=+0.00277 draws=20 passed=False

## [INFO] 2026-08-03 10:44:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:44:09 UTC (tier 0)

trial `71c3d579-5a43-4a3f-bc2b-465169c266bc` model=hist_mean tier=0 target=quantile pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:09 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00295 skill_surrogate=+0.00031

## [INFO] 2026-08-03 10:44:09 UTC (tier 0)

trial `330c4091-a370-4c73-aeb6-fda356302fac` model=ridge tier=0 target=quantile pf=0.951 n=6014 gates=FAIL

## [INFO] 2026-08-03 10:44:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01431 skill_surrogate=-0.01088

## [INFO] 2026-08-03 10:44:10 UTC (tier 0)

trial `9a935e2a-5bd2-4f13-966f-ed51423c5c49` model=lgbm_regressor tier=0 target=quantile pf=0.930 n=6824 gates=FAIL

## [INFO] 2026-08-03 10:44:13 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.01322 skill_surrogate=-2.68694

## [INFO] 2026-08-03 10:44:13 UTC (tier 0)

trial `8cb27efa-b764-44dd-a29b-040867f115f6` model=lgbm_classifier tier=0 target=quantile pf=0.905 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:13 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_095_ETHUSDT_4h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:44:13 UTC (tier 0)

AUTONOMY screen autog2_095_ETHUSDT_4h_quantile_pivot_v1 tier=0 proxy_pf=0.9510175596610267 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:44:13 UTC (tier 0)

START gen=autog2_096_SOLUSDT_4h_quantile_ohlcv_v1 SOLUSDT 4h target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:44:16 UTC (tier 0)

PREDICTABILITY real=-0.02437 p=1.0000 surr_q95=+0.00219 surr_max=+0.00222 draws=20 passed=False

## [INFO] 2026-08-03 10:44:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:44:17 UTC (tier 0)

trial `abc0dfaf-2c7c-4a2b-9308-15df2777e423` model=hist_mean tier=0 target=quantile pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:17 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01743 skill_surrogate=-0.00753

## [INFO] 2026-08-03 10:44:17 UTC (tier 0)

trial `73293b2a-934b-4078-ba80-fec99769ba52` model=ridge tier=0 target=quantile pf=0.997 n=7292 gates=FAIL

## [INFO] 2026-08-03 10:44:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02577 skill_surrogate=-0.02091

## [INFO] 2026-08-03 10:44:18 UTC (tier 0)

trial `42877b3f-e086-4294-9322-6728da7a1fc2` model=lgbm_regressor tier=0 target=quantile pf=0.958 n=7161 gates=FAIL

## [INFO] 2026-08-03 10:44:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.52165 skill_surrogate=-1.47638

## [INFO] 2026-08-03 10:44:21 UTC (tier 0)

trial `37c1914f-2159-428a-8ad5-48f4c7d6c0e2` model=lgbm_classifier tier=0 target=quantile pf=0.989 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:21 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_096_SOLUSDT_4h_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:44:21 UTC (tier 0)

AUTONOMY screen autog2_096_SOLUSDT_4h_quantile_ohlcv_v1 tier=0 proxy_pf=0.9965702191452582 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:44:21 UTC (tier 0)

START gen=autog2_097_SOLUSDT_4h_quantile_indicators_v1 SOLUSDT 4h target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:44:26 UTC (tier 0)

PREDICTABILITY real=-0.01378 p=0.2857 surr_q95=-0.00313 surr_max=-0.00192 draws=20 passed=False

## [INFO] 2026-08-03 10:44:26 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 10:44:26 UTC (tier 0)

trial `aab2fb75-ff46-431e-a153-5e56d0a1daa8` model=hist_mean tier=0 target=quantile pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:26 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00250 skill_surrogate=-0.01403

## [INFO] 2026-08-03 10:44:26 UTC (tier 0)

trial `a2597781-10ae-4cd7-99c7-ee6ce3e5a19f` model=ridge tier=0 target=quantile pf=1.042 n=7405 gates=FAIL

## [INFO] 2026-08-03 10:44:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01843 skill_surrogate=-0.01847

## [INFO] 2026-08-03 10:44:28 UTC (tier 0)

trial `90cffbb3-f8c0-4012-afa9-bb5727bd9722` model=lgbm_regressor tier=0 target=quantile pf=0.951 n=7318 gates=FAIL

## [INFO] 2026-08-03 10:44:31 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.44360 skill_surrogate=-2.74855

## [INFO] 2026-08-03 10:44:31 UTC (tier 0)

trial `e947cbd7-18f3-44aa-ad0b-d1e64adda94b` model=lgbm_classifier tier=0 target=quantile pf=0.918 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:31 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_097_SOLUSDT_4h_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:44:31 UTC (tier 0)

AUTONOMY screen autog2_097_SOLUSDT_4h_quantile_indicators_v1 tier=0 proxy_pf=1.0422191080060303 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:44:31 UTC (tier 0)

START gen=autog2_098_SOLUSDT_4h_quantile_pivot_v1 SOLUSDT 4h target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:44:34 UTC (tier 0)

PREDICTABILITY real=-0.01625 p=0.8095 surr_q95=+0.00091 surr_max=+0.00122 draws=20 passed=False

## [INFO] 2026-08-03 10:44:35 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:44:35 UTC (tier 0)

trial `31861c51-7e68-4cbc-8d42-cfe1053126c8` model=hist_mean tier=0 target=quantile pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:35 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00757 skill_surrogate=-0.00052

## [INFO] 2026-08-03 10:44:35 UTC (tier 0)

trial `83ac19fb-33b7-4e7f-b457-c613e3f65cb7` model=ridge tier=0 target=quantile pf=0.975 n=6843 gates=FAIL

## [INFO] 2026-08-03 10:44:36 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04768 skill_surrogate=-0.01214

## [INFO] 2026-08-03 10:44:36 UTC (tier 0)

trial `87adc56e-c035-4edd-a9c7-0284e9bc4f1c` model=lgbm_regressor tier=0 target=quantile pf=0.987 n=7360 gates=FAIL

## [INFO] 2026-08-03 10:44:41 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.44952 skill_surrogate=-2.25744

## [INFO] 2026-08-03 10:44:41 UTC (tier 0)

trial `7f8d6fb7-87b4-491b-9380-b70ca0eeac8d` model=lgbm_classifier tier=0 target=quantile pf=0.921 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:44:41 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_098_SOLUSDT_4h_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:44:41 UTC (tier 0)

AUTONOMY screen autog2_098_SOLUSDT_4h_quantile_pivot_v1 tier=0 proxy_pf=0.9868588821857988 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:44:41 UTC (tier 0)

START gen=autog2_099_BTCUSDT_15m_quantile_ohlcv_v1 BTCUSDT 15m target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:45:20 UTC (tier 0)

PREDICTABILITY real=-0.00358 p=1.0000 surr_q95=+0.00021 surr_max=+0.00023 draws=20 passed=False

## [INFO] 2026-08-03 10:45:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:45:27 UTC (tier 0)

trial `5a4aee37-f92a-4122-99cc-623554ed6a37` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:45:28 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00863 skill_surrogate=+0.00078

## [INFO] 2026-08-03 10:45:28 UTC (tier 0)

trial `cadb25e8-cc82-4b9a-b3ec-ed7259af9bcd` model=ridge tier=0 target=quantile pf=1.045 n=790 gates=FAIL

## [INFO] 2026-08-03 10:45:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00290 skill_surrogate=-0.00196

## [INFO] 2026-08-03 10:45:32 UTC (tier 0)

trial `6c0aa16c-819b-4823-a7a4-da02d352c36b` model=lgbm_regressor tier=0 target=quantile pf=0.810 n=2069 gates=FAIL

## [INFO] 2026-08-03 10:45:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-278.14698 skill_surrogate=-5.70952

## [INFO] 2026-08-03 10:45:44 UTC (tier 0)

trial `af8dbd75-a48a-4a0b-b1da-08a622ac6fa9` model=lgbm_classifier tier=0 target=quantile pf=0.467 n=130835 gates=FAIL

## [INFO] 2026-08-03 10:45:44 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_099_BTCUSDT_15m_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:45:44 UTC (tier 0)

AUTONOMY screen autog2_099_BTCUSDT_15m_quantile_ohlcv_v1 tier=0 proxy_pf=1.0445968814778723 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:45:44 UTC (tier 0)

START gen=autog2_100_BTCUSDT_15m_quantile_indicators_v1 BTCUSDT 15m target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:46:20 UTC (tier 0)

PREDICTABILITY real=+0.00022 p=0.0952 surr_q95=+0.00005 surr_max=+0.00034 draws=20 passed=False

## [INFO] 2026-08-03 10:46:29 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:46:29 UTC (tier 0)

trial `8a281258-fb62-471b-997b-7a5df07debbc` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:46:29 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01350 skill_surrogate=-0.00078

## [INFO] 2026-08-03 10:46:29 UTC (tier 0)

trial `c41a0e65-697d-4249-909d-d680a874409c` model=ridge tier=0 target=quantile pf=0.765 n=4559 gates=FAIL

## [INFO] 2026-08-03 10:46:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00271 skill_surrogate=-0.00586

## [INFO] 2026-08-03 10:46:34 UTC (tier 0)

trial `00bd6dc3-5248-4cd8-b739-563cbf6178ee` model=lgbm_regressor tier=0 target=quantile pf=0.511 n=11633 gates=FAIL

## [INFO] 2026-08-03 10:46:46 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-277.38180 skill_surrogate=-7.46693

## [INFO] 2026-08-03 10:46:46 UTC (tier 0)

trial `387388e0-e38c-4baf-bb85-1a4329d69ff7` model=lgbm_classifier tier=0 target=quantile pf=0.462 n=130999 gates=FAIL

## [INFO] 2026-08-03 10:46:46 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_100_BTCUSDT_15m_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:46:46 UTC (tier 0)

AUTONOMY screen autog2_100_BTCUSDT_15m_quantile_indicators_v1 tier=0 proxy_pf=0.7654162061547987 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:46:46 UTC (tier 0)

START gen=autog2_101_BTCUSDT_15m_quantile_pivot_v1 BTCUSDT 15m target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:47:08 UTC (tier 0)

PREDICTABILITY real=-0.00054 p=0.8095 surr_q95=+0.00002 surr_max=+0.00008 draws=20 passed=False

## [INFO] 2026-08-03 10:47:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:47:17 UTC (tier 0)

trial `baa158a8-daf4-449c-a6cb-fa973a9595d9` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:47:17 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00154 skill_surrogate=-0.00009

## [INFO] 2026-08-03 10:47:17 UTC (tier 0)

trial `580295f3-687b-437d-8c6f-cda72b9ca0cb` model=ridge tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:47:20 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00626 skill_surrogate=-0.00212

## [INFO] 2026-08-03 10:47:20 UTC (tier 0)

trial `c3a58e26-33a6-4670-8f74-928cd796db94` model=lgbm_regressor tier=0 target=quantile pf=0.598 n=3861 gates=FAIL

## [INFO] 2026-08-03 10:47:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-278.16756 skill_surrogate=-6.05904

## [INFO] 2026-08-03 10:47:28 UTC (tier 0)

trial `6d914808-490d-4250-a823-285008cc0183` model=lgbm_classifier tier=0 target=quantile pf=0.466 n=131317 gates=FAIL

## [INFO] 2026-08-03 10:47:28 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_101_BTCUSDT_15m_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:47:28 UTC (tier 0)

AUTONOMY screen autog2_101_BTCUSDT_15m_quantile_pivot_v1 tier=0 proxy_pf=0.5975835294509682 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:47:28 UTC (tier 0)

START gen=autog2_102_ETHUSDT_15m_quantile_ohlcv_v1 ETHUSDT 15m target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:48:09 UTC (tier 0)

PREDICTABILITY real=-0.00537 p=1.0000 surr_q95=-0.00007 surr_max=-0.00001 draws=20 passed=False

## [INFO] 2026-08-03 10:48:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:48:17 UTC (tier 0)

trial `56017a8f-d080-4226-81b0-a4a71f115ec3` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:48:18 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00542 skill_surrogate=-0.00009

## [INFO] 2026-08-03 10:48:18 UTC (tier 0)

trial `25ed0145-6ef1-42cf-9385-d25b55fedc9b` model=ridge tier=0 target=quantile pf=0.881 n=3512 gates=FAIL

## [INFO] 2026-08-03 10:48:22 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00470 skill_surrogate=-0.00053

## [INFO] 2026-08-03 10:48:22 UTC (tier 0)

trial `6db5090e-c163-4293-a253-2f28ce24f777` model=lgbm_regressor tier=0 target=quantile pf=1.022 n=2467 gates=FAIL

## [INFO] 2026-08-03 10:48:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.36925 skill_surrogate=-3.44623

## [INFO] 2026-08-03 10:48:35 UTC (tier 0)

trial `37cfec46-ff55-405f-84e3-665b36e89bde` model=lgbm_classifier tier=0 target=quantile pf=0.545 n=131409 gates=FAIL

## [INFO] 2026-08-03 10:48:35 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_102_ETHUSDT_15m_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:48:35 UTC (tier 0)

AUTONOMY screen autog2_102_ETHUSDT_15m_quantile_ohlcv_v1 tier=0 proxy_pf=1.022178284329403 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:48:35 UTC (tier 0)

START gen=autog2_103_ETHUSDT_15m_quantile_indicators_v1 ETHUSDT 15m target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:49:10 UTC (tier 0)

PREDICTABILITY real=-0.00943 p=0.9524 surr_q95=-0.00001 surr_max=+0.00126 draws=20 passed=False

## [INFO] 2026-08-03 10:49:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:49:17 UTC (tier 0)

trial `91ac9bc3-1572-4570-9048-c59f4e828fa2` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:49:18 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00595 skill_surrogate=-0.00037

## [INFO] 2026-08-03 10:49:18 UTC (tier 0)

trial `e2719ea9-38a9-46f9-b9f0-9f3949258ade` model=ridge tier=0 target=quantile pf=0.743 n=14768 gates=FAIL

## [INFO] 2026-08-03 10:49:22 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00380 skill_surrogate=-0.00330

## [INFO] 2026-08-03 10:49:22 UTC (tier 0)

trial `4c80189b-fd5a-4781-9371-115aafd193dc` model=lgbm_regressor tier=0 target=quantile pf=0.689 n=20360 gates=FAIL

## [INFO] 2026-08-03 10:49:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.35786 skill_surrogate=-3.25835

## [INFO] 2026-08-03 10:49:32 UTC (tier 0)

trial `050b9114-333f-461f-9885-adcf110edd93` model=lgbm_classifier tier=0 target=quantile pf=0.540 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:49:32 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_103_ETHUSDT_15m_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:49:32 UTC (tier 0)

AUTONOMY screen autog2_103_ETHUSDT_15m_quantile_indicators_v1 tier=0 proxy_pf=0.7433357706857794 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:49:32 UTC (tier 0)

START gen=autog2_104_ETHUSDT_15m_quantile_pivot_v1 ETHUSDT 15m target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:49:50 UTC (tier 0)

PREDICTABILITY real=-0.00081 p=0.9524 surr_q95=+0.00024 surr_max=+0.00026 draws=20 passed=False

## [INFO] 2026-08-03 10:49:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:49:57 UTC (tier 0)

trial `a27e2281-a09a-43f7-bc20-2ad39ca76b2f` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:49:57 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00074 skill_surrogate=-0.00017

## [INFO] 2026-08-03 10:49:57 UTC (tier 0)

trial `47b0577f-3c59-4632-8117-219fa1b99324` model=ridge tier=0 target=quantile pf=0.714 n=216 gates=FAIL

## [INFO] 2026-08-03 10:49:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00242 skill_surrogate=-0.00063

## [INFO] 2026-08-03 10:49:59 UTC (tier 0)

trial `9254642f-5ab0-4a04-9eee-6376fea2bf43` model=lgbm_regressor tier=0 target=quantile pf=0.609 n=4625 gates=FAIL

## [INFO] 2026-08-03 10:50:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.38200 skill_surrogate=-3.43643

## [INFO] 2026-08-03 10:50:06 UTC (tier 0)

trial `f18fac21-80ce-4b1f-a1b7-56a2ff25d554` model=lgbm_classifier tier=0 target=quantile pf=0.538 n=131424 gates=FAIL

## [INFO] 2026-08-03 10:50:06 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_104_ETHUSDT_15m_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:50:06 UTC (tier 0)

AUTONOMY screen autog2_104_ETHUSDT_15m_quantile_pivot_v1 tier=0 proxy_pf=0.7137730515448887 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:50:06 UTC (tier 0)

START gen=autog2_105_SOLUSDT_15m_quantile_ohlcv_v1 SOLUSDT 15m target=quantile space=ohlcv_v1

## [INFO] 2026-08-03 10:50:36 UTC (tier 0)

PREDICTABILITY real=+0.00050 p=0.0476 surr_q95=-0.00003 surr_max=+0.00013 draws=20 passed=True

## [INFO] 2026-08-03 10:50:38 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:50:38 UTC (tier 0)

trial `4202ceeb-988c-4bc1-99f0-5ebd5cff8f6f` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:50:38 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00469 skill_surrogate=-0.00019

## [INFO] 2026-08-03 10:50:38 UTC (tier 0)

trial `2bc548b6-4590-4530-8781-a4decbb5c0cb` model=ridge tier=0 target=quantile pf=0.830 n=17256 gates=FAIL

## [INFO] 2026-08-03 10:50:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00193 skill_surrogate=-0.00245

## [INFO] 2026-08-03 10:50:45 UTC (tier 0)

trial `a261c0bf-9053-4371-9a6c-01caf8a6f61d` model=lgbm_regressor tier=0 target=quantile pf=1.030 n=5137 gates=FAIL

## [INFO] 2026-08-03 10:51:00 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.25482 skill_surrogate=-1.47565

## [INFO] 2026-08-03 10:51:00 UTC (tier 0)

trial `297dfd7e-df05-443d-a4c9-a902292458e0` model=lgbm_classifier tier=0 target=quantile pf=0.698 n=131420 gates=FAIL

## [INFO] 2026-08-03 10:51:00 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_105_SOLUSDT_15m_quantile_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:51:00 UTC (tier 0)

AUTONOMY screen autog2_105_SOLUSDT_15m_quantile_ohlcv_v1 tier=0 proxy_pf=1.0303105414187936 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:51:00 UTC (tier 0)

START gen=autog2_106_SOLUSDT_15m_quantile_indicators_v1 SOLUSDT 15m target=quantile space=indicators_v1

## [INFO] 2026-08-03 10:51:49 UTC (tier 0)

PREDICTABILITY real=-0.00304 p=0.9524 surr_q95=+0.00012 surr_max=+0.00053 draws=20 passed=False

## [INFO] 2026-08-03 10:51:52 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:51:52 UTC (tier 0)

trial `ad094fed-a023-47c0-974b-9a877d025821` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:51:52 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00278 skill_surrogate=-0.00123

## [INFO] 2026-08-03 10:51:52 UTC (tier 0)

trial `5c251d0e-911f-4a3d-91f4-246b4dc6df80` model=ridge tier=0 target=quantile pf=0.805 n=27631 gates=FAIL

## [INFO] 2026-08-03 10:51:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01027 skill_surrogate=-0.00022

## [INFO] 2026-08-03 10:51:57 UTC (tier 0)

trial `99798755-eabf-42a2-905c-f7326f48a9b0` model=lgbm_regressor tier=0 target=quantile pf=0.774 n=30223 gates=FAIL

## [INFO] 2026-08-03 10:52:08 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.25741 skill_surrogate=-1.58664

## [INFO] 2026-08-03 10:52:08 UTC (tier 0)

trial `cad3b228-8045-4041-8c4e-9e1c31d178ec` model=lgbm_classifier tier=0 target=quantile pf=0.687 n=129756 gates=FAIL

## [INFO] 2026-08-03 10:52:08 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_106_SOLUSDT_15m_quantile_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:52:08 UTC (tier 0)

AUTONOMY screen autog2_106_SOLUSDT_15m_quantile_indicators_v1 tier=0 proxy_pf=0.8048929656613859 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:52:08 UTC (tier 0)

START gen=autog2_107_SOLUSDT_15m_quantile_pivot_v1 SOLUSDT 15m target=quantile space=pivot_v1

## [INFO] 2026-08-03 10:52:30 UTC (tier 0)

PREDICTABILITY real=-0.00106 p=1.0000 surr_q95=+0.00007 surr_max=+0.00009 draws=20 passed=False

## [INFO] 2026-08-03 10:52:32 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:52:32 UTC (tier 0)

trial `7e623e5a-a1fc-45d6-9031-b2ea6fcd8fee` model=hist_mean tier=0 target=quantile pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:52:32 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00062 skill_surrogate=-0.00002

## [INFO] 2026-08-03 10:52:32 UTC (tier 0)

trial `48be5bed-b0d0-446f-b2ca-91f565862942` model=ridge tier=0 target=quantile pf=0.749 n=4755 gates=FAIL

## [INFO] 2026-08-03 10:52:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00177 skill_surrogate=-0.00257

## [INFO] 2026-08-03 10:52:35 UTC (tier 0)

trial `bbaae237-d7e0-47f4-b9e3-553050c3f368` model=lgbm_regressor tier=0 target=quantile pf=0.741 n=10958 gates=FAIL

## [INFO] 2026-08-03 10:52:41 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.27253 skill_surrogate=-1.60802

## [INFO] 2026-08-03 10:52:41 UTC (tier 0)

trial `5078d9ba-fd44-47bd-b01c-cea3197ce4d7` model=lgbm_classifier tier=0 target=quantile pf=0.697 n=131423 gates=FAIL

## [INFO] 2026-08-03 10:52:41 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_107_SOLUSDT_15m_quantile_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:52:41 UTC (tier 0)

AUTONOMY screen autog2_107_SOLUSDT_15m_quantile_pivot_v1 tier=0 proxy_pf=0.749015333263043 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:52:41 UTC (tier 0)

START gen=autog2_108_BTCUSDT_1h_fwd_return_ohlcv_v1 BTCUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 10:52:55 UTC (tier 0)

PREDICTABILITY real=-0.01659 p=1.0000 surr_q95=-0.00002 surr_max=+0.00034 draws=20 passed=False

## [INFO] 2026-08-03 10:52:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:52:57 UTC (tier 0)

trial `41dbc7bb-80cd-4f62-8260-2c588e962e69` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:52:58 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00806 skill_surrogate=+0.00208

## [INFO] 2026-08-03 10:52:58 UTC (tier 0)

trial `a4c6b179-d532-4502-94a0-f9b2be5eaaf5` model=ridge tier=0 target=fwd_return pf=0.824 n=6802 gates=FAIL

## [INFO] 2026-08-03 10:53:00 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01158 skill_surrogate=-0.00797

## [INFO] 2026-08-03 10:53:00 UTC (tier 0)

trial `ad2385a8-3625-4285-bd4c-41501506eb71` model=lgbm_regressor tier=0 target=fwd_return pf=0.769 n=4203 gates=FAIL

## [INFO] 2026-08-03 10:53:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.88126 skill_surrogate=-5.16850

## [INFO] 2026-08-03 10:53:07 UTC (tier 0)

trial `cf62906a-1598-43c3-beea-2c2b43bae645` model=lgbm_classifier tier=0 target=fwd_return pf=0.713 n=32726 gates=FAIL

## [INFO] 2026-08-03 10:53:07 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_108_BTCUSDT_1h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:53:07 UTC (tier 0)

AUTONOMY screen autog2_108_BTCUSDT_1h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.8241790932610158 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:53:07 UTC (tier 0)

START gen=autog2_109_BTCUSDT_1h_fwd_return_indicators_v1 BTCUSDT 1h target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 10:53:25 UTC (tier 0)

PREDICTABILITY real=-0.01816 p=1.0000 surr_q95=-0.00047 surr_max=-0.00008 draws=20 passed=False

## [INFO] 2026-08-03 10:53:28 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:53:28 UTC (tier 0)

trial `dae14675-349a-446a-9bb9-1bceead7ca44` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:53:28 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.03431 skill_surrogate=-0.00150

## [INFO] 2026-08-03 10:53:28 UTC (tier 0)

trial `117f3753-0bc8-4ace-b4d2-d4e1e051c049` model=ridge tier=0 target=fwd_return pf=0.802 n=14771 gates=FAIL

## [INFO] 2026-08-03 10:53:30 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01395 skill_surrogate=-0.02015

## [INFO] 2026-08-03 10:53:30 UTC (tier 0)

trial `2f4c16ba-e47c-4080-88b0-5b2b00944738` model=lgbm_regressor tier=0 target=fwd_return pf=0.729 n=12986 gates=FAIL

## [INFO] 2026-08-03 10:53:37 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-134.00153 skill_surrogate=-5.99580

## [INFO] 2026-08-03 10:53:37 UTC (tier 0)

trial `de54437e-df01-4234-8b3e-d19a1ee4c47a` model=lgbm_classifier tier=0 target=fwd_return pf=0.690 n=32709 gates=FAIL

## [INFO] 2026-08-03 10:53:37 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_109_BTCUSDT_1h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:53:37 UTC (tier 0)

AUTONOMY screen autog2_109_BTCUSDT_1h_fwd_return_indicators_v1 tier=0 proxy_pf=0.8019564394607935 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:53:37 UTC (tier 0)

START gen=autog2_110_BTCUSDT_1h_fwd_return_pivot_v1 BTCUSDT 1h target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 10:53:45 UTC (tier 0)

PREDICTABILITY real=-0.00261 p=0.7619 surr_q95=+0.00125 surr_max=+0.00230 draws=20 passed=False

## [INFO] 2026-08-03 10:53:48 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:53:48 UTC (tier 0)

trial `25c8c3ee-8f52-43dd-9a9a-d50d70121d3d` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:53:48 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00596 skill_surrogate=-0.00093

## [INFO] 2026-08-03 10:53:48 UTC (tier 0)

trial `27223cc3-9efc-494a-ba4d-fc00bd8b8f48` model=ridge tier=0 target=fwd_return pf=0.782 n=2380 gates=FAIL

## [INFO] 2026-08-03 10:53:49 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02190 skill_surrogate=-0.00929

## [INFO] 2026-08-03 10:53:49 UTC (tier 0)

trial `01f0502c-8583-4c9e-9fff-41f1a3f62db4` model=lgbm_regressor tier=0 target=fwd_return pf=0.730 n=7895 gates=FAIL

## [INFO] 2026-08-03 10:53:53 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.89018 skill_surrogate=-5.26027

## [INFO] 2026-08-03 10:53:53 UTC (tier 0)

trial `2e021cc7-1140-42fa-934a-6e530184a99a` model=lgbm_classifier tier=0 target=fwd_return pf=0.713 n=32840 gates=FAIL

## [INFO] 2026-08-03 10:53:53 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_110_BTCUSDT_1h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:53:53 UTC (tier 0)

AUTONOMY screen autog2_110_BTCUSDT_1h_fwd_return_pivot_v1 tier=0 proxy_pf=0.7815190217194922 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:53:53 UTC (tier 0)

START gen=autog2_111_ETHUSDT_1h_fwd_return_ohlcv_v1 ETHUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 10:54:11 UTC (tier 0)

PREDICTABILITY real=-0.00340 p=0.7143 surr_q95=-0.00016 surr_max=+0.00009 draws=20 passed=False

## [INFO] 2026-08-03 10:54:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:54:12 UTC (tier 0)

trial `5495a0b5-1840-495e-b9b1-b9606c3404b6` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:54:12 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00388 skill_surrogate=-0.00120

## [INFO] 2026-08-03 10:54:12 UTC (tier 0)

trial `2b3aef8e-d2df-47f1-8394-71181488d238` model=ridge tier=0 target=fwd_return pf=0.836 n=11451 gates=FAIL

## [INFO] 2026-08-03 10:54:15 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00683 skill_surrogate=-0.00393

## [INFO] 2026-08-03 10:54:15 UTC (tier 0)

trial `7ccfc678-5b90-4dc9-a036-64629b72a852` model=lgbm_regressor tier=0 target=fwd_return pf=0.898 n=7192 gates=FAIL

## [INFO] 2026-08-03 10:54:20 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.69690 skill_surrogate=-2.37310

## [INFO] 2026-08-03 10:54:20 UTC (tier 0)

trial `d3cf9bb3-7516-47cb-a5e6-1ce67c5949d8` model=lgbm_classifier tier=0 target=fwd_return pf=0.754 n=32855 gates=FAIL

## [INFO] 2026-08-03 10:54:20 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_111_ETHUSDT_1h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:54:20 UTC (tier 0)

AUTONOMY screen autog2_111_ETHUSDT_1h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.8983023017364945 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:54:20 UTC (tier 0)

START gen=autog2_112_ETHUSDT_1h_fwd_return_indicators_v1 ETHUSDT 1h target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 10:54:31 UTC (tier 0)

PREDICTABILITY real=-0.00963 p=0.8571 surr_q95=-0.00028 surr_max=+0.00103 draws=20 passed=False

## [INFO] 2026-08-03 10:54:33 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:54:33 UTC (tier 0)

trial `820ae9b4-b723-404c-a02b-31fe169967cf` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:54:33 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00937 skill_surrogate=+0.00069

## [INFO] 2026-08-03 10:54:33 UTC (tier 0)

trial `ae918a08-f26d-44ba-80d1-dc1c63711b14` model=ridge tier=0 target=fwd_return pf=0.906 n=15512 gates=FAIL

## [INFO] 2026-08-03 10:54:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04618 skill_surrogate=-0.00491

## [INFO] 2026-08-03 10:54:35 UTC (tier 0)

trial `e203e536-ca9e-4252-be60-a16142629c29` model=lgbm_regressor tier=0 target=fwd_return pf=0.844 n=19181 gates=FAIL

## [INFO] 2026-08-03 10:54:40 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.69431 skill_surrogate=-2.80776

## [INFO] 2026-08-03 10:54:40 UTC (tier 0)

trial `f4556a7e-dc75-49e9-953a-2b5d0182c270` model=lgbm_classifier tier=0 target=fwd_return pf=0.727 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:54:40 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_112_ETHUSDT_1h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:54:40 UTC (tier 0)

AUTONOMY screen autog2_112_ETHUSDT_1h_fwd_return_indicators_v1 tier=0 proxy_pf=0.906214041880571 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:54:40 UTC (tier 0)

START gen=autog2_113_ETHUSDT_1h_fwd_return_pivot_v1 ETHUSDT 1h target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 10:54:47 UTC (tier 0)

PREDICTABILITY real=-0.00464 p=0.9524 surr_q95=+0.00101 surr_max=+0.00180 draws=20 passed=False

## [INFO] 2026-08-03 10:54:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:54:49 UTC (tier 0)

trial `84f9aea7-7267-4c9e-b267-2b4afcce765d` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:54:49 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00410 skill_surrogate=-0.00087

## [INFO] 2026-08-03 10:54:49 UTC (tier 0)

trial `1c0faa71-9e89-4acc-b854-6ec77e5a74e7` model=ridge tier=0 target=fwd_return pf=0.732 n=4466 gates=FAIL

## [INFO] 2026-08-03 10:54:51 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01122 skill_surrogate=-0.00488

## [INFO] 2026-08-03 10:54:51 UTC (tier 0)

trial `d11c9452-fcf7-451d-b786-5c6dd96a421d` model=lgbm_regressor tier=0 target=fwd_return pf=0.804 n=10953 gates=FAIL

## [INFO] 2026-08-03 10:54:54 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.71388 skill_surrogate=-2.33615

## [INFO] 2026-08-03 10:54:54 UTC (tier 0)

trial `cc1516ac-315c-4086-8551-d02202cfe2e4` model=lgbm_classifier tier=0 target=fwd_return pf=0.748 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:54:54 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_113_ETHUSDT_1h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:54:54 UTC (tier 0)

AUTONOMY screen autog2_113_ETHUSDT_1h_fwd_return_pivot_v1 tier=0 proxy_pf=0.8044483162827601 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:54:54 UTC (tier 0)

START gen=autog2_114_SOLUSDT_1h_fwd_return_ohlcv_v1 SOLUSDT 1h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 10:55:08 UTC (tier 0)

PREDICTABILITY real=-0.00647 p=1.0000 surr_q95=+0.00024 surr_max=+0.00228 draws=20 passed=False

## [INFO] 2026-08-03 10:55:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:55:09 UTC (tier 0)

trial `af5895b9-e2a7-409a-8d8c-604fc383f43c` model=hist_mean tier=0 target=fwd_return pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-03 10:55:09 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00462 skill_surrogate=+0.00053

## [INFO] 2026-08-03 10:55:09 UTC (tier 0)

trial `db722b31-929e-44b8-9c69-2250c3c6d2d5` model=ridge tier=0 target=fwd_return pf=0.902 n=17004 gates=FAIL

## [INFO] 2026-08-03 10:55:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01179 skill_surrogate=-0.00431

## [INFO] 2026-08-03 10:55:14 UTC (tier 0)

trial `5092ebf4-4ab1-4a2e-a976-1355b98863a7` model=lgbm_regressor tier=0 target=fwd_return pf=0.846 n=12027 gates=FAIL

## [INFO] 2026-08-03 10:55:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.08167 skill_surrogate=-1.53531

## [INFO] 2026-08-03 10:55:21 UTC (tier 0)

trial `403bf807-bd39-44ab-864b-8e70af75fbd5` model=lgbm_classifier tier=0 target=fwd_return pf=0.874 n=32854 gates=FAIL

## [INFO] 2026-08-03 10:55:21 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_114_SOLUSDT_1h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:55:21 UTC (tier 0)

AUTONOMY screen autog2_114_SOLUSDT_1h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.9022273781710141 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:55:21 UTC (tier 0)

START gen=autog2_115_SOLUSDT_1h_fwd_return_indicators_v1 SOLUSDT 1h target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 10:55:35 UTC (tier 0)

PREDICTABILITY real=+0.00280 p=0.0952 surr_q95=-0.00028 surr_max=+0.00334 draws=20 passed=False

## [INFO] 2026-08-03 10:55:37 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:55:37 UTC (tier 0)

trial `8a104117-39e9-4d14-98ab-26f9f560d695` model=hist_mean tier=0 target=fwd_return pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-03 10:55:37 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01219 skill_surrogate=-0.00289

## [INFO] 2026-08-03 10:55:37 UTC (tier 0)

trial `41d370a4-e7da-4d31-82ab-9854535641ba` model=ridge tier=0 target=fwd_return pf=0.884 n=22651 gates=FAIL

## [INFO] 2026-08-03 10:55:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01149 skill_surrogate=-0.00429

## [INFO] 2026-08-03 10:55:39 UTC (tier 0)

trial `835023a7-f79e-4711-a7be-62d12be36d1b` model=lgbm_regressor tier=0 target=fwd_return pf=0.958 n=15633 gates=FAIL

## [INFO] 2026-08-03 10:55:46 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.05580 skill_surrogate=-1.93033

## [INFO] 2026-08-03 10:55:46 UTC (tier 0)

trial `db8fba2b-8636-4a40-b615-c73dc3b94e37` model=lgbm_classifier tier=0 target=fwd_return pf=0.860 n=32699 gates=FAIL

## [INFO] 2026-08-03 10:55:46 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_115_SOLUSDT_1h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:55:46 UTC (tier 0)

AUTONOMY screen autog2_115_SOLUSDT_1h_fwd_return_indicators_v1 tier=0 proxy_pf=0.958342346586077 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:55:46 UTC (tier 0)

START gen=autog2_116_SOLUSDT_1h_fwd_return_pivot_v1 SOLUSDT 1h target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 10:55:52 UTC (tier 0)

PREDICTABILITY real=-0.00184 p=0.7619 surr_q95=+0.00017 surr_max=+0.00126 draws=20 passed=False

## [INFO] 2026-08-03 10:55:53 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:55:53 UTC (tier 0)

trial `5500867c-dd7d-4d2b-942a-ba01fdbb447c` model=hist_mean tier=0 target=fwd_return pf=0.753 n=6552 gates=FAIL

## [INFO] 2026-08-03 10:55:53 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00186 skill_surrogate=-0.00048

## [INFO] 2026-08-03 10:55:54 UTC (tier 0)

trial `6aa86258-6b09-41ca-ad22-d3383f0bdedc` model=ridge tier=0 target=fwd_return pf=0.745 n=8221 gates=FAIL

## [INFO] 2026-08-03 10:55:55 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01905 skill_surrogate=-0.00702

## [INFO] 2026-08-03 10:55:55 UTC (tier 0)

trial `221b6149-d430-4359-b20b-a5c0969e3c3f` model=lgbm_regressor tier=0 target=fwd_return pf=0.890 n=17033 gates=FAIL

## [INFO] 2026-08-03 10:55:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-62.08766 skill_surrogate=-1.57613

## [INFO] 2026-08-03 10:55:59 UTC (tier 0)

trial `f11a3488-2245-47c2-b4b8-1a95b302b40e` model=lgbm_classifier tier=0 target=fwd_return pf=0.840 n=32856 gates=FAIL

## [INFO] 2026-08-03 10:55:59 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_116_SOLUSDT_1h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:55:59 UTC (tier 0)

AUTONOMY screen autog2_116_SOLUSDT_1h_fwd_return_pivot_v1 tier=0 proxy_pf=0.8901217750441386 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:55:59 UTC (tier 0)

START gen=autog2_117_BTCUSDT_4h_fwd_return_ohlcv_v1 BTCUSDT 4h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 10:56:04 UTC (tier 0)

PREDICTABILITY real=-0.00524 p=0.6190 surr_q95=+0.00150 surr_max=+0.00420 draws=20 passed=False

## [INFO] 2026-08-03 10:56:05 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:56:05 UTC (tier 0)

trial `43177b46-c5c0-4648-9955-c678bc21268c` model=hist_mean tier=0 target=fwd_return pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-03 10:56:05 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00342 skill_surrogate=-0.00882

## [INFO] 2026-08-03 10:56:05 UTC (tier 0)

trial `f079c0fd-eb78-404d-ae2a-32171a7e426c` model=ridge tier=0 target=fwd_return pf=1.018 n=5223 gates=FAIL

## [INFO] 2026-08-03 10:56:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04444 skill_surrogate=-0.02884

## [INFO] 2026-08-03 10:56:06 UTC (tier 0)

trial `29f6d08e-6906-4fea-9c7d-fe102a6f4345` model=lgbm_regressor tier=0 target=fwd_return pf=0.864 n=5565 gates=FAIL

## [INFO] 2026-08-03 10:56:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.22449 skill_surrogate=-4.36823

## [INFO] 2026-08-03 10:56:10 UTC (tier 0)

trial `f2e5ea42-1c0c-402f-840e-f4e8b5a31741` model=lgbm_classifier tier=0 target=fwd_return pf=0.834 n=8204 gates=FAIL

## [INFO] 2026-08-03 10:56:10 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_117_BTCUSDT_4h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:56:10 UTC (tier 0)

AUTONOMY screen autog2_117_BTCUSDT_4h_fwd_return_ohlcv_v1 tier=0 proxy_pf=1.0176857259100298 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:56:10 UTC (tier 0)

START gen=autog2_118_BTCUSDT_4h_fwd_return_indicators_v1 BTCUSDT 4h target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 10:56:15 UTC (tier 0)

PREDICTABILITY real=-0.05673 p=0.9524 surr_q95=-0.00099 surr_max=+0.00098 draws=20 passed=False

## [INFO] 2026-08-03 10:56:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:56:16 UTC (tier 0)

trial `4d35a832-f1d5-46c5-9754-1a8dbfa5ab80` model=hist_mean tier=0 target=fwd_return pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-03 10:56:16 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.04064 skill_surrogate=-0.00925

## [INFO] 2026-08-03 10:56:16 UTC (tier 0)

trial `245e9142-60c5-494e-a5ef-451e8e6437f8` model=ridge tier=0 target=fwd_return pf=0.827 n=6439 gates=FAIL

## [INFO] 2026-08-03 10:56:17 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.05483 skill_surrogate=-0.04181

## [INFO] 2026-08-03 10:56:18 UTC (tier 0)

trial `2cee3525-2dd3-4a53-8cf1-1b8799694581` model=lgbm_regressor tier=0 target=fwd_return pf=0.800 n=7028 gates=FAIL

## [INFO] 2026-08-03 10:56:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16491 skill_surrogate=-6.95168

## [INFO] 2026-08-03 10:56:21 UTC (tier 0)

trial `9de6d58e-a445-46b7-a4b7-4fc7245250cb` model=lgbm_classifier tier=0 target=fwd_return pf=0.817 n=8213 gates=FAIL

## [INFO] 2026-08-03 10:56:21 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_118_BTCUSDT_4h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:56:21 UTC (tier 0)

AUTONOMY screen autog2_118_BTCUSDT_4h_fwd_return_indicators_v1 tier=0 proxy_pf=0.8266177086033331 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:56:21 UTC (tier 0)

START gen=autog2_119_BTCUSDT_4h_fwd_return_pivot_v1 BTCUSDT 4h target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 10:56:24 UTC (tier 0)

PREDICTABILITY real=-0.00099 p=0.3333 surr_q95=+0.00322 surr_max=+0.00343 draws=20 passed=False

## [INFO] 2026-08-03 10:56:24 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:56:24 UTC (tier 0)

trial `340ea849-6cfa-4123-a11c-0cfd79a11c84` model=hist_mean tier=0 target=fwd_return pf=0.683 n=1638 gates=FAIL

## [INFO] 2026-08-03 10:56:24 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00530 skill_surrogate=+0.00020

## [INFO] 2026-08-03 10:56:24 UTC (tier 0)

trial `4d92ab14-b15a-401a-9538-edd397f95107` model=ridge tier=0 target=fwd_return pf=0.842 n=2815 gates=FAIL

## [INFO] 2026-08-03 10:56:26 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03841 skill_surrogate=-0.00734

## [INFO] 2026-08-03 10:56:26 UTC (tier 0)

trial `b21964f9-166e-436d-b61a-e921000c3eff` model=lgbm_regressor tier=0 target=fwd_return pf=0.842 n=5743 gates=FAIL

## [INFO] 2026-08-03 10:56:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16893 skill_surrogate=-4.75857

## [INFO] 2026-08-03 10:56:28 UTC (tier 0)

trial `a0ebf257-eb96-4338-8ca0-b5836822fff8` model=lgbm_classifier tier=0 target=fwd_return pf=0.846 n=8210 gates=FAIL

## [INFO] 2026-08-03 10:56:28 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_119_BTCUSDT_4h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:56:28 UTC (tier 0)

AUTONOMY screen autog2_119_BTCUSDT_4h_fwd_return_pivot_v1 tier=0 proxy_pf=0.8464266512174518 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:56:28 UTC (tier 0)

START gen=autog2_120_ETHUSDT_4h_fwd_return_ohlcv_v1 ETHUSDT 4h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 10:56:33 UTC (tier 0)

PREDICTABILITY real=-0.00991 p=0.6190 surr_q95=+0.00728 surr_max=+0.00810 draws=20 passed=False

## [INFO] 2026-08-03 10:56:33 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:56:33 UTC (tier 0)

trial `844d37c9-62c3-4ddb-84bb-df5f047539b5` model=hist_mean tier=0 target=fwd_return pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:56:33 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00136 skill_surrogate=-0.00007

## [INFO] 2026-08-03 10:56:33 UTC (tier 0)

trial `8d12e6e0-ac7d-4967-b325-6da0dee64d9c` model=ridge tier=0 target=fwd_return pf=0.946 n=6072 gates=FAIL

## [INFO] 2026-08-03 10:56:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02168 skill_surrogate=-0.00761

## [INFO] 2026-08-03 10:56:35 UTC (tier 0)

trial `b9044e6b-c743-4fb8-81c6-db5bdfd37f07` model=lgbm_regressor tier=0 target=fwd_return pf=0.930 n=6253 gates=FAIL

## [INFO] 2026-08-03 10:56:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.11179 skill_surrogate=-2.38091

## [INFO] 2026-08-03 10:56:38 UTC (tier 0)

trial `e41600d3-5891-4f58-a9aa-5679401741cf` model=lgbm_classifier tier=0 target=fwd_return pf=0.903 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:56:38 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_120_ETHUSDT_4h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:56:38 UTC (tier 0)

AUTONOMY screen autog2_120_ETHUSDT_4h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.9460121773106233 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:56:38 UTC (tier 0)

START gen=autog2_121_ETHUSDT_4h_fwd_return_indicators_v1 ETHUSDT 4h target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 10:56:43 UTC (tier 0)

PREDICTABILITY real=-0.07290 p=1.0000 surr_q95=-0.00201 surr_max=-0.00128 draws=20 passed=False

## [INFO] 2026-08-03 10:56:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:56:44 UTC (tier 0)

trial `6751680f-070b-4b12-81e0-62991f704955` model=hist_mean tier=0 target=fwd_return pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:56:44 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00167 skill_surrogate=-0.00523

## [INFO] 2026-08-03 10:56:44 UTC (tier 0)

trial `c2100b40-019a-4a52-8625-30429f7facae` model=ridge tier=0 target=fwd_return pf=0.888 n=6885 gates=FAIL

## [INFO] 2026-08-03 10:56:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.03816 skill_surrogate=-0.01158

## [INFO] 2026-08-03 10:56:45 UTC (tier 0)

trial `a0cd6226-3cc3-4d8b-9be5-d426dad89f40` model=lgbm_regressor tier=0 target=fwd_return pf=0.918 n=7147 gates=FAIL

## [INFO] 2026-08-03 10:56:48 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.01013 skill_surrogate=-2.65853

## [INFO] 2026-08-03 10:56:48 UTC (tier 0)

trial `5aceb57d-df4e-4c29-8db2-6ce0385a77d8` model=lgbm_classifier tier=0 target=fwd_return pf=0.915 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:56:48 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_121_ETHUSDT_4h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:56:48 UTC (tier 0)

AUTONOMY screen autog2_121_ETHUSDT_4h_fwd_return_indicators_v1 tier=0 proxy_pf=0.9200856060065038 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:56:48 UTC (tier 0)

START gen=autog2_122_ETHUSDT_4h_fwd_return_pivot_v1 ETHUSDT 4h target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 10:56:51 UTC (tier 0)

PREDICTABILITY real=-0.00131 p=0.4286 surr_q95=+0.00145 surr_max=+0.00277 draws=20 passed=False

## [INFO] 2026-08-03 10:56:51 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:56:52 UTC (tier 0)

trial `1effca04-1e81-448d-a128-8076fe143408` model=hist_mean tier=0 target=fwd_return pf=0.920 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:56:52 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00295 skill_surrogate=+0.00031

## [INFO] 2026-08-03 10:56:52 UTC (tier 0)

trial `f5355094-d8ec-40d4-8957-a6f52a08dd9c` model=ridge tier=0 target=fwd_return pf=0.951 n=6014 gates=FAIL

## [INFO] 2026-08-03 10:56:53 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01431 skill_surrogate=-0.01088

## [INFO] 2026-08-03 10:56:53 UTC (tier 0)

trial `c0e61125-191b-4c35-8d96-e2b6ed255bb5` model=lgbm_regressor tier=0 target=fwd_return pf=0.930 n=6824 gates=FAIL

## [INFO] 2026-08-03 10:56:55 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.01322 skill_surrogate=-2.68694

## [INFO] 2026-08-03 10:56:55 UTC (tier 0)

trial `db0d363b-6f9a-468e-af31-8a050ede4b3e` model=lgbm_classifier tier=0 target=fwd_return pf=0.905 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:56:55 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_122_ETHUSDT_4h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:56:55 UTC (tier 0)

AUTONOMY screen autog2_122_ETHUSDT_4h_fwd_return_pivot_v1 tier=0 proxy_pf=0.9510175596610267 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:56:55 UTC (tier 0)

START gen=autog2_123_SOLUSDT_4h_fwd_return_ohlcv_v1 SOLUSDT 4h target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 10:57:00 UTC (tier 0)

PREDICTABILITY real=-0.02437 p=1.0000 surr_q95=+0.00219 surr_max=+0.00222 draws=20 passed=False

## [INFO] 2026-08-03 10:57:00 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:57:00 UTC (tier 0)

trial `661d53fa-240b-4af7-8d03-9d1eb3f69b9b` model=hist_mean tier=0 target=fwd_return pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:57:00 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01743 skill_surrogate=-0.00753

## [INFO] 2026-08-03 10:57:00 UTC (tier 0)

trial `fd317216-b837-43a6-accb-f92822deb0df` model=ridge tier=0 target=fwd_return pf=0.997 n=7292 gates=FAIL

## [INFO] 2026-08-03 10:57:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02577 skill_surrogate=-0.02091

## [INFO] 2026-08-03 10:57:02 UTC (tier 0)

trial `adf5c926-177b-4a65-a38e-805f8cd935d9` model=lgbm_regressor tier=0 target=fwd_return pf=0.958 n=7161 gates=FAIL

## [INFO] 2026-08-03 10:57:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.52165 skill_surrogate=-1.47638

## [INFO] 2026-08-03 10:57:06 UTC (tier 0)

trial `c29c98e5-b289-47ca-89d0-b220599592cf` model=lgbm_classifier tier=0 target=fwd_return pf=0.989 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:57:06 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_123_SOLUSDT_4h_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:57:06 UTC (tier 0)

AUTONOMY screen autog2_123_SOLUSDT_4h_fwd_return_ohlcv_v1 tier=0 proxy_pf=0.9965702191452582 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:57:06 UTC (tier 0)

START gen=autog2_124_SOLUSDT_4h_fwd_return_indicators_v1 SOLUSDT 4h target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 10:57:10 UTC (tier 0)

PREDICTABILITY real=-0.01378 p=0.2857 surr_q95=-0.00313 surr_max=-0.00192 draws=20 passed=False

## [INFO] 2026-08-03 10:57:11 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=-0.00000

## [INFO] 2026-08-03 10:57:11 UTC (tier 0)

trial `d4c1cc8b-a720-40b8-a5ad-088415053195` model=hist_mean tier=0 target=fwd_return pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:57:11 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00250 skill_surrogate=-0.01403

## [INFO] 2026-08-03 10:57:11 UTC (tier 0)

trial `cee53fcc-c5f0-4863-9a48-e2c5b466fc33` model=ridge tier=0 target=fwd_return pf=1.042 n=7405 gates=FAIL

## [INFO] 2026-08-03 10:57:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01843 skill_surrogate=-0.01847

## [INFO] 2026-08-03 10:57:12 UTC (tier 0)

trial `3de53fa4-89b9-4ace-bee2-b3201516d175` model=lgbm_regressor tier=0 target=fwd_return pf=0.951 n=7318 gates=FAIL

## [INFO] 2026-08-03 10:57:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.44360 skill_surrogate=-2.74855

## [INFO] 2026-08-03 10:57:18 UTC (tier 0)

trial `cd3be390-6aaa-4421-889f-c6e4bf7e6c83` model=lgbm_classifier tier=0 target=fwd_return pf=0.918 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:57:18 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_124_SOLUSDT_4h_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:57:18 UTC (tier 0)

AUTONOMY screen autog2_124_SOLUSDT_4h_fwd_return_indicators_v1 tier=0 proxy_pf=1.0422191080060303 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:57:18 UTC (tier 0)

START gen=autog2_125_SOLUSDT_4h_fwd_return_pivot_v1 SOLUSDT 4h target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 10:57:21 UTC (tier 0)

PREDICTABILITY real=-0.01625 p=0.8095 surr_q95=+0.00091 surr_max=+0.00122 draws=20 passed=False

## [INFO] 2026-08-03 10:57:21 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:57:21 UTC (tier 0)

trial `e427087d-f394-4c2a-a450-5e2be68c5202` model=hist_mean tier=0 target=fwd_return pf=0.970 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:57:21 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00757 skill_surrogate=-0.00052

## [INFO] 2026-08-03 10:57:21 UTC (tier 0)

trial `9001977e-fe00-4d4c-bf7f-750ac8bd74e8` model=ridge tier=0 target=fwd_return pf=0.975 n=6843 gates=FAIL

## [INFO] 2026-08-03 10:57:25 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.04768 skill_surrogate=-0.01214

## [INFO] 2026-08-03 10:57:25 UTC (tier 0)

trial `3668c7a0-661b-45f2-9031-8103b002e11f` model=lgbm_regressor tier=0 target=fwd_return pf=0.987 n=7360 gates=FAIL

## [INFO] 2026-08-03 10:57:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-28.44952 skill_surrogate=-2.25744

## [INFO] 2026-08-03 10:57:28 UTC (tier 0)

trial `2d8606c8-f21c-4ae0-b3c0-b4a99280acca` model=lgbm_classifier tier=0 target=fwd_return pf=0.921 n=8214 gates=FAIL

## [INFO] 2026-08-03 10:57:28 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_125_SOLUSDT_4h_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:57:28 UTC (tier 0)

AUTONOMY screen autog2_125_SOLUSDT_4h_fwd_return_pivot_v1 tier=0 proxy_pf=0.9868588821857988 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:57:28 UTC (tier 0)

START gen=autog2_126_BTCUSDT_15m_fwd_return_ohlcv_v1 BTCUSDT 15m target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 10:58:11 UTC (tier 0)

PREDICTABILITY real=-0.00358 p=1.0000 surr_q95=+0.00021 surr_max=+0.00023 draws=20 passed=False

## [INFO] 2026-08-03 10:58:21 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:58:21 UTC (tier 0)

trial `23d754ed-7de7-4ba6-b863-7f462e5655dc` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:58:22 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00863 skill_surrogate=+0.00078

## [INFO] 2026-08-03 10:58:22 UTC (tier 0)

trial `6bc38ad5-90a5-4eb1-9ad1-2efe08f077c8` model=ridge tier=0 target=fwd_return pf=1.045 n=790 gates=FAIL

## [INFO] 2026-08-03 10:58:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00290 skill_surrogate=-0.00196

## [INFO] 2026-08-03 10:58:27 UTC (tier 0)

trial `6660d08f-43eb-47dc-a019-493203ec1bed` model=lgbm_regressor tier=0 target=fwd_return pf=0.810 n=2069 gates=FAIL

## [INFO] 2026-08-03 10:58:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-278.14698 skill_surrogate=-5.70952

## [INFO] 2026-08-03 10:58:43 UTC (tier 0)

trial `b06bea2f-e3a1-4f72-af12-32633e01c49a` model=lgbm_classifier tier=0 target=fwd_return pf=0.467 n=130835 gates=FAIL

## [INFO] 2026-08-03 10:58:43 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_126_BTCUSDT_15m_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 10:58:43 UTC (tier 0)

AUTONOMY screen autog2_126_BTCUSDT_15m_fwd_return_ohlcv_v1 tier=0 proxy_pf=1.0445968814778723 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 10:58:43 UTC (tier 0)

START gen=autog2_127_BTCUSDT_15m_fwd_return_indicators_v1 BTCUSDT 15m target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 10:59:30 UTC (tier 0)

PREDICTABILITY real=+0.00022 p=0.0952 surr_q95=+0.00005 surr_max=+0.00034 draws=20 passed=False

## [INFO] 2026-08-03 10:59:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 10:59:50 UTC (tier 0)

trial `5e07ad96-d851-4d67-9bde-ea106afe070f` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 10:59:51 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01350 skill_surrogate=-0.00078

## [INFO] 2026-08-03 10:59:51 UTC (tier 0)

trial `9b68c8f0-d8df-4de6-8b42-fcae79de5658` model=ridge tier=0 target=fwd_return pf=0.765 n=4559 gates=FAIL

## [INFO] 2026-08-03 10:59:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00271 skill_surrogate=-0.00586

## [INFO] 2026-08-03 10:59:57 UTC (tier 0)

trial `8d23d69a-4cfb-4d96-9a0c-012a4f576d0d` model=lgbm_regressor tier=0 target=fwd_return pf=0.511 n=11633 gates=FAIL

## [INFO] 2026-08-03 11:00:11 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-277.38180 skill_surrogate=-7.46693

## [INFO] 2026-08-03 11:00:12 UTC (tier 0)

trial `a1b9cc89-2735-45ba-9804-6a2f2920a239` model=lgbm_classifier tier=0 target=fwd_return pf=0.462 n=130999 gates=FAIL

## [INFO] 2026-08-03 11:00:12 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_127_BTCUSDT_15m_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:00:12 UTC (tier 0)

AUTONOMY screen autog2_127_BTCUSDT_15m_fwd_return_indicators_v1 tier=0 proxy_pf=0.7654162061547987 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:00:12 UTC (tier 0)

START gen=autog2_128_BTCUSDT_15m_fwd_return_pivot_v1 BTCUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 11:00:38 UTC (tier 0)

PREDICTABILITY real=-0.00054 p=0.8095 surr_q95=+0.00002 surr_max=+0.00008 draws=20 passed=False

## [INFO] 2026-08-03 11:00:51 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:00:52 UTC (tier 0)

trial `57aefd1a-0fe5-4429-b474-47891e63cbf2` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:00:52 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00154 skill_surrogate=-0.00009

## [INFO] 2026-08-03 11:00:52 UTC (tier 0)

trial `3d57f68b-ba3d-4a60-9f5b-d3ef091513c5` model=ridge tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:00:55 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00626 skill_surrogate=-0.00212

## [INFO] 2026-08-03 11:00:55 UTC (tier 0)

trial `b3e605d7-3c80-4272-9243-dae93ed3a8a1` model=lgbm_regressor tier=0 target=fwd_return pf=0.598 n=3861 gates=FAIL

## [INFO] 2026-08-03 11:01:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-278.16756 skill_surrogate=-6.05904

## [INFO] 2026-08-03 11:01:07 UTC (tier 0)

trial `cee44396-35ee-45b4-9755-d2fd853bdce2` model=lgbm_classifier tier=0 target=fwd_return pf=0.466 n=131317 gates=FAIL

## [INFO] 2026-08-03 11:01:07 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_128_BTCUSDT_15m_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:01:07 UTC (tier 0)

AUTONOMY screen autog2_128_BTCUSDT_15m_fwd_return_pivot_v1 tier=0 proxy_pf=0.5975835294509682 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:01:07 UTC (tier 0)

START gen=autog2_129_ETHUSDT_15m_fwd_return_ohlcv_v1 ETHUSDT 15m target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 11:01:49 UTC (tier 0)

PREDICTABILITY real=-0.00537 p=1.0000 surr_q95=-0.00007 surr_max=-0.00001 draws=20 passed=False

## [INFO] 2026-08-03 11:01:58 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:01:58 UTC (tier 0)

trial `6fcee278-2834-416a-b227-b89756c6ee32` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:01:59 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00542 skill_surrogate=-0.00009

## [INFO] 2026-08-03 11:01:59 UTC (tier 0)

trial `d628f43a-b7e9-4103-8efe-86286f5adf0a` model=ridge tier=0 target=fwd_return pf=0.881 n=3512 gates=FAIL

## [INFO] 2026-08-03 11:02:03 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00470 skill_surrogate=-0.00053

## [INFO] 2026-08-03 11:02:03 UTC (tier 0)

trial `d1138318-d4f2-4cb0-b5ab-95c373258ea4` model=lgbm_regressor tier=0 target=fwd_return pf=1.022 n=2467 gates=FAIL

## [INFO] 2026-08-03 11:02:17 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.36925 skill_surrogate=-3.44623

## [INFO] 2026-08-03 11:02:17 UTC (tier 0)

trial `aec855b8-271f-4c70-b454-ba52d7c2849d` model=lgbm_classifier tier=0 target=fwd_return pf=0.545 n=131409 gates=FAIL

## [INFO] 2026-08-03 11:02:17 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_129_ETHUSDT_15m_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:02:17 UTC (tier 0)

AUTONOMY screen autog2_129_ETHUSDT_15m_fwd_return_ohlcv_v1 tier=0 proxy_pf=1.022178284329403 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:02:17 UTC (tier 0)

START gen=autog2_130_ETHUSDT_15m_fwd_return_indicators_v1 ETHUSDT 15m target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 11:03:00 UTC (tier 0)

PREDICTABILITY real=-0.00943 p=0.9524 surr_q95=-0.00001 surr_max=+0.00126 draws=20 passed=False

## [INFO] 2026-08-03 11:03:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:03:12 UTC (tier 0)

trial `940026fd-0a64-4550-87ea-fcb7b7150ab8` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:03:13 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00595 skill_surrogate=-0.00037

## [INFO] 2026-08-03 11:03:13 UTC (tier 0)

trial `41f3ca21-e7da-429a-bb76-61dbbeeee52b` model=ridge tier=0 target=fwd_return pf=0.743 n=14768 gates=FAIL

## [INFO] 2026-08-03 11:03:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00380 skill_surrogate=-0.00330

## [INFO] 2026-08-03 11:03:18 UTC (tier 0)

trial `006ee144-33db-4c01-a234-a9817219f249` model=lgbm_regressor tier=0 target=fwd_return pf=0.689 n=20360 gates=FAIL

## [INFO] 2026-08-03 11:03:31 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.35786 skill_surrogate=-3.25835

## [INFO] 2026-08-03 11:03:31 UTC (tier 0)

trial `4ed1d2e7-b5f9-4df4-9616-a0809f237763` model=lgbm_classifier tier=0 target=fwd_return pf=0.540 n=131424 gates=FAIL

## [INFO] 2026-08-03 11:03:31 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_130_ETHUSDT_15m_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:03:31 UTC (tier 0)

AUTONOMY screen autog2_130_ETHUSDT_15m_fwd_return_indicators_v1 tier=0 proxy_pf=0.7433357706857794 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:03:31 UTC (tier 0)

START gen=autog2_131_ETHUSDT_15m_fwd_return_pivot_v1 ETHUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 11:03:55 UTC (tier 0)

PREDICTABILITY real=-0.00081 p=0.9524 surr_q95=+0.00024 surr_max=+0.00026 draws=20 passed=False

## [INFO] 2026-08-03 11:04:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:04:04 UTC (tier 0)

trial `0ec4b8b8-1e29-4bb7-aea8-93d6e33d86c5` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:04:04 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00074 skill_surrogate=-0.00017

## [INFO] 2026-08-03 11:04:04 UTC (tier 0)

trial `d5aa3c62-868b-4d34-8c83-1a60baab7a3a` model=ridge tier=0 target=fwd_return pf=0.714 n=216 gates=FAIL

## [INFO] 2026-08-03 11:04:07 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00242 skill_surrogate=-0.00063

## [INFO] 2026-08-03 11:04:07 UTC (tier 0)

trial `55f5422a-01ec-4cb7-a4a7-3d79f329d712` model=lgbm_regressor tier=0 target=fwd_return pf=0.609 n=4625 gates=FAIL

## [INFO] 2026-08-03 11:04:16 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-162.38200 skill_surrogate=-3.43643

## [INFO] 2026-08-03 11:04:16 UTC (tier 0)

trial `377d2dad-ab45-4f5c-8724-b9a5279f6010` model=lgbm_classifier tier=0 target=fwd_return pf=0.538 n=131424 gates=FAIL

## [INFO] 2026-08-03 11:04:16 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_131_ETHUSDT_15m_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:04:16 UTC (tier 0)

AUTONOMY screen autog2_131_ETHUSDT_15m_fwd_return_pivot_v1 tier=0 proxy_pf=0.7137730515448887 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:04:16 UTC (tier 0)

START gen=autog2_132_SOLUSDT_15m_fwd_return_ohlcv_v1 SOLUSDT 15m target=fwd_return space=ohlcv_v1

## [INFO] 2026-08-03 11:04:58 UTC (tier 0)

PREDICTABILITY real=+0.00050 p=0.0476 surr_q95=-0.00003 surr_max=+0.00013 draws=20 passed=True

## [INFO] 2026-08-03 11:05:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:05:04 UTC (tier 0)

trial `69527312-ca0e-47ce-a061-e43299b857e8` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:05:04 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00469 skill_surrogate=-0.00019

## [INFO] 2026-08-03 11:05:04 UTC (tier 0)

trial `fe00f14e-0800-49ad-8803-b1a0f4d53ebb` model=ridge tier=0 target=fwd_return pf=0.830 n=17256 gates=FAIL

## [INFO] 2026-08-03 11:05:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00193 skill_surrogate=-0.00245

## [INFO] 2026-08-03 11:05:10 UTC (tier 0)

trial `98697d04-96db-4c3b-a30d-7d25516e815c` model=lgbm_regressor tier=0 target=fwd_return pf=1.030 n=5137 gates=FAIL

## [INFO] 2026-08-03 11:05:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.25482 skill_surrogate=-1.47565

## [INFO] 2026-08-03 11:05:27 UTC (tier 0)

trial `9ad32a1e-64c9-4d18-92ea-380ceb6fb42d` model=lgbm_classifier tier=0 target=fwd_return pf=0.698 n=131420 gates=FAIL

## [INFO] 2026-08-03 11:05:27 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_132_SOLUSDT_15m_fwd_return_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:05:27 UTC (tier 0)

AUTONOMY screen autog2_132_SOLUSDT_15m_fwd_return_ohlcv_v1 tier=0 proxy_pf=1.0303105414187936 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:05:27 UTC (tier 0)

START gen=autog2_133_SOLUSDT_15m_fwd_return_indicators_v1 SOLUSDT 15m target=fwd_return space=indicators_v1

## [INFO] 2026-08-03 11:06:37 UTC (tier 0)

PREDICTABILITY real=-0.00304 p=0.9524 surr_q95=+0.00012 surr_max=+0.00053 draws=20 passed=False

## [INFO] 2026-08-03 11:06:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:06:42 UTC (tier 0)

trial `935d8dcc-20a6-472e-8cbb-66641dc60730` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:06:44 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00278 skill_surrogate=-0.00123

## [INFO] 2026-08-03 11:06:44 UTC (tier 0)

trial `e60d4aad-2fdc-45eb-a7de-f2441d10b429` model=ridge tier=0 target=fwd_return pf=0.805 n=27631 gates=FAIL

## [INFO] 2026-08-03 11:06:53 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01027 skill_surrogate=-0.00022

## [INFO] 2026-08-03 11:06:53 UTC (tier 0)

trial `746cbf79-fa3f-4b71-bba1-1a9705fa405d` model=lgbm_regressor tier=0 target=fwd_return pf=0.774 n=30223 gates=FAIL

## [INFO] 2026-08-03 11:07:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.25741 skill_surrogate=-1.58664

## [INFO] 2026-08-03 11:07:14 UTC (tier 0)

trial `22b5d3bf-ca67-473c-bf0a-8041a7ebff44` model=lgbm_classifier tier=0 target=fwd_return pf=0.687 n=129756 gates=FAIL

## [INFO] 2026-08-03 11:07:14 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_133_SOLUSDT_15m_fwd_return_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:07:14 UTC (tier 0)

AUTONOMY screen autog2_133_SOLUSDT_15m_fwd_return_indicators_v1 tier=0 proxy_pf=0.8048929656613859 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:07:14 UTC (tier 0)

START gen=autog2_134_SOLUSDT_15m_fwd_return_pivot_v1 SOLUSDT 15m target=fwd_return space=pivot_v1

## [INFO] 2026-08-03 11:08:14 UTC (tier 0)

PREDICTABILITY real=-0.00106 p=1.0000 surr_q95=+0.00007 surr_max=+0.00009 draws=20 passed=False

## [INFO] 2026-08-03 11:08:21 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:08:21 UTC (tier 0)

trial `2975ef38-f032-48b5-90e0-78be41fae18f` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:08:21 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00062 skill_surrogate=-0.00002

## [INFO] 2026-08-03 11:08:21 UTC (tier 0)

trial `6415ec4c-53c2-4138-b966-bcad7a78ba7b` model=ridge tier=0 target=fwd_return pf=0.749 n=4755 gates=FAIL

## [INFO] 2026-08-03 11:08:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00177 skill_surrogate=-0.00257

## [INFO] 2026-08-03 11:08:28 UTC (tier 0)

trial `0a99256d-7588-490d-97a4-47a6d8c47330` model=lgbm_regressor tier=0 target=fwd_return pf=0.741 n=10958 gates=FAIL

## [INFO] 2026-08-03 11:08:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-130.27253 skill_surrogate=-1.60802

## [INFO] 2026-08-03 11:08:59 UTC (tier 0)

trial `9aa4dec0-3eae-41fb-bc1e-efd3234d4047` model=lgbm_classifier tier=0 target=fwd_return pf=0.697 n=131423 gates=FAIL

## [INFO] 2026-08-03 11:08:59 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_134_SOLUSDT_15m_fwd_return_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:09:00 UTC (tier 0)

AUTONOMY screen autog2_134_SOLUSDT_15m_fwd_return_pivot_v1 tier=0 proxy_pf=0.749015333263043 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:09:00 UTC (tier 0)

START gen=autog2_135_BTCUSDT_1h_direction_ohlcv_v1 BTCUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:09:36 UTC (tier 0)

PREDICTABILITY real=+0.00789 p=0.0476 surr_q95=-0.00021 surr_max=-0.00007 draws=20 passed=True

## [INFO] 2026-08-03 11:09:48 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:09:48 UTC (tier 0)

trial `1d4d0951-0ea8-4487-a21e-94052773f55e` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:09:49 UTC (tier 1)

trial `968ff9a8-7a41-445d-a342-3edb1e037c4a` model=ridge tier=1 target=direction pf=0.751 n=10841 gates=FAIL

## [INFO] 2026-08-03 11:09:57 UTC (tier 1)

trial `e7aff49d-6b1c-4b3c-943b-7511a881dca0` model=lgbm_regressor tier=1 target=direction pf=0.726 n=15427 gates=FAIL

## [INFO] 2026-08-03 11:10:26 UTC (tier 1)

trial `bc75f903-ac1b-4d1d-86c8-0ed4a09ef93b` model=lgbm_classifier tier=1 target=direction pf=0.713 n=32726 gates=FAIL

## [INFO] 2026-08-03 11:10:26 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_135_BTCUSDT_1h_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:10:27 UTC (tier 1)

AUTONOMY screen autog2_135_BTCUSDT_1h_direction_ohlcv_v1 tier=1 proxy_pf=0.750736914131483 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:10:27 UTC (tier 0)

START gen=autog2_135_BTCUSDT_1h_direction_ohlcv_v1_ts BTCUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:11:11 UTC (tier 0)

PREDICTABILITY real=+0.00789 p=0.0476 surr_q95=-0.00021 surr_max=-0.00007 draws=20 passed=True

## [INFO] 2026-08-03 11:11:31 UTC (tier 1)

trial `d48d76c3-9e47-4157-b032-f5ab22a4c848` model=ridge tier=1 target=direction pf=0.761 n=2772 gates=FAIL

## [INFO] 2026-08-03 11:11:31 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_135_BTCUSDT_1h_direction_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:11:31 UTC (tier 1)

AUTONOMY tradesim autog2_135_BTCUSDT_1h_direction_ohlcv_v1 tier=1 proxy_pf=0.7612627163516539

## [INFO] 2026-08-03 11:11:31 UTC (tier 0)

START gen=autog2_136_BTCUSDT_1h_direction_indicators_v1 BTCUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 11:12:10 UTC (tier 0)

PREDICTABILITY real=-0.00281 p=0.7619 surr_q95=+0.00097 surr_max=+0.00103 draws=20 passed=False

## [INFO] 2026-08-03 11:12:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:12:16 UTC (tier 0)

trial `b169d63e-6063-4f8f-93e1-290914e1ddeb` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:12:17 UTC (tier 0)

trial `b8831683-af75-4938-bd00-c801dc18024b` model=ridge tier=0 target=direction pf=0.786 n=13944 gates=FAIL

## [INFO] 2026-08-03 11:12:21 UTC (tier 0)

trial `dcf46613-9c62-42a7-8bb3-3b5dc47bcd56` model=lgbm_regressor tier=0 target=direction pf=0.703 n=16419 gates=FAIL

## [INFO] 2026-08-03 11:12:33 UTC (tier 0)

trial `2679b58d-d3c4-4109-ba7f-e541cc85e6d0` model=lgbm_classifier tier=0 target=direction pf=0.690 n=32709 gates=FAIL

## [INFO] 2026-08-03 11:12:33 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_136_BTCUSDT_1h_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:12:33 UTC (tier 0)

AUTONOMY screen autog2_136_BTCUSDT_1h_direction_indicators_v1 tier=0 proxy_pf=0.7864948790990453 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:12:33 UTC (tier 0)

START gen=autog2_137_BTCUSDT_1h_direction_pivot_v1 BTCUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 11:12:45 UTC (tier 0)

PREDICTABILITY real=+0.00829 p=0.0476 surr_q95=+0.00090 surr_max=+0.00094 draws=20 passed=True

## [INFO] 2026-08-03 11:12:48 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:12:48 UTC (tier 0)

trial `4260d392-b883-417c-a424-66e5bd2cb6b4` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:12:48 UTC (tier 1)

trial `c4c04b0f-1929-4f5a-8c71-f4364a12e10c` model=ridge tier=1 target=direction pf=0.705 n=8280 gates=FAIL

## [INFO] 2026-08-03 11:12:52 UTC (tier 1)

trial `0826c60d-0126-4146-99ae-5f8f39521626` model=lgbm_regressor tier=1 target=direction pf=0.718 n=14378 gates=FAIL

## [INFO] 2026-08-03 11:13:01 UTC (tier 1)

trial `10fd11d3-73da-4c21-b33f-7b3e9ccb03ce` model=lgbm_classifier tier=1 target=direction pf=0.713 n=32840 gates=FAIL

## [INFO] 2026-08-03 11:13:01 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_137_BTCUSDT_1h_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:13:01 UTC (tier 1)

AUTONOMY screen autog2_137_BTCUSDT_1h_direction_pivot_v1 tier=1 proxy_pf=0.7176946924235061 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:13:01 UTC (tier 0)

START gen=autog2_137_BTCUSDT_1h_direction_pivot_v1_ts BTCUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 11:13:13 UTC (tier 0)

PREDICTABILITY real=+0.00829 p=0.0476 surr_q95=+0.00090 surr_max=+0.00094 draws=20 passed=True

## [INFO] 2026-08-03 11:13:33 UTC (tier 1)

trial `e774d106-6e81-4810-9847-147a3fc7979d` model=lgbm_regressor tier=1 target=direction pf=0.834 n=2889 gates=FAIL

## [INFO] 2026-08-03 11:13:33 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_137_BTCUSDT_1h_direction_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:13:33 UTC (tier 1)

AUTONOMY tradesim autog2_137_BTCUSDT_1h_direction_pivot_v1 tier=1 proxy_pf=0.8342632110592022

## [INFO] 2026-08-03 11:13:33 UTC (tier 0)

START gen=autog2_138_ETHUSDT_1h_direction_ohlcv_v1 ETHUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:14:00 UTC (tier 0)

PREDICTABILITY real=+0.00392 p=0.0476 surr_q95=-0.00007 surr_max=-0.00003 draws=20 passed=True

## [INFO] 2026-08-03 11:14:03 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:14:03 UTC (tier 0)

trial `d0e1d66d-f249-40fb-8f96-98b6509b578c` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:14:04 UTC (tier 1)

trial `6c810643-2389-4c74-90d6-05f6ab0b3a7a` model=ridge tier=1 target=direction pf=0.803 n=7808 gates=FAIL

## [INFO] 2026-08-03 11:14:09 UTC (tier 1)

trial `1e05cdaa-6f37-4d5f-9655-35245e88719c` model=lgbm_regressor tier=1 target=direction pf=0.787 n=16131 gates=FAIL

## [INFO] 2026-08-03 11:14:21 UTC (tier 1)

trial `4e83ad1a-ed8f-4b58-be68-51ca95040d9c` model=lgbm_classifier tier=1 target=direction pf=0.754 n=32855 gates=FAIL

## [INFO] 2026-08-03 11:14:21 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_138_ETHUSDT_1h_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:14:21 UTC (tier 1)

AUTONOMY screen autog2_138_ETHUSDT_1h_direction_ohlcv_v1 tier=1 proxy_pf=0.8033910526886388 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:14:21 UTC (tier 0)

START gen=autog2_138_ETHUSDT_1h_direction_ohlcv_v1_ts ETHUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:14:43 UTC (tier 0)

PREDICTABILITY real=+0.00392 p=0.0476 surr_q95=-0.00007 surr_max=-0.00003 draws=20 passed=True

## [INFO] 2026-08-03 11:14:53 UTC (tier 1)

trial `9bc1e2ec-5d7b-4c95-b8c6-d80fa6dda556` model=ridge tier=1 target=direction pf=0.745 n=3295 gates=FAIL

## [INFO] 2026-08-03 11:14:53 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_138_ETHUSDT_1h_direction_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:14:53 UTC (tier 1)

AUTONOMY tradesim autog2_138_ETHUSDT_1h_direction_ohlcv_v1 tier=1 proxy_pf=0.7454965465225042

## [INFO] 2026-08-03 11:14:53 UTC (tier 0)

START gen=autog2_139_ETHUSDT_1h_direction_indicators_v1 ETHUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 11:15:18 UTC (tier 0)

PREDICTABILITY real=+0.00459 p=0.0476 surr_q95=+0.00036 surr_max=+0.00108 draws=20 passed=True

## [INFO] 2026-08-03 11:15:21 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:15:21 UTC (tier 0)

trial `d92abf71-f13d-4a8a-9b5f-17313a5644fd` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:15:22 UTC (tier 1)

trial `25b991c5-6999-44bf-836f-611eb6897b34` model=ridge tier=1 target=direction pf=0.844 n=7179 gates=FAIL

## [INFO] 2026-08-03 11:15:26 UTC (tier 1)

trial `7dbfb78d-b163-4459-ba33-05fc9fbcdd6a` model=lgbm_regressor tier=1 target=direction pf=0.761 n=19781 gates=FAIL

## [INFO] 2026-08-03 11:15:37 UTC (tier 1)

trial `fa325fbf-cd7c-4698-b735-3d05b6ac9e79` model=lgbm_classifier tier=1 target=direction pf=0.727 n=32856 gates=FAIL

## [INFO] 2026-08-03 11:15:37 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_139_ETHUSDT_1h_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:15:37 UTC (tier 1)

AUTONOMY screen autog2_139_ETHUSDT_1h_direction_indicators_v1 tier=1 proxy_pf=0.8441927944379599 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:15:37 UTC (tier 0)

START gen=autog2_139_ETHUSDT_1h_direction_indicators_v1_ts ETHUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 11:16:07 UTC (tier 0)

PREDICTABILITY real=+0.00459 p=0.0476 surr_q95=+0.00036 surr_max=+0.00108 draws=20 passed=True

## [INFO] 2026-08-03 11:16:18 UTC (tier 1)

trial `a3338453-ffd1-4af2-8154-7b65f3a3bdd6` model=ridge tier=1 target=direction pf=0.763 n=2886 gates=FAIL

## [INFO] 2026-08-03 11:16:18 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_139_ETHUSDT_1h_direction_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:16:18 UTC (tier 1)

AUTONOMY tradesim autog2_139_ETHUSDT_1h_direction_indicators_v1 tier=1 proxy_pf=0.7630292200518085

## [INFO] 2026-08-03 11:16:18 UTC (tier 0)

START gen=autog2_140_ETHUSDT_1h_direction_pivot_v1 ETHUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 11:16:37 UTC (tier 0)

PREDICTABILITY real=+0.00190 p=0.0476 surr_q95=+0.00011 surr_max=+0.00121 draws=20 passed=True

## [INFO] 2026-08-03 11:16:40 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:16:40 UTC (tier 0)

trial `a031a099-4675-47fb-9056-bd21a4888a71` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:16:40 UTC (tier 1)

trial `0cc1021d-3fd4-4d98-a654-def4b06c886b` model=ridge tier=1 target=direction pf=0.635 n=4845 gates=FAIL

## [INFO] 2026-08-03 11:16:44 UTC (tier 1)

trial `0c14427e-720d-4a4c-833c-327ad494ad91` model=lgbm_regressor tier=1 target=direction pf=0.787 n=13467 gates=FAIL

## [INFO] 2026-08-03 11:16:52 UTC (tier 1)

trial `dcc855b3-3438-4bf8-a53d-cbd29997ad2a` model=lgbm_classifier tier=1 target=direction pf=0.748 n=32856 gates=FAIL

## [INFO] 2026-08-03 11:16:52 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_140_ETHUSDT_1h_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:16:52 UTC (tier 1)

AUTONOMY screen autog2_140_ETHUSDT_1h_direction_pivot_v1 tier=1 proxy_pf=0.7870325500887417 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:16:52 UTC (tier 0)

START gen=autog2_140_ETHUSDT_1h_direction_pivot_v1_ts ETHUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 11:17:15 UTC (tier 0)

PREDICTABILITY real=+0.00190 p=0.0476 surr_q95=+0.00011 surr_max=+0.00121 draws=20 passed=True

## [INFO] 2026-08-03 11:17:31 UTC (tier 1)

trial `0ff4214c-fb56-48ee-b7f7-48f989ae1145` model=lgbm_regressor tier=1 target=direction pf=0.838 n=4140 gates=FAIL

## [INFO] 2026-08-03 11:17:31 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_140_ETHUSDT_1h_direction_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:17:31 UTC (tier 1)

AUTONOMY tradesim autog2_140_ETHUSDT_1h_direction_pivot_v1 tier=1 proxy_pf=0.8378145601978286

## [INFO] 2026-08-03 11:17:31 UTC (tier 0)

START gen=autog2_141_SOLUSDT_1h_direction_ohlcv_v1 SOLUSDT 1h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:17:53 UTC (tier 0)

PREDICTABILITY real=+0.00058 p=0.0952 surr_q95=+0.00029 surr_max=+0.00067 draws=20 passed=False

## [INFO] 2026-08-03 11:17:56 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:17:56 UTC (tier 0)

trial `120c0627-732d-44fb-b4aa-17dc18e1c932` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:17:56 UTC (tier 0)

trial `582e3198-50ff-4f7b-acc2-5f9bdcb471ab` model=ridge tier=0 target=direction pf=0.881 n=4872 gates=FAIL

## [INFO] 2026-08-03 11:18:01 UTC (tier 0)

trial `38b102d2-aee0-41d9-8548-c0896a1281f5` model=lgbm_regressor tier=0 target=direction pf=0.921 n=14592 gates=FAIL

## [INFO] 2026-08-03 11:18:12 UTC (tier 0)

trial `52cbc58f-7c27-4d92-8772-b304630bcc3a` model=lgbm_classifier tier=0 target=direction pf=0.874 n=32854 gates=FAIL

## [INFO] 2026-08-03 11:18:12 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_141_SOLUSDT_1h_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:18:12 UTC (tier 0)

AUTONOMY screen autog2_141_SOLUSDT_1h_direction_ohlcv_v1 tier=0 proxy_pf=0.9213430401159978 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:18:12 UTC (tier 0)

START gen=autog2_142_SOLUSDT_1h_direction_indicators_v1 SOLUSDT 1h target=direction space=indicators_v1

## [INFO] 2026-08-03 11:18:33 UTC (tier 0)

PREDICTABILITY real=-0.00553 p=0.8095 surr_q95=+0.00075 surr_max=+0.00312 draws=20 passed=False

## [INFO] 2026-08-03 11:18:38 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:18:38 UTC (tier 0)

trial `0c45809c-1433-4cfe-974d-8ae739242431` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:18:38 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00068 skill_surrogate=+0.00036

## [INFO] 2026-08-03 11:18:38 UTC (tier 0)

trial `e1445bda-718a-4133-916f-d8d7a359e5c4` model=ridge tier=0 target=direction pf=0.950 n=10128 gates=FAIL

## [INFO] 2026-08-03 11:18:43 UTC (tier 0)

trial `e383c494-9561-4655-8f32-dd227d480b52` model=lgbm_regressor tier=0 target=direction pf=0.918 n=15051 gates=FAIL

## [INFO] 2026-08-03 11:18:57 UTC (tier 0)

trial `69a0c330-0e7a-44fb-bbf3-40aa4bafa007` model=lgbm_classifier tier=0 target=direction pf=0.860 n=32699 gates=FAIL

## [INFO] 2026-08-03 11:18:57 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_142_SOLUSDT_1h_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:18:57 UTC (tier 0)

AUTONOMY screen autog2_142_SOLUSDT_1h_direction_indicators_v1 tier=0 proxy_pf=0.9498703530068965 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:18:57 UTC (tier 0)

START gen=autog2_143_SOLUSDT_1h_direction_pivot_v1 SOLUSDT 1h target=direction space=pivot_v1

## [INFO] 2026-08-03 11:19:10 UTC (tier 0)

PREDICTABILITY real=-0.00256 p=0.9048 surr_q95=+0.00118 surr_max=+0.00127 draws=20 passed=False

## [INFO] 2026-08-03 11:19:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:19:16 UTC (tier 0)

trial `8add5313-2607-4ba1-a822-d68dd9ea365d` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:19:16 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00065 skill_surrogate=+0.00021

## [INFO] 2026-08-03 11:19:16 UTC (tier 0)

trial `4010f964-2dac-475d-b0f3-a645f17c7935` model=ridge tier=0 target=direction pf=0.652 n=2894 gates=FAIL

## [INFO] 2026-08-03 11:19:20 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00007 skill_surrogate=+0.00001

## [INFO] 2026-08-03 11:19:20 UTC (tier 0)

trial `42ec6894-607c-40e4-b188-a1d00d6f479a` model=lgbm_regressor tier=0 target=direction pf=0.834 n=9155 gates=FAIL

## [INFO] 2026-08-03 11:19:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.00978 skill_surrogate=-0.00024

## [INFO] 2026-08-03 11:19:32 UTC (tier 0)

trial `833c874b-c803-4ad5-ba58-dbd59a6f5a95` model=lgbm_classifier tier=0 target=direction pf=0.840 n=32856 gates=FAIL

## [INFO] 2026-08-03 11:19:32 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_143_SOLUSDT_1h_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:19:32 UTC (tier 0)

AUTONOMY screen autog2_143_SOLUSDT_1h_direction_pivot_v1 tier=0 proxy_pf=0.8395990728486454 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:19:32 UTC (tier 0)

START gen=autog2_144_BTCUSDT_4h_direction_ohlcv_v1 BTCUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:19:44 UTC (tier 0)

PREDICTABILITY real=+0.00571 p=0.0476 surr_q95=+0.00297 surr_max=+0.00351 draws=20 passed=True

## [INFO] 2026-08-03 11:19:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:19:46 UTC (tier 0)

trial `8795049a-9368-499b-828b-3b6c77be9be3` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:19:46 UTC (tier 1)

trial `15fb0b52-d65e-468c-97b2-2374017ee3f2` model=ridge tier=1 target=direction pf=0.950 n=1880 gates=FAIL

## [INFO] 2026-08-03 11:19:54 UTC (tier 1)

trial `6f64efd1-ac97-4071-88b7-0d3e26202c2e` model=lgbm_regressor tier=1 target=direction pf=0.842 n=5020 gates=FAIL

## [INFO] 2026-08-03 11:20:18 UTC (tier 1)

trial `34a55788-506c-4685-9022-7d89f21e6ba6` model=lgbm_classifier tier=1 target=direction pf=0.834 n=8204 gates=FAIL

## [INFO] 2026-08-03 11:20:18 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_144_BTCUSDT_4h_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:20:18 UTC (tier 1)

AUTONOMY screen autog2_144_BTCUSDT_4h_direction_ohlcv_v1 tier=1 proxy_pf=0.9497434992812297 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:20:18 UTC (tier 0)

START gen=autog2_144_BTCUSDT_4h_direction_ohlcv_v1_ts BTCUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:20:42 UTC (tier 0)

PREDICTABILITY real=+0.00571 p=0.0476 surr_q95=+0.00297 surr_max=+0.00351 draws=20 passed=True

## [INFO] 2026-08-03 11:20:52 UTC (tier 1)

trial `4a060908-622f-4a2e-bf83-bc4336c20456` model=ridge tier=1 target=direction pf=0.807 n=1097 gates=FAIL

## [INFO] 2026-08-03 11:20:52 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_144_BTCUSDT_4h_direction_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:20:52 UTC (tier 1)

AUTONOMY tradesim autog2_144_BTCUSDT_4h_direction_ohlcv_v1 tier=1 proxy_pf=0.8069995324330064

## [INFO] 2026-08-03 11:20:52 UTC (tier 0)

START gen=autog2_145_BTCUSDT_4h_direction_indicators_v1 BTCUSDT 4h target=direction space=indicators_v1

## [INFO] 2026-08-03 11:21:07 UTC (tier 0)

PREDICTABILITY real=-0.01554 p=0.6190 surr_q95=-0.00120 surr_max=+0.00292 draws=20 passed=False

## [INFO] 2026-08-03 11:21:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:21:08 UTC (tier 0)

trial `7d50d6ea-7646-4bea-830c-2472e6a93aa6` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:21:08 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00853 skill_surrogate=+0.00185

## [INFO] 2026-08-03 11:21:08 UTC (tier 0)

trial `38963776-3532-43f8-b064-1cec8a32bbeb` model=ridge tier=0 target=direction pf=0.777 n=4167 gates=FAIL

## [INFO] 2026-08-03 11:21:14 UTC (tier 0)

trial `779127d8-362d-4e82-b04c-e0657049c1e8` model=lgbm_regressor tier=0 target=direction pf=0.775 n=5963 gates=FAIL

## [INFO] 2026-08-03 11:21:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.02398 skill_surrogate=+0.00509

## [INFO] 2026-08-03 11:21:32 UTC (tier 0)

trial `c5249437-a035-427e-9cf7-53f169bb1ea0` model=lgbm_classifier tier=0 target=direction pf=0.817 n=8213 gates=FAIL

## [INFO] 2026-08-03 11:21:32 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_145_BTCUSDT_4h_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:21:32 UTC (tier 0)

AUTONOMY screen autog2_145_BTCUSDT_4h_direction_indicators_v1 tier=0 proxy_pf=0.8173885359250557 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:21:32 UTC (tier 0)

START gen=autog2_146_BTCUSDT_4h_direction_pivot_v1 BTCUSDT 4h target=direction space=pivot_v1

## [INFO] 2026-08-03 11:21:42 UTC (tier 0)

PREDICTABILITY real=-0.00009 p=0.1429 surr_q95=+0.00024 surr_max=+0.00443 draws=20 passed=False

## [INFO] 2026-08-03 11:21:43 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:21:43 UTC (tier 0)

trial `9c195d2e-f6fa-466e-a25e-03948f34b253` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:21:43 UTC (tier 0)

trial `959737cf-63e3-4629-b47e-cdc075a85303` model=ridge tier=0 target=direction pf=0.900 n=1811 gates=FAIL

## [INFO] 2026-08-03 11:21:50 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=+0.00389 skill_surrogate=+0.00492

## [INFO] 2026-08-03 11:21:50 UTC (tier 0)

trial `3927e9e5-a05b-451b-96f9-670ecbb5fc01` model=lgbm_regressor tier=0 target=direction pf=0.806 n=4372 gates=FAIL

## [INFO] 2026-08-03 11:22:05 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-0.00055 skill_surrogate=+0.00203

## [INFO] 2026-08-03 11:22:05 UTC (tier 0)

trial `01ce3580-fe78-4689-89bd-4c70d755299c` model=lgbm_classifier tier=0 target=direction pf=0.846 n=8210 gates=FAIL

## [INFO] 2026-08-03 11:22:05 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_146_BTCUSDT_4h_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:22:05 UTC (tier 0)

AUTONOMY screen autog2_146_BTCUSDT_4h_direction_pivot_v1 tier=0 proxy_pf=0.9001411636103439 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:22:05 UTC (tier 0)

START gen=autog2_147_ETHUSDT_4h_direction_ohlcv_v1 ETHUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:22:25 UTC (tier 0)

PREDICTABILITY real=+0.00359 p=0.0476 surr_q95=-0.00075 surr_max=+0.00030 draws=20 passed=True

## [INFO] 2026-08-03 11:22:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:22:27 UTC (tier 0)

trial `17f6b42a-25c3-420d-b9d3-197167727e4e` model=hist_mean tier=0 target=direction pf=0.738 n=1638 gates=FAIL

## [INFO] 2026-08-03 11:22:27 UTC (tier 1)

trial `7031d030-bec8-4e32-926c-2d958cf0cc15` model=ridge tier=1 target=direction pf=0.832 n=2641 gates=FAIL

## [INFO] 2026-08-03 11:22:34 UTC (tier 1)

trial `fa39d8b5-1c32-422d-b20c-197466660ad3` model=lgbm_regressor tier=1 target=direction pf=0.939 n=5380 gates=FAIL

## [INFO] 2026-08-03 11:22:50 UTC (tier 1)

trial `755baeeb-88ba-4811-ad15-e6a7a9675f9f` model=lgbm_classifier tier=1 target=direction pf=0.903 n=8214 gates=FAIL

## [INFO] 2026-08-03 11:22:50 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_147_ETHUSDT_4h_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:22:50 UTC (tier 1)

AUTONOMY screen autog2_147_ETHUSDT_4h_direction_ohlcv_v1 tier=1 proxy_pf=0.9389995321765089 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:22:50 UTC (tier 0)

START gen=autog2_147_ETHUSDT_4h_direction_ohlcv_v1_ts ETHUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:23:03 UTC (tier 0)

PREDICTABILITY real=+0.00359 p=0.0476 surr_q95=-0.00075 surr_max=+0.00030 draws=20 passed=True

## [INFO] 2026-08-03 11:23:19 UTC (tier 1)

trial `0addb4e2-8109-44c1-b087-ebe7956e981a` model=lgbm_regressor tier=1 target=direction pf=0.831 n=2935 gates=FAIL

## [INFO] 2026-08-03 11:23:19 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_147_ETHUSDT_4h_direction_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:23:19 UTC (tier 1)

AUTONOMY tradesim autog2_147_ETHUSDT_4h_direction_ohlcv_v1 tier=1 proxy_pf=0.8313016540484222

## [INFO] 2026-08-03 11:23:19 UTC (tier 0)

START gen=autog2_148_ETHUSDT_4h_direction_indicators_v1 ETHUSDT 4h target=direction space=indicators_v1

## [INFO] 2026-08-03 11:23:33 UTC (tier 0)

PREDICTABILITY real=-0.01466 p=0.8095 surr_q95=-0.00081 surr_max=+0.00570 draws=20 passed=False

## [INFO] 2026-08-03 11:23:34 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:23:34 UTC (tier 0)

trial `a5ee7caa-c739-464b-806b-c910d3b6f028` model=hist_mean tier=0 target=direction pf=0.738 n=1638 gates=FAIL

## [INFO] 2026-08-03 11:23:34 UTC (tier 0)

trial `b9ac7c1b-4797-4c13-a40c-1389afd0849c` model=ridge tier=0 target=direction pf=0.898 n=4376 gates=FAIL

## [INFO] 2026-08-03 11:23:41 UTC (tier 0)

trial `ce290988-e485-4f22-bb56-140a175f0fa3` model=lgbm_regressor tier=0 target=direction pf=0.967 n=5856 gates=FAIL

## [INFO] 2026-08-03 11:24:04 UTC (tier 0)

trial `c900b0da-fea4-48fe-bca9-b0efc4d73c12` model=lgbm_classifier tier=0 target=direction pf=0.915 n=8214 gates=FAIL

## [INFO] 2026-08-03 11:24:04 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_148_ETHUSDT_4h_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:24:04 UTC (tier 0)

AUTONOMY screen autog2_148_ETHUSDT_4h_direction_indicators_v1 tier=0 proxy_pf=0.9667334031442565 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:24:04 UTC (tier 0)

START gen=autog2_149_ETHUSDT_4h_direction_pivot_v1 ETHUSDT 4h target=direction space=pivot_v1

## [INFO] 2026-08-03 11:24:15 UTC (tier 0)

PREDICTABILITY real=-0.00215 p=0.3810 surr_q95=+0.00087 surr_max=+0.00130 draws=20 passed=False

## [INFO] 2026-08-03 11:24:18 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:24:18 UTC (tier 0)

trial `df8def50-4593-45bb-97ad-f9bc0a2ff568` model=hist_mean tier=0 target=direction pf=0.738 n=1638 gates=FAIL

## [INFO] 2026-08-03 11:24:18 UTC (tier 0)

trial `af6aa600-ef6f-49ce-9abe-25e72b8181fc` model=ridge tier=0 target=direction pf=0.855 n=3533 gates=FAIL

## [INFO] 2026-08-03 11:24:28 UTC (tier 0)

trial `7d62961b-5944-476a-9936-fb75b6aa571f` model=lgbm_regressor tier=0 target=direction pf=0.918 n=4885 gates=FAIL

## [INFO] 2026-08-03 11:24:53 UTC (tier 0)

trial `8e0744f7-7318-4e6a-ba36-584d3cc09afa` model=lgbm_classifier tier=0 target=direction pf=0.905 n=8214 gates=FAIL

## [INFO] 2026-08-03 11:24:53 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_149_ETHUSDT_4h_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:24:53 UTC (tier 0)

AUTONOMY screen autog2_149_ETHUSDT_4h_direction_pivot_v1 tier=0 proxy_pf=0.9177890930529463 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:24:54 UTC (tier 0)

START gen=autog2_150_SOLUSDT_4h_direction_ohlcv_v1 SOLUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:25:12 UTC (tier 0)

PREDICTABILITY real=+0.00339 p=0.0476 surr_q95=-0.00013 surr_max=+0.00033 draws=20 passed=True

## [INFO] 2026-08-03 11:25:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:25:12 UTC (tier 0)

trial `1cea8c4b-8f29-4030-b42e-caad95ba62b0` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:25:12 UTC (tier 1)

trial `f0831d0d-44ba-4f61-b97b-99eb21f149fa` model=ridge tier=1 target=direction pf=0.978 n=3315 gates=FAIL

## [INFO] 2026-08-03 11:25:17 UTC (tier 1)

trial `9cc622e2-a536-45eb-909b-fc26d8aed47b` model=lgbm_regressor tier=1 target=direction pf=0.975 n=5492 gates=FAIL

## [INFO] 2026-08-03 11:25:24 UTC (tier 1)

trial `3b66d0a6-40b0-4d74-b725-43eca73bea3a` model=lgbm_classifier tier=1 target=direction pf=0.989 n=8214 gates=FAIL

## [INFO] 2026-08-03 11:25:24 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_150_SOLUSDT_4h_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:25:24 UTC (tier 1)

AUTONOMY screen autog2_150_SOLUSDT_4h_direction_ohlcv_v1 tier=1 proxy_pf=0.989292539317457 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:25:24 UTC (tier 0)

START gen=autog2_150_SOLUSDT_4h_direction_ohlcv_v1_ts SOLUSDT 4h target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:25:33 UTC (tier 0)

PREDICTABILITY real=+0.00339 p=0.0476 surr_q95=-0.00013 surr_max=+0.00033 draws=20 passed=True

## [INFO] 2026-08-03 11:25:44 UTC (tier 1)

trial `39cb0459-b45e-49c8-91a6-e9075445181e` model=lgbm_classifier tier=1 target=direction pf=0.795 n=5751 gates=FAIL

## [INFO] 2026-08-03 11:25:44 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_150_SOLUSDT_4h_direction_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:25:44 UTC (tier 1)

AUTONOMY tradesim autog2_150_SOLUSDT_4h_direction_ohlcv_v1 tier=1 proxy_pf=0.7954635197157351

## [INFO] 2026-08-03 11:25:44 UTC (tier 0)

START gen=autog2_151_SOLUSDT_4h_direction_indicators_v1 SOLUSDT 4h target=direction space=indicators_v1

## [INFO] 2026-08-03 11:25:51 UTC (tier 0)

PREDICTABILITY real=+0.00113 p=0.0476 surr_q95=-0.00297 surr_max=-0.00164 draws=20 passed=True

## [INFO] 2026-08-03 11:25:52 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:25:52 UTC (tier 0)

trial `1cb3fb0b-87d8-47fb-8911-39002a9a3363` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:25:52 UTC (tier 1)

trial `1cb979e2-0a87-4ee6-a3e4-b7cf0503581e` model=ridge tier=1 target=direction pf=0.943 n=4164 gates=FAIL

## [INFO] 2026-08-03 11:25:54 UTC (tier 1)

trial `cb0b2385-62dd-46f1-8609-d1a99648f6d4` model=lgbm_regressor tier=1 target=direction pf=0.917 n=5779 gates=FAIL

## [INFO] 2026-08-03 11:25:59 UTC (tier 1)

trial `e4d8ef38-3813-4a68-8763-f872cac71d55` model=lgbm_classifier tier=1 target=direction pf=0.918 n=8214 gates=FAIL

## [INFO] 2026-08-03 11:25:59 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_151_SOLUSDT_4h_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:25:59 UTC (tier 1)

AUTONOMY screen autog2_151_SOLUSDT_4h_direction_indicators_v1 tier=1 proxy_pf=0.9428943384111805 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:25:59 UTC (tier 0)

START gen=autog2_151_SOLUSDT_4h_direction_indicators_v1_ts SOLUSDT 4h target=direction space=indicators_v1

## [INFO] 2026-08-03 11:26:06 UTC (tier 0)

PREDICTABILITY real=+0.00113 p=0.0476 surr_q95=-0.00297 surr_max=-0.00164 draws=20 passed=True

## [INFO] 2026-08-03 11:26:09 UTC (tier 1)

trial `f381719c-7c8d-4789-9737-6042455dcd2b` model=ridge tier=1 target=direction pf=0.825 n=3077 gates=FAIL

## [INFO] 2026-08-03 11:26:09 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_151_SOLUSDT_4h_direction_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:26:09 UTC (tier 1)

AUTONOMY tradesim autog2_151_SOLUSDT_4h_direction_indicators_v1 tier=1 proxy_pf=0.8249212417771661

## [INFO] 2026-08-03 11:26:09 UTC (tier 0)

START gen=autog2_152_SOLUSDT_4h_direction_pivot_v1 SOLUSDT 4h target=direction space=pivot_v1

## [INFO] 2026-08-03 11:26:11 UTC (tier 0)

PREDICTABILITY real=-0.00838 p=0.9048 surr_q95=+0.00217 surr_max=+0.00439 draws=20 passed=False

## [INFO] 2026-08-03 11:26:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:26:12 UTC (tier 0)

trial `a40c871b-7c25-4801-9ace-c2e0da886ef1` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:26:12 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00052 skill_surrogate=+0.00067

## [INFO] 2026-08-03 11:26:12 UTC (tier 0)

trial `91c445d9-59c4-4793-b41d-2d369d2acba9` model=ridge tier=0 target=direction pf=0.801 n=2244 gates=FAIL

## [INFO] 2026-08-03 11:26:13 UTC (tier 0)

trial `ff73e956-4baa-462b-8b81-3fc8111b8a00` model=lgbm_regressor tier=0 target=direction pf=0.935 n=4764 gates=FAIL

## [INFO] 2026-08-03 11:26:17 UTC (tier 0)

trial `3803eda7-7142-493f-80a8-bbd8fe078d81` model=lgbm_classifier tier=0 target=direction pf=0.921 n=8214 gates=FAIL

## [INFO] 2026-08-03 11:26:17 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_152_SOLUSDT_4h_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:26:17 UTC (tier 0)

AUTONOMY screen autog2_152_SOLUSDT_4h_direction_pivot_v1 tier=0 proxy_pf=0.9351275466483436 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:26:17 UTC (tier 0)

START gen=autog2_153_BTCUSDT_15m_direction_ohlcv_v1 BTCUSDT 15m target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:28:24 UTC (tier 0)

PREDICTABILITY real=+0.00985 p=0.0476 surr_q95=-0.00003 surr_max=+0.00004 draws=20 passed=True

## [INFO] 2026-08-03 11:28:58 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:28:58 UTC (tier 0)

trial `50e39dcb-3a7c-4dff-995b-f2ec098a9f0a` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:29:00 UTC (tier 1)

trial `a34a4938-adcb-4f36-af38-fe708d1e9811` model=ridge tier=1 target=direction pf=0.477 n=47939 gates=FAIL

## [INFO] 2026-08-03 11:29:21 UTC (tier 1)

trial `5b8e2d1b-fd2f-4019-804a-bb127d287091` model=lgbm_regressor tier=1 target=direction pf=0.463 n=56062 gates=FAIL

## [INFO] 2026-08-03 11:29:51 UTC (tier 1)

trial `de521dc3-d30b-4872-9329-097d886cddaf` model=lgbm_classifier tier=1 target=direction pf=0.467 n=130835 gates=FAIL

## [INFO] 2026-08-03 11:29:51 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_153_BTCUSDT_15m_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:29:51 UTC (tier 1)

AUTONOMY screen autog2_153_BTCUSDT_15m_direction_ohlcv_v1 tier=1 proxy_pf=0.4765989651595006 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:29:51 UTC (tier 0)

START gen=autog2_153_BTCUSDT_15m_direction_ohlcv_v1_ts BTCUSDT 15m target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:31:40 UTC (tier 0)

PREDICTABILITY real=+0.00985 p=0.0476 surr_q95=-0.00003 surr_max=+0.00004 draws=20 passed=True

## [INFO] 2026-08-03 11:32:51 UTC (tier 1)

trial `bbaf8ce2-b323-458b-bb55-11672c8a70f9` model=ridge tier=1 target=direction pf=0.740 n=3709 gates=FAIL

## [INFO] 2026-08-03 11:32:51 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_153_BTCUSDT_15m_direction_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:32:51 UTC (tier 1)

AUTONOMY tradesim autog2_153_BTCUSDT_15m_direction_ohlcv_v1 tier=1 proxy_pf=0.7398416386373508

## [INFO] 2026-08-03 11:32:51 UTC (tier 0)

START gen=autog2_154_BTCUSDT_15m_direction_indicators_v1 BTCUSDT 15m target=direction space=indicators_v1

## [INFO] 2026-08-03 11:34:42 UTC (tier 0)

PREDICTABILITY real=+0.00323 p=0.0476 surr_q95=+0.00008 surr_max=+0.00016 draws=20 passed=True

## [INFO] 2026-08-03 11:35:06 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:35:06 UTC (tier 0)

trial `5897dec8-1142-4e51-aacf-c581dae73144` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:35:07 UTC (tier 1)

trial `8d5eee10-9882-42f9-a038-1f2384995252` model=ridge tier=1 target=direction pf=0.497 n=39065 gates=FAIL

## [INFO] 2026-08-03 11:35:21 UTC (tier 1)

trial `0e926791-a2ca-45e4-8e75-162f37edfdf9` model=lgbm_regressor tier=1 target=direction pf=0.487 n=60660 gates=FAIL

## [INFO] 2026-08-03 11:35:46 UTC (tier 1)

trial `0e25a72b-7f41-4887-82d4-427afe9b9fbe` model=lgbm_classifier tier=1 target=direction pf=0.462 n=130999 gates=FAIL

## [INFO] 2026-08-03 11:35:46 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_154_BTCUSDT_15m_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:35:46 UTC (tier 1)

AUTONOMY screen autog2_154_BTCUSDT_15m_direction_indicators_v1 tier=1 proxy_pf=0.4974191429004285 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:35:46 UTC (tier 0)

START gen=autog2_154_BTCUSDT_15m_direction_indicators_v1_ts BTCUSDT 15m target=direction space=indicators_v1

## [INFO] 2026-08-03 11:37:13 UTC (tier 0)

PREDICTABILITY real=+0.00323 p=0.0476 surr_q95=+0.00008 surr_max=+0.00016 draws=20 passed=True

## [INFO] 2026-08-03 11:38:16 UTC (tier 1)

trial `63855240-6689-439e-904f-65064ce4bb48` model=ridge tier=1 target=direction pf=0.767 n=3522 gates=FAIL

## [INFO] 2026-08-03 11:38:16 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_154_BTCUSDT_15m_direction_indicators_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:38:16 UTC (tier 1)

AUTONOMY tradesim autog2_154_BTCUSDT_15m_direction_indicators_v1 tier=1 proxy_pf=0.7670919842298674

## [INFO] 2026-08-03 11:38:16 UTC (tier 0)

START gen=autog2_155_BTCUSDT_15m_direction_pivot_v1 BTCUSDT 15m target=direction space=pivot_v1

## [INFO] 2026-08-03 11:39:40 UTC (tier 0)

PREDICTABILITY real=+0.00617 p=0.0476 surr_q95=+0.00010 surr_max=+0.00022 draws=20 passed=True

## [INFO] 2026-08-03 11:40:58 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:40:58 UTC (tier 0)

trial `77110e65-cedd-4977-b85b-927b940aaeb2` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:40:59 UTC (tier 1)

trial `69932fa2-76b2-410a-aedb-220d5ba9c321` model=ridge tier=1 target=direction pf=0.508 n=33498 gates=FAIL

## [INFO] 2026-08-03 11:41:16 UTC (tier 1)

trial `f649dbb4-c8bc-4bfb-b1e3-2459c7cab06b` model=lgbm_regressor tier=1 target=direction pf=0.475 n=49832 gates=FAIL

## [INFO] 2026-08-03 11:42:57 UTC (tier 1)

trial `24d096cb-380f-42e3-9087-95b09e80db98` model=lgbm_classifier tier=1 target=direction pf=0.466 n=131317 gates=FAIL

## [INFO] 2026-08-03 11:42:57 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_155_BTCUSDT_15m_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:42:57 UTC (tier 1)

AUTONOMY screen autog2_155_BTCUSDT_15m_direction_pivot_v1 tier=1 proxy_pf=0.5079276680864211 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:42:57 UTC (tier 0)

START gen=autog2_155_BTCUSDT_15m_direction_pivot_v1_ts BTCUSDT 15m target=direction space=pivot_v1

## [INFO] 2026-08-03 11:44:41 UTC (tier 0)

PREDICTABILITY real=+0.00617 p=0.0476 surr_q95=+0.00010 surr_max=+0.00022 draws=20 passed=True

## [INFO] 2026-08-03 11:46:45 UTC (tier 1)

trial `7aa5a3d8-49b1-4273-98fd-fc68d11c7176` model=ridge tier=1 target=direction pf=0.739 n=3454 gates=FAIL

## [INFO] 2026-08-03 11:46:45 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_155_BTCUSDT_15m_direction_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:46:45 UTC (tier 1)

AUTONOMY tradesim autog2_155_BTCUSDT_15m_direction_pivot_v1 tier=1 proxy_pf=0.7387362002971228

## [INFO] 2026-08-03 11:46:45 UTC (tier 0)

START gen=autog2_156_ETHUSDT_15m_direction_ohlcv_v1 ETHUSDT 15m target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:48:52 UTC (tier 0)

PREDICTABILITY real=+0.00820 p=0.0476 surr_q95=+0.00002 surr_max=+0.00036 draws=20 passed=True

## [INFO] 2026-08-03 11:49:56 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:49:56 UTC (tier 0)

trial `d7a99ff8-3420-49f1-bf69-18899b7afea5` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:49:57 UTC (tier 1)

trial `04fef735-ffba-4efc-9f40-5a1d25c0718a` model=ridge tier=1 target=direction pf=0.573 n=36319 gates=FAIL

## [INFO] 2026-08-03 11:50:07 UTC (tier 1)

trial `3e372f3a-5d61-4ec8-acf9-0f6258fb12d0` model=lgbm_regressor tier=1 target=direction pf=0.561 n=52087 gates=FAIL

## [INFO] 2026-08-03 11:50:31 UTC (tier 1)

trial `c1df20f5-6d90-469b-8fb6-e303885850f9` model=lgbm_classifier tier=1 target=direction pf=0.545 n=131409 gates=FAIL

## [INFO] 2026-08-03 11:50:31 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_156_ETHUSDT_15m_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:50:31 UTC (tier 1)

AUTONOMY screen autog2_156_ETHUSDT_15m_direction_ohlcv_v1 tier=1 proxy_pf=0.5730198127728042 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 11:50:31 UTC (tier 0)

START gen=autog2_156_ETHUSDT_15m_direction_ohlcv_v1_ts ETHUSDT 15m target=direction space=ohlcv_v1

## [INFO] 2026-08-03 11:52:33 UTC (tier 0)

PREDICTABILITY real=+0.00820 p=0.0476 surr_q95=+0.00002 surr_max=+0.00036 draws=20 passed=True

## [INFO] 2026-08-03 11:54:45 UTC (tier 1)

trial `0760934f-eb65-4dce-97dd-ea5e1724b03a` model=ridge tier=1 target=direction pf=0.728 n=5194 gates=FAIL

## [INFO] 2026-08-03 11:54:45 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_156_ETHUSDT_15m_direction_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 11:54:45 UTC (tier 1)

AUTONOMY tradesim autog2_156_ETHUSDT_15m_direction_ohlcv_v1 tier=1 proxy_pf=0.728070710465481

## [INFO] 2026-08-03 11:54:45 UTC (tier 0)

START gen=autog2_157_ETHUSDT_15m_direction_indicators_v1 ETHUSDT 15m target=direction space=indicators_v1

## [INFO] 2026-08-03 11:57:38 UTC (tier 0)

PREDICTABILITY real=+0.00498 p=0.0476 surr_q95=-0.00020 surr_max=-0.00013 draws=20 passed=True

## [INFO] 2026-08-03 11:59:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 11:59:09 UTC (tier 0)

trial `f8259904-d9c9-4efd-aa19-eccbeab8fc3c` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 11:59:12 UTC (tier 1)

trial `265b516c-9670-4b59-9732-be43e17dcb48` model=ridge tier=1 target=direction pf=0.586 n=33842 gates=FAIL

## [INFO] 2026-08-03 11:59:36 UTC (tier 1)

trial `f4f3fdee-df61-4c20-b744-43a2e0ca5084` model=lgbm_regressor tier=1 target=direction pf=0.558 n=60286 gates=FAIL

## [INFO] 2026-08-03 12:00:32 UTC (tier 1)

trial `28c0c917-d41b-4999-8577-a611dbbd2acd` model=lgbm_classifier tier=1 target=direction pf=0.540 n=131424 gates=FAIL

## [INFO] 2026-08-03 12:00:32 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_157_ETHUSDT_15m_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 12:00:32 UTC (tier 1)

AUTONOMY screen autog2_157_ETHUSDT_15m_direction_indicators_v1 tier=1 proxy_pf=0.5857055261610974 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 12:00:32 UTC (tier 0)

START gen=autog2_157_ETHUSDT_15m_direction_indicators_v1_ts ETHUSDT 15m target=direction space=indicators_v1

## [INFO] 2026-08-03 12:19:45 UTC (tier 0)

AUTONOMY start 162 combos; gate_revision=g2; parquet_engine=pyarrow; frozen_out=[]; active=['vol_ratio', 'volatility', 'xs_rank', 'quantile', 'fwd_return', 'direction']

## [INFO] 2026-08-03 12:19:46 UTC (tier 0)

START gen=autog2_158_ETHUSDT_15m_direction_pivot_v1 ETHUSDT 15m target=direction space=pivot_v1

## [INFO] 2026-08-03 12:20:52 UTC (tier 0)

PREDICTABILITY real=+0.00510 p=0.0476 surr_q95=+0.00008 surr_max=+0.00050 draws=20 passed=True

## [INFO] 2026-08-03 12:21:53 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 12:21:53 UTC (tier 0)

trial `c21f6cf9-5448-4b25-ba34-dad0f57a8136` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 12:21:54 UTC (tier 1)

trial `11586f0d-3f4c-42ae-9290-41e25ae84696` model=ridge tier=1 target=direction pf=0.580 n=29062 gates=FAIL

## [INFO] 2026-08-03 12:22:16 UTC (tier 1)

trial `2d418417-aba6-4011-b4c4-19b81b6574e1` model=lgbm_regressor tier=1 target=direction pf=0.552 n=48712 gates=FAIL

## [INFO] 2026-08-03 12:22:32 UTC (tier 1)

trial `25fd076e-d2ef-4e3b-8fcb-4a2a21d59d1b` model=lgbm_classifier tier=1 target=direction pf=0.538 n=131424 gates=FAIL

## [INFO] 2026-08-03 12:22:32 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_158_ETHUSDT_15m_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 12:22:32 UTC (tier 1)

AUTONOMY screen autog2_158_ETHUSDT_15m_direction_pivot_v1 tier=1 proxy_pf=0.5799188826928021 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 12:22:32 UTC (tier 0)

START gen=autog2_158_ETHUSDT_15m_direction_pivot_v1_ts ETHUSDT 15m target=direction space=pivot_v1

## [INFO] 2026-08-03 12:23:21 UTC (tier 0)

PREDICTABILITY real=+0.00510 p=0.0476 surr_q95=+0.00008 surr_max=+0.00050 draws=20 passed=True

## [INFO] 2026-08-03 12:24:14 UTC (tier 1)

trial `16905355-0224-4cec-a1ba-e5f5811b5daf` model=ridge tier=1 target=direction pf=0.714 n=4719 gates=FAIL

## [INFO] 2026-08-03 12:24:14 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_158_ETHUSDT_15m_direction_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 12:24:14 UTC (tier 1)

AUTONOMY tradesim autog2_158_ETHUSDT_15m_direction_pivot_v1 tier=1 proxy_pf=0.713505171814249

## [INFO] 2026-08-03 12:24:14 UTC (tier 0)

START gen=autog2_159_SOLUSDT_15m_direction_ohlcv_v1 SOLUSDT 15m target=direction space=ohlcv_v1

## [INFO] 2026-08-03 12:25:10 UTC (tier 0)

PREDICTABILITY real=+0.00182 p=0.0476 surr_q95=+0.00008 surr_max=+0.00015 draws=20 passed=True

## [INFO] 2026-08-03 12:25:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 12:25:16 UTC (tier 0)

trial `057b9fa4-4cb4-4bb6-af42-ccd26124a80b` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 12:25:17 UTC (tier 1)

trial `8169f2a1-2537-457f-96a2-13e72a6c8286` model=ridge tier=1 target=direction pf=0.841 n=10262 gates=FAIL

## [INFO] 2026-08-03 12:25:23 UTC (tier 1)

trial `77c8c10d-55ac-40c4-8518-01a9a51e56d4` model=lgbm_regressor tier=1 target=direction pf=0.782 n=29616 gates=FAIL

## [INFO] 2026-08-03 12:25:36 UTC (tier 1)

trial `4596dc5f-7887-4425-aff9-77e14b74f92b` model=lgbm_classifier tier=1 target=direction pf=0.698 n=131420 gates=FAIL

## [INFO] 2026-08-03 12:25:36 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_159_SOLUSDT_15m_direction_ohlcv_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 12:25:36 UTC (tier 1)

AUTONOMY screen autog2_159_SOLUSDT_15m_direction_ohlcv_v1 tier=1 proxy_pf=0.8410141356085575 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 12:25:36 UTC (tier 0)

START gen=autog2_159_SOLUSDT_15m_direction_ohlcv_v1_ts SOLUSDT 15m target=direction space=ohlcv_v1

## [INFO] 2026-08-03 12:26:11 UTC (tier 0)

PREDICTABILITY real=+0.00182 p=0.0476 surr_q95=+0.00008 surr_max=+0.00015 draws=20 passed=True

## [INFO] 2026-08-03 12:26:19 UTC (tier 1)

trial `292d0fac-a586-4d5d-8e7c-b389c7ac8429` model=ridge tier=1 target=direction pf=0.773 n=4420 gates=FAIL

## [INFO] 2026-08-03 12:26:19 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_159_SOLUSDT_15m_direction_ohlcv_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 12:26:19 UTC (tier 1)

AUTONOMY tradesim autog2_159_SOLUSDT_15m_direction_ohlcv_v1 tier=1 proxy_pf=0.7725646607809039

## [INFO] 2026-08-03 12:26:19 UTC (tier 0)

START gen=autog2_160_SOLUSDT_15m_direction_indicators_v1 SOLUSDT 15m target=direction space=indicators_v1

## [INFO] 2026-08-03 12:26:53 UTC (tier 0)

PREDICTABILITY real=-0.00140 p=0.6190 surr_q95=-0.00001 surr_max=+0.00005 draws=20 passed=False

## [INFO] 2026-08-03 12:26:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 12:26:55 UTC (tier 0)

trial `1c1a3c9d-cf27-49e0-83a0-49969d43e1d9` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 12:26:55 UTC (tier 0)

trial `14a20fbc-a984-4b62-b304-f2795243bc06` model=ridge tier=0 target=direction pf=0.832 n=18057 gates=FAIL

## [INFO] 2026-08-03 12:26:59 UTC (tier 0)

trial `824300bb-7cd5-49b5-bf17-c603386a74a6` model=lgbm_regressor tier=0 target=direction pf=0.703 n=47881 gates=FAIL

## [INFO] 2026-08-03 12:27:08 UTC (tier 0)

trial `94190f85-1204-418f-9d13-e89f39ace072` model=lgbm_classifier tier=0 target=direction pf=0.687 n=129756 gates=FAIL

## [INFO] 2026-08-03 12:27:08 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_160_SOLUSDT_15m_direction_indicators_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 12:27:08 UTC (tier 0)

AUTONOMY screen autog2_160_SOLUSDT_15m_direction_indicators_v1 tier=0 proxy_pf=0.8319657123014361 predictability=False (proxy is a filter, not evidence)

## [INFO] 2026-08-03 12:27:08 UTC (tier 0)

START gen=autog2_161_SOLUSDT_15m_direction_pivot_v1 SOLUSDT 15m target=direction space=pivot_v1

## [INFO] 2026-08-03 12:27:25 UTC (tier 0)

PREDICTABILITY real=+0.00123 p=0.0476 surr_q95=+0.00021 surr_max=+0.00025 draws=20 passed=True

## [INFO] 2026-08-03 12:27:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 12:27:27 UTC (tier 0)

trial `972234c9-52e1-42ca-954e-b69765be54e0` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 12:27:27 UTC (tier 1)

trial `0eb5f840-d50b-41a6-9294-35f2ba5a2a74` model=ridge tier=1 target=direction pf=0.738 n=9102 gates=FAIL

## [INFO] 2026-08-03 12:27:30 UTC (tier 1)

trial `8eee7ac3-67f3-41e5-9176-0a2246ab70ae` model=lgbm_regressor tier=1 target=direction pf=0.737 n=20630 gates=FAIL

## [INFO] 2026-08-03 12:27:35 UTC (tier 1)

trial `a251b584-ae9c-42e8-9a2d-5ded6ae07662` model=lgbm_classifier tier=1 target=direction pf=0.697 n=131423 gates=FAIL

## [INFO] 2026-08-03 12:27:35 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_161_SOLUSDT_15m_direction_pivot_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 12:27:35 UTC (tier 1)

AUTONOMY screen autog2_161_SOLUSDT_15m_direction_pivot_v1 tier=1 proxy_pf=0.7377907882736581 predictability=True (proxy is a filter, not evidence)

## [INFO] 2026-08-03 12:27:35 UTC (tier 0)

START gen=autog2_161_SOLUSDT_15m_direction_pivot_v1_ts SOLUSDT 15m target=direction space=pivot_v1

## [INFO] 2026-08-03 12:27:53 UTC (tier 0)

PREDICTABILITY real=+0.00123 p=0.0476 surr_q95=+0.00021 surr_max=+0.00025 draws=20 passed=True

## [INFO] 2026-08-03 12:27:58 UTC (tier 1)

trial `d93c3bcc-ef47-4589-9ba4-05092c33dfcd` model=ridge tier=1 target=direction pf=0.726 n=2885 gates=FAIL

## [INFO] 2026-08-03 12:27:58 UTC (tier 0)

Hunt complete: {"generation_id": "autog2_161_SOLUSDT_15m_direction_pivot_v1_ts", "status": "COMPLETE", "n_trials": 1, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 12:27:58 UTC (tier 1)

AUTONOMY tradesim autog2_161_SOLUSDT_15m_direction_pivot_v1 tier=1 proxy_pf=0.7260715309530733

## [INFO] 2026-08-03 12:27:58 UTC (tier 0)

AUTONOMY sweep complete — no tier>=2 candidate

## [INFO] 2026-08-03 12:59:33 UTC (tier 0)

PREREG abc_bounce_001_BTCUSDT_1h status=FROZEN sha256=79299eb6fcc587dc hold=6 sl=0.04 lev=10.0 eval=forward_lockbox_once engine_stamp=9a037b290c8a

## [INFO] 2026-08-03 12:59:36 UTC (tier 0)

ABC_BOUNCE_UNDERPOWERED abc_bounce_001_BTCUSDT_1h: bounce_pf=0.5442 pnl=-7.02 n=46 | ctrl_pf=inf pnl=0.21 n=1 | entry_bar_stops=0 liq=0 underpowered=True

## [INFO] 2026-08-03 13:00:12 UTC (tier 0)

PREREG abc_bounce_001_BTCUSDT_1h status=FROZEN sha256=79299eb6fcc587dc hold=6 sl=0.04 lev=10.0 eval=forward_lockbox_once engine_stamp=9a037b290c8a

## [INFO] 2026-08-03 13:00:16 UTC (tier 0)

ABC_BOUNCE_UNDERPOWERED abc_bounce_001_BTCUSDT_1h: bounce_pf=0.5442 pnl=-7.02 n=46 | ctrl_pf=0.5895 pnl=-4.40 n=42 | entry_bar_stops=0 liq=0 underpowered=True

## [INFO] 2026-08-03 13:06:57 UTC (tier 0)

STRUCTURE_V1_HUNT: ABC continuation CLOSED (D-030); bounce UNDERPOWERED_HOLD (D-031); hunting audited structure_v1 only; video rules not evidence

## [INFO] 2026-08-03 13:06:57 UTC (tier 0)

STRUCTURE_V1_HUNT start n=8 space=structure_v1 rev=struct1

## [INFO] 2026-08-03 13:06:57 UTC (tier 0)

START gen=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1 BTCUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 13:08:10 UTC (tier 0)

TE_FALSIFY BTCUSDT 1h: NONLINEAR_CROSSASSET_PARTIAL pairs=31 all3=0 any=4 closed=27

## [INFO] 2026-08-03 13:08:53 UTC (tier 0)

STRUCTURE_V1_HUNT: ABC continuation CLOSED (D-030); bounce UNDERPOWERED_HOLD (D-031); hunting audited structure_v1 only; video rules not evidence

## [INFO] 2026-08-03 13:08:53 UTC (tier 0)

STRUCTURE_V1_HUNT start n=8 space=structure_v1 rev=struct1

## [INFO] 2026-08-03 13:08:53 UTC (tier 0)

START gen=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1 BTCUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 13:09:33 UTC (tier 0)

PREDICTABILITY real=+0.13001 p=0.0476 surr_q95=-0.00046 surr_max=-0.00037 draws=20 passed=True

## [INFO] 2026-08-03 13:09:40 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:09:40 UTC (tier 0)

trial `60b041d7-9756-4564-9353-6e446c9a62b2` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 13:09:41 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01617 skill_surrogate=-0.00182

## [INFO] 2026-08-03 13:09:41 UTC (tier 0)

trial `43b974fa-6d3d-407e-808a-76844c056317` model=ridge tier=0 target=fwd_return pf=0.892 n=12807 gates=FAIL

## [ALERT] 2026-08-03 13:09:48 UTC (tier 2)

trial `553b9db1-ec2b-4779-a9e4-5bf14a2db96c` model=lgbm_regressor tier=2 target=fwd_return pf=2.834 n=14470 gates=UNKNOWN

## [INFO] 2026-08-03 13:10:02 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.76124 skill_surrogate=-4.62229

## [INFO] 2026-08-03 13:10:02 UTC (tier 0)

trial `14bb4761-f951-4cdf-85e5-e9af30e73479` model=lgbm_classifier tier=0 target=fwd_return pf=1.792 n=32700 gates=UNKNOWN

## [INFO] 2026-08-03 13:10:02 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 13:10:02 UTC (tier 2)

ALERT structure_v1 tier>=2 autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1

## [INFO] 2026-08-03 13:10:51 UTC (tier 0)

START gen=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__review BTCUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 13:11:36 UTC (tier 0)

PREDICTABILITY real=+0.13001 p=0.0476 surr_q95=-0.00046 surr_max=-0.00037 draws=20 passed=True

## [ALERT] 2026-08-03 13:11:53 UTC (tier 2)

trial `b0e0b09d-cc06-41bc-b3ca-36730c8a5296` model=lgbm_regressor tier=2 target=fwd_return pf=1.774 n=3403 gates=UNKNOWN

## [INFO] 2026-08-03 13:11:53 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__review", "status": "COMPLETE", "n_trials": 1, "best_tier": 2, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 13:23:12 UTC (tier 0)

STRUCTURE_TIER2_SETTLE start base=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1 run=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_20260803

## [INFO] 2026-08-03 13:23:12 UTC (tier 0)

START gen=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_20260803 BTCUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 13:23:51 UTC (tier 0)

PREDICTABILITY real=+0.13001 p=0.0476 surr_q95=-0.00046 surr_max=-0.00037 draws=20 passed=True

## [INFO] 2026-08-03 13:23:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:23:55 UTC (tier 0)

trial `2aba78b4-be5d-4380-9b0d-d2188809d86e` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 13:24:10 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01617 skill_surrogate=-0.00546

## [INFO] 2026-08-03 13:24:10 UTC (tier 0)

trial `af1ef941-49cb-4b5b-9834-ef5ff9de270d` model=ridge tier=0 target=fwd_return pf=0.904 n=2695 gates=FAIL

## [ALERT] 2026-08-03 13:24:47 UTC (tier 3)

trial `f41c72fe-ffcb-4826-9879-8f12b20b5903` model=lgbm_regressor tier=3 target=fwd_return pf=1.840 n=3403 gates=PASS

## [INFO] 2026-08-03 13:25:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.76124 skill_surrogate=-4.99258

## [INFO] 2026-08-03 13:25:32 UTC (tier 0)

trial `b3dcf8c6-9ff3-4e69-89e0-58df0e7c12a4` model=lgbm_classifier tier=0 target=fwd_return pf=1.481 n=4093 gates=PASS

## [INFO] 2026-08-03 13:25:32 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 13:25:32 UTC (tier 3)

STRUCTURE_TIER2_SETTLE SHADOW_READY_CANDIDATE overall=PASS tier=3 pf=1.8403908959352018 resume_others=True

## [INFO] 2026-08-03 13:26:07 UTC (tier 0)

STRUCTURE_TIER2_SETTLE start base=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1 run=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_20260803

## [INFO] 2026-08-03 13:26:07 UTC (tier 0)

START gen=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_20260803 BTCUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 13:26:46 UTC (tier 0)

PREDICTABILITY real=+0.13001 p=0.0476 surr_q95=-0.00046 surr_max=-0.00037 draws=20 passed=True

## [INFO] 2026-08-03 13:26:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:26:50 UTC (tier 0)

trial `14912dd8-f0a3-4b4f-80b0-c01ea8cf76f9` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 13:27:06 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01617 skill_surrogate=-0.00546

## [INFO] 2026-08-03 13:27:06 UTC (tier 0)

trial `71d7a0e7-66fe-447d-a2ef-3943925d95fb` model=ridge tier=0 target=fwd_return pf=0.904 n=2695 gates=FAIL

## [ALERT] 2026-08-03 13:27:33 UTC (tier 3)

trial `d237b8a8-8448-4bb9-a0c9-738c7f2a2b52` model=lgbm_regressor tier=3 target=fwd_return pf=1.840 n=3403 gates=PASS

## [INFO] 2026-08-03 13:28:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-133.76124 skill_surrogate=-4.99258

## [INFO] 2026-08-03 13:28:12 UTC (tier 0)

trial `ee1aa6e6-7c32-48bd-bde8-ab2938226e5a` model=lgbm_classifier tier=0 target=fwd_return pf=1.481 n=4093 gates=PASS

## [INFO] 2026-08-03 13:28:12 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 13:28:12 UTC (tier 3)

STRUCTURE_TIER2_SETTLE SHADOW_READY_CANDIDATE overall=PASS tier=3 pf=1.8403908959352018 resume_others=True

## [INFO] 2026-08-03 13:28:43 UTC (tier 0)

STRUCTURE_V1_HUNT: ABC continuation CLOSED (D-030); bounce UNDERPOWERED_HOLD (D-031); hunting audited structure_v1 only; video rules not evidence

## [INFO] 2026-08-03 13:28:43 UTC (tier 0)

STRUCTURE_V1_HUNT start n=7 space=structure_v1 rev=struct1

## [INFO] 2026-08-03 13:28:43 UTC (tier 0)

START gen=autostruct1_00_BTCUSDT_1h_direction_structure_v1 BTCUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 13:29:39 UTC (tier 0)

PREDICTABILITY real=+0.11678 p=0.0476 surr_q95=-0.00044 surr_max=-0.00041 draws=20 passed=True

## [INFO] 2026-08-03 13:29:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:29:44 UTC (tier 0)

trial `c9eb3244-92de-452e-8032-ad2de24ee5c6` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 13:29:45 UTC (tier 1)

trial `f46c78d5-9a45-4f7f-9d19-34f5ad827422` model=ridge tier=1 target=direction pf=0.886 n=8466 gates=FAIL

## [ALERT] 2026-08-03 13:29:53 UTC (tier 2)

trial `89773de1-7523-4367-90e4-401238a21e50` model=lgbm_regressor tier=2 target=direction pf=2.468 n=23777 gates=UNKNOWN

## [ALERT] 2026-08-03 13:30:10 UTC (tier 2)

trial `a7351d05-25f2-4aa9-85ab-495a583fa905` model=lgbm_classifier tier=2 target=direction pf=1.792 n=32700 gates=UNKNOWN

## [INFO] 2026-08-03 13:30:10 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_00_BTCUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 13:30:10 UTC (tier 2)

ALERT structure_v1 tier>=2 autostruct1_00_BTCUSDT_1h_direction_structure_v1

## [INFO] 2026-08-03 13:30:28 UTC (tier 0)

STRUCTURE_V1_HUNT: ABC continuation CLOSED (D-030); bounce UNDERPOWERED_HOLD (D-031); hunting audited structure_v1 only; video rules not evidence

## [INFO] 2026-08-03 13:30:28 UTC (tier 0)

STRUCTURE_V1_HUNT start n=7 space=structure_v1 rev=struct1

## [INFO] 2026-08-03 13:30:28 UTC (tier 0)

START gen=autostruct1_01_BTCUSDT_4h_fwd_return_structure_v1 BTCUSDT 4h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 13:30:43 UTC (tier 0)

PREDICTABILITY real=+0.02714 p=0.0476 surr_q95=-0.00295 surr_max=+0.00008 draws=20 passed=True

## [INFO] 2026-08-03 13:30:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:30:49 UTC (tier 0)

trial `d28887e9-48fd-45dd-9145-c4cb7da48d98` model=hist_mean tier=0 target=fwd_return pf=0.681 n=1637 gates=FAIL

## [INFO] 2026-08-03 13:30:49 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01571 skill_surrogate=-0.00221

## [INFO] 2026-08-03 13:30:49 UTC (tier 0)

trial `c6a688ec-6b23-49fc-9c62-09832186befa` model=ridge tier=0 target=fwd_return pf=0.853 n=5926 gates=FAIL

## [INFO] 2026-08-03 13:30:54 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00298 skill_surrogate=-0.01860

## [INFO] 2026-08-03 13:30:54 UTC (tier 0)

trial `183bcedb-7e7b-4989-9338-f55f0295d7ed` model=lgbm_regressor tier=0 target=fwd_return pf=1.316 n=6179 gates=UNKNOWN

## [INFO] 2026-08-03 13:31:06 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-64.16847 skill_surrogate=-4.38406

## [INFO] 2026-08-03 13:31:06 UTC (tier 0)

trial `64b91037-e006-4797-9590-c80b7ac27100` model=lgbm_classifier tier=0 target=fwd_return pf=1.172 n=8182 gates=FAIL

## [INFO] 2026-08-03 13:31:06 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_01_BTCUSDT_4h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 13:31:06 UTC (tier 0)

START gen=autostruct1_02_BTCUSDT_4h_direction_structure_v1 BTCUSDT 4h target=direction space=structure_v1

## [INFO] 2026-08-03 13:31:25 UTC (tier 0)

PREDICTABILITY real=+0.01546 p=0.0476 surr_q95=-0.00133 surr_max=-0.00009 draws=20 passed=True

## [INFO] 2026-08-03 13:31:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:31:27 UTC (tier 0)

trial `1661a99f-37dc-4dca-92ef-a063bf466ac0` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 13:31:28 UTC (tier 1)

trial `e595a03e-f00d-470e-b887-ff14cb3f32b1` model=ridge tier=1 target=direction pf=0.954 n=2774 gates=FAIL

## [ALERT] 2026-08-03 13:31:31 UTC (tier 2)

trial `1b71ffaf-82f4-46df-baf0-a8edc586e7c0` model=lgbm_regressor tier=2 target=direction pf=1.385 n=5099 gates=UNKNOWN

## [INFO] 2026-08-03 13:31:43 UTC (tier 1)

trial `a365688a-7004-4a4a-8fb1-742d7318a722` model=lgbm_classifier tier=1 target=direction pf=1.172 n=8182 gates=FAIL

## [INFO] 2026-08-03 13:31:43 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_02_BTCUSDT_4h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 13:31:43 UTC (tier 2)

ALERT structure_v1 tier>=2 autostruct1_02_BTCUSDT_4h_direction_structure_v1

## [INFO] 2026-08-03 13:46:01 UTC (tier 0)

STRUCTURE_V1_HUNT: ABC continuation CLOSED (D-030); bounce UNDERPOWERED_HOLD (D-031); hunting audited structure_v1 only; video rules not evidence

## [INFO] 2026-08-03 13:46:01 UTC (tier 0)

STRUCTURE_V1_HUNT start n=7 space=structure_v1 rev=struct1

## [INFO] 2026-08-03 13:46:01 UTC (tier 0)

START gen=autostruct1_03_ETHUSDT_1h_fwd_return_structure_v1 ETHUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 13:46:40 UTC (tier 0)

PREDICTABILITY real=+0.15409 p=0.0476 surr_q95=+0.00052 surr_max=+0.00313 draws=20 passed=True

## [INFO] 2026-08-03 13:46:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:46:42 UTC (tier 0)

trial `5f9664b1-e408-407f-8bf0-344f033e361d` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 13:46:42 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00155 skill_surrogate=+0.00037

## [INFO] 2026-08-03 13:46:42 UTC (tier 0)

trial `cbdc66f5-9b4f-4796-9e67-c77b09db702b` model=ridge tier=0 target=fwd_return pf=0.755 n=12537 gates=FAIL

## [ALERT] 2026-08-03 13:46:50 UTC (tier 2)

trial `9d7924e5-7f79-4a6c-8877-ef311f799a6e` model=lgbm_regressor tier=2 target=fwd_return pf=2.515 n=20384 gates=UNKNOWN

## [INFO] 2026-08-03 13:46:59 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-74.16006 skill_surrogate=-2.87979

## [INFO] 2026-08-03 13:46:59 UTC (tier 0)

trial `5becaead-4a75-4e37-b53c-9b28b6e2ccec` model=lgbm_classifier tier=0 target=fwd_return pf=1.970 n=32786 gates=UNKNOWN

## [INFO] 2026-08-03 13:46:59 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_03_ETHUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 13:46:59 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct1_03_ETHUSDT_1h_fwd_return_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 13:46:59 UTC (tier 0)

START gen=autostruct1_04_ETHUSDT_1h_direction_structure_v1 ETHUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 13:47:24 UTC (tier 0)

PREDICTABILITY real=+0.11497 p=0.0476 surr_q95=+0.00151 surr_max=+0.00156 draws=20 passed=True

## [INFO] 2026-08-03 13:47:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:47:27 UTC (tier 0)

trial `5d0e6f61-9c72-4251-ad2d-02e4930450e3` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 13:47:29 UTC (tier 1)

trial `221de370-586f-41ed-9158-e0aef02aedfa` model=ridge tier=1 target=direction pf=0.737 n=7049 gates=FAIL

## [ALERT] 2026-08-03 13:47:38 UTC (tier 2)

trial `0984e37a-e9cb-4711-b424-108acedb1ff4` model=lgbm_regressor tier=2 target=direction pf=2.666 n=23474 gates=UNKNOWN

## [ALERT] 2026-08-03 13:48:07 UTC (tier 2)

trial `837f8741-3afe-41a8-8252-2ab1a2a42c90` model=lgbm_classifier tier=2 target=direction pf=1.970 n=32786 gates=UNKNOWN

## [INFO] 2026-08-03 13:48:07 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_04_ETHUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 13:48:07 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct1_04_ETHUSDT_1h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 13:48:07 UTC (tier 0)

START gen=autostruct1_05_ETHUSDT_4h_fwd_return_structure_v1 ETHUSDT 4h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 13:48:25 UTC (tier 0)

PREDICTABILITY real=+0.00712 p=0.0476 surr_q95=-0.00079 surr_max=+0.00213 draws=20 passed=True

## [INFO] 2026-08-03 13:48:32 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:48:32 UTC (tier 0)

trial `d738e7df-a421-4808-a1c4-dad1826de843` model=hist_mean tier=0 target=fwd_return pf=0.922 n=8196 gates=FAIL

## [INFO] 2026-08-03 13:48:32 UTC (tier 1)

trial `d4f63601-f73d-4771-a2d1-fe252fb894bf` model=ridge tier=1 target=fwd_return pf=0.794 n=5747 gates=FAIL

## [INFO] 2026-08-03 13:48:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00353 skill_surrogate=-0.00903

## [INFO] 2026-08-03 13:48:38 UTC (tier 0)

trial `961136ea-c3bf-4a03-8385-88ac0a3e9dbc` model=lgbm_regressor tier=0 target=fwd_return pf=1.149 n=6752 gates=FAIL

## [INFO] 2026-08-03 13:48:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-35.00072 skill_surrogate=-2.78143

## [INFO] 2026-08-03 13:48:57 UTC (tier 0)

trial `ced28001-e453-4736-8b89-c02aeceff442` model=lgbm_classifier tier=0 target=fwd_return pf=1.094 n=8196 gates=FAIL

## [INFO] 2026-08-03 13:48:57 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_05_ETHUSDT_4h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 13:48:57 UTC (tier 0)

START gen=autostruct1_06_ETHUSDT_4h_direction_structure_v1 ETHUSDT 4h target=direction space=structure_v1

## [INFO] 2026-08-03 13:49:16 UTC (tier 0)

PREDICTABILITY real=-0.01553 p=0.8571 surr_q95=+0.00160 surr_max=+0.01358 draws=20 passed=False

## [INFO] 2026-08-03 13:49:19 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 13:49:19 UTC (tier 0)

trial `56d016e3-2b08-4739-8da6-782d3acc6ec5` model=hist_mean tier=0 target=direction pf=0.737 n=1637 gates=FAIL

## [INFO] 2026-08-03 13:49:19 UTC (tier 0)

trial `0910a61b-42e1-44fa-b11c-aab5252ea630` model=ridge tier=0 target=direction pf=0.814 n=2918 gates=FAIL

## [INFO] 2026-08-03 13:49:29 UTC (tier 0)

trial `b6a8b9fd-7a4b-4521-9957-c3e474ad3633` model=lgbm_regressor tier=0 target=direction pf=1.251 n=5310 gates=UNKNOWN

## [INFO] 2026-08-03 13:49:41 UTC (tier 0)

trial `ffdf42ec-7259-48e1-827d-03504d355fdd` model=lgbm_classifier tier=0 target=direction pf=1.094 n=8196 gates=FAIL

## [INFO] 2026-08-03 13:49:41 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_06_ETHUSDT_4h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 5, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 13:49:41 UTC (tier 2)

STRUCTURE_V1_HUNT complete best_tier=2 report=structure_v1_hunt_20260803T134941Z.json

## [INFO] 2026-08-03 15:09:37 UTC (tier 0)

VPS_REFUSED_AS_EXPECTED: VPS deploy REFUSED for structure_v1_lgbm_BTCUSDT_1h: status='BLOCKED' authorized_by_user=False pack_hash=None. Settle PASS / Finplot / SHADOW_READY_CANDIDATE are research evidence only. Require a frozen live pack, funding+Mark parity, and explicit user authorization on the certificate. Requested host='94.156.189.76'.

## [INFO] 2026-08-03 15:09:37 UTC (tier 0)

STRUCTURE_TIER2_SETTLE_V2 start fold_geometry=v2 n_folds=6 prereg_sha=60b19403685c9e1d run=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_v2_20260803

## [INFO] 2026-08-03 15:09:37 UTC (tier 0)

START gen=autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_v2_20260803 BTCUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:09:59 UTC (tier 0)

PREDICTABILITY real=+0.13001 p=0.0476 surr_q95=-0.00046 surr_max=-0.00037 draws=20 passed=True

## [INFO] 2026-08-03 15:10:02 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:10:02 UTC (tier 0)

trial `48b610a1-619f-4e73-8fb3-ee1c533d84ae` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:10:12 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01509 skill_surrogate=-0.00306

## [INFO] 2026-08-03 15:10:13 UTC (tier 0)

trial `06cbdcd8-36c8-4640-b106-d5ddb75d2aa7` model=ridge tier=0 target=fwd_return pf=0.875 n=3016 gates=FAIL

## [ALERT] 2026-08-03 15:10:29 UTC (tier 3)

trial `e79a5522-57ed-4453-9038-ae70e157860b` model=lgbm_regressor tier=3 target=fwd_return pf=1.865 n=3903 gates=PASS

## [INFO] 2026-08-03 15:10:56 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-113.20552 skill_surrogate=-4.21799

## [INFO] 2026-08-03 15:10:56 UTC (tier 0)

trial `a2d5db16-ab97-420c-ad4b-56e71ed8bce6` model=lgbm_classifier tier=0 target=fwd_return pf=1.511 n=4713 gates=PASS

## [INFO] 2026-08-03 15:10:56 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct1_00_BTCUSDT_1h_fwd_return_structure_v1__settle_v2_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 15:10:56 UTC (tier 3)

STRUCTURE_TIER2_SETTLE_V2 SHADOW_READY_CANDIDATE overall=PASS tier=3 pf=1.8651444550275214 pack=D:\projects\LLM2\artifacts\live_packs\structure_v1_lgbm

## [INFO] 2026-08-03 15:54:37 UTC (tier 0)

STRUCTURE_V1_HUNT: ABC continuation CLOSED (D-030); bounce UNDERPOWERED_HOLD (D-031); hunting audited structure_v1 only; video rules not evidence

## [INFO] 2026-08-03 15:54:37 UTC (tier 0)

STRUCTURE_V1_HUNT start n=19 space=structure_v1 rev=struct2

## [INFO] 2026-08-03 15:54:37 UTC (tier 0)

START gen=autostruct2_00_BTCUSDT_1h_direction_structure_v1 BTCUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 15:54:51 UTC (tier 0)

PREDICTABILITY real=+0.11678 p=0.0476 surr_q95=-0.00044 surr_max=-0.00041 draws=20 passed=True

## [INFO] 2026-08-03 15:54:52 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:54:52 UTC (tier 0)

trial `25a7b6e2-e1f0-42dc-9280-d2041bccbb79` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:54:53 UTC (tier 1)

trial `ea18d0ff-a92b-491f-a523-f437f0d36b8b` model=ridge tier=1 target=direction pf=0.860 n=9826 gates=FAIL

## [ALERT] 2026-08-03 15:54:57 UTC (tier 2)

trial `9a919ed5-e929-40e8-b6c5-fbdfad374b5c` model=lgbm_regressor tier=2 target=direction pf=2.499 n=27489 gates=UNKNOWN

## [ALERT] 2026-08-03 15:55:04 UTC (tier 2)

trial `8e873a59-c71d-4b3b-9711-efa7e11fe4b9` model=lgbm_classifier tier=2 target=direction pf=1.821 n=37777 gates=UNKNOWN

## [INFO] 2026-08-03 15:55:04 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_00_BTCUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:55:04 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_00_BTCUSDT_1h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:55:04 UTC (tier 0)

START gen=autostruct2_01_BTCUSDT_4h_fwd_return_structure_v1 BTCUSDT 4h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:55:09 UTC (tier 0)

PREDICTABILITY real=+0.02714 p=0.0476 surr_q95=-0.00295 surr_max=+0.00008 draws=20 passed=True

## [INFO] 2026-08-03 15:55:11 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:55:11 UTC (tier 0)

trial `db2ee8b1-7ca6-4ce6-8585-dad2fff8d715` model=hist_mean tier=0 target=fwd_return pf=0.681 n=1637 gates=FAIL

## [INFO] 2026-08-03 15:55:11 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.03020 skill_surrogate=-0.00051

## [INFO] 2026-08-03 15:55:11 UTC (tier 0)

trial `b88a16bd-d9eb-467e-a636-777929713f6e` model=ridge tier=0 target=fwd_return pf=0.814 n=6791 gates=FAIL

## [INFO] 2026-08-03 15:55:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.08146 skill_surrogate=-0.01561

## [INFO] 2026-08-03 15:55:12 UTC (tier 0)

trial `c8a3c2bf-711d-4fb9-bc2f-7fbf0ec1bc2f` model=lgbm_regressor tier=0 target=fwd_return pf=1.252 n=7112 gates=FAIL

## [INFO] 2026-08-03 15:55:16 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-53.54676 skill_surrogate=-4.09155

## [INFO] 2026-08-03 15:55:16 UTC (tier 0)

trial `264c607c-3c06-4d09-a2ce-a2097cdd5394` model=lgbm_classifier tier=0 target=fwd_return pf=1.152 n=9446 gates=FAIL

## [INFO] 2026-08-03 15:55:16 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_01_BTCUSDT_4h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:55:16 UTC (tier 0)

START gen=autostruct2_02_BTCUSDT_4h_direction_structure_v1 BTCUSDT 4h target=direction space=structure_v1

## [INFO] 2026-08-03 15:55:22 UTC (tier 0)

PREDICTABILITY real=+0.01546 p=0.0476 surr_q95=-0.00133 surr_max=-0.00009 draws=20 passed=True

## [INFO] 2026-08-03 15:55:23 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:55:23 UTC (tier 0)

trial `5e7a0f1c-b522-4b20-b237-1de077f29117` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:55:23 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00977 skill_surrogate=+0.00272

## [INFO] 2026-08-03 15:55:23 UTC (tier 0)

trial `ceaa3532-a02b-4756-82a7-da3c4a37f508` model=ridge tier=0 target=direction pf=0.868 n=3437 gates=FAIL

## [ALERT] 2026-08-03 15:55:24 UTC (tier 2)

trial `0f383002-be86-44cd-972f-390a97555ee5` model=lgbm_regressor tier=2 target=direction pf=1.339 n=5850 gates=UNKNOWN

## [INFO] 2026-08-03 15:55:28 UTC (tier 1)

trial `d64b1b4f-4bca-4cef-8ef2-59c61c112889` model=lgbm_classifier tier=1 target=direction pf=1.152 n=9446 gates=FAIL

## [INFO] 2026-08-03 15:55:28 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_02_BTCUSDT_4h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:55:28 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_02_BTCUSDT_4h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:55:28 UTC (tier 0)

START gen=autostruct2_03_ETHUSDT_1h_fwd_return_structure_v1 ETHUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:55:42 UTC (tier 0)

PREDICTABILITY real=+0.15409 p=0.0476 surr_q95=+0.00052 surr_max=+0.00313 draws=20 passed=True

## [INFO] 2026-08-03 15:55:45 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:55:45 UTC (tier 0)

trial `0ac99bf9-3de8-40b1-a865-471138f074f0` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:55:46 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00425 skill_surrogate=-0.00251

## [INFO] 2026-08-03 15:55:46 UTC (tier 0)

trial `bfdb0f15-b780-412a-8ec9-e15d2c40f056` model=ridge tier=0 target=fwd_return pf=0.756 n=13504 gates=FAIL

## [ALERT] 2026-08-03 15:55:48 UTC (tier 2)

trial `60e35411-5fa5-49a8-b4cc-291b5787a033` model=lgbm_regressor tier=2 target=fwd_return pf=2.639 n=23519 gates=UNKNOWN

## [INFO] 2026-08-03 15:55:54 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-79.82235 skill_surrogate=-2.60717

## [INFO] 2026-08-03 15:55:54 UTC (tier 0)

trial `87e53037-3975-4b8d-923a-e4d3022137df` model=lgbm_classifier tier=0 target=fwd_return pf=2.032 n=37851 gates=UNKNOWN

## [INFO] 2026-08-03 15:55:54 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_03_ETHUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:55:54 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_03_ETHUSDT_1h_fwd_return_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:55:54 UTC (tier 0)

START gen=autostruct2_04_ETHUSDT_1h_direction_structure_v1 ETHUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 15:56:08 UTC (tier 0)

PREDICTABILITY real=+0.11497 p=0.0476 surr_q95=+0.00151 surr_max=+0.00156 draws=20 passed=True

## [INFO] 2026-08-03 15:56:09 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:56:09 UTC (tier 0)

trial `16165806-4e28-4a81-9d4f-7b9a87d9cfe1` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:56:10 UTC (tier 1)

trial `44887688-bf93-4dcb-8790-1b0ee13dd86e` model=ridge tier=1 target=direction pf=0.745 n=7576 gates=FAIL

## [ALERT] 2026-08-03 15:56:13 UTC (tier 2)

trial `630f507e-6dac-486a-902c-5ea5703580cd` model=lgbm_regressor tier=2 target=direction pf=2.762 n=26949 gates=UNKNOWN

## [ALERT] 2026-08-03 15:56:20 UTC (tier 2)

trial `5933ab3b-a74f-4a87-8b7b-1a48a85956ec` model=lgbm_classifier tier=2 target=direction pf=2.032 n=37851 gates=UNKNOWN

## [INFO] 2026-08-03 15:56:20 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_04_ETHUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:56:20 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_04_ETHUSDT_1h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:56:20 UTC (tier 0)

START gen=autostruct2_05_ETHUSDT_4h_fwd_return_structure_v1 ETHUSDT 4h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:56:26 UTC (tier 0)

PREDICTABILITY real=+0.00712 p=0.0476 surr_q95=-0.00079 surr_max=+0.00213 draws=20 passed=True

## [INFO] 2026-08-03 15:56:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:56:27 UTC (tier 0)

trial `ad709ebf-dd39-4195-9873-7b6191aa2609` model=hist_mean tier=0 target=fwd_return pf=0.892 n=9458 gates=FAIL

## [INFO] 2026-08-03 15:56:27 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00576 skill_surrogate=-0.00937

## [INFO] 2026-08-03 15:56:27 UTC (tier 0)

trial `89d52d7e-874a-4e03-a103-2f363774b9bc` model=ridge tier=0 target=fwd_return pf=0.803 n=6467 gates=FAIL

## [INFO] 2026-08-03 15:56:28 UTC (tier 1)

trial `c7385575-d0d7-466f-a4ad-863fa9190bd5` model=lgbm_regressor tier=1 target=fwd_return pf=1.143 n=7744 gates=FAIL

## [INFO] 2026-08-03 15:56:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-36.91620 skill_surrogate=-2.39872

## [INFO] 2026-08-03 15:56:33 UTC (tier 0)

trial `049c8df5-a97b-4c67-9402-21e4c6de70b3` model=lgbm_classifier tier=0 target=fwd_return pf=1.089 n=9458 gates=FAIL

## [INFO] 2026-08-03 15:56:33 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_05_ETHUSDT_4h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 1, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:56:33 UTC (tier 0)

START gen=autostruct2_06_ETHUSDT_4h_direction_structure_v1 ETHUSDT 4h target=direction space=structure_v1

## [INFO] 2026-08-03 15:56:38 UTC (tier 0)

PREDICTABILITY real=-0.01553 p=0.8571 surr_q95=+0.00160 surr_max=+0.01358 draws=20 passed=False

## [INFO] 2026-08-03 15:56:39 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:56:39 UTC (tier 0)

trial `76e9379e-335c-4243-839d-72fcaa05b5fc` model=hist_mean tier=0 target=direction pf=0.737 n=1637 gates=FAIL

## [INFO] 2026-08-03 15:56:39 UTC (tier 0)

trial `7469bf73-2fa0-415b-89ba-6317fab25f4d` model=ridge tier=0 target=direction pf=0.815 n=3136 gates=FAIL

## [INFO] 2026-08-03 15:56:40 UTC (tier 0)

trial `e8a02d0c-95c9-4772-b083-2727289107b1` model=lgbm_regressor tier=0 target=direction pf=1.254 n=6012 gates=UNKNOWN

## [INFO] 2026-08-03 15:56:45 UTC (tier 0)

trial `74dbbc4d-8d35-4981-b6f1-e84440b53e57` model=lgbm_classifier tier=0 target=direction pf=1.089 n=9458 gates=FAIL

## [INFO] 2026-08-03 15:56:45 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_06_ETHUSDT_4h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:56:45 UTC (tier 0)

START gen=autostruct2_07_SOLUSDT_1h_fwd_return_structure_v1 SOLUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:56:57 UTC (tier 0)

PREDICTABILITY real=+0.06248 p=0.0476 surr_q95=-0.00107 surr_max=-0.00088 draws=20 passed=True

## [INFO] 2026-08-03 15:57:01 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:57:01 UTC (tier 0)

trial `21b2b318-3a7f-4370-9af4-33443bcbecc7` model=hist_mean tier=0 target=fwd_return pf=0.753 n=6455 gates=FAIL

## [INFO] 2026-08-03 15:57:01 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00140 skill_surrogate=-0.00377

## [INFO] 2026-08-03 15:57:01 UTC (tier 0)

trial `bb37af80-c356-4f5c-81aa-602430a36a80` model=ridge tier=0 target=fwd_return pf=0.898 n=23625 gates=FAIL

## [ALERT] 2026-08-03 15:57:04 UTC (tier 2)

trial `dc105f4b-37a6-4f99-af1e-fdcc801dce93` model=lgbm_regressor tier=2 target=fwd_return pf=2.272 n=27303 gates=UNKNOWN

## [INFO] 2026-08-03 15:57:09 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-70.30322 skill_surrogate=-1.95160

## [INFO] 2026-08-03 15:57:09 UTC (tier 0)

trial `1235a416-c3dd-4b0c-aac7-8eebef559e82` model=lgbm_classifier tier=0 target=fwd_return pf=2.095 n=37449 gates=UNKNOWN

## [INFO] 2026-08-03 15:57:09 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_07_SOLUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:57:09 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_07_SOLUSDT_1h_fwd_return_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:57:09 UTC (tier 0)

START gen=autostruct2_08_SOLUSDT_1h_direction_structure_v1 SOLUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 15:57:21 UTC (tier 0)

PREDICTABILITY real=+0.12335 p=0.0476 surr_q95=-0.00049 surr_max=+0.00152 draws=20 passed=True

## [INFO] 2026-08-03 15:57:23 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:57:23 UTC (tier 0)

trial `3495992e-64d7-49d0-8072-34eb2cc09814` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:57:23 UTC (tier 1)

trial `b3ea13d1-70d4-47a9-98bc-e48be6f668ef` model=ridge tier=1 target=direction pf=0.842 n=11793 gates=FAIL

## [ALERT] 2026-08-03 15:57:25 UTC (tier 2)

trial `405db93c-f462-45a5-9527-f4d3b45dde00` model=lgbm_regressor tier=2 target=direction pf=2.941 n=25666 gates=UNKNOWN

## [ALERT] 2026-08-03 15:57:31 UTC (tier 2)

trial `072196fe-9657-49aa-a73b-9936b6f6a7ee` model=lgbm_classifier tier=2 target=direction pf=2.095 n=37449 gates=UNKNOWN

## [INFO] 2026-08-03 15:57:31 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_08_SOLUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:57:31 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_08_SOLUSDT_1h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:57:31 UTC (tier 0)

START gen=autostruct2_09_SOLUSDT_4h_fwd_return_structure_v1 SOLUSDT 4h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:57:36 UTC (tier 0)

PREDICTABILITY real=-0.03988 p=0.9524 surr_q95=-0.00191 surr_max=+0.00225 draws=20 passed=False

## [INFO] 2026-08-03 15:57:38 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:57:38 UTC (tier 0)

trial `62282ca2-f40a-4b89-9480-be884a7d8a07` model=hist_mean tier=0 target=fwd_return pf=0.931 n=9356 gates=FAIL

## [INFO] 2026-08-03 15:57:38 UTC (tier 0)

trial `34272994-1158-4a62-981a-5b6957e4e656` model=ridge tier=0 target=fwd_return pf=1.006 n=8198 gates=FAIL

## [INFO] 2026-08-03 15:57:39 UTC (tier 0)

trial `783e256f-e709-4d7f-ac4b-96d702c245ec` model=lgbm_regressor tier=0 target=fwd_return pf=1.101 n=8291 gates=FAIL

## [INFO] 2026-08-03 15:57:43 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-33.03772 skill_surrogate=-2.02607

## [INFO] 2026-08-03 15:57:43 UTC (tier 0)

trial `d907ca34-cc3c-4672-a6f0-ef22907edcb0` model=lgbm_classifier tier=0 target=fwd_return pf=1.230 n=9356 gates=UNKNOWN

## [INFO] 2026-08-03 15:57:43 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_09_SOLUSDT_4h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:57:44 UTC (tier 0)

START gen=autostruct2_10_SOLUSDT_4h_direction_structure_v1 SOLUSDT 4h target=direction space=structure_v1

## [INFO] 2026-08-03 15:57:49 UTC (tier 0)

PREDICTABILITY real=+0.01374 p=0.0476 surr_q95=+0.00206 surr_max=+0.00510 draws=20 passed=True

## [INFO] 2026-08-03 15:57:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:57:50 UTC (tier 0)

trial `6e31d8a3-d49c-43df-a947-e996e0e50aa6` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:57:50 UTC (tier 1)

trial `7995af8b-def9-4910-84f7-0b71a8a8caaa` model=ridge tier=1 target=direction pf=0.948 n=4302 gates=FAIL

## [ALERT] 2026-08-03 15:57:51 UTC (tier 2)

trial `bd117b56-0294-4784-8f8e-335e85697f14` model=lgbm_regressor tier=2 target=direction pf=1.328 n=6292 gates=UNKNOWN

## [ALERT] 2026-08-03 15:57:54 UTC (tier 2)

trial `9edb26e6-dcd2-40b5-aaec-b8237e0b98e6` model=lgbm_classifier tier=2 target=direction pf=1.230 n=9356 gates=UNKNOWN

## [INFO] 2026-08-03 15:57:54 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_10_SOLUSDT_4h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:57:54 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_10_SOLUSDT_4h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:57:54 UTC (tier 0)

START gen=autostruct2_11_BNBUSDT_1h_fwd_return_structure_v1 BNBUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:58:09 UTC (tier 0)

PREDICTABILITY real=+0.06326 p=0.0476 surr_q95=+0.00014 surr_max=+0.00086 draws=20 passed=True

## [INFO] 2026-08-03 15:58:12 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:58:12 UTC (tier 0)

trial `929cda23-d76f-41b1-9765-54ab276e036b` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:58:12 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00795 skill_surrogate=+0.00190

## [INFO] 2026-08-03 15:58:12 UTC (tier 0)

trial `afe61711-a78f-4f69-95a6-446005bf8a1f` model=ridge tier=0 target=fwd_return pf=0.762 n=17875 gates=FAIL

## [ALERT] 2026-08-03 15:58:15 UTC (tier 2)

trial `aff9ae77-0115-41db-b997-5c331f163b49` model=lgbm_regressor tier=2 target=fwd_return pf=2.913 n=15375 gates=UNKNOWN

## [INFO] 2026-08-03 15:58:21 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-99.39669 skill_surrogate=-4.27125

## [INFO] 2026-08-03 15:58:21 UTC (tier 0)

trial `267494ea-a4e5-48c7-b82b-7e5cf3b81177` model=lgbm_classifier tier=0 target=fwd_return pf=1.910 n=37488 gates=UNKNOWN

## [INFO] 2026-08-03 15:58:21 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_11_BNBUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:58:21 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_11_BNBUSDT_1h_fwd_return_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:58:21 UTC (tier 0)

START gen=autostruct2_12_BNBUSDT_1h_direction_structure_v1 BNBUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 15:58:34 UTC (tier 0)

PREDICTABILITY real=+0.13125 p=0.0476 surr_q95=+0.00049 surr_max=+0.00134 draws=20 passed=True

## [INFO] 2026-08-03 15:58:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:58:36 UTC (tier 0)

trial `119a2583-2288-4b94-ad76-af58629be435` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:58:36 UTC (tier 1)

trial `8df77733-948a-45c1-ace4-530c4ea76790` model=ridge tier=1 target=direction pf=0.801 n=9394 gates=FAIL

## [ALERT] 2026-08-03 15:58:39 UTC (tier 2)

trial `344b7fda-f740-40db-8ac7-77f848f1c153` model=lgbm_regressor tier=2 target=direction pf=2.630 n=26865 gates=UNKNOWN

## [ALERT] 2026-08-03 15:58:45 UTC (tier 2)

trial `aaec1ed6-eb12-4eb2-80bb-fc9b97188360` model=lgbm_classifier tier=2 target=direction pf=1.910 n=37488 gates=UNKNOWN

## [INFO] 2026-08-03 15:58:45 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_12_BNBUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:58:45 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_12_BNBUSDT_1h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:58:45 UTC (tier 0)

START gen=autostruct2_13_BNBUSDT_4h_fwd_return_structure_v1 BNBUSDT 4h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:58:51 UTC (tier 0)

PREDICTABILITY real=-0.07462 p=1.0000 surr_q95=-0.00073 surr_max=+0.00137 draws=20 passed=False

## [INFO] 2026-08-03 15:58:52 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:58:52 UTC (tier 0)

trial `9098c57f-ef8a-44a6-8f8a-5faa31e11c1e` model=hist_mean tier=0 target=fwd_return pf=0.901 n=9372 gates=FAIL

## [INFO] 2026-08-03 15:58:52 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00789 skill_surrogate=-0.00367

## [INFO] 2026-08-03 15:58:52 UTC (tier 0)

trial `7f8081e9-c1f9-4864-911f-85514924c4dd` model=ridge tier=0 target=fwd_return pf=0.829 n=7521 gates=FAIL

## [INFO] 2026-08-03 15:58:54 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.05259 skill_surrogate=-0.01427

## [INFO] 2026-08-03 15:58:54 UTC (tier 0)

trial `193f8074-34f4-433b-bfff-028939e69b70` model=lgbm_regressor tier=0 target=fwd_return pf=1.099 n=7357 gates=FAIL

## [INFO] 2026-08-03 15:58:57 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-46.80579 skill_surrogate=-3.87253

## [INFO] 2026-08-03 15:58:57 UTC (tier 0)

trial `5ed5150c-bf54-4369-bbe1-9fe688d5fed2` model=lgbm_classifier tier=0 target=fwd_return pf=0.980 n=9372 gates=FAIL

## [INFO] 2026-08-03 15:58:57 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_13_BNBUSDT_4h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:58:57 UTC (tier 0)

START gen=autostruct2_14_BNBUSDT_4h_direction_structure_v1 BNBUSDT 4h target=direction space=structure_v1

## [INFO] 2026-08-03 15:59:03 UTC (tier 0)

PREDICTABILITY real=-0.01652 p=0.9524 surr_q95=-0.00217 surr_max=-0.00215 draws=20 passed=False

## [INFO] 2026-08-03 15:59:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:59:04 UTC (tier 0)

trial `88f4d06e-d8cb-44c4-a881-ca0cdd2a0bc6` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:59:04 UTC (tier 0)

trial `84f6ae80-870e-4cc1-b113-d45298331e02` model=ridge tier=0 target=direction pf=0.859 n=3498 gates=FAIL

## [INFO] 2026-08-03 15:59:06 UTC (tier 0)

trial `8a40c163-ad0c-4798-905e-06879e78d560` model=lgbm_regressor tier=0 target=direction pf=1.044 n=6072 gates=FAIL

## [INFO] 2026-08-03 15:59:10 UTC (tier 0)

trial `2afc05d7-2916-4be4-aaf8-ec278b977ae0` model=lgbm_classifier tier=0 target=direction pf=0.980 n=9372 gates=FAIL

## [INFO] 2026-08-03 15:59:10 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_14_BNBUSDT_4h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:59:10 UTC (tier 0)

START gen=autostruct2_15_XRPUSDT_1h_fwd_return_structure_v1 XRPUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 15:59:23 UTC (tier 0)

PREDICTABILITY real=+0.02002 p=0.0476 surr_q95=+0.00029 surr_max=+0.00093 draws=20 passed=True

## [INFO] 2026-08-03 15:59:26 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:59:26 UTC (tier 0)

trial `d5ac2d57-466e-4309-bcb0-c34978321023` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:59:27 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01612 skill_surrogate=-0.00152

## [INFO] 2026-08-03 15:59:27 UTC (tier 0)

trial `7106e9d4-89a2-4af2-af00-aeb006c442d6` model=ridge tier=0 target=fwd_return pf=0.833 n=19355 gates=FAIL

## [ALERT] 2026-08-03 15:59:29 UTC (tier 2)

trial `a803caa4-337f-448c-b15d-2026776714f0` model=lgbm_regressor tier=2 target=fwd_return pf=2.294 n=14388 gates=UNKNOWN

## [INFO] 2026-08-03 15:59:35 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-78.07793 skill_surrogate=-2.54375

## [INFO] 2026-08-03 15:59:35 UTC (tier 0)

trial `b44ad9dd-2d8c-4529-8a9a-12ba69b6cf95` model=lgbm_classifier tier=0 target=fwd_return pf=2.160 n=32673 gates=UNKNOWN

## [INFO] 2026-08-03 15:59:35 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_15_XRPUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 15:59:35 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_15_XRPUSDT_1h_fwd_return_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 15:59:35 UTC (tier 0)

START gen=autostruct2_16_XRPUSDT_1h_direction_structure_v1 XRPUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 15:59:48 UTC (tier 0)

PREDICTABILITY real=+0.12132 p=0.0476 surr_q95=+0.00042 surr_max=+0.00131 draws=20 passed=True

## [INFO] 2026-08-03 15:59:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 15:59:50 UTC (tier 0)

trial `1e10edb8-c6cb-4660-a1cc-ed768d9cc6e9` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 15:59:50 UTC (tier 1)

trial `69ec3a2a-5af6-49ef-a885-8b0fb17a5f17` model=ridge tier=1 target=direction pf=0.795 n=8302 gates=FAIL

## [ALERT] 2026-08-03 15:59:53 UTC (tier 2)

trial `5774b0e4-56e7-4d41-8fd9-7bda8cc688c5` model=lgbm_regressor tier=2 target=direction pf=2.934 n=23616 gates=UNKNOWN

## [ALERT] 2026-08-03 16:00:00 UTC (tier 2)

trial `499e8b71-b26f-45e2-a253-33e5b9aa8877` model=lgbm_classifier tier=2 target=direction pf=2.160 n=32673 gates=UNKNOWN

## [INFO] 2026-08-03 16:00:00 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_16_XRPUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:00:00 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_16_XRPUSDT_1h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [INFO] 2026-08-03 16:00:00 UTC (tier 0)

START gen=autostruct2_17_XRPUSDT_4h_fwd_return_structure_v1 XRPUSDT 4h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 16:00:06 UTC (tier 0)

PREDICTABILITY real=-0.01098 p=0.5714 surr_q95=-0.00035 surr_max=+0.01451 draws=20 passed=False

## [INFO] 2026-08-03 16:00:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 16:00:08 UTC (tier 0)

trial `1bc0916e-6f61-48e9-ba9c-df55ef0644be` model=hist_mean tier=0 target=fwd_return pf=0.786 n=1581 gates=FAIL

## [INFO] 2026-08-03 16:00:08 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.04597 skill_surrogate=+0.00624

## [INFO] 2026-08-03 16:00:08 UTC (tier 0)

trial `5ea7cda5-d53b-455d-864e-43b2980c888b` model=ridge tier=0 target=fwd_return pf=0.909 n=7045 gates=FAIL

## [INFO] 2026-08-03 16:00:10 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.17378 skill_surrogate=-0.02965

## [INFO] 2026-08-03 16:00:10 UTC (tier 0)

trial `998d83e3-64b5-4336-b7cb-f3889de24636` model=lgbm_regressor tier=0 target=fwd_return pf=1.262 n=6511 gates=UNKNOWN

## [INFO] 2026-08-03 16:00:14 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-37.30017 skill_surrogate=-2.11257

## [INFO] 2026-08-03 16:00:14 UTC (tier 0)

trial `7862f075-3478-4436-b897-92146d66ff16` model=lgbm_classifier tier=0 target=fwd_return pf=1.183 n=8164 gates=FAIL

## [INFO] 2026-08-03 16:00:14 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_17_XRPUSDT_4h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:00:14 UTC (tier 0)

START gen=autostruct2_18_XRPUSDT_4h_direction_structure_v1 XRPUSDT 4h target=direction space=structure_v1

## [INFO] 2026-08-03 16:00:20 UTC (tier 0)

PREDICTABILITY real=+0.02057 p=0.0476 surr_q95=-0.00059 surr_max=+0.00919 draws=20 passed=True

## [INFO] 2026-08-03 16:00:20 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 16:00:20 UTC (tier 0)

trial `ea4c8d5a-c9ef-42e2-8ffc-624c22b0d6d8` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 16:00:20 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00304 skill_surrogate=+0.00394

## [INFO] 2026-08-03 16:00:20 UTC (tier 0)

trial `4965e478-1fe8-4291-b7fe-8636ec63e695` model=ridge tier=0 target=direction pf=0.961 n=3641 gates=FAIL

## [ALERT] 2026-08-03 16:00:22 UTC (tier 2)

trial `85091191-28e1-4217-a671-a3a8b8a6aaf9` model=lgbm_regressor tier=2 target=direction pf=1.301 n=5276 gates=UNKNOWN

## [INFO] 2026-08-03 16:00:26 UTC (tier 1)

trial `7b4bdc4c-edaa-49ff-bf7e-a812a3d2ce8d` model=lgbm_classifier tier=1 target=direction pf=1.183 n=8164 gates=FAIL

## [INFO] 2026-08-03 16:00:26 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct2_18_XRPUSDT_4h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:00:26 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct2_18_XRPUSDT_4h_direction_structure_v1 proxy_tier=2 (not a full-gate alert; stress/MDD unbound on proxy path)

## [ALERT] 2026-08-03 16:00:26 UTC (tier 2)

STRUCTURE_V1_HUNT complete best_tier=2 report=structure_v1_hunt_20260803T160026Z.json

## [INFO] 2026-08-03 16:13:46 UTC (tier 0)

STRUCTURE_ETH_SOL_SETTLE start settle_struct2_00_ETHUSDT_1h_fwd_return_20260803 fold=v2

## [INFO] 2026-08-03 16:13:46 UTC (tier 0)

START gen=settle_struct2_00_ETHUSDT_1h_fwd_return_20260803 ETHUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 16:14:09 UTC (tier 0)

PREDICTABILITY real=+0.15409 p=0.0476 surr_q95=+0.00052 surr_max=+0.00313 draws=20 passed=True

## [INFO] 2026-08-03 16:14:13 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 16:14:13 UTC (tier 0)

trial `839337ed-968a-46bf-a051-45f44b4be041` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 16:14:25 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00425 skill_surrogate=+0.00086

## [INFO] 2026-08-03 16:14:25 UTC (tier 0)

trial `b81a50ac-0b2f-4487-b983-8c5fe7c7e948` model=ridge tier=0 target=fwd_return pf=0.849 n=4163 gates=FAIL

## [ALERT] 2026-08-03 16:14:48 UTC (tier 3)

trial `e2c04d12-db49-467e-84cc-0ff9e430d95f` model=lgbm_regressor tier=3 target=fwd_return pf=1.733 n=6337 gates=PASS

## [INFO] 2026-08-03 16:15:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-79.82235 skill_surrogate=-2.95367

## [INFO] 2026-08-03 16:15:18 UTC (tier 0)

trial `3f32be5f-49af-4c86-9f13-064b3e9c54e7` model=lgbm_classifier tier=0 target=fwd_return pf=1.499 n=7467 gates=PASS

## [INFO] 2026-08-03 16:15:18 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct2_00_ETHUSDT_1h_fwd_return_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:15:18 UTC (tier 0)

STRUCTURE_ETH_SOL_SETTLE start settle_struct2_01_ETHUSDT_1h_direction_20260803 fold=v2

## [INFO] 2026-08-03 16:15:18 UTC (tier 0)

START gen=settle_struct2_01_ETHUSDT_1h_direction_20260803 ETHUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 16:15:45 UTC (tier 0)

PREDICTABILITY real=+0.11497 p=0.0476 surr_q95=+0.00151 surr_max=+0.00156 draws=20 passed=True

## [INFO] 2026-08-03 16:15:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 16:15:49 UTC (tier 0)

trial `69ba4915-338c-471c-b9ef-d937e84b63ea` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 16:16:01 UTC (tier 0)

trial `c86d3150-4d1f-4884-a884-c5fd8a9ba066` model=ridge tier=0 target=direction pf=0.740 n=2787 gates=FAIL

## [ALERT] 2026-08-03 16:16:27 UTC (tier 3)

trial `cd89f070-1b3f-4979-a814-ecd3730f3e04` model=lgbm_regressor tier=3 target=direction pf=1.768 n=6473 gates=PASS

## [ALERT] 2026-08-03 16:17:00 UTC (tier 3)

trial `d50f9841-29a2-4323-bd6c-360e62738f9a` model=lgbm_classifier tier=3 target=direction pf=1.499 n=7467 gates=PASS

## [INFO] 2026-08-03 16:17:00 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct2_01_ETHUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:17:00 UTC (tier 0)

STRUCTURE_ETH_SOL_SETTLE start settle_struct2_02_SOLUSDT_1h_fwd_return_20260803 fold=v2

## [INFO] 2026-08-03 16:17:00 UTC (tier 0)

START gen=settle_struct2_02_SOLUSDT_1h_fwd_return_20260803 SOLUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 16:17:28 UTC (tier 0)

PREDICTABILITY real=+0.06248 p=0.0476 surr_q95=-0.00107 surr_max=-0.00088 draws=20 passed=True

## [INFO] 2026-08-03 16:17:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 16:17:36 UTC (tier 0)

trial `5ad78a04-da07-4e71-ab88-0ba09306c466` model=hist_mean tier=0 target=fwd_return pf=0.751 n=2800 gates=FAIL

## [INFO] 2026-08-03 16:17:54 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00140 skill_surrogate=-0.00422

## [INFO] 2026-08-03 16:17:54 UTC (tier 0)

trial `afd248ab-ddc0-452b-8b68-1e72a6fbcdf5` model=ridge tier=0 target=fwd_return pf=0.791 n=9196 gates=FAIL

## [ALERT] 2026-08-03 16:18:18 UTC (tier 3)

trial `330a75ba-93f6-48d8-b14b-02a4295b222f` model=lgbm_regressor tier=3 target=fwd_return pf=1.471 n=10832 gates=PASS

## [INFO] 2026-08-03 16:18:48 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-70.30322 skill_surrogate=-2.14433

## [INFO] 2026-08-03 16:18:48 UTC (tier 0)

trial `52d45253-8c42-4f86-8b64-cf8052f0e18a` model=lgbm_classifier tier=0 target=fwd_return pf=1.517 n=12547 gates=PASS

## [INFO] 2026-08-03 16:18:48 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct2_02_SOLUSDT_1h_fwd_return_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:18:48 UTC (tier 0)

STRUCTURE_ETH_SOL_SETTLE start settle_struct2_03_SOLUSDT_1h_direction_20260803 fold=v2

## [INFO] 2026-08-03 16:18:48 UTC (tier 0)

START gen=settle_struct2_03_SOLUSDT_1h_direction_20260803 SOLUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 16:19:12 UTC (tier 0)

PREDICTABILITY real=+0.12335 p=0.0476 surr_q95=-0.00049 surr_max=+0.00152 draws=20 passed=True

## [INFO] 2026-08-03 16:19:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 16:19:16 UTC (tier 0)

trial `59f9524e-21f7-4aff-82b0-ec6fea1d1a29` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 16:19:27 UTC (tier 0)

trial `72c83457-18db-4518-a85c-0c70ec7135ba` model=ridge tier=0 target=direction pf=0.815 n=5484 gates=FAIL

## [ALERT] 2026-08-03 16:19:46 UTC (tier 3)

trial `4a277aeb-36d4-48af-bff1-1a8c47ca2739` model=lgbm_regressor tier=3 target=direction pf=1.858 n=10318 gates=PASS

## [ALERT] 2026-08-03 16:20:20 UTC (tier 3)

trial `8cb91ab3-8ab6-48e2-afdc-14ad6058dad4` model=lgbm_classifier tier=3 target=direction pf=1.517 n=12547 gates=PASS

## [INFO] 2026-08-03 16:20:20 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct2_03_SOLUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 16:20:20 UTC (tier 2)

STRUCTURE_ETH_SOL_SETTLE done best_pass=True path=D:\projects\LLM2\artifacts\reports\structure_v1_eth_sol_settle_20260803T161346Z.json

## [INFO] 2026-08-03 16:38:32 UTC (tier 0)

START gen=metrics_struct2_00_ETHUSDT_1h_fwd_return_20260803 ETHUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 16:38:49 UTC (tier 0)

PREDICTABILITY real=+0.15409 p=0.0476 surr_q95=+0.00052 surr_max=+0.00313 draws=20 passed=True

## [ALERT] 2026-08-03 16:39:06 UTC (tier 3)

trial `82b1d7c5-9999-467b-8672-95193dfd7d2a` model=lgbm_regressor tier=3 target=fwd_return pf=1.733 n=6337 gates=PASS

## [INFO] 2026-08-03 16:39:06 UTC (tier 0)

Hunt complete: {"generation_id": "metrics_struct2_00_ETHUSDT_1h_fwd_return_20260803", "status": "COMPLETE", "n_trials": 1, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:39:06 UTC (tier 0)

START gen=metrics_struct2_01_ETHUSDT_1h_direction_20260803 ETHUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 16:39:22 UTC (tier 0)

PREDICTABILITY real=+0.11497 p=0.0476 surr_q95=+0.00151 surr_max=+0.00156 draws=20 passed=True

## [ALERT] 2026-08-03 16:39:37 UTC (tier 3)

trial `4cff985d-c8a5-41a7-a72d-9ad8c2779523` model=lgbm_regressor tier=3 target=direction pf=1.768 n=6473 gates=PASS

## [INFO] 2026-08-03 16:39:37 UTC (tier 0)

Hunt complete: {"generation_id": "metrics_struct2_01_ETHUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 1, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:39:37 UTC (tier 0)

START gen=metrics_struct2_02_SOLUSDT_1h_fwd_return_20260803 SOLUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 16:39:49 UTC (tier 0)

PREDICTABILITY real=+0.06248 p=0.0476 surr_q95=-0.00107 surr_max=-0.00088 draws=20 passed=True

## [ALERT] 2026-08-03 16:40:03 UTC (tier 3)

trial `9552f443-228e-4176-95e7-9d1b9184f6f0` model=lgbm_regressor tier=3 target=fwd_return pf=1.471 n=10832 gates=PASS

## [INFO] 2026-08-03 16:40:03 UTC (tier 0)

Hunt complete: {"generation_id": "metrics_struct2_02_SOLUSDT_1h_fwd_return_20260803", "status": "COMPLETE", "n_trials": 1, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 16:40:03 UTC (tier 0)

START gen=metrics_struct2_03_SOLUSDT_1h_direction_20260803 SOLUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 16:40:26 UTC (tier 0)

PREDICTABILITY real=+0.12335 p=0.0476 surr_q95=-0.00049 surr_max=+0.00152 draws=20 passed=True

## [ALERT] 2026-08-03 16:40:51 UTC (tier 3)

trial `265c50f8-d5bc-4e13-ad6c-13663e24292f` model=lgbm_regressor tier=3 target=direction pf=1.858 n=10318 gates=PASS

## [INFO] 2026-08-03 16:40:51 UTC (tier 0)

Hunt complete: {"generation_id": "metrics_struct2_03_SOLUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 1, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:01:24 UTC (tier 0)

STRUCTURE_LEAKAGE_RECHECK overall_ok=True pass=26/26 path=structure_v1_leakage_recheck_20260803T175941Z.json

## [INFO] 2026-08-03 18:01:55 UTC (tier 0)

STRUCTURE_V1_EXPANSION_HUNT start rev=struct3 leakage=structure_v1_leakage_recheck_20260803T175941Z.json

## [INFO] 2026-08-03 18:01:55 UTC (tier 0)

START gen=autostruct3_00_BNBUSDT_1h_fwd_return_structure_v1 BNBUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:02:14 UTC (tier 0)

PREDICTABILITY real=+0.06326 p=0.0476 surr_q95=+0.00014 surr_max=+0.00086 draws=20 passed=True

## [INFO] 2026-08-03 18:02:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:02:17 UTC (tier 0)

trial `7de991db-475e-4bfa-a0a2-3bfcdbfc2648` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:02:18 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00795 skill_surrogate=-0.00099

## [INFO] 2026-08-03 18:02:18 UTC (tier 0)

trial `82e1049a-8c9d-43ec-9c0f-4a036a7f0621` model=ridge tier=0 target=fwd_return pf=0.762 n=17875 gates=FAIL

## [ALERT] 2026-08-03 18:02:22 UTC (tier 2)

trial `a68c1d6b-77c8-40c5-9362-c0e21383c55e` model=lgbm_regressor tier=2 target=fwd_return pf=2.913 n=15375 gates=UNKNOWN

## [INFO] 2026-08-03 18:02:30 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-99.39669 skill_surrogate=-4.08678

## [INFO] 2026-08-03 18:02:30 UTC (tier 0)

trial `d6b6ae45-25fc-40fa-b621-55834e1e6e82` model=lgbm_classifier tier=0 target=fwd_return pf=1.910 n=37488 gates=UNKNOWN

## [INFO] 2026-08-03 18:02:30 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_00_BNBUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:02:30 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_00_BNBUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:02:31 UTC (tier 0)

START gen=autostruct3_01_BNBUSDT_1h_direction_structure_v1 BNBUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:02:49 UTC (tier 0)

PREDICTABILITY real=+0.13125 p=0.0476 surr_q95=+0.00049 surr_max=+0.00134 draws=20 passed=True

## [INFO] 2026-08-03 18:02:50 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:02:50 UTC (tier 0)

trial `b391a383-abee-4ca2-9224-0d24796f3df4` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:02:50 UTC (tier 1)

trial `9b624e48-3602-41d8-9182-5d1b675347f7` model=ridge tier=1 target=direction pf=0.801 n=9394 gates=FAIL

## [ALERT] 2026-08-03 18:02:53 UTC (tier 2)

trial `d5f3d41c-9222-4f79-9825-feb063670830` model=lgbm_regressor tier=2 target=direction pf=2.630 n=26865 gates=UNKNOWN

## [ALERT] 2026-08-03 18:02:59 UTC (tier 2)

trial `cefb0302-9d41-488d-bbaf-e1d62140702e` model=lgbm_classifier tier=2 target=direction pf=1.910 n=37488 gates=UNKNOWN

## [INFO] 2026-08-03 18:02:59 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_01_BNBUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:02:59 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_01_BNBUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:02:59 UTC (tier 0)

START gen=autostruct3_02_XRPUSDT_1h_fwd_return_structure_v1 XRPUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:03:16 UTC (tier 0)

PREDICTABILITY real=+0.03707 p=0.0476 surr_q95=+0.00093 surr_max=+0.00153 draws=20 passed=True

## [INFO] 2026-08-03 18:03:19 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:03:19 UTC (tier 0)

trial `34ac8435-8a95-4c5c-96b3-b9d0943c8c69` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:03:19 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01595 skill_surrogate=-0.00282

## [INFO] 2026-08-03 18:03:19 UTC (tier 0)

trial `c71ae313-c7ad-494a-9ced-fc9e5861dc34` model=ridge tier=0 target=fwd_return pf=0.830 n=19258 gates=FAIL

## [ALERT] 2026-08-03 18:03:22 UTC (tier 2)

trial `30b25f83-9feb-46f1-957d-d73e4e6145d1` model=lgbm_regressor tier=2 target=fwd_return pf=2.296 n=14768 gates=UNKNOWN

## [INFO] 2026-08-03 18:03:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-78.07186 skill_surrogate=-1.99536

## [INFO] 2026-08-03 18:03:28 UTC (tier 0)

trial `ca379298-2f4d-4042-8b12-0ee454636a7a` model=lgbm_classifier tier=0 target=fwd_return pf=2.192 n=32557 gates=UNKNOWN

## [INFO] 2026-08-03 18:03:28 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_02_XRPUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:03:28 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_02_XRPUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:03:28 UTC (tier 0)

START gen=autostruct3_03_XRPUSDT_1h_direction_structure_v1 XRPUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:03:44 UTC (tier 0)

PREDICTABILITY real=+0.13225 p=0.0476 surr_q95=+0.00019 surr_max=+0.00112 draws=20 passed=True

## [INFO] 2026-08-03 18:03:45 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:03:45 UTC (tier 0)

trial `947e1ee1-f5ca-4b9a-bc59-efb0e847db1f` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:03:46 UTC (tier 1)

trial `a9251bcf-837a-49db-ac03-ddcbee073612` model=ridge tier=1 target=direction pf=0.792 n=8322 gates=FAIL

## [ALERT] 2026-08-03 18:03:48 UTC (tier 2)

trial `f7250f42-c00c-4ff3-91dd-afff7380a9a3` model=lgbm_regressor tier=2 target=direction pf=2.924 n=23622 gates=UNKNOWN

## [ALERT] 2026-08-03 18:03:57 UTC (tier 2)

trial `cd912bfb-5f7d-423f-baf1-22a7819296d2` model=lgbm_classifier tier=2 target=direction pf=2.192 n=32557 gates=UNKNOWN

## [INFO] 2026-08-03 18:03:57 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_03_XRPUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:03:57 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_03_XRPUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:03:57 UTC (tier 0)

START gen=autostruct3_04_VETUSDT_1h_fwd_return_structure_v1 VETUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:04:12 UTC (tier 0)

PREDICTABILITY real=+0.06513 p=0.0476 surr_q95=+0.00045 surr_max=+0.00053 draws=20 passed=True

## [INFO] 2026-08-03 18:04:15 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:04:15 UTC (tier 0)

trial `a63e3d65-ec65-432a-8c2b-610e393de2ff` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:04:15 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.15564 skill_surrogate=-0.01488

## [INFO] 2026-08-03 18:04:15 UTC (tier 0)

trial `31bb0d07-04d4-44fd-9a21-dbd6a310ce32` model=ridge tier=0 target=fwd_return pf=0.783 n=21941 gates=FAIL

## [ALERT] 2026-08-03 18:04:18 UTC (tier 2)

trial `7b245c28-3b73-46ff-83e2-fc6edd8bef5a` model=lgbm_regressor tier=2 target=fwd_return pf=2.678 n=22719 gates=UNKNOWN

## [INFO] 2026-08-03 18:04:26 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-65.33592 skill_surrogate=-7.03612

## [INFO] 2026-08-03 18:04:26 UTC (tier 0)

trial `0d35ae00-8272-4c82-82bf-89c5aa371cd8` model=lgbm_classifier tier=0 target=fwd_return pf=2.246 n=33312 gates=UNKNOWN

## [INFO] 2026-08-03 18:04:26 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_04_VETUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:04:26 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_04_VETUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:04:26 UTC (tier 0)

START gen=autostruct3_05_VETUSDT_1h_direction_structure_v1 VETUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:04:39 UTC (tier 0)

PREDICTABILITY real=+0.10259 p=0.0476 surr_q95=+0.00017 surr_max=+0.00032 draws=20 passed=True

## [INFO] 2026-08-03 18:04:41 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:04:41 UTC (tier 0)

trial `37826e85-50ea-471a-9f7a-f739c1a2d541` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:04:41 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.02182 skill_surrogate=+0.00390

## [INFO] 2026-08-03 18:04:41 UTC (tier 0)

trial `567afcb7-2a0a-429a-97aa-fd3913a1b505` model=ridge tier=0 target=direction pf=0.828 n=12802 gates=FAIL

## [ALERT] 2026-08-03 18:04:44 UTC (tier 2)

trial `a4d8bca3-63a4-4cf1-8599-1c4c62c8ea57` model=lgbm_regressor tier=2 target=direction pf=3.176 n=22747 gates=UNKNOWN

## [ALERT] 2026-08-03 18:04:50 UTC (tier 2)

trial `17d5b658-5a77-4915-a964-94f1492db278` model=lgbm_classifier tier=2 target=direction pf=2.246 n=33312 gates=UNKNOWN

## [INFO] 2026-08-03 18:04:50 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_05_VETUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:04:50 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_05_VETUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:04:50 UTC (tier 0)

START gen=autostruct3_06_ADAUSDT_1h_fwd_return_structure_v1 ADAUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:05:06 UTC (tier 0)

PREDICTABILITY real=+0.12057 p=0.0476 surr_q95=-0.00111 surr_max=-0.00045 draws=20 passed=True

## [INFO] 2026-08-03 18:05:10 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:05:10 UTC (tier 0)

trial `3b31ec1d-3781-4060-be2d-45c78c466155` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:05:10 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.08511 skill_surrogate=-0.00270

## [INFO] 2026-08-03 18:05:10 UTC (tier 0)

trial `ce46ee1b-2d5b-46ff-8187-c8e6333f3156` model=ridge tier=0 target=fwd_return pf=0.866 n=20307 gates=FAIL

## [ALERT] 2026-08-03 18:05:12 UTC (tier 2)

trial `0ac0ac66-37e2-4fc2-b50e-c71e342e49e9` model=lgbm_regressor tier=2 target=fwd_return pf=2.525 n=21455 gates=UNKNOWN

## [INFO] 2026-08-03 18:05:18 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-63.49471 skill_surrogate=-1.47274

## [INFO] 2026-08-03 18:05:18 UTC (tier 0)

trial `f9eb0152-0817-4084-bf44-3b12c4ddd95f` model=lgbm_classifier tier=0 target=fwd_return pf=2.187 n=32966 gates=UNKNOWN

## [INFO] 2026-08-03 18:05:18 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_06_ADAUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:05:18 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_06_ADAUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:05:18 UTC (tier 0)

START gen=autostruct3_07_ADAUSDT_1h_direction_structure_v1 ADAUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:05:36 UTC (tier 0)

PREDICTABILITY real=+0.12392 p=0.0476 surr_q95=-0.00184 surr_max=-0.00127 draws=20 passed=True

## [INFO] 2026-08-03 18:05:40 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:05:40 UTC (tier 0)

trial `93ae5cf5-2c8d-4499-8dcb-b426176ab7f2` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:05:40 UTC (tier 1)

trial `15f1c250-1a02-40bc-b1b8-a96f364654ed` model=ridge tier=1 target=direction pf=0.913 n=10809 gates=FAIL

## [ALERT] 2026-08-03 18:05:43 UTC (tier 2)

trial `1f1c9257-4a22-487b-8012-e3f84583b381` model=lgbm_regressor tier=2 target=direction pf=2.865 n=24045 gates=UNKNOWN

## [ALERT] 2026-08-03 18:05:52 UTC (tier 2)

trial `fc05c877-f38c-4edb-bc09-e591013584dd` model=lgbm_classifier tier=2 target=direction pf=2.187 n=32966 gates=UNKNOWN

## [INFO] 2026-08-03 18:05:52 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_07_ADAUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:05:52 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_07_ADAUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:05:52 UTC (tier 0)

START gen=autostruct3_08_DOGEUSDT_1h_fwd_return_structure_v1 DOGEUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:06:11 UTC (tier 0)

PREDICTABILITY real=+0.02216 p=0.0476 surr_q95=-0.00064 surr_max=+0.00164 draws=20 passed=True

## [INFO] 2026-08-03 18:06:17 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:06:17 UTC (tier 0)

trial `1221e6c1-0c7e-40fd-83d3-4e5d51cfe7a7` model=hist_mean tier=0 target=fwd_return pf=0.741 n=6498 gates=FAIL

## [INFO] 2026-08-03 18:06:18 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01626 skill_surrogate=-0.00038

## [INFO] 2026-08-03 18:06:18 UTC (tier 0)

trial `be359887-2233-4e20-b225-d63c51cc175d` model=ridge tier=0 target=fwd_return pf=0.864 n=23451 gates=FAIL

## [ALERT] 2026-08-03 18:06:20 UTC (tier 2)

trial `eab33979-3a13-4975-9fb1-50fa8fbfb0ed` model=lgbm_regressor tier=2 target=fwd_return pf=2.365 n=16613 gates=UNKNOWN

## [INFO] 2026-08-03 18:06:27 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-68.05329 skill_surrogate=-1.87366

## [INFO] 2026-08-03 18:06:27 UTC (tier 0)

trial `b3c043cd-7b41-412d-b60b-f70bb82211e3` model=lgbm_classifier tier=0 target=fwd_return pf=2.015 n=36275 gates=UNKNOWN

## [INFO] 2026-08-03 18:06:27 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_08_DOGEUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:06:27 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_08_DOGEUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:06:27 UTC (tier 0)

START gen=autostruct3_09_DOGEUSDT_1h_direction_structure_v1 DOGEUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:06:40 UTC (tier 0)

PREDICTABILITY real=+0.12007 p=0.0476 surr_q95=-0.00045 surr_max=+0.00090 draws=20 passed=True

## [INFO] 2026-08-03 18:06:43 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:06:43 UTC (tier 0)

trial `75464a7a-8290-4190-aaca-7cdf31847c58` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:06:44 UTC (tier 1)

trial `d4ed51bd-a685-4331-a3a2-cf2bfc9b649c` model=ridge tier=1 target=direction pf=0.872 n=10898 gates=FAIL

## [ALERT] 2026-08-03 18:06:47 UTC (tier 2)

trial `3d14efa3-8d4a-462c-aad1-c2047e538cde` model=lgbm_regressor tier=2 target=direction pf=2.660 n=26031 gates=UNKNOWN

## [ALERT] 2026-08-03 18:06:55 UTC (tier 2)

trial `90ba2845-7819-4c96-ab0c-d72fd7c88251` model=lgbm_classifier tier=2 target=direction pf=2.015 n=36275 gates=UNKNOWN

## [INFO] 2026-08-03 18:06:55 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_09_DOGEUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:06:55 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_09_DOGEUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:06:55 UTC (tier 0)

START gen=autostruct3_10_AVAXUSDT_1h_fwd_return_structure_v1 AVAXUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:07:10 UTC (tier 0)

PREDICTABILITY real=+0.06003 p=0.0476 surr_q95=-0.00070 surr_max=+0.00023 draws=20 passed=True

## [INFO] 2026-08-03 18:07:15 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:07:15 UTC (tier 0)

trial `0c6cbb4a-6727-471c-b604-9b63aa2132cf` model=hist_mean tier=0 target=fwd_return pf=0.750 n=6429 gates=FAIL

## [INFO] 2026-08-03 18:07:16 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00443 skill_surrogate=-0.00146

## [INFO] 2026-08-03 18:07:16 UTC (tier 0)

trial `ab6c3bab-bde1-4cc0-b9a5-043867dfb02f` model=ridge tier=0 target=fwd_return pf=0.801 n=19178 gates=FAIL

## [ALERT] 2026-08-03 18:07:18 UTC (tier 2)

trial `179e588e-3d91-43a3-bd64-9257d3ec06b0` model=lgbm_regressor tier=2 target=fwd_return pf=2.464 n=27723 gates=UNKNOWN

## [INFO] 2026-08-03 18:07:25 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-68.81044 skill_surrogate=-1.69504

## [INFO] 2026-08-03 18:07:25 UTC (tier 0)

trial `53273984-fa0d-49ae-9980-da6b48df46fa` model=lgbm_classifier tier=0 target=fwd_return pf=2.153 n=37177 gates=UNKNOWN

## [INFO] 2026-08-03 18:07:25 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_10_AVAXUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:07:25 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_10_AVAXUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:07:25 UTC (tier 0)

START gen=autostruct3_11_AVAXUSDT_1h_direction_structure_v1 AVAXUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:07:42 UTC (tier 0)

PREDICTABILITY real=+0.10390 p=0.0476 surr_q95=-0.00009 surr_max=+0.00039 draws=20 passed=True

## [INFO] 2026-08-03 18:07:44 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:07:44 UTC (tier 0)

trial `1e118572-fcd8-4a64-9dc0-caf3784ad731` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:07:44 UTC (tier 1)

trial `7821494e-12bd-4519-bb4c-7cfe49e642d1` model=ridge tier=1 target=direction pf=0.779 n=8670 gates=FAIL

## [ALERT] 2026-08-03 18:07:46 UTC (tier 2)

trial `736d16dc-eb90-4373-8522-55d1326500bf` model=lgbm_regressor tier=2 target=direction pf=2.947 n=26397 gates=UNKNOWN

## [ALERT] 2026-08-03 18:07:52 UTC (tier 2)

trial `9a47d5b3-c50e-4556-a647-bda2cd328c08` model=lgbm_classifier tier=2 target=direction pf=2.153 n=37177 gates=UNKNOWN

## [INFO] 2026-08-03 18:07:52 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_11_AVAXUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:07:52 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_11_AVAXUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:07:52 UTC (tier 0)

START gen=autostruct3_12_LINKUSDT_1h_fwd_return_structure_v1 LINKUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:08:07 UTC (tier 0)

PREDICTABILITY real=+0.13018 p=0.0476 surr_q95=-0.00008 surr_max=+0.00016 draws=20 passed=True

## [INFO] 2026-08-03 18:08:11 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:08:11 UTC (tier 0)

trial `a0fec1ff-49f0-4d66-bd0e-30522db75382` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:08:11 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00607 skill_surrogate=-0.00223

## [INFO] 2026-08-03 18:08:11 UTC (tier 0)

trial `bb1cf591-0889-488b-998e-fa451758bf2d` model=ridge tier=0 target=fwd_return pf=0.857 n=20917 gates=FAIL

## [ALERT] 2026-08-03 18:08:16 UTC (tier 2)

trial `69fedacf-29c8-4023-8169-1987aea75e80` model=lgbm_regressor tier=2 target=fwd_return pf=2.598 n=27293 gates=UNKNOWN

## [INFO] 2026-08-03 18:08:25 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-68.45865 skill_surrogate=-2.16490

## [INFO] 2026-08-03 18:08:25 UTC (tier 0)

trial `85f6a6cc-5963-4a80-9ce5-d86d76070816` model=lgbm_classifier tier=0 target=fwd_return pf=2.227 n=35615 gates=UNKNOWN

## [INFO] 2026-08-03 18:08:25 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_12_LINKUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:08:25 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_12_LINKUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:08:25 UTC (tier 0)

START gen=autostruct3_13_LINKUSDT_1h_direction_structure_v1 LINKUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:08:43 UTC (tier 0)

PREDICTABILITY real=+0.11884 p=0.0476 surr_q95=-0.00156 surr_max=-0.00127 draws=20 passed=True

## [INFO] 2026-08-03 18:08:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:08:46 UTC (tier 0)

trial `82fcaf85-01ad-45d1-8e58-7bbadb947d55` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:08:47 UTC (tier 1)

trial `61943702-86ec-4c20-b2b0-4023f1ce66f9` model=ridge tier=1 target=direction pf=0.842 n=10339 gates=FAIL

## [ALERT] 2026-08-03 18:08:50 UTC (tier 2)

trial `49230e86-9ffc-400f-a954-5b98efeac2af` model=lgbm_regressor tier=2 target=direction pf=3.124 n=24689 gates=UNKNOWN

## [ALERT] 2026-08-03 18:08:57 UTC (tier 2)

trial `76d4bf50-82e3-448e-8511-bad9d22e80ee` model=lgbm_classifier tier=2 target=direction pf=2.227 n=35615 gates=UNKNOWN

## [INFO] 2026-08-03 18:08:57 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_13_LINKUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:08:57 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_13_LINKUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:08:57 UTC (tier 0)

START gen=autostruct3_14_DOTUSDT_1h_fwd_return_structure_v1 DOTUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:09:13 UTC (tier 0)

PREDICTABILITY real=+0.10821 p=0.0476 surr_q95=-0.00160 surr_max=-0.00087 draws=20 passed=True

## [INFO] 2026-08-03 18:09:20 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:09:20 UTC (tier 0)

trial `5e272a7d-a4dd-4d94-a28a-b66cbbb5227c` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:09:20 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.03592 skill_surrogate=-0.01977

## [INFO] 2026-08-03 18:09:20 UTC (tier 0)

trial `c562d3a5-9a79-461f-ba37-bf798daaf2b3` model=ridge tier=0 target=fwd_return pf=0.835 n=19789 gates=FAIL

## [ALERT] 2026-08-03 18:09:22 UTC (tier 2)

trial `df712055-a6bc-4dda-a316-ac43ac2130fe` model=lgbm_regressor tier=2 target=fwd_return pf=2.393 n=22790 gates=UNKNOWN

## [INFO] 2026-08-03 18:09:28 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-61.39610 skill_surrogate=-2.12203

## [INFO] 2026-08-03 18:09:28 UTC (tier 0)

trial `0bb995b6-4856-4430-81c1-f1c4e3e2a833` model=lgbm_classifier tier=0 target=fwd_return pf=2.103 n=32435 gates=UNKNOWN

## [INFO] 2026-08-03 18:09:28 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_14_DOTUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:09:28 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_14_DOTUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:09:28 UTC (tier 0)

START gen=autostruct3_15_DOTUSDT_1h_direction_structure_v1 DOTUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:09:43 UTC (tier 0)

PREDICTABILITY real=+0.12322 p=0.0476 surr_q95=-0.00204 surr_max=-0.00102 draws=20 passed=True

## [INFO] 2026-08-03 18:09:46 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:09:46 UTC (tier 0)

trial `5a959fa8-ea16-4d38-bf49-1f9e132ee6c1` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:09:46 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00278 skill_surrogate=+0.00109

## [INFO] 2026-08-03 18:09:46 UTC (tier 0)

trial `a572d6ff-28c6-45ed-b250-64e1f63e660c` model=ridge tier=0 target=direction pf=0.810 n=10397 gates=FAIL

## [ALERT] 2026-08-03 18:09:49 UTC (tier 2)

trial `5bf03f72-fe13-4a22-a4d5-0e0c159c6809` model=lgbm_regressor tier=2 target=direction pf=2.940 n=23095 gates=UNKNOWN

## [ALERT] 2026-08-03 18:09:55 UTC (tier 2)

trial `eb841d71-2e0e-485b-8721-3f10519ed69e` model=lgbm_classifier tier=2 target=direction pf=2.103 n=32435 gates=UNKNOWN

## [INFO] 2026-08-03 18:09:55 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_15_DOTUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:09:55 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_15_DOTUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:09:55 UTC (tier 0)

START gen=autostruct3_16_TRXUSDT_1h_fwd_return_structure_v1 TRXUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:10:12 UTC (tier 0)

PREDICTABILITY real=-0.00797 p=0.6667 surr_q95=-0.00059 surr_max=-0.00011 draws=20 passed=False

## [INFO] 2026-08-03 18:10:20 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:10:20 UTC (tier 0)

trial `aa69f3c4-941d-40e0-8627-ac4be489cc53` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:10:21 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.03180 skill_surrogate=-0.00324

## [INFO] 2026-08-03 18:10:21 UTC (tier 0)

trial `f73b7373-a2b4-496a-afb3-6dcceeda5ce3` model=ridge tier=0 target=fwd_return pf=0.807 n=16393 gates=FAIL

## [INFO] 2026-08-03 18:10:23 UTC (tier 0)

trial `da280acb-9b88-4fa3-a0ee-c38303b90c69` model=lgbm_regressor tier=0 target=fwd_return pf=2.262 n=12950 gates=UNKNOWN

## [INFO] 2026-08-03 18:10:29 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-196.57225 skill_surrogate=-12.54602

## [INFO] 2026-08-03 18:10:29 UTC (tier 0)

trial `101406eb-ee13-4590-97bb-1bb690eb7083` model=lgbm_classifier tier=0 target=fwd_return pf=1.722 n=34907 gates=UNKNOWN

## [INFO] 2026-08-03 18:10:29 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_16_TRXUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:10:29 UTC (tier 0)

START gen=autostruct3_17_TRXUSDT_1h_direction_structure_v1 TRXUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:10:46 UTC (tier 0)

PREDICTABILITY real=+0.11841 p=0.0476 surr_q95=-0.00085 surr_max=-0.00059 draws=20 passed=True

## [INFO] 2026-08-03 18:10:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:10:49 UTC (tier 0)

trial `7119fff1-2391-41fd-987e-514d17f59dd0` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:10:49 UTC (tier 1)

trial `5c937193-4a89-47b0-b43c-fc3d2c351406` model=ridge tier=1 target=direction pf=0.783 n=12817 gates=FAIL

## [ALERT] 2026-08-03 18:10:52 UTC (tier 2)

trial `1b076ea3-287d-46b7-a8d3-4f53b8e3ba6e` model=lgbm_regressor tier=2 target=direction pf=2.328 n=24123 gates=UNKNOWN

## [ALERT] 2026-08-03 18:10:58 UTC (tier 2)

trial `c90af802-0123-4478-af82-964adfc897a1` model=lgbm_classifier tier=2 target=direction pf=1.722 n=34907 gates=UNKNOWN

## [INFO] 2026-08-03 18:10:58 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_17_TRXUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:10:58 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_17_TRXUSDT_1h_direction_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:10:58 UTC (tier 0)

START gen=autostruct3_18_XLMUSDT_1h_fwd_return_structure_v1 XLMUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:11:17 UTC (tier 0)

PREDICTABILITY real=+0.09639 p=0.0476 surr_q95=-0.00050 surr_max=-0.00030 draws=20 passed=True

## [INFO] 2026-08-03 18:11:24 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:11:24 UTC (tier 0)

trial `b07365ca-7fed-468c-8539-8363a8ddb45f` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:11:24 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00000 skill_surrogate=+0.00002

## [INFO] 2026-08-03 18:11:24 UTC (tier 0)

trial `3ac0663d-91a4-450c-aca5-5a9b8a8c8883` model=ridge tier=0 target=fwd_return pf=0.832 n=20507 gates=FAIL

## [ALERT] 2026-08-03 18:11:27 UTC (tier 2)

trial `f84e903f-8e06-47d1-b127-00a4edc96a6f` model=lgbm_regressor tier=2 target=fwd_return pf=2.616 n=20548 gates=UNKNOWN

## [INFO] 2026-08-03 18:11:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-71.23154 skill_surrogate=-1.64654

## [INFO] 2026-08-03 18:11:34 UTC (tier 0)

trial `13e01e64-28ba-4c49-bb0f-ddb334731e2d` model=lgbm_classifier tier=0 target=fwd_return pf=2.032 n=35854 gates=UNKNOWN

## [INFO] 2026-08-03 18:11:34 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_18_XLMUSDT_1h_fwd_return_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:11:34 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_18_XLMUSDT_1h_fwd_return_structure_v1 proxy_tier=2

## [INFO] 2026-08-03 18:11:34 UTC (tier 0)

START gen=autostruct3_19_XLMUSDT_1h_direction_structure_v1 XLMUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:11:50 UTC (tier 0)

PREDICTABILITY real=+0.11188 p=0.0476 surr_q95=-0.00095 surr_max=-0.00052 draws=20 passed=True

## [INFO] 2026-08-03 18:11:53 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:11:53 UTC (tier 0)

trial `8f910ea7-b03d-426e-95ca-0d22c82b1864` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:11:54 UTC (tier 1)

trial `da1710ec-a32e-415c-a305-a4f6bb7c71df` model=ridge tier=1 target=direction pf=0.827 n=10192 gates=FAIL

## [ALERT] 2026-08-03 18:11:56 UTC (tier 2)

trial `a3d3f53f-4906-4d27-8ed6-d1cd1fc99385` model=lgbm_regressor tier=2 target=direction pf=2.712 n=24853 gates=UNKNOWN

## [ALERT] 2026-08-03 18:12:03 UTC (tier 2)

trial `1a5cd70b-502b-4c1a-9a54-433cc9fb1f78` model=lgbm_classifier tier=2 target=direction pf=2.032 n=35854 gates=UNKNOWN

## [INFO] 2026-08-03 18:12:03 UTC (tier 0)

Hunt complete: {"generation_id": "autostruct3_19_XLMUSDT_1h_direction_structure_v1", "status": "COMPLETE", "n_trials": 4, "best_tier": 2, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:12:03 UTC (tier 1)

SCREEN_CANDIDATE structure_v1 autostruct3_19_XLMUSDT_1h_direction_structure_v1 proxy_tier=2

## [ALERT] 2026-08-03 18:12:03 UTC (tier 2)

STRUCTURE_V1_EXPANSION_HUNT complete best_tier=2 report=structure_v1_expansion_hunt_20260803T181203Z.json

## [INFO] 2026-08-03 18:12:35 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_00_VETUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:12:35 UTC (tier 0)

START gen=settle_struct3_00_VETUSDT_1h_direction_20260803 VETUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:12:53 UTC (tier 0)

PREDICTABILITY real=+0.10259 p=0.0476 surr_q95=+0.00017 surr_max=+0.00032 draws=20 passed=True

## [INFO] 2026-08-03 18:12:57 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:12:57 UTC (tier 0)

trial `2132befe-5796-4207-a495-3e2c2a00a453` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:13:04 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.02182 skill_surrogate=+0.00528

## [INFO] 2026-08-03 18:13:04 UTC (tier 0)

trial `6cfea2d9-1fc8-435e-9c8b-15a12beff8e9` model=ridge tier=0 target=direction pf=0.805 n=4687 gates=FAIL

## [ALERT] 2026-08-03 18:13:19 UTC (tier 3)

trial `bee97470-6202-4fe8-ad97-c34276837c20` model=lgbm_regressor tier=3 target=direction pf=1.921 n=8699 gates=PASS

## [ALERT] 2026-08-03 18:13:38 UTC (tier 3)

trial `ccbf6c4e-fbb4-4cbf-be31-7fa9a38cd714` model=lgbm_classifier tier=3 target=direction pf=1.509 n=10620 gates=PASS

## [INFO] 2026-08-03 18:13:38 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_00_VETUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:13:38 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_01_VETUSDT_1h_fwd_return_20260803

## [INFO] 2026-08-03 18:13:38 UTC (tier 0)

START gen=settle_struct3_01_VETUSDT_1h_fwd_return_20260803 VETUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:13:55 UTC (tier 0)

PREDICTABILITY real=+0.06513 p=0.0476 surr_q95=+0.00045 surr_max=+0.00053 draws=20 passed=True

## [INFO] 2026-08-03 18:13:58 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:13:58 UTC (tier 0)

trial `aa30ce08-9841-4791-9b47-fc82ff9635aa` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:14:08 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.15564 skill_surrogate=-0.01394

## [INFO] 2026-08-03 18:14:08 UTC (tier 0)

trial `6141e3eb-519f-419c-997f-412aec00e96a` model=ridge tier=0 target=fwd_return pf=0.794 n=7664 gates=FAIL

## [ALERT] 2026-08-03 18:14:21 UTC (tier 3)

trial `17cfa1f9-0ed9-42c4-b534-b829763ffad3` model=lgbm_regressor tier=3 target=fwd_return pf=1.689 n=8807 gates=PASS

## [INFO] 2026-08-03 18:14:38 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-65.33592 skill_surrogate=-1.79030

## [INFO] 2026-08-03 18:14:38 UTC (tier 0)

trial `ebd08100-5f56-481f-aa56-98de825f5410` model=lgbm_classifier tier=0 target=fwd_return pf=1.509 n=10620 gates=PASS

## [INFO] 2026-08-03 18:14:38 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_01_VETUSDT_1h_fwd_return_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:14:38 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_02_XRPUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:14:38 UTC (tier 0)

START gen=settle_struct3_02_XRPUSDT_1h_direction_20260803 XRPUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:14:54 UTC (tier 0)

PREDICTABILITY real=+0.13225 p=0.0476 surr_q95=+0.00019 surr_max=+0.00112 draws=20 passed=True

## [INFO] 2026-08-03 18:14:55 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:14:55 UTC (tier 0)

trial `d5dbbd91-038c-4ea9-bf0b-ab5243d6d61a` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:14:58 UTC (tier 0)

trial `b77bb406-9417-4274-8c13-ea726ea2d6aa` model=ridge tier=0 target=direction pf=0.698 n=3221 gates=FAIL

## [ALERT] 2026-08-03 18:15:06 UTC (tier 3)

trial `73ff9ac9-b19c-4e0d-aeae-f4095d8f3000` model=lgbm_regressor tier=3 target=direction pf=1.711 n=6853 gates=PASS

## [ALERT] 2026-08-03 18:15:17 UTC (tier 3)

trial `de066a09-a540-4bcf-8ae9-bb60e64cf84c` model=lgbm_classifier tier=3 target=direction pf=1.427 n=7992 gates=PASS

## [INFO] 2026-08-03 18:15:17 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_02_XRPUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:15:17 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_03_XRPUSDT_1h_fwd_return_20260803

## [INFO] 2026-08-03 18:15:17 UTC (tier 0)

START gen=settle_struct3_03_XRPUSDT_1h_fwd_return_20260803 XRPUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:15:30 UTC (tier 0)

PREDICTABILITY real=+0.03707 p=0.0476 surr_q95=+0.00093 surr_max=+0.00153 draws=20 passed=True

## [INFO] 2026-08-03 18:15:31 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:15:31 UTC (tier 0)

trial `f78c9c7a-7e68-4f07-b900-1e2d999e5b59` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:15:36 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.01595 skill_surrogate=-0.00198

## [INFO] 2026-08-03 18:15:36 UTC (tier 0)

trial `0ecec9bd-1c29-4855-b27a-21c6a2bcc3ea` model=ridge tier=0 target=fwd_return pf=0.739 n=5638 gates=FAIL

## [ALERT] 2026-08-03 18:15:44 UTC (tier 3)

trial `399eef9d-78f6-4fc2-b1e6-f1eab0fb8d4b` model=lgbm_regressor tier=3 target=fwd_return pf=1.313 n=5223 gates=PASS

## [INFO] 2026-08-03 18:15:58 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-78.07186 skill_surrogate=-2.33657

## [INFO] 2026-08-03 18:15:58 UTC (tier 0)

trial `f6bc19cb-32d5-41d1-9489-71f75c27a771` model=lgbm_classifier tier=0 target=fwd_return pf=1.427 n=7992 gates=PASS

## [INFO] 2026-08-03 18:15:58 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_03_XRPUSDT_1h_fwd_return_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:15:58 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_04_BNBUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:15:58 UTC (tier 0)

START gen=settle_struct3_04_BNBUSDT_1h_direction_20260803 BNBUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:16:14 UTC (tier 0)

PREDICTABILITY real=+0.13125 p=0.0476 surr_q95=+0.00049 surr_max=+0.00134 draws=20 passed=True

## [INFO] 2026-08-03 18:16:16 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:16:16 UTC (tier 0)

trial `a188ddb2-0495-4dcf-985a-7aff7aeb2b02` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:16:20 UTC (tier 0)

trial `2cecba8f-9af4-4fed-bd89-f7eea60b6505` model=ridge tier=0 target=direction pf=0.742 n=2867 gates=FAIL

## [ALERT] 2026-08-03 18:16:27 UTC (tier 3)

trial `41c33025-cf9e-499e-b292-db504857c05e` model=lgbm_regressor tier=3 target=direction pf=1.567 n=5216 gates=PASS

## [ALERT] 2026-08-03 18:16:42 UTC (tier 3)

trial `24e4f546-ea91-4957-991d-166aa330eacc` model=lgbm_classifier tier=3 target=direction pf=1.328 n=5742 gates=PASS

## [INFO] 2026-08-03 18:16:42 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_04_BNBUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:16:42 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_05_BNBUSDT_1h_fwd_return_20260803

## [INFO] 2026-08-03 18:16:42 UTC (tier 0)

START gen=settle_struct3_05_BNBUSDT_1h_fwd_return_20260803 BNBUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-03 18:16:57 UTC (tier 0)

PREDICTABILITY real=+0.06326 p=0.0476 surr_q95=+0.00014 surr_max=+0.00086 draws=20 passed=True

## [INFO] 2026-08-03 18:16:58 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:16:59 UTC (tier 0)

trial `5d036550-1599-419b-b3bd-e8be184b74de` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:17:02 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00795 skill_surrogate=-0.00372

## [INFO] 2026-08-03 18:17:02 UTC (tier 0)

trial `1a3265d1-6c02-4f12-a1a4-77a47d3960c7` model=ridge tier=0 target=fwd_return pf=0.748 n=3978 gates=FAIL

## [ALERT] 2026-08-03 18:17:09 UTC (tier 3)

trial `6854d33f-7957-496c-8f46-38aa320e1283` model=lgbm_regressor tier=3 target=fwd_return pf=1.650 n=4502 gates=PASS

## [INFO] 2026-08-03 18:17:23 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-99.39669 skill_surrogate=-4.78468

## [INFO] 2026-08-03 18:17:23 UTC (tier 0)

trial `2af3a881-25da-4c99-b0de-cd0006106a9f` model=lgbm_classifier tier=0 target=fwd_return pf=1.328 n=5742 gates=PASS

## [INFO] 2026-08-03 18:17:23 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_05_BNBUSDT_1h_fwd_return_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:17:23 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_06_ADAUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:17:23 UTC (tier 0)

START gen=settle_struct3_06_ADAUSDT_1h_direction_20260803 ADAUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:17:40 UTC (tier 0)

PREDICTABILITY real=+0.12392 p=0.0476 surr_q95=-0.00184 surr_max=-0.00127 draws=20 passed=True

## [INFO] 2026-08-03 18:17:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:17:42 UTC (tier 0)

trial `fa9a3cc1-2116-48c6-afd5-f03febe7d92e` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:17:48 UTC (tier 0)

trial `b417d058-9041-4f0d-8144-dd7b93adcb86` model=ridge tier=0 target=direction pf=0.831 n=4363 gates=FAIL

## [ALERT] 2026-08-03 18:17:58 UTC (tier 3)

trial `1ab945bc-5baf-4eed-a7e0-d0c8fbf39957` model=lgbm_regressor tier=3 target=direction pf=1.915 n=8332 gates=PASS

## [ALERT] 2026-08-03 18:18:16 UTC (tier 3)

trial `c5369ab6-7f2c-44d5-8e8a-a69b0f3a8810` model=lgbm_classifier tier=3 target=direction pf=1.547 n=9734 gates=PASS

## [INFO] 2026-08-03 18:18:16 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_06_ADAUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:18:16 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_07_DOGEUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:18:16 UTC (tier 0)

START gen=settle_struct3_07_DOGEUSDT_1h_direction_20260803 DOGEUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:18:33 UTC (tier 0)

PREDICTABILITY real=+0.12007 p=0.0476 surr_q95=-0.00045 surr_max=+0.00090 draws=20 passed=True

## [INFO] 2026-08-03 18:18:35 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:18:35 UTC (tier 0)

trial `0aedcd72-9c51-4fea-8921-ba4ef8563b2c` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:18:45 UTC (tier 0)

trial `f122a365-d9fa-468b-8d93-e2ad78528fbb` model=ridge tier=0 target=direction pf=0.767 n=5066 gates=FAIL

## [ALERT] 2026-08-03 18:18:57 UTC (tier 3)

trial `7f71057b-4a57-4b2a-b83f-b42435312928` model=lgbm_regressor tier=3 target=direction pf=1.606 n=9432 gates=PASS

## [ALERT] 2026-08-03 18:19:14 UTC (tier 3)

trial `4fc034b1-835c-45b5-a46e-268203682254` model=lgbm_classifier tier=3 target=direction pf=1.357 n=11246 gates=PASS

## [INFO] 2026-08-03 18:19:14 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_07_DOGEUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:19:14 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_08_AVAXUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:19:14 UTC (tier 0)

START gen=settle_struct3_08_AVAXUSDT_1h_direction_20260803 AVAXUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:19:28 UTC (tier 0)

PREDICTABILITY real=+0.10390 p=0.0476 surr_q95=-0.00009 surr_max=+0.00039 draws=20 passed=True

## [INFO] 2026-08-03 18:19:30 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:19:30 UTC (tier 0)

trial `bb25aa56-833a-4a4f-894b-70c04d876cdb` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:19:36 UTC (tier 0)

trial `01a3d8f7-9fa1-4d0e-a2dd-8352c8550793` model=ridge tier=0 target=direction pf=0.765 n=4383 gates=FAIL

## [ALERT] 2026-08-03 18:19:48 UTC (tier 3)

trial `b1c2192b-aa63-4c92-9293-2713f42065ce` model=lgbm_regressor tier=3 target=direction pf=1.799 n=10249 gates=PASS

## [ALERT] 2026-08-03 18:20:05 UTC (tier 3)

trial `1ddddd62-0ae0-4c35-bf85-ccd1e77dc0cf` model=lgbm_classifier tier=3 target=direction pf=1.455 n=12245 gates=PASS

## [INFO] 2026-08-03 18:20:05 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_08_AVAXUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:20:05 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_09_LINKUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:20:05 UTC (tier 0)

START gen=settle_struct3_09_LINKUSDT_1h_direction_20260803 LINKUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:20:22 UTC (tier 0)

PREDICTABILITY real=+0.11884 p=0.0476 surr_q95=-0.00156 surr_max=-0.00127 draws=20 passed=True

## [INFO] 2026-08-03 18:20:26 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:20:26 UTC (tier 0)

trial `5b94da92-6a47-4cfe-a462-ff6ac43864d2` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:20:32 UTC (tier 0)

trial `ba5e5471-175f-41c8-8769-3abf27816b86` model=ridge tier=0 target=direction pf=0.818 n=4173 gates=FAIL

## [ALERT] 2026-08-03 18:20:43 UTC (tier 3)

trial `755e3d13-c985-401e-9c81-dc49c113e269` model=lgbm_regressor tier=3 target=direction pf=1.953 n=9317 gates=PASS

## [ALERT] 2026-08-03 18:21:05 UTC (tier 3)

trial `33724f4d-1fd0-4441-a78e-701ce2d5a941` model=lgbm_classifier tier=3 target=direction pf=1.555 n=11376 gates=PASS

## [INFO] 2026-08-03 18:21:05 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_09_LINKUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:21:05 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_10_DOTUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:21:05 UTC (tier 0)

START gen=settle_struct3_10_DOTUSDT_1h_direction_20260803 DOTUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:21:23 UTC (tier 0)

PREDICTABILITY real=+0.12322 p=0.0476 surr_q95=-0.00204 surr_max=-0.00102 draws=20 passed=True

## [INFO] 2026-08-03 18:21:27 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:21:27 UTC (tier 0)

trial `e8bd2753-b5df-4fc3-bc3d-5d0004c0afbb` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:21:36 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00278 skill_surrogate=+0.00256

## [INFO] 2026-08-03 18:21:36 UTC (tier 0)

trial `0927163b-7d5c-4e3a-b72b-97cda6c22e3b` model=ridge tier=0 target=direction pf=0.769 n=3902 gates=FAIL

## [ALERT] 2026-08-03 18:21:51 UTC (tier 3)

trial `8a9433a6-540a-4679-878b-3dcd2c95c72d` model=lgbm_regressor tier=3 target=direction pf=1.840 n=7777 gates=PASS

## [ALERT] 2026-08-03 18:22:12 UTC (tier 3)

trial `157acd14-a445-4e93-ae98-960a1761e6a3` model=lgbm_classifier tier=3 target=direction pf=1.469 n=9091 gates=PASS

## [INFO] 2026-08-03 18:22:12 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_10_DOTUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:22:12 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_11_TRXUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:22:12 UTC (tier 0)

START gen=settle_struct3_11_TRXUSDT_1h_direction_20260803 TRXUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:22:38 UTC (tier 0)

PREDICTABILITY real=+0.11841 p=0.0476 surr_q95=-0.00085 surr_max=-0.00059 draws=20 passed=True

## [INFO] 2026-08-03 18:22:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:22:42 UTC (tier 0)

trial `b89b7737-3355-4711-a465-c7bfd4b703e3` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:22:51 UTC (tier 0)

trial `4bb18300-eba3-4649-9b5d-42a59702cc52` model=ridge tier=0 target=direction pf=0.861 n=2206 gates=FAIL

## [ALERT] 2026-08-03 18:23:12 UTC (tier 3)

trial `c1b2539d-6d15-4c86-b1e6-4aa694f577ed` model=lgbm_regressor tier=3 target=direction pf=1.538 n=3326 gates=PASS

## [ALERT] 2026-08-03 18:23:34 UTC (tier 3)

trial `119471ce-e643-44c4-b222-2481fa1348ea` model=lgbm_classifier tier=3 target=direction pf=1.348 n=3750 gates=PASS

## [INFO] 2026-08-03 18:23:34 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_11_TRXUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-03 18:23:34 UTC (tier 0)

STRUCTURE_EXPANSION_SETTLE start settle_struct3_12_XLMUSDT_1h_direction_20260803

## [INFO] 2026-08-03 18:23:34 UTC (tier 0)

START gen=settle_struct3_12_XLMUSDT_1h_direction_20260803 XLMUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-03 18:23:53 UTC (tier 0)

PREDICTABILITY real=+0.11188 p=0.0476 surr_q95=-0.00095 surr_max=-0.00052 draws=20 passed=True

## [INFO] 2026-08-03 18:23:56 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-03 18:23:56 UTC (tier 0)

trial `ee53d34c-3d26-4654-a75b-f5c92fd70915` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-03 18:24:05 UTC (tier 0)

trial `259cd271-5e90-4aff-8a03-d04e1d5858c5` model=ridge tier=0 target=direction pf=0.829 n=3816 gates=FAIL

## [ALERT] 2026-08-03 18:24:20 UTC (tier 3)

trial `d9f4314e-b560-4b8a-ad1f-d9d2d9928cb7` model=lgbm_regressor tier=3 target=direction pf=1.691 n=7351 gates=PASS

## [ALERT] 2026-08-03 18:24:39 UTC (tier 3)

trial `9c701598-6847-49af-b992-8ce52158b802` model=lgbm_classifier tier=3 target=direction pf=1.434 n=8755 gates=PASS

## [INFO] 2026-08-03 18:24:39 UTC (tier 0)

Hunt complete: {"generation_id": "settle_struct3_12_XLMUSDT_1h_direction_20260803", "status": "COMPLETE", "n_trials": 4, "best_tier": 3, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [ALERT] 2026-08-03 18:24:39 UTC (tier 2)

STRUCTURE_EXPANSION_SETTLE done best_pass=True path=D:\projects\LLM2\artifacts\reports\structure_v1_expansion_settle_20260803T181235Z.json

## [INFO] 2026-08-04 14:43:34 UTC (tier 0)

STRUCTURE_LEAKAGE_RECHECK overall_ok=True pass=26/26 path=structure_v1_leakage_recheck_20260804T144240Z.json

## [INFO] 2026-08-04 16:26:00 UTC (tier 1)

PACK_LIVE version_id=btc_k5_double3h_v1 deployed=True service=llm2-structure-btc-k5-double3h-v1 account=Xxobster10

## [INFO] 2026-08-04 16:26:00 UTC (tier 1)

PACK_LIVE version_id=eth_k5_double3h_v1 deployed=True service=llm2-structure-eth-k5-double3h-v1 account=Xxobster6

## [INFO] 2026-08-04 16:26:00 UTC (tier 1)

PACK_LIVE version_id=eth_multitrade_v1_2 deployed=True service=llm2-structure-eth-multitrade-v1_2 account=Xxobster8

## [INFO] 2026-08-04 16:26:00 UTC (tier 1)

PACK_LIVE version_id=sol_k5_double3h_v1 deployed=True service=llm2-structure-sol-k5-double3h-v1 account=Xxobster10

## [INFO] 2026-08-04 16:26:00 UTC (tier 0)

PACK_REGISTRY_BACKFILL n=22 versions=['adausdt_direction', 'avaxusdt_direction', 'bnbusdt_direction', 'btcusdt_clarity_hold12_v1', 'btc_k5_double3h_v1', 'dogeusdt_direction', 'dotusdt_direction', 'ethusdt_clarity_hold12_v1', 'ethusdt_direction', 'eth_k5_double3h_v1', 'eth_multitrade_v1', 'eth_multitrade_v1_1', 'eth_multitrade_v1_2', 'lgbm', 'linkusdt_direction', 'solusdt_clarity_hold12_v1', 'solusdt_direction', 'sol_k5_double3h_v1', 'trxusdt_direction', 'vetusdt_direction', 'xlmusdt_direction', 'xrpusdt_direction']

## [INFO] 2026-08-04 16:26:20 UTC (tier 1)

PACK_LIVE version_id=eth_k5_double3h_v1 deployed=True service=llm2-structure-eth-k5-double3h-v1 account=Xxobster6

## [INFO] 2026-08-04 16:26:20 UTC (tier 1)

PACK_LIVE version_id=eth_multitrade_v1_2 deployed=True service=llm2-structure-eth-multitrade-v1_2 account=Xxobster8

## [INFO] 2026-08-04 16:26:20 UTC (tier 1)

PACK_LIVE version_id=btc_k5_double3h_v1 deployed=True service=llm2-structure-btc-k5-double3h-v1 account=Xxobster10

## [INFO] 2026-08-04 16:26:20 UTC (tier 1)

PACK_LIVE version_id=sol_k5_double3h_v1 deployed=True service=llm2-structure-sol-k5-double3h-v1 account=Xxobster10

## [INFO] 2026-08-04 16:26:59 UTC (tier 1)

PACK_LIVE version_id=btc_k5_double3h_v1 deployed=True service=llm2-structure-btc-k5-double3h-v1 account=Xxobster10

## [INFO] 2026-08-04 16:26:59 UTC (tier 1)

PACK_LIVE version_id=eth_k5_double3h_v1 deployed=True service=llm2-structure-eth-k5-double3h-v1 account=Xxobster6

## [INFO] 2026-08-04 16:26:59 UTC (tier 1)

PACK_LIVE version_id=eth_multitrade_v1_2 deployed=True service=llm2-structure-eth-multitrade-v1_2 account=Xxobster8

## [INFO] 2026-08-04 16:26:59 UTC (tier 1)

PACK_LIVE version_id=sol_k5_double3h_v1 deployed=True service=llm2-structure-sol-k5-double3h-v1 account=Xxobster10

## [INFO] 2026-08-04 16:26:59 UTC (tier 0)

PACK_REGISTRY_BACKFILL n=22 versions=['adausdt_direction', 'avaxusdt_direction', 'bnbusdt_direction', 'btcusdt_clarity_hold12_v1', 'btc_k5_double3h_v1', 'dogeusdt_direction', 'dotusdt_direction', 'ethusdt_clarity_hold12_v1', 'ethusdt_direction', 'eth_k5_double3h_v1', 'eth_multitrade_v1', 'eth_multitrade_v1_1', 'eth_multitrade_v1_2', 'lgbm', 'linkusdt_direction', 'solusdt_clarity_hold12_v1', 'solusdt_direction', 'sol_k5_double3h_v1', 'trxusdt_direction', 'vetusdt_direction', 'xlmusdt_direction', 'xrpusdt_direction']

## [INFO] 2026-08-04 16:28:28 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_k5_expectancy_strength_p75_001 control_exp_ru=0.005206316921173494 cand_exp_ru=0.0064316547337478335 control_pf=4.114418041595842 cand_pf=7.044474928687612 path=artifacts/reports/structure_v1_eth_k5_expectancy_strength_p75_001_latest.json

## [INFO] 2026-08-05 05:50:21 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_multitrade_loss_streak_cooloff_001 control_exp_ru=0.008020978933362125 cand_exp_ru=0.007974530894855244 control_pf=4.255642815858733 cand_pf=4.309749181761305 path=artifacts/reports/structure_v1_eth_multitrade_loss_streak_cooloff_001_latest.json

## [INFO] 2026-08-05 06:54:13 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_k5_ev_calibrated_pi_star_001 control_exp_ru=0.005198623714457994 cand_exp_ru=0.005198623714457994 control_pf=4.1206087557058195 cand_pf=4.1206087557058195 path=artifacts/reports/structure_v1_eth_k5_ev_calibrated_pi_star_001_latest.json

## [INFO] 2026-08-05 06:57:36 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_k5_ev_calibrated_pi_star_001 control_exp_ru=0.005206316921173494 cand_exp_ru=0.005203171582749607 control_pf=4.114418041595842 cand_pf=4.071947094142618 path=artifacts/reports/structure_v1_eth_k5_ev_calibrated_pi_star_001_latest.json

## [INFO] 2026-08-05 08:02:10 UTC (tier 0)

PACK_FREEZE version_id=eth_k5_double3h_p75_v1 pack_hash=b54e7846bdfc3a8e7de86d4f86bc5dfda4838dca4374674e5cb7d4e054504a3c run_ids=['structure_v1_eth_k5_expectancy_strength_p75_001_candidate-f0-0a209f4b9b', 'structure_v1_eth_k5_expectancy_strength_p75_001_candidate-f1-e3ae5bfcd5', 'structure_v1_eth_k5_expectancy_strength_p75_001_candidate-f2-7c6a732672', 'structure_v1_eth_k5_expectancy_strength_p75_001_candidate-f3-7c2ad77565', 'structure_v1_eth_k5_expectancy_strength_p75_001_candidate-f4-350ffeac18', 'structure_v1_eth_k5_expectancy_strength_p75_001_candidate-f5-bc45ca42d8'] path=artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1

## [INFO] 2026-08-05 08:05:24 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_multitrade_strength_p75_001 control_exp_ru=0.008020978933362125 cand_exp_ru=0.00951747831620085 control_pf=4.255642815858733 cand_pf=6.9621444934318975 path=artifacts/reports/structure_v1_eth_multitrade_strength_p75_001_latest.json

## [INFO] 2026-08-05 08:07:06 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_multitrade_skip_weak_short_book1_001 control_exp_ru=0.008020978933362125 cand_exp_ru=0.008260004183604055 control_pf=4.255642815858733 cand_pf=4.432029580486041 path=artifacts/reports/structure_v1_eth_multitrade_skip_weak_short_book1_001_latest.json

## [INFO] 2026-08-05 08:20:43 UTC (tier 0)

PACK_FREEZE version_id=eth_k5_double3h_p75_v1 pack_hash=a291ed3ccb813def63dfc341c9c5e668cb6ddbcccc9d478d9e4178352fb696c7 run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1

## [INFO] 2026-08-05 08:20:43 UTC (tier 1)

PACK_LIVE version_id=eth_k5_double3h_p75_v1 deployed=True service=llm2-structure-eth-k5-double3h-p75-v1 account=Xxobster3

## [INFO] 2026-08-05 08:23:10 UTC (tier 0)

PACK_FREEZE version_id=eth_k5_double3h_p75_v1 pack_hash=3cbe9f34f2bd0a94d583d9ee23436a2d4e66dbf6ce864ad2c2edb49ebb8ba1d3 run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1

## [INFO] 2026-08-05 08:23:10 UTC (tier 1)

PACK_LIVE version_id=eth_k5_double3h_p75_v1 deployed=True service=llm2-structure-eth-k5-double3h-p75-v1 account=Xxobster3

## [INFO] 2026-08-05 08:32:14 UTC (tier 0)

PACK_FREEZE version_id=eth_k5_double3h_p75_v1 pack_hash=3cbe9f34f2bd0a94d583d9ee23436a2d4e66dbf6ce864ad2c2edb49ebb8ba1d3 run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1

## [INFO] 2026-08-05 08:35:33 UTC (tier 0)

PACK_FREEZE version_id=eth_k5_double3h_p75_v1 pack_hash=3dc73d4e9c20d980c4d37c0636e3738ecc00cd4409bfb98b9b7697cff6b108b7 run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1

## [INFO] 2026-08-05 08:35:33 UTC (tier 1)

PACK_LIVE version_id=eth_k5_double3h_p75_v1 deployed=True service=llm2-structure-eth-k5-double3h-p75-v1 account=Xxobster3

## [INFO] 2026-08-05 08:38:52 UTC (tier 0)

PACK_FREEZE version_id=eth_k5_double3h_p75_v1 pack_hash=b36912b6358a921d6e115bdcd7e439bba09b654822cd2def63ec5fd2cd40f2ca run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_k5_double3h_p75_v1

## [INFO] 2026-08-05 08:38:52 UTC (tier 1)

PACK_LIVE version_id=eth_k5_double3h_p75_v1 deployed=True service=llm2-structure-eth-k5-double3h-p75-v1 account=Xxobster3

## [INFO] 2026-08-05 08:46:28 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_k5_p75_tp_scale_absmean_001 control_exp_ru=0.0064316547337478335 cand_exp_ru=0.0070315418923162 control_pf=7.044474928687612 cand_pf=7.450904301658215 path=artifacts/reports/structure_v1_eth_k5_p75_tp_scale_absmean_001_latest.json

## [INFO] 2026-08-05 09:15:10 UTC (tier 0)

PACK_FREEZE version_id=eth_multitrade_p75_v1 pack_hash=d86d5407d181d19c4fc379eaff4db9112e52cfe4c910933f1902036f7504d170 run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_multitrade_p75_v1

## [INFO] 2026-08-05 09:15:10 UTC (tier 1)

PACK_LIVE version_id=eth_multitrade_p75_v1 deployed=True service=llm2-structure-eth-multitrade-p75-v1 account=Xxobster9

## [INFO] 2026-08-05 13:47:26 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_15m_multitrade_geometry_001 control_exp_ru=0.00809385597623016 cand_exp_ru=0.010396663555539894 control_pf=3.72589641601175 cand_pf=6.485352060119762 path=artifacts/reports/structure_v1_eth_15m_multitrade_geometry_001_latest.json

## [INFO] 2026-08-05 13:56:01 UTC (tier 0)

PACK_FREEZE version_id=eth_15m_multitrade_wall_clock_p75_v1 pack_hash=03beafc58556db9adc4937d00eb43829cb5fb04d4284eaab1dbe66dd6de795fc run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1

## [INFO] 2026-08-05 13:59:27 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_15m_wall_clock_p75_tp_scale_absmean_001 control_exp_ru=0.010396663555539894 cand_exp_ru=0.010776107777752992 control_pf=6.485352060119762 cand_pf=6.643387213344491 path=artifacts/reports/structure_v1_eth_15m_wall_clock_p75_tp_scale_absmean_001_latest.json

## [INFO] 2026-08-05 14:03:15 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_btc_15m_multitrade_geometry_001 control_exp_ru=0.005566861248867574 cand_exp_ru=0.00796047183425502 control_pf=2.986898816168234 cand_pf=5.280938428297618 path=artifacts/reports/structure_v1_btc_15m_multitrade_geometry_001_latest.json

## [INFO] 2026-08-05 14:10:36 UTC (tier 0)

PACK_FREEZE version_id=eth_15m_multitrade_wall_clock_p75_v1 pack_hash=66cf1c4d9de61ce1d54848c5cc9222f67324cc45568b73925919c35e7d0b6db8 run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1

## [INFO] 2026-08-05 14:10:36 UTC (tier 1)

PACK_LIVE version_id=eth_15m_multitrade_wall_clock_p75_v1 deployed=True service=llm2-structure-eth-15m-multitrade-wall-clock-p75-v1 account=Xxobster11

## [INFO] 2026-08-05 14:10:43 UTC (tier 0)

PACK_FREEZE version_id=eth_15m_multitrade_wall_clock_p75_v1 pack_hash=fb6f91112b6530e6a8f96bc54a55ad2b3725ff8becdd41837431b55380605a13 run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1

## [INFO] 2026-08-05 14:10:43 UTC (tier 1)

PACK_LIVE version_id=eth_15m_multitrade_wall_clock_p75_v1 deployed=True service=llm2-structure-eth-15m-multitrade-wall-clock-p75-v1 account=Xxobster11

## [INFO] 2026-08-05 14:11:27 UTC (tier 0)

PACK_FREEZE version_id=eth_15m_multitrade_wall_clock_p75_v1 pack_hash=fa0e121cef5a10036d4a423528ddf0fb163536ea24e3a1630d6bd4542fe183a7 run_ids=[] path=artifacts/live_packs/structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1

## [INFO] 2026-08-05 14:11:27 UTC (tier 1)

PACK_LIVE version_id=eth_15m_multitrade_wall_clock_p75_v1 deployed=True service=llm2-structure-eth-15m-multitrade-wall-clock-p75-v1 account=Xxobster11

## [INFO] 2026-08-06 08:55:54 UTC (tier 0)

CAUS_RETRAIN_001 start stamp=20260806T085554Z prereg_sha=93d76d2e5d9f31a2 fold=v2 lockbox=2026-05-01

## [INFO] 2026-08-06 08:56:39 UTC (tier 0)

CAUS_RETRAIN_001 hunt start caus_retrain_001_00_BTCUSDT_1h_fwd_return_20260806

## [INFO] 2026-08-06 08:56:39 UTC (tier 0)

START gen=caus_retrain_001_00_BTCUSDT_1h_fwd_return_20260806 BTCUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-06 08:57:13 UTC (tier 0)

PREDICTABILITY real=-0.01602 p=1.0000 surr_q95=-0.00072 surr_max=-0.00049 draws=20 passed=False

## [INFO] 2026-08-06 08:57:39 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-06 08:57:39 UTC (tier 0)

trial `38ae0c6d-f0ab-425a-be02-1816e5779915` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-06 08:58:02 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00813 skill_surrogate=-0.00076

## [INFO] 2026-08-06 08:58:02 UTC (tier 0)

trial `b54c3a92-3848-4c0d-98ad-3a2f673804b3` model=ridge tier=0 target=fwd_return pf=0.809 n=2274 gates=FAIL

## [INFO] 2026-08-06 08:58:24 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01600 skill_surrogate=-0.00323

## [INFO] 2026-08-06 08:58:24 UTC (tier 0)

trial `1a8af35c-bf05-46d7-bea8-1f713c60c67e` model=lgbm_regressor tier=0 target=fwd_return pf=0.798 n=2235 gates=FAIL

## [INFO] 2026-08-06 08:59:08 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-113.28300 skill_surrogate=-3.81511

## [INFO] 2026-08-06 08:59:08 UTC (tier 0)

trial `df2d4007-1087-43aa-8f24-36cca0b044f3` model=lgbm_classifier tier=0 target=fwd_return pf=0.747 n=4328 gates=FAIL

## [INFO] 2026-08-06 08:59:08 UTC (tier 0)

Hunt complete: {"generation_id": "caus_retrain_001_00_BTCUSDT_1h_fwd_return_20260806", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-06 08:59:08 UTC (tier 0)

CAUS_RETRAIN_001 hunt start caus_retrain_001_01_ETHUSDT_1h_direction_20260806

## [INFO] 2026-08-06 08:59:08 UTC (tier 0)

START gen=caus_retrain_001_01_ETHUSDT_1h_direction_20260806 ETHUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-06 08:59:41 UTC (tier 0)

PREDICTABILITY real=-0.00456 p=0.9048 surr_q95=+0.00046 surr_max=+0.00170 draws=20 passed=False

## [INFO] 2026-08-06 09:00:04 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-06 09:00:04 UTC (tier 0)

trial `5edec790-7332-45ee-981f-ab7b89289838` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-06 09:00:19 UTC (tier 0)

trial `1c133c75-b392-40ae-9d38-78f090f1b661` model=ridge tier=0 target=direction pf=0.762 n=2875 gates=FAIL

## [INFO] 2026-08-06 09:00:42 UTC (tier 0)

trial `4e432304-6a83-4fbf-aaf6-a5bc46e9caa9` model=lgbm_regressor tier=0 target=direction pf=0.757 n=4763 gates=FAIL

## [INFO] 2026-08-06 09:01:14 UTC (tier 0)

trial `67c9d279-4e6d-400f-9689-d036061877ee` model=lgbm_classifier tier=0 target=direction pf=0.783 n=6926 gates=FAIL

## [INFO] 2026-08-06 09:01:14 UTC (tier 0)

Hunt complete: {"generation_id": "caus_retrain_001_01_ETHUSDT_1h_direction_20260806", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-06 09:01:14 UTC (tier 0)

CAUS_RETRAIN_001 hunt start caus_retrain_001_02_SOLUSDT_1h_direction_20260806

## [INFO] 2026-08-06 09:01:14 UTC (tier 0)

START gen=caus_retrain_001_02_SOLUSDT_1h_direction_20260806 SOLUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-06 09:01:42 UTC (tier 0)

PREDICTABILITY real=-0.00043 p=0.0952 surr_q95=-0.00062 surr_max=+0.00018 draws=20 passed=False

## [INFO] 2026-08-06 09:01:54 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-06 09:01:54 UTC (tier 0)

trial `f2a47c38-2ee8-4a74-9fdc-c22d1dd0bf73` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-06 09:02:08 UTC (tier 0)

trial `1086efee-aa65-4ea1-a459-90233f929d77` model=ridge tier=0 target=direction pf=0.799 n=5457 gates=FAIL

## [INFO] 2026-08-06 09:02:26 UTC (tier 0)

trial `06fa0672-4de7-4211-94fd-c8d04253a34b` model=lgbm_regressor tier=0 target=direction pf=0.792 n=7140 gates=FAIL

## [INFO] 2026-08-06 09:02:56 UTC (tier 0)

trial `5cb44ea6-e73e-4171-a5d0-c934abaf6816` model=lgbm_classifier tier=0 target=direction pf=0.805 n=11839 gates=FAIL

## [INFO] 2026-08-06 09:02:56 UTC (tier 0)

Hunt complete: {"generation_id": "caus_retrain_001_02_SOLUSDT_1h_direction_20260806", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-06 09:02:56 UTC (tier 0)

CAUS_RETRAIN_001 hunt start caus_retrain_001_03_ETHUSDT_1h_fwd_return_20260806

## [INFO] 2026-08-06 09:02:56 UTC (tier 0)

START gen=caus_retrain_001_03_ETHUSDT_1h_fwd_return_20260806 ETHUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-06 09:03:19 UTC (tier 0)

PREDICTABILITY real=-0.00894 p=0.8571 surr_q95=+0.00101 surr_max=+0.00234 draws=20 passed=False

## [INFO] 2026-08-06 09:03:28 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-06 09:03:28 UTC (tier 0)

trial `e8bdec56-2790-4c1f-b8fa-a5b59279fee8` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-06 09:03:45 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00375 skill_surrogate=-0.00096

## [INFO] 2026-08-06 09:03:45 UTC (tier 0)

trial `ddea96a0-7a36-4c65-8c3b-15e3e8eabbdc` model=ridge tier=0 target=fwd_return pf=0.851 n=4158 gates=FAIL

## [INFO] 2026-08-06 09:04:03 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01195 skill_surrogate=-0.00454

## [INFO] 2026-08-06 09:04:03 UTC (tier 0)

trial `75d9cde0-586f-4084-9e6f-8f440cd806aa` model=lgbm_regressor tier=0 target=fwd_return pf=0.827 n=4063 gates=FAIL

## [INFO] 2026-08-06 09:04:34 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-80.36274 skill_surrogate=-2.76346

## [INFO] 2026-08-06 09:04:34 UTC (tier 0)

trial `97a4b510-3da4-405d-a616-0dc6c7297621` model=lgbm_classifier tier=0 target=fwd_return pf=0.783 n=6926 gates=FAIL

## [INFO] 2026-08-06 09:04:34 UTC (tier 0)

Hunt complete: {"generation_id": "caus_retrain_001_03_ETHUSDT_1h_fwd_return_20260806", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-06 09:04:34 UTC (tier 0)

CAUS_RETRAIN_001 hunt start caus_retrain_001_04_SOLUSDT_1h_fwd_return_20260806

## [INFO] 2026-08-06 09:04:34 UTC (tier 0)

START gen=caus_retrain_001_04_SOLUSDT_1h_fwd_return_20260806 SOLUSDT 1h target=fwd_return space=structure_v1

## [INFO] 2026-08-06 09:04:54 UTC (tier 0)

PREDICTABILITY real=-0.01147 p=1.0000 surr_q95=-0.00036 surr_max=+0.00021 draws=20 passed=False

## [INFO] 2026-08-06 09:05:07 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-06 09:05:07 UTC (tier 0)

trial `b0546f0d-2d48-49a6-9306-bcd22e397b6a` model=hist_mean tier=0 target=fwd_return pf=0.751 n=2800 gates=FAIL

## [INFO] 2026-08-06 09:05:27 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00018 skill_surrogate=-0.00450

## [INFO] 2026-08-06 09:05:27 UTC (tier 0)

trial `0e133efd-c58c-4548-8729-e9da35ef66df` model=ridge tier=0 target=fwd_return pf=0.802 n=9178 gates=FAIL

## [INFO] 2026-08-06 09:05:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.01076 skill_surrogate=-0.00417

## [INFO] 2026-08-06 09:05:45 UTC (tier 0)

trial `3fbb291e-3530-40ce-9b85-a8e5860bf15c` model=lgbm_regressor tier=0 target=fwd_return pf=0.759 n=7766 gates=FAIL

## [INFO] 2026-08-06 09:06:16 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-70.68581 skill_surrogate=-2.09549

## [INFO] 2026-08-06 09:06:16 UTC (tier 0)

trial `1355c456-07e4-4d9d-8f29-5beb36bdc865` model=lgbm_classifier tier=0 target=fwd_return pf=0.805 n=11839 gates=FAIL

## [INFO] 2026-08-06 09:06:16 UTC (tier 0)

Hunt complete: {"generation_id": "caus_retrain_001_04_SOLUSDT_1h_fwd_return_20260806", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-06 09:06:17 UTC (tier 0)

CAUS_RETRAIN_001 hunt start caus_retrain_001_05_BTCUSDT_1h_direction_20260806

## [INFO] 2026-08-06 09:06:17 UTC (tier 0)

START gen=caus_retrain_001_05_BTCUSDT_1h_direction_20260806 BTCUSDT 1h target=direction space=structure_v1

## [INFO] 2026-08-06 09:06:46 UTC (tier 0)

PREDICTABILITY real=+0.00093 p=0.0476 surr_q95=-0.00040 surr_max=-0.00020 draws=20 passed=True

## [INFO] 2026-08-06 09:06:56 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-06 09:06:56 UTC (tier 0)

trial `8204b563-a363-4f39-b50e-a40b89155aa3` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-06 09:07:09 UTC (tier 0)

trial `15d11fda-1d3d-47ff-8ac2-9f4d36350582` model=ridge tier=0 target=direction pf=0.736 n=1934 gates=FAIL

## [INFO] 2026-08-06 09:07:34 UTC (tier 0)

trial `2f0853c5-106e-4195-8169-52d5ace8ae60` model=lgbm_regressor tier=0 target=direction pf=0.717 n=3196 gates=FAIL

## [INFO] 2026-08-06 09:08:10 UTC (tier 0)

trial `326f3c8b-5fda-4aa9-98a8-32001496780c` model=lgbm_classifier tier=0 target=direction pf=0.747 n=4328 gates=FAIL

## [INFO] 2026-08-06 09:08:10 UTC (tier 0)

Hunt complete: {"generation_id": "caus_retrain_001_05_BTCUSDT_1h_direction_20260806", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-06 17:23:44 UTC (tier 0)

NEXT_RETRACE_FORECAST_001 start sha=36bf1127d2382c81 fold=v2

## [INFO] 2026-08-06 17:26:26 UTC (tier 0)

NEXT_RETRACE_FORECAST_001 start sha=e237dae8ef4d8fcb fold=v2

## [INFO] 2026-08-06 17:28:07 UTC (tier 0)

NEXT_RETRACE_FORECAST_001 start sha=6f4cf86e59757201 fold=v2

## [INFO] 2026-08-06 21:37:41 UTC (tier 0)

FORECAST_FILTER_ON_DIRECTION_001 start sha=d962852a62603ba6 fold=v2

## [INFO] 2026-08-08 04:44:30 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 start stamp=20260808T044430Z prereg_sha=876c2028740b8253 space=structure_v1_no_retrace fold=v2 lockbox=2026-05-01

## [INFO] 2026-08-08 04:47:14 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 hunt start causal_drop_retrace_001_00_BTCUSDT_1h_fwd_return_20260808

## [INFO] 2026-08-08 04:47:14 UTC (tier 0)

START gen=causal_drop_retrace_001_00_BTCUSDT_1h_fwd_return_20260808 BTCUSDT 1h target=fwd_return space=structure_v1_no_retrace

## [INFO] 2026-08-08 04:53:08 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 start stamp=20260808T045308Z prereg_sha=3d45e08a503f70fc space=structure_v1_no_retrace fold=v2 lockbox=2026-05-01

## [INFO] 2026-08-08 04:55:38 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 hunt start causal_drop_retrace_001_00_BTCUSDT_1h_fwd_return_20260808

## [INFO] 2026-08-08 04:55:38 UTC (tier 0)

START gen=causal_drop_retrace_001_00_BTCUSDT_1h_fwd_return_20260808 BTCUSDT 1h target=fwd_return space=structure_v1_no_retrace

## [INFO] 2026-08-08 04:58:57 UTC (tier 0)

PREDICTABILITY real=-0.01429 p=0.9524 surr_q95=-0.00057 surr_max=-0.00042 draws=20 passed=False

## [INFO] 2026-08-08 05:00:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 05:00:08 UTC (tier 0)

trial `26c4bb43-02ec-48b6-ac46-7d497c3d56f5` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-08 05:01:15 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00538 skill_surrogate=-0.00184

## [INFO] 2026-08-08 05:01:15 UTC (tier 0)

trial `f6873408-f52d-47ae-a9e1-c647e41f40b0` model=ridge tier=0 target=fwd_return pf=0.805 n=2150 gates=FAIL

## [INFO] 2026-08-08 05:02:32 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.02163 skill_surrogate=-0.00578

## [INFO] 2026-08-08 05:02:32 UTC (tier 0)

trial `23628c84-c40b-44b3-871e-d976a8f554ab` model=lgbm_regressor tier=0 target=fwd_return pf=0.812 n=2201 gates=FAIL

## [INFO] 2026-08-08 05:05:12 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-113.71569 skill_surrogate=-4.05940

## [INFO] 2026-08-08 05:05:12 UTC (tier 0)

trial `4c39307a-3afa-4183-ac77-242a7292c53b` model=lgbm_classifier tier=0 target=fwd_return pf=0.787 n=4321 gates=FAIL

## [INFO] 2026-08-08 05:05:12 UTC (tier 0)

Hunt complete: {"generation_id": "causal_drop_retrace_001_00_BTCUSDT_1h_fwd_return_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 05:05:12 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 hunt start causal_drop_retrace_001_01_ETHUSDT_1h_direction_20260808

## [INFO] 2026-08-08 05:05:12 UTC (tier 0)

START gen=causal_drop_retrace_001_01_ETHUSDT_1h_direction_20260808 ETHUSDT 1h target=direction space=structure_v1_no_retrace

## [INFO] 2026-08-08 05:08:27 UTC (tier 0)

PREDICTABILITY real=-0.00481 p=0.9048 surr_q95=+0.00022 surr_max=+0.00181 draws=20 passed=False

## [INFO] 2026-08-08 05:09:42 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 05:09:42 UTC (tier 0)

trial `dcc5a8b0-2ea6-4760-ab01-e03662618e2d` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-08 05:10:30 UTC (tier 0)

trial `4a85e3d3-30a9-4d7d-a78c-a36e9bce2bbf` model=ridge tier=0 target=direction pf=0.771 n=2689 gates=FAIL

## [INFO] 2026-08-08 05:12:12 UTC (tier 0)

trial `e7cfed98-7f48-4ced-8409-b3c8065eb539` model=lgbm_regressor tier=0 target=direction pf=0.755 n=4587 gates=FAIL

## [INFO] 2026-08-08 05:14:56 UTC (tier 0)

trial `3620dfb1-ee93-4ff7-a8be-dfe6cbb1a67d` model=lgbm_classifier tier=0 target=direction pf=0.770 n=6958 gates=FAIL

## [INFO] 2026-08-08 05:14:56 UTC (tier 0)

Hunt complete: {"generation_id": "causal_drop_retrace_001_01_ETHUSDT_1h_direction_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 05:14:56 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 hunt start causal_drop_retrace_001_02_SOLUSDT_1h_direction_20260808

## [INFO] 2026-08-08 05:14:56 UTC (tier 0)

START gen=causal_drop_retrace_001_02_SOLUSDT_1h_direction_20260808 SOLUSDT 1h target=direction space=structure_v1_no_retrace

## [INFO] 2026-08-08 05:16:48 UTC (tier 0)

PREDICTABILITY real=-0.00022 p=0.1429 surr_q95=+0.00041 surr_max=+0.00072 draws=20 passed=False

## [INFO] 2026-08-08 05:17:03 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 05:17:03 UTC (tier 0)

trial `71fe28af-0f59-43c8-afc2-3d4592db3dc0` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-08 05:17:19 UTC (tier 0)

trial `8bdf7ac6-6712-455d-ab0b-276dc88eae7a` model=ridge tier=0 target=direction pf=0.811 n=5246 gates=FAIL

## [INFO] 2026-08-08 05:17:47 UTC (tier 0)

trial `9b3a6aa5-9ac7-42b4-b953-e3bbb755fa15` model=lgbm_regressor tier=0 target=direction pf=0.793 n=7132 gates=FAIL

## [INFO] 2026-08-08 05:18:36 UTC (tier 0)

trial `1f896d5d-8f91-4bf8-a0a9-f214d1ee9f44` model=lgbm_classifier tier=0 target=direction pf=0.806 n=11841 gates=FAIL

## [INFO] 2026-08-08 05:18:36 UTC (tier 0)

Hunt complete: {"generation_id": "causal_drop_retrace_001_02_SOLUSDT_1h_direction_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 05:18:36 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 hunt start causal_drop_retrace_001_03_ETHUSDT_1h_fwd_return_20260808

## [INFO] 2026-08-08 05:18:36 UTC (tier 0)

START gen=causal_drop_retrace_001_03_ETHUSDT_1h_fwd_return_20260808 ETHUSDT 1h target=fwd_return space=structure_v1_no_retrace

## [INFO] 2026-08-08 05:19:48 UTC (tier 0)

PREDICTABILITY real=-0.00348 p=0.7143 surr_q95=+0.00063 surr_max=+0.00296 draws=20 passed=False

## [INFO] 2026-08-08 05:20:01 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 05:20:01 UTC (tier 0)

trial `3f1b9d62-00ad-48f9-aaee-3e36a588e0ce` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-08 05:20:24 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00332 skill_surrogate=-0.00064

## [INFO] 2026-08-08 05:20:24 UTC (tier 0)

trial `c583a24f-e23d-462c-ad22-23a63f980a08` model=ridge tier=0 target=fwd_return pf=0.859 n=3995 gates=FAIL

## [INFO] 2026-08-08 05:20:50 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00756 skill_surrogate=-0.00349

## [INFO] 2026-08-08 05:20:50 UTC (tier 0)

trial `75d726b6-8d03-49a8-b839-fc5c330cded3` model=lgbm_regressor tier=0 target=fwd_return pf=0.837 n=3953 gates=FAIL

## [INFO] 2026-08-08 05:21:40 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-80.37481 skill_surrogate=-2.89887

## [INFO] 2026-08-08 05:21:40 UTC (tier 0)

trial `43b70c94-8fc9-47ed-8b7b-b9823ffc4f96` model=lgbm_classifier tier=0 target=fwd_return pf=0.770 n=6958 gates=FAIL

## [INFO] 2026-08-08 05:21:40 UTC (tier 0)

Hunt complete: {"generation_id": "causal_drop_retrace_001_03_ETHUSDT_1h_fwd_return_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 05:21:40 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 hunt start causal_drop_retrace_001_04_SOLUSDT_1h_fwd_return_20260808

## [INFO] 2026-08-08 05:21:40 UTC (tier 0)

START gen=causal_drop_retrace_001_04_SOLUSDT_1h_fwd_return_20260808 SOLUSDT 1h target=fwd_return space=structure_v1_no_retrace

## [INFO] 2026-08-08 05:22:38 UTC (tier 0)

PREDICTABILITY real=-0.00609 p=0.6667 surr_q95=-0.00091 surr_max=+0.00012 draws=20 passed=False

## [INFO] 2026-08-08 05:22:54 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 05:22:54 UTC (tier 0)

trial `00c02b09-c98a-4305-a41f-9cdad008fa0c` model=hist_mean tier=0 target=fwd_return pf=0.751 n=2800 gates=FAIL

## [INFO] 2026-08-08 05:23:20 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00033 skill_surrogate=+0.00236

## [INFO] 2026-08-08 05:23:20 UTC (tier 0)

trial `12c0ae74-859a-457e-aab8-323eefc013d9` model=ridge tier=0 target=fwd_return pf=0.810 n=9043 gates=FAIL

## [INFO] 2026-08-08 05:23:45 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00313 skill_surrogate=-0.00958

## [INFO] 2026-08-08 05:23:45 UTC (tier 0)

trial `17c386f1-2b04-4d98-9984-f621664918c6` model=lgbm_regressor tier=0 target=fwd_return pf=0.765 n=7308 gates=FAIL

## [INFO] 2026-08-08 05:24:33 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-70.66874 skill_surrogate=-1.69123

## [INFO] 2026-08-08 05:24:33 UTC (tier 0)

trial `3fce64d9-3b69-4aab-b525-c87794d55fdb` model=lgbm_classifier tier=0 target=fwd_return pf=0.806 n=11841 gates=FAIL

## [INFO] 2026-08-08 05:24:33 UTC (tier 0)

Hunt complete: {"generation_id": "causal_drop_retrace_001_04_SOLUSDT_1h_fwd_return_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 05:24:33 UTC (tier 0)

CAUSAL_DROP_RETRACE_001 hunt start causal_drop_retrace_001_05_BTCUSDT_1h_direction_20260808

## [INFO] 2026-08-08 05:24:33 UTC (tier 0)

START gen=causal_drop_retrace_001_05_BTCUSDT_1h_direction_20260808 BTCUSDT 1h target=direction space=structure_v1_no_retrace

## [INFO] 2026-08-08 05:25:34 UTC (tier 0)

PREDICTABILITY real=+0.00127 p=0.0476 surr_q95=-0.00019 surr_max=+0.00018 draws=20 passed=True

## [INFO] 2026-08-08 05:26:08 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 05:26:08 UTC (tier 0)

trial `18eb368f-fded-4fa1-b8d7-ecab62822f05` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-08 05:27:01 UTC (tier 0)

trial `d2af3681-a997-4573-9846-1c016f9d379f` model=ridge tier=0 target=direction pf=0.737 n=1803 gates=FAIL

## [INFO] 2026-08-08 05:28:47 UTC (tier 0)

trial `2bcbb581-d044-4504-83b2-9420ea32b851` model=lgbm_regressor tier=0 target=direction pf=0.756 n=3183 gates=FAIL

## [INFO] 2026-08-08 05:31:24 UTC (tier 0)

trial `bbdc3138-9f47-4f83-8745-4ecd1f2fef01` model=lgbm_classifier tier=0 target=direction pf=0.787 n=4321 gates=FAIL

## [INFO] 2026-08-08 05:31:24 UTC (tier 0)

Hunt complete: {"generation_id": "causal_drop_retrace_001_05_BTCUSDT_1h_direction_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": true, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 09:12:13 UTC (tier 0)

D-060 CLOSED_TRADING_FAIL nest-filter + inventory NO parent PF>=1; optional sparse_leg_vol_skip_001 OPEN_OPTIONAL not auto-run

## [INFO] 2026-08-08 09:12:31 UTC (tier 0)

RUN_RETRACE_ALPHA_001 start stamp=20260808T091231Z prereg_sha=9fb2a833ce67e384 space=structure_v1_run_retrace fold=v2 lockbox=2026-05-01

## [INFO] 2026-08-08 09:19:26 UTC (tier 0)

RUN_RETRACE_ALPHA_001 hunt start run_retrace_alpha_001_00_BTCUSDT_1h_fwd_return_20260808

## [INFO] 2026-08-08 09:19:26 UTC (tier 0)

START gen=run_retrace_alpha_001_00_BTCUSDT_1h_fwd_return_20260808 BTCUSDT 1h target=fwd_return space=structure_v1_run_retrace

## [INFO] 2026-08-08 09:25:11 UTC (tier 0)

PREDICTABILITY real=-0.01937 p=0.9048 surr_q95=-0.00113 surr_max=-0.00025 draws=20 passed=False

## [INFO] 2026-08-08 09:26:36 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 09:26:36 UTC (tier 0)

trial `9559ed8b-b1f3-4979-acb2-eed94de33de4` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-08 09:27:57 UTC (tier 0)

SURROGATE FAIL model=ridge skill_real=-0.00622 skill_surrogate=-0.00245

## [INFO] 2026-08-08 09:27:57 UTC (tier 0)

trial `692a6776-9220-412f-b7d1-f80ae65feca1` model=ridge tier=0 target=fwd_return pf=0.818 n=2409 gates=FAIL

## [INFO] 2026-08-08 09:29:39 UTC (tier 0)

SURROGATE FAIL model=lgbm_regressor skill_real=-0.00871 skill_surrogate=-0.00747

## [INFO] 2026-08-08 09:29:39 UTC (tier 0)

trial `9e04e8cb-c17a-42b6-9f45-67da6b38e59b` model=lgbm_regressor tier=0 target=fwd_return pf=0.846 n=2635 gates=FAIL

## [INFO] 2026-08-08 09:32:44 UTC (tier 0)

SURROGATE FAIL model=lgbm_classifier skill_real=-113.73165 skill_surrogate=-4.58868

## [INFO] 2026-08-08 09:32:44 UTC (tier 0)

trial `5e3375f5-904f-462f-b0e8-b4d9728859cf` model=lgbm_classifier tier=0 target=fwd_return pf=0.761 n=4312 gates=FAIL

## [INFO] 2026-08-08 09:32:44 UTC (tier 0)

Hunt complete: {"generation_id": "run_retrace_alpha_001_00_BTCUSDT_1h_fwd_return_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 09:32:44 UTC (tier 0)

RUN_RETRACE_ALPHA_001 hunt start run_retrace_alpha_001_01_ETHUSDT_1h_direction_20260808

## [INFO] 2026-08-08 09:32:44 UTC (tier 0)

START gen=run_retrace_alpha_001_01_ETHUSDT_1h_direction_20260808 ETHUSDT 1h target=direction space=structure_v1_run_retrace

## [INFO] 2026-08-08 09:37:12 UTC (tier 0)

PREDICTABILITY real=-0.01086 p=0.9524 surr_q95=+0.00027 surr_max=+0.00404 draws=20 passed=False

## [INFO] 2026-08-08 09:38:49 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 09:38:49 UTC (tier 0)

trial `f69ca72f-a644-4c0c-bb7f-ac7e142eba25` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-08 09:39:48 UTC (tier 0)

trial `e0e14e95-a454-402f-b8c4-35f0f7f5efb1` model=ridge tier=0 target=direction pf=0.759 n=3151 gates=FAIL

## [INFO] 2026-08-08 09:41:56 UTC (tier 0)

trial `97481bb4-40ce-4066-bed4-53392539107c` model=lgbm_regressor tier=0 target=direction pf=0.765 n=5298 gates=FAIL

## [INFO] 2026-08-08 09:45:09 UTC (tier 0)

trial `c053fbc4-2671-4e0d-912b-2473ba4b092b` model=lgbm_classifier tier=0 target=direction pf=0.780 n=6972 gates=FAIL

## [INFO] 2026-08-08 09:45:09 UTC (tier 0)

Hunt complete: {"generation_id": "run_retrace_alpha_001_01_ETHUSDT_1h_direction_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 09:45:09 UTC (tier 0)

RUN_RETRACE_ALPHA_001 hunt start run_retrace_alpha_001_02_SOLUSDT_1h_direction_20260808

## [INFO] 2026-08-08 09:45:09 UTC (tier 0)

START gen=run_retrace_alpha_001_02_SOLUSDT_1h_direction_20260808 SOLUSDT 1h target=direction space=structure_v1_run_retrace

## [INFO] 2026-08-08 09:47:39 UTC (tier 0)

PREDICTABILITY real=-0.00019 p=0.1429 surr_q95=+0.00002 surr_max=+0.00035 draws=20 passed=False

## [INFO] 2026-08-08 09:47:51 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 09:47:51 UTC (tier 0)

trial `f4911c61-9bba-4658-8a95-ddf708882586` model=hist_mean tier=0 target=direction pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-08 09:48:04 UTC (tier 0)

trial `7e9ced94-0690-4c16-a59e-03ef9705be6a` model=ridge tier=0 target=direction pf=0.784 n=6213 gates=FAIL

## [INFO] 2026-08-08 09:48:27 UTC (tier 0)

trial `7649f56a-97b0-4993-b507-48dcdfa63746` model=lgbm_regressor tier=0 target=direction pf=0.775 n=7926 gates=FAIL

## [INFO] 2026-08-08 09:50:36 UTC (tier 0)

trial `5fdc1d0b-b768-4618-919d-629db3e21d03` model=lgbm_classifier tier=0 target=direction pf=0.790 n=11797 gates=FAIL

## [INFO] 2026-08-08 09:50:36 UTC (tier 0)

Hunt complete: {"generation_id": "run_retrace_alpha_001_02_SOLUSDT_1h_direction_20260808", "status": "COMPLETE", "n_trials": 4, "best_tier": 0, "predictability_passed": false, "n_folds": 6, "cost_hurdle": 0.0016, "break_even_p": 0.72}

## [INFO] 2026-08-08 09:50:36 UTC (tier 0)

RUN_RETRACE_ALPHA_001 hunt start run_retrace_alpha_001_03_ETHUSDT_1h_fwd_return_20260808

## [INFO] 2026-08-08 09:50:36 UTC (tier 0)

START gen=run_retrace_alpha_001_03_ETHUSDT_1h_fwd_return_20260808 ETHUSDT 1h target=fwd_return space=structure_v1_run_retrace

## [INFO] 2026-08-08 09:53:29 UTC (tier 0)

PREDICTABILITY real=-0.00594 p=0.6190 surr_q95=+0.00140 surr_max=+0.00267 draws=20 passed=False

## [INFO] 2026-08-08 09:53:41 UTC (tier 0)

SURROGATE FAIL model=hist_mean skill_real=+0.00000 skill_surrogate=+0.00000

## [INFO] 2026-08-08 09:53:41 UTC (tier 0)

trial `ecf9a954-f282-44ea-8359-e91ceb50310d` model=hist_mean tier=0 target=fwd_return pf=0.000 n=0 gates=FAIL

## [INFO] 2026-08-10 08:13:09 UTC (tier 0)

PIVOT_TRAIN_MATRIX start fold=v2

## [INFO] 2026-08-10 10:13:59 UTC (tier 0)

PIVOT_MULTIHEAD_RARE start fold=v2

## [INFO] 2026-08-10 10:21:57 UTC (tier 0)

PIVOT_MULTIHEAD_RARE start fold=v2

## [INFO] 2026-08-10 10:32:45 UTC (tier 0)

PIVOT_LIMIT_STRAT_DIAG start 20260810T103245Z

## [INFO] 2026-08-10 10:38:19 UTC (tier 0)

PIVOT_LIMIT_STRAT_DIAG_GRID start 20260810T103819Z

## [INFO] 2026-08-10 11:39:03 UTC (tier 0)

PIVOT_STRATEGY_STACK start 20260810T113903Z

## [INFO] 2026-08-10 11:39:13 UTC (tier 0)

PIVOT_STRATEGY_STACK start 20260810T113913Z

## [INFO] 2026-08-10 16:12:56 UTC (tier 0)

PIVOT_LEVEL_PLACE_TF start 20260810T161256Z

## [INFO] 2026-08-10 16:14:41 UTC (tier 0)

PIVOT_LEVEL_PLACE_TF start 20260810T161441Z

## [INFO] 2026-08-10 16:15:59 UTC (tier 0)

PIVOT_LEVEL_PLACE_TF start 20260810T161559Z

## [INFO] 2026-08-12 04:52:36 UTC (tier 0)

PIVOT_REENTRY_VSA start 20260812T045236Z

## [INFO] 2026-08-12 04:57:11 UTC (tier 0)

PIVOT_REENTRY_VSA start 20260812T045711Z

## [INFO] 2026-08-12 05:05:34 UTC (tier 0)

PIVOT_REENTRY_VSA start 20260812T050534Z

## [INFO] 2026-08-12 05:39:04 UTC (tier 0)

PIVOT_TIMING_LEVEL_STACK start 20260812T053904Z

## [ALERT] 2026-08-12 13:09:18 UTC (tier 2)

PIVOT_LIVE_AUTH arm=pivot_sol_geo_tp1_sl1_p75_w4 account=Xxobster7 host=94.156.189.76 hash=a94465fd6cd4110f four_proof_ok=true

## [ALERT] 2026-08-12 13:09:20 UTC (tier 2)

PIVOT_LIVE_AUTH arm=pivot_eth_p75_ctrl_atr_w4 account=Xxobster7 host=94.156.189.76 hash=37dc6d256f1c0a9a four_proof_ok=true

## [INFO] 2026-08-15 04:21:27 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_k5_tp1_be_tp2_hold24_001 control_exp_ru=-0.001879089858340348 cand_exp_ru=-0.0018065623450530086 control_pf=0.7145039065339663 cand_pf=0.75137581819614 path=artifacts/reports/structure_v1_eth_k5_tp1_be_tp2_hold24_001_latest.json

## [INFO] 2026-08-15 04:22:40 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_k5_tp1_be_tp2_hold24_001 control_exp_ru=-0.001879089858340348 cand_exp_ru=-0.0018065623450530086 control_pf=0.7145039065339663 cand_pf=0.75137581819614 path=artifacts/reports/structure_v1_eth_k5_tp1_be_tp2_hold24_001_latest.json

## [INFO] 2026-08-15 04:23:06 UTC (tier 0)

OUTER_TRANSFER_COMPARE generation_id=structure_v1_eth_k5_tp1_be_tp2_hold24_001 control_exp_ru=-0.001879089858340348 cand_exp_ru=-0.0018065623450530086 control_pf=0.7145039065339663 cand_pf=0.75137581819614 path=artifacts/reports/structure_v1_eth_k5_tp1_be_tp2_hold24_001_latest.json

## [INFO] 2026-08-19 03:57:49 UTC (tier 0)

CONFLUENCE_EVENT_IMPORTANCE_001 start 20260819T035749Z

## [INFO] 2026-08-19 03:59:15 UTC (tier 0)

CONFLUENCE_EVENT_IMPORTANCE_001 start 20260819T035915Z

## [INFO] 2026-08-19 04:46:25 UTC (tier 0)

CONFLUENCE_EVENT_IMPORTANCE_001 done survivors=14 path=D:\projects\LLM2\artifacts\reports\confluence\event_importance_001_latest.json

## [INFO] 2026-08-19 04:49:25 UTC (tier 0)

CONFLUENCE_EVENT_PACK_TRAIN_001 start 20260819T044925Z n_surv=14

## [INFO] 2026-08-19 04:51:36 UTC (tier 0)

CONFLUENCE_EVENT_PACK_TRAIN_001 done path=D:\projects\LLM2\artifacts\reports\confluence\event_pack_train_001_latest.json

## [INFO] 2026-08-19 04:59:29 UTC (tier 0)

CONFLUENCE_AUTONOMOUS_HUNT_002 start 20260819T045929Z

## [INFO] 2026-08-19 05:20:25 UTC (tier 0)

CONFLUENCE_AUTONOMOUS_HUNT_002 checkpoint arms=1092 path=D:\projects\LLM2\artifacts\reports\confluence\autonomous_hunt_002_latest.md

## [ALERT] 2026-08-20 21:20:30 UTC (tier 2)

PIVOT_LIVE_AUTH ETH+SOL 15m 0.5pct/0.5pct account=Xxobster9 host=212.73.150.178 packs=eth_p50_tp05_sl05_w4,sol_p50_tp05_sl05_w4 (research remains LIVE_STOP; user operational authorize)
