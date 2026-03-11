"""Dataset loading utilities for ViHSD-style CSV files."""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

REQUIRED_COLUMNS = ("text", "label")


def load_dataset(csv_path: str | Path) -> pd.DataFrame:
    """Load dataset and validate required schema."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    df = pd.read_csv(path)
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df[list(REQUIRED_COLUMNS)].dropna().copy()
    df["text"] = df["text"].astype(str)
    df["label"] = df["label"].astype(str)
    return df


def stratified_split(
    df: pd.DataFrame,
    seed: int = 42,
    test_size: float = 0.2,
    val_size: float = 0.1,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Create deterministic train/val/test split with stratification."""
    if not 0 < test_size < 1:
        raise ValueError("test_size must be in (0, 1)")
    if not 0 < val_size < 1:
        raise ValueError("val_size must be in (0, 1)")
    if val_size + test_size >= 1:
        raise ValueError("val_size + test_size must be < 1")

    train_val, test = train_test_split(
        df,
        test_size=test_size,
        random_state=seed,
        stratify=df["label"],
    )
    relative_val_size = val_size / (1 - test_size)
    train, val = train_test_split(
        train_val,
        test_size=relative_val_size,
        random_state=seed,
        stratify=train_val["label"],
    )
    return train.reset_index(drop=True), val.reset_index(drop=True), test.reset_index(drop=True)
