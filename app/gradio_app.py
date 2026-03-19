"""Small Gradio app for PhoBiHSD proposed model inference."""

from __future__ import annotations

import os
from typing import Dict, Tuple

import gradio as gr

from src.inference.proposed_predictor import ProposedPredictor


def _default_ckpt_path() -> str:
    env_ckpt = os.getenv("PHOBIHSD_PROPOSED_CKPT")
    if env_ckpt:
        return env_ckpt
    if os.path.exists("models/phobihsd_proposed.safetensors"):
        return "models/phobihsd_proposed.safetensors"
    if os.path.exists("results/checkpoints/phobihsd_proposed.safetensors"):
        return "results/checkpoints/phobihsd_proposed.safetensors"
    if os.path.exists("models/phobihsd_proposed.pt"):
        return "models/phobihsd_proposed.pt"
    if os.path.exists("results/checkpoints/phobihsd_proposed.pt"):
        return "results/checkpoints/phobihsd_proposed.pt"
    return "models/phobihsd_proposed.safetensors"


DEFAULT_CKPT = _default_ckpt_path()
DEFAULT_CFG = os.getenv("PHOBIHSD_CONFIG", "config/experiments/model_comparison.yaml")
DEFAULT_DEVICE = os.getenv("PHOBIHSD_DEVICE", "auto")
DEFAULT_HOST = os.getenv("PHOBIHSD_HOST", "0.0.0.0")
DEFAULT_PORT = int(os.getenv("PHOBIHSD_PORT", "7860"))


def load_predictor() -> ProposedPredictor:
    return ProposedPredictor(checkpoint_path=DEFAULT_CKPT, config_path=DEFAULT_CFG, device=DEFAULT_DEVICE)


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
    "The app returns label, class probabilities, and toxicity level. "
    f"Runtime device mode: {DEFAULT_DEVICE}."
)

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap');

:root {
  --phb-bg-a: #f7fbff;
  --phb-bg-b: #eef6f2;
  --phb-card: #ffffff;
  --phb-ink: #0f172a;
  --phb-soft: #475569;
  --phb-accent: #0f766e;
}

body, .gradio-container {
  font-family: "Be Vietnam Pro", "Segoe UI", sans-serif !important;
  color: var(--phb-ink);
  font-size: 18px !important;
}

.gradio-container {
  max-width: 1100px !important;
  margin: 0 auto !important;
  background: radial-gradient(1200px 600px at 0% 0%, var(--phb-bg-a), transparent),
              radial-gradient(1200px 600px at 100% 0%, var(--phb-bg-b), transparent);
}

.phb-hero {
  background: linear-gradient(135deg, #f8fafc, #ecfeff);
  border: 1px solid #dbeafe;
  border-radius: 18px;
  padding: 18px 20px;
  margin-bottom: 12px;
}

.phb-hero h1 {
  margin: 0 0 8px 0;
  font-size: 36px;
  line-height: 1.2;
}

.phb-hero p {
  margin: 0;
  font-size: 19px;
  color: var(--phb-soft);
}

.phb-card {
  background: var(--phb-card);
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 10px 12px;
}

.phb-card h3 {
  margin: 6px 6px 10px 6px;
  font-size: 22px;
}

.phb-footnote {
  font-size: 15px;
  color: var(--phb-soft);
  margin-top: 8px;
}

.gr-button {
  font-size: 19px !important;
  font-weight: 700 !important;
  border-radius: 14px !important;
  min-height: 54px !important;
}

textarea, input, .gr-textbox, .gr-label, .gr-markdown, .gr-form {
  font-size: 18px !important;
}

.gr-textbox textarea {
  line-height: 1.6 !important;
}

label span {
  font-size: 17px !important;
  font-weight: 600 !important;
}
"""

APP_THEME = gr.themes.Soft(
    primary_hue="emerald",
    secondary_hue="blue",
    neutral_hue="slate",
)

with gr.Blocks(title="PhoBiHSD Proposed Model Demo", css=CUSTOM_CSS, theme=APP_THEME) as demo:
    gr.Markdown(
        f"""
<div class="phb-hero">
  <h1>PhoBiHSD Demo</h1>
  <p>{DESCRIPTION}</p>
</div>
"""
    )

    with gr.Row():
        with gr.Column(scale=6, elem_classes=["phb-card"]):
            gr.Markdown("### Input")
            textbox = gr.Textbox(
                label="Vietnamese text",
                lines=5,
                placeholder="Nhap cau tieng Viet can du doan...",
            )
            btn = gr.Button("Analyze Text", variant="primary")
            gr.Markdown('<div class="phb-footnote">Mẹo: nhập câu ngắn, rõ nghĩa để kết quả ổn định hơn.</div>')

        with gr.Column(scale=6, elem_classes=["phb-card"]):
            gr.Markdown("### Result")
            output_summary = gr.Textbox(label="Prediction summary", lines=4)
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
