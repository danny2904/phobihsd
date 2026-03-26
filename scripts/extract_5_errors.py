import pandas as pd
from src.inference.proposed_predictor import ProposedPredictor

LABEL_MAP={0:'Clean',1:'Offensive',2:'Hate'}

model=ProposedPredictor(
    checkpoint_path='models/phobihsd_proposed.safetensors',
    config_path='config/experiments/model_comparison.yaml',
    device='cuda',
)

df=pd.read_csv('data/raw/test.csv')
errors=[]
for i,row in df.iterrows():
    text=str(row['free_text'])
    true_label=LABEL_MAP[int(row['label_id'])]
    out=model.predict(text)
    pred_label=out['label']
    if pred_label!=true_label:
        t=out['text_clean'].replace('\n',' ').strip()
        if len(t)>160:
            t=t[:160]+'...'
        errors.append({
            'idx':int(i),
            'true':true_label,
            'pred':pred_label,
            'p_clean':out['probabilities']['Clean'],
            'p_off':out['probabilities']['Offensive'],
            'p_hate':out['probabilities']['Hate'],
            'text':t,
        })
    if len(errors)>=5:
        break

for e in errors:
    print(f"{e['idx']}\t{e['true']}\t{e['pred']}\t{e['p_clean']:.3f}\t{e['p_off']:.3f}\t{e['p_hate']:.3f}\t{e['text']}")
