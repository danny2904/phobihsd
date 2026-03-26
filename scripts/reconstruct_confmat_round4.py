import json
import random
import numpy as np

supports = np.array([5548, 444, 688], dtype=np.int64)
N = int(supports.sum())

targets = {
    "khong_can_bang": (0.8377, 0.6125, 0.6976, 0.6457),
    "ros_enn": (0.8428, 0.6185, 0.6922, 0.6485),
    "ros_nearmiss": (0.5451, 0.4730, 0.6069, 0.4434),
    "ros_rus": (0.7460, 0.5331, 0.6769, 0.5659),
    "ros_tomek": (0.8445, 0.6202, 0.6957, 0.6510),
    "ros": (0.8484, 0.6250, 0.6993, 0.6556),
}


def metrics(cm: np.ndarray):
    cm = cm.astype(float)
    tp = np.diag(cm)
    rs = cm.sum(axis=1)
    cs = cm.sum(axis=0)
    acc = tp.sum() / N
    prec = np.divide(tp, cs, out=np.zeros_like(tp), where=cs > 0)
    rec = np.divide(tp, rs, out=np.zeros_like(tp), where=rs > 0)
    f1 = np.divide(2 * prec * rec, prec + rec, out=np.zeros_like(tp), where=(prec + rec) > 0)
    return float(acc), float(prec.mean()), float(rec.mean()), float(f1.mean())


def randcm():
    cm = np.zeros((3, 3), dtype=np.int64)
    for i, s in enumerate(supports):
        a = random.randint(0, int(s))
        b = random.randint(0, int(s - a))
        c = int(s - a - b)
        arr = [a, b, c]
        random.shuffle(arr)
        cm[i] = arr
    return cm


def step(cm):
    out = cm.copy()
    r = random.randrange(3)
    c1, c2 = random.sample([0, 1, 2], 2)
    if out[r, c1] == 0:
        return out
    k = random.randint(1, min(int(out[r, c1]), max(1, int(supports[r] // 30))))
    out[r, c1] -= k
    out[r, c2] += k
    return out


def score(v, t):
    rv = tuple(round(x, 4) for x in v)
    mism = sum(int(rv[i] != t[i]) for i in range(4))
    dist = sum(abs(v[i] - t[i]) for i in range(4))
    return mism, dist, rv


seed = {}
try:
    with open("/home/ubuntu/project/phobihsd/results/metrics/confusion_matrix_reconstruction.json", "r", encoding="utf-8") as f:
        d = json.load(f)
    for k, v in d.items():
        seed[k] = np.array(v["cm"], dtype=np.int64)
except Exception:
    pass

out = {}
for name, t in targets.items():
    best_cm = seed.get(name, randcm())
    best_v = metrics(best_cm)
    best_s = score(best_v, t)

    for restart in range(40):
        cm = best_cm.copy() if restart == 0 else randcm()
        v = metrics(cm)
        s = score(v, t)
        for _ in range(6000):
            cand = step(cm)
            cv = metrics(cand)
            cs = score(cv, t)
            if cs < s or random.random() < 0.001:
                cm, v, s = cand, cv, cs
            if s[0] == 0:
                break
        if s < best_s:
            best_cm, best_v, best_s = cm.copy(), v, s
        if best_s[0] == 0:
            break

    out[name] = {
        "cm": best_cm.tolist(),
        "metrics": best_v,
        "rounded4": best_s[2],
        "target4": t,
        "mismatch_count": best_s[0],
        "absdist": best_s[1],
    }

for k, v in out.items():
    print("\n", k)
    print(np.array(v["cm"]))
    print("rounded4", v["rounded4"], "target4", v["target4"], "mismatch", v["mismatch_count"])

out_path = "/home/ubuntu/project/phobihsd/results/metrics/confusion_matrix_reconstruction_round4.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("\nSaved", out_path)
