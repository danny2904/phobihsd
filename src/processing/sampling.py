"""Sampling strategies for imbalanced classification."""

from __future__ import annotations

from typing import Dict, Tuple

import numpy as np
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import EditedNearestNeighbours, NearMiss, RandomUnderSampler, TomekLinks

SamplerResult = Tuple[np.ndarray, np.ndarray]
SamplerWithIdxResult = Tuple[np.ndarray, np.ndarray, np.ndarray]


def _chain_with_indices(sampler, X: np.ndarray, y: np.ndarray, indices: np.ndarray) -> SamplerWithIdxResult:
    """Apply a sampler and propagate sample indices."""
    X_res, y_res = sampler.fit_resample(X, y)
    sample_idx = getattr(sampler, "sample_indices_", None)
    if sample_idx is None:
        raise RuntimeError(f"Sampler {sampler.__class__.__name__} does not expose sample_indices_.")
    idx_res = indices[np.asarray(sample_idx, dtype=np.int64)]
    return X_res, y_res, idx_res


def apply_sampling(method: str, X: np.ndarray, y: np.ndarray, seed: int = 42) -> SamplerResult:
    """Apply one of the supported sampling methods."""
    if method == "ROS":
        sampler = RandomOverSampler(random_state=seed)
        return sampler.fit_resample(X, y)

    if method == "ROS+ENN":
        X1, y1 = RandomOverSampler(random_state=seed).fit_resample(X, y)
        return EditedNearestNeighbours().fit_resample(X1, y1)

    if method == "ROS+NearMiss":
        # Avoid no-op: apply NearMiss first, then ROS to recover class coverage.
        X1, y1 = NearMiss().fit_resample(X, y)
        return RandomOverSampler(random_state=seed).fit_resample(X1, y1)

    if method == "ROS+RUS":
        # Avoid no-op: apply RUS first, then ROS.
        X1, y1 = RandomUnderSampler(random_state=seed).fit_resample(X, y)
        return RandomOverSampler(random_state=seed).fit_resample(X1, y1)

    if method == "ROS+RUS+Tomek":
        # Hybrid under/over with final boundary cleaning.
        X1, y1 = RandomUnderSampler(random_state=seed).fit_resample(X, y)
        X2, y2 = RandomOverSampler(random_state=seed).fit_resample(X1, y1)
        return TomekLinks().fit_resample(X2, y2)

    if method == "ROS+Tomek":
        # Oversample then clean Tomek links near class boundary.
        X1, y1 = RandomOverSampler(random_state=seed).fit_resample(X, y)
        return TomekLinks().fit_resample(X1, y1)

    raise ValueError(f"Unsupported sampling method: {method}")


def apply_sampling_with_indices(
    method: str,
    X: np.ndarray,
    y: np.ndarray,
    seed: int = 42,
) -> SamplerWithIdxResult:
    """Apply sampling and return (X_res, y_res, selected_original_indices)."""
    base_indices = np.arange(len(y), dtype=np.int64)

    if method == "ROS":
        ros = RandomOverSampler(random_state=seed)
        return _chain_with_indices(ros, X, y, base_indices)

    if method == "ROS+ENN":
        ros = RandomOverSampler(random_state=seed)
        X1, y1, idx1 = _chain_with_indices(ros, X, y, base_indices)
        enn = EditedNearestNeighbours()
        return _chain_with_indices(enn, X1, y1, idx1)

    if method == "ROS+NearMiss":
        nm = NearMiss()
        X1, y1, idx1 = _chain_with_indices(nm, X, y, base_indices)
        ros = RandomOverSampler(random_state=seed)
        return _chain_with_indices(ros, X1, y1, idx1)

    if method == "ROS+RUS":
        rus = RandomUnderSampler(random_state=seed)
        X1, y1, idx1 = _chain_with_indices(rus, X, y, base_indices)
        ros = RandomOverSampler(random_state=seed)
        return _chain_with_indices(ros, X1, y1, idx1)

    if method == "ROS+RUS+Tomek":
        rus = RandomUnderSampler(random_state=seed)
        X1, y1, idx1 = _chain_with_indices(rus, X, y, base_indices)
        ros = RandomOverSampler(random_state=seed)
        X2, y2, idx2 = _chain_with_indices(ros, X1, y1, idx1)
        tomek = TomekLinks()
        return _chain_with_indices(tomek, X2, y2, idx2)

    if method == "ROS+Tomek":
        ros = RandomOverSampler(random_state=seed)
        X1, y1, idx1 = _chain_with_indices(ros, X, y, base_indices)
        tomek = TomekLinks()
        return _chain_with_indices(tomek, X1, y1, idx1)

    raise ValueError(f"Unsupported sampling method: {method}")


def class_distribution(y: np.ndarray) -> Dict[str, int]:
    """Return class frequency dict."""
    labels, counts = np.unique(y, return_counts=True)
    return {str(k): int(v) for k, v in zip(labels, counts)}
