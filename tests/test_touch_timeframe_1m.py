from llm2.paths import touch_timeframe


def test_decision_books_use_one_minute_touch():
    assert touch_timeframe("15m", "ETHUSDT") == "1m"
    assert touch_timeframe("15m", "BTCUSDT") == "1m"
    assert touch_timeframe("15m", "SOLUSDT") == "1m"
    assert touch_timeframe("1h", "ETHUSDT") == "1m"
    assert touch_timeframe("4h", "BTCUSDT") == "1m"
