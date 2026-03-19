"""Shared PhoBERT-BiLSTM classifier module for training and inference."""

from __future__ import annotations

import torch
from torch import nn
from transformers import AutoModel


def load_hf_model_safetensors_first(model_cls, model_name: str, **kwargs):
    try:
        return model_cls.from_pretrained(model_name, use_safetensors=True, **kwargs)
    except Exception as exc:
        msg = str(exc).lower()
        if "safetensors" in msg and ("not found" in msg or "could not locate" in msg or "no file named" in msg):
            return model_cls.from_pretrained(model_name, **kwargs)
        raise


class PhoBertSequenceClassifier(nn.Module):
    def __init__(
        self,
        model_name: str,
        num_classes: int,
        head_type: str = "cls_mlp",
        hidden_dim: int = 256,
        dropout: float = 0.3,
        freeze_encoder: bool = False,
    ):
        super().__init__()
        self.encoder = load_hf_model_safetensors_first(AutoModel, model_name)
        self.freeze_encoder = freeze_encoder
        for p in self.encoder.parameters():
            p.requires_grad = not freeze_encoder

        self.head_type = head_type
        enc_dim = int(self.encoder.config.hidden_size)
        self.dropout = nn.Dropout(dropout)

        if head_type == "bilstm":
            self.bilstm = nn.LSTM(enc_dim, hidden_dim, batch_first=True, bidirectional=True)
            self.head = nn.Linear(hidden_dim * 2, num_classes)
        elif head_type == "attn_mlp":
            self.attn_score = nn.Linear(enc_dim, 1)
            self.head = nn.Sequential(
                nn.Linear(enc_dim, hidden_dim),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, num_classes),
            )
        elif head_type in {"cls_mlp", "mean_mlp"}:
            self.head = nn.Sequential(
                nn.Linear(enc_dim, hidden_dim),
                nn.GELU(),
                nn.Dropout(dropout),
                nn.Linear(hidden_dim, num_classes),
            )
        else:
            raise ValueError(f"Unsupported head_type={head_type}")

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        if self.freeze_encoder:
            with torch.no_grad():
                hidden = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        else:
            hidden = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state

        if self.head_type == "bilstm":
            out, _ = self.bilstm(hidden)
            mask = attention_mask.unsqueeze(-1).float()
            pooled = (out * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1.0)
            return self.head(self.dropout(pooled))

        if self.head_type == "mean_mlp":
            mask = attention_mask.unsqueeze(-1).float()
            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1.0)
            return self.head(pooled)

        if self.head_type == "attn_mlp":
            mask = attention_mask.bool()
            scores = self.attn_score(hidden).squeeze(-1)
            scores = scores.masked_fill(~mask, -1e4)
            weights = torch.softmax(scores, dim=1).unsqueeze(-1)
            pooled = (weights * hidden).sum(dim=1)
            return self.head(pooled)

        return self.head(hidden[:, 0, :])
