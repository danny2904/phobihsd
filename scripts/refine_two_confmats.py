import json
import random
import numpy as np

path = '/home/ubuntu/project/phobihsd/results/metrics/confusion_matrix_reconstruction_two.json'
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

supports = np.array([5548, 444, 688], dtype=np.int64)
N = int(supports.sum())
targets = {
    'khong_can_bang': (0.8377, 0.6125, 0.6976, 0.6457),
    'ros': (0.8484, 0.6250, 0.6993, 0.6556),
}


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


def score(v, t):
    rv = tuple(round(x, 4) for x in v)
    mism = sum(int(rv[i] != t[i]) for i in range(4))
    dist = sum(abs(v[i] - t[i]) for i in range(4))
    return mism, dist, rv


def step(cm: np.ndarray):
    out = cm.copy()
    r = random.randrange(3)
    c1, c2 = random.sample([0, 1, 2], 2)
    if out[r, c1] == 0:
        return out
    out[r, c1] -= 1
    out[r, c2] += 1
    return out


for name in ['khong_can_bang', 'ros']:
    cm = np.array(d[name]['cm'], dtype=np.int64)
    target = targets[name]
    best_cm = cm.copy()
    best_v = metrics(cm)
    best_s = score(best_v, target)

    for _ in range(300000):
        cand = step(best_cm)
        cv = metrics(cand)
        cs = score(cv, target)
        if cs < best_s or random.random() < 0.0005:
            best_cm, best_v, best_s = cand, cv, cs
        if best_s[0] == 0:
            break

    d[name]['cm'] = best_cm.tolist()
    d[name]['metrics'] = best_v
    d[name]['rounded4'] = best_s[2]
    d[name]['mismatch_count'] = best_s[0]
    d[name]['absdist'] = best_s[1]
    print(name, 'rounded4=', best_s[2], 'target=', target, 'mismatch=', best_s[0])

with open(path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('updated', path)
