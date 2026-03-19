#!/usr/bin/env python
"""Upload PhoBiHSD pretrained checkpoint to Hugging Face Hub."""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path

from huggingface_hub import HfApi


def _resolve_checkpoint(explicit_ckpt: str | None) -> Path:
    candidates = []
    if explicit_ckpt:
        candidates.append(Path(explicit_ckpt))
    candidates.extend(
        [
            Path("models/phobihsd_proposed.pt"),
            Path("results/checkpoints/phobihsd_proposed.pt"),
        ]
    )
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(
        "Could not find pretrained checkpoint. Checked: "
        + ", ".join(str(p) for p in candidates)
    )


def _load_meta(ckpt_path: Path) -> dict:
    meta_path = ckpt_path.with_suffix(".meta.json")
    if meta_path.exists():
        return json.loads(meta_path.read_text(encoding="utf-8"))
    return {}


def _make_model_card(repo_id: str, ckpt_name: str, meta: dict) -> str:
    return f"""---
library_name: transformers
license: apache-2.0
tags:
  - vietnamese
  - hate-speech-detection
  - phobert
  - bilstm
  - text-classification
pipeline_tag: text-classification
---

# {repo_id}

PhoBiHSD proposed checkpoint (PhoBERT-BiLSTM) for Vietnamese hate speech detection on ViHSD.

## Files
- `{ckpt_name}`: PyTorch checkpoint (`state_dict` + optional thresholds).
- `phobihsd_proposed.meta.json`: model metadata.
- `model_comparison.yaml`: training/inference config used by this repository.

## Label Mapping
- `0`: Clean
- `1`: Offensive
- `2`: Hate

## Metadata (from checkpoint sidecar)
```json
{json.dumps(meta, ensure_ascii=False, indent=2)}
```

## Inference (from this repo)
```bash
export PHOBIHSD_PROPOSED_CKPT={ckpt_name}
export PHOBIHSD_CONFIG=config/experiments/model_comparison.yaml
python -m app.gradio_app
```
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-id", type=str, default="", help="Hugging Face repo id (e.g. username/phobihsd-proposed)")
    parser.add_argument("--checkpoint", type=str, default="", help="Custom checkpoint path")
    parser.add_argument("--private", action="store_true", help="Create private repository")
    parser.add_argument("--commit-message", type=str, default="Upload PhoBiHSD pretrained checkpoint")
    args = parser.parse_args()

    ckpt_path = _resolve_checkpoint(args.checkpoint or None)
    meta = _load_meta(ckpt_path)

    api = HfApi()
    if not args.repo_id:
        who = api.whoami()
        username = who.get("name") or who.get("fullname")
        if not username:
            raise RuntimeError("Unable to resolve Hugging Face username. Use --repo-id explicitly.")
        repo_id = f"{username}/phobihsd-proposed"
    else:
        repo_id = args.repo_id

    api.create_repo(repo_id=repo_id, repo_type="model", private=args.private, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="phobihsd_hf_") as tmp:
        tmp_dir = Path(tmp)
        ckpt_target = tmp_dir / ckpt_path.name
        shutil.copy2(ckpt_path, ckpt_target)

        meta_path = ckpt_path.with_suffix(".meta.json")
        if meta_path.exists():
            shutil.copy2(meta_path, tmp_dir / meta_path.name)

        cfg_path = Path("config/experiments/model_comparison.yaml")
        if cfg_path.exists():
            shutil.copy2(cfg_path, tmp_dir / cfg_path.name)

        model_card = _make_model_card(repo_id=repo_id, ckpt_name=ckpt_path.name, meta=meta)
        (tmp_dir / "README.md").write_text(model_card, encoding="utf-8")

        api.upload_folder(
            repo_id=repo_id,
            repo_type="model",
            folder_path=str(tmp_dir),
            commit_message=args.commit_message,
        )

    print(f"[DONE] Uploaded pretrained model to https://huggingface.co/{repo_id}")


if __name__ == "__main__":
    main()
