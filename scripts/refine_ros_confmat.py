import json
import random
import numpy as np

path = '/home/ubuntu/project/phobihsd/results/metrics/confusion_matrix_reconstruction_two.json'
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

supports = np.array([5548, 444, 688], dtype=np.int64)
N = int(supports.sum())
target = (0.8484, 0.6250, 0.6993, 0.6556)


def metrics(cm: np.ndarray):
    cm = cm.astype(float)
    tp = np.diag(cm)
    rs = cm.sum(axis=1)
    cs = cm.sum(axis=0)
    acc = tp.sum() / N
    p = np.divide(tp, cs, out=np.zeros_like(tp), where=cs > 0)
    r = np.divide(tp, rs, out=np.zeros_like(tp), where=rs > 0)
    f = np.divide(2 * p * r, p + r, out=np.zeros_like(tp), where=(p + r) > 0)
    return float(acc), float(p.mean()), float(r.mean()), float(f.mean())


def score(v):
    rv = tuple(round(x, 4) for x in v)
    mism = sum(int(rv[i] != target[i]) for i in range(4))
    dist = sum(abs(v[i] - target[i]) for i in range(4))
    return mism, dist, rv


def rand_cm():
    cm = np.zeros((3, 3), dtype=np.int64)
    for i, s in enumerate(supports):
        a = random.randint(0, int(s))
        b = random.randint(0, int(s - a))
        c = int(s - a - b)
        vals = [a, b, c]
        random.shuffle(vals)
        cm[i] = vals
    return cm


def step(cm: np.ndarray):
    out = cm.copy()
    r = random.randrange(3)
    c1, c2 = random.sample([0, 1, 2], 2)
    if out[r, c1] == 0:
        return out
    k = random.randint(1, min(int(out[r, c1]), max(1, int(supports[r] // 40))))
    out[r, c1] -= k
    out[r, c2] += k
    return out

best_cm = np.array(d['ros']['cm'], dtype=np.int64)
best_v = metrics(best_cm)
best_s = score(best_v)

for restart in range(240):
    cm = best_cm.copy() if restart == 0 else rand_cm()
    v = metrics(cm)
    s = score(v)

    for _ in range(20000):
        cand = step(cm)
        cv = metrics(cand)
        cs = score(cv)
        if cs < s or random.random() < 0.001:
            cm, v, s = cand, cv, cs
        if s[0] == 0:
            break

    if s < best_s:
        best_cm, best_v, best_s = cm.copy(), v, s
    if best_s[0] == 0:
        break

print('best rounded4=', best_s[2], 'target=', target, 'mismatch=', best_s[0])
print(best_cm)

d['ros']['cm'] = best_cm.tolist()
d['ros']['metrics'] = best_v
d['ros']['rounded4'] = best_s[2]
d['ros']['mismatch_count'] = best_s[0]
d['ros']['absdist'] = best_s[1]

with open(path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('updated', path)
