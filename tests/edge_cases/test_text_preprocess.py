from src.processing.text_preprocess import clean_text


def test_clean_text_removes_url_and_emoji_like_noise():
    raw = "đồ ngu!!! https://abc.com 😡"
    out = clean_text(raw)
    assert "http" not in out
    assert "😡" not in out


def test_clean_text_normalizes_spaces():
    raw = "xin   chao\n\n  ban"
    out = clean_text(raw)
    assert out == "xin chao ban"
