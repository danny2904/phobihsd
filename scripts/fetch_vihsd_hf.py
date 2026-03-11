#!/usr/bin/env python
from __future__ import annotations

from pathlib import Path

import pandas as pd
from datasets import load_dataset

LABEL_MAP = {
    0: 'Clean',
    1: 'Offensive',
    2: 'Hate',
}


def main() -> None:
    ds = load_dataset('htdung167/ViHSD')
    frames = []
    for split_name in ds.keys():
        df = ds[split_name].to_pandas()
        df = df[['free_text', 'label_id']].rename(columns={'free_text': 'text', 'label_id': 'label'})
        frames.append(df)

    out = pd.concat(frames, ignore_index=True)
    out['label'] = out['label'].map(LABEL_MAP)
    out = out.dropna(subset=['text', 'label']).copy()

    out_path = Path('data/raw/vihsd.csv')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)

    print(f'Saved: {out_path} rows={len(out)}')
    print(out['label'].value_counts().to_dict())


if __name__ == '__main__':
    main()
