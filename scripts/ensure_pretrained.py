#!/usr/bin/env python
"""Ensure PhoBiHSD pretrained checkpoint exists locally."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from huggingface_hub import hf_hub_download


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-id", type=str, default="joshswift/phobihsd-proposed")
    parser.add_argument("--filename", type=str, default="phobihsd_proposed.pt")
    parser.add_argument("--meta-filename", type=str, default="phobihsd_proposed.meta.json")
    parser.add_argument("--target-path", type=str, default="models/phobihsd_proposed.pt")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    target = Path(args.target_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    meta_target = target.with_suffix(".meta.json")

    if target.exists() and meta_target.exists() and not args.force:
        print(f"[OK] Checkpoint exists: {target}")
        return

    print(f"[INFO] Downloading checkpoint from {args.repo_id} ...")
    ckpt_src = hf_hub_download(repo_id=args.repo_id, filename=args.filename, repo_type="model")
    meta_src = hf_hub_download(repo_id=args.repo_id, filename=args.meta_filename, repo_type="model")

    shutil.copy2(ckpt_src, target)
    shutil.copy2(meta_src, meta_target)
    print(f"[DONE] Saved checkpoint: {target}")
    print(f"[DONE] Saved metadata: {meta_target}")


if __name__ == "__main__":
    main()
