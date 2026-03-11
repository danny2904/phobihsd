"""Small Gradio app for PhoBiHSD proposed model inference."""

from __future__ import annotations

import os
from typing import Dict, Tuple

import gradio as gr

from src.inference.proposed_predictor import ProposedPredictor

DEFAULT_CKPT = os.getenv("PHOBIHSD_PROPOSED_CKPT", "models/phobihsd_proposed.pt")
DEFAULT_CFG = os.getenv("PHOBIHSD_CONFIG", "config/experiments/model_comparison.yaml")
DEFAULT_HOST = os.getenv("PHOBIHSD_HOST", "0.0.0.0")
DEFAULT_PORT = int(os.getenv("PHOBIHSD_PORT", "7860"))


def load_predictor() -> ProposedPredictor:
    return ProposedPredictor(checkpoint_path=DEFAULT_CKPT, config_path=DEFAULT_CFG)


PREDICTOR = None
LOAD_ERROR = None
try:
    PREDICTOR = load_predictor()
except Exception as exc:  # pragma: no cover
    LOAD_ERROR = str(exc)


def _format_probs(prob: Dict[str, float]) -> Dict[str, float]:
    return {
        "Clean": round(prob["Clean"], 4),
        "Offensive": round(prob["Offensive"], 4),
        "Hate": round(prob["Hate"], 4),
    }


def predict_text(text: str) -> Tuple[str, Dict[str, float], str]:
    if LOAD_ERROR is not None or PREDICTOR is None:
        msg = (
            "Model not loaded. "
            f"Error: {LOAD_ERROR}. "
            "Set PHOBIHSD_PROPOSED_CKPT to a valid proposed checkpoint path."
        )
        return msg, {"Clean": 0.0, "Offensive": 0.0, "Hate": 0.0}, ""

    if not text or not text.strip():
        return "Please enter a Vietnamese sentence.", {"Clean": 0.0, "Offensive": 0.0, "Hate": 0.0}, ""

    out = PREDICTOR.predict(text)
    summary = (
        f"Label: {out['label']}\n"
        f"Toxicity score: {out['toxic_score']:.4f}\n"
        f"Toxicity level: {out['toxicity_level']}"
    )
    detail = f"Cleaned text: {out['text_clean']}"
    return summary, _format_probs(out["probabilities"]), detail


DESCRIPTION = (
    "Enter a Vietnamese social-media sentence to classify into Clean / Offensive / Hate. "
    "The app returns label, class probabilities, and toxicity level."
)


with gr.Blocks(title="PhoBiHSD Proposed Model Demo") as demo:
    gr.Markdown("# PhoBiHSD Proposed Model Demo")
    gr.Markdown(DESCRIPTION)

    with gr.Row():
        textbox = gr.Textbox(
            label="Input text",
            lines=4,
            placeholder="Nhap cau tieng Viet can du doan...",
        )

    with gr.Row():
        btn = gr.Button("Predict", variant="primary")

    with gr.Row():
        output_summary = gr.Textbox(label="Prediction", lines=4)
        output_probs = gr.Label(label="Class probabilities", num_top_classes=3)

    output_detail = gr.Textbox(label="Details", lines=2)

    gr.Examples(
        examples=[
            ["Mày nói chuyện lịch sự dùm cái."],
            ["Đồ ngu, cút đi cho khuất mắt."],
            ["Tụi nó toàn lũ rác rưởi cần bị loại bỏ."],
        ],
        inputs=[textbox],
    )

    btn.click(fn=predict_text, inputs=[textbox], outputs=[output_summary, output_probs, output_detail])


if __name__ == "__main__":
    demo.queue().launch(server_name=DEFAULT_HOST, server_port=DEFAULT_PORT)
