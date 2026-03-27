"""Text preprocessing for Vietnamese hate speech detection."""

from __future__ import annotations

import re
import unicodedata

import pandas as pd

URL_PATTERN = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
WHITESPACE_PATTERN = re.compile(r"\s+")
PUNCT_REPEAT_PATTERN = re.compile(r"([!?.,;:])\1+")
# Remove only control characters while preserving regular Unicode text.
NOISE_PATTERN = re.compile(r"[\u0000-\u001F\u007F]")


def _remove_symbol_chars(text: str) -> str:
    """Replace Unicode Symbol characters (emoji, currency, math symbols, etc.) with spaces."""
    return "".join(" " if unicodedata.category(ch).startswith("S") else ch for ch in text)


def clean_text(text: str, lowercase: bool = False) -> str:
    """Normalize a single text sample."""
    if not isinstance(text, str):
        text = str(text)

    text = URL_PATTERN.sub(" ", text)
    text = NOISE_PATTERN.sub(" ", text)
    text = _remove_symbol_chars(text)
    text = PUNCT_REPEAT_PATTERN.sub(r"\1", text)
    text = WHITESPACE_PATTERN.sub(" ", text).strip()
    if lowercase:
        text = text.lower()
    return text


def preprocess_dataframe(df: pd.DataFrame, text_col: str = "text", lowercase: bool = False) -> pd.DataFrame:
    """Apply cleaning to an input dataframe."""
    out = df.copy()
    out[text_col] = out[text_col].astype(str).map(lambda x: clean_text(x, lowercase=lowercase))
    return out
