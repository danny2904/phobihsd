"""Device selection helpers for CPU/GPU runtime."""

from __future__ import annotations

import torch


VALID_DEVICE_PREFS = {"auto", "cpu", "cuda"}


def resolve_torch_device(preference: str | None = None) -> torch.device:
    pref = (preference or "auto").strip().lower()
    if pref not in VALID_DEVICE_PREFS:
        raise ValueError(f"Unsupported device preference: {preference}. Use one of: auto,cpu,cuda")

    if pref == "cpu":
        return torch.device("cpu")

    if pref == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("Requested device='cuda' but CUDA is not available.")
        return torch.device("cuda")

    # auto
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")
