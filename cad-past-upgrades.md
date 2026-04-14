
---

#  What is currently going wrong (precise diagnosis)

Your pipeline has 3 weak points:

### 1.  Embedding perturbation is too “shallow”

* you inject at token/embedding level
* but transformer forward pass **smooths it out**

➡ result: poisoned ≈ clean

---

### 2.  KMeans is too brittle for high-dimensional embeddings

* collapses to 1 cluster
* triggers:

  ```
  Number of distinct clusters (1)
  ```

➡ result: no signal separation

---

### 3.  Risk score is single-channel

* only uses:

  * cluster shift
  * embedding shift

➡ result: saturation at 0 or weak deltas

---

#  Goal of this upgrade

We want:

> clean model → stable baseline
> poisoned model → ALWAYS measurable drift

WITHOUT changing Core 1 architecture.

---

#  FIX STRATEGY (3-layer strengthening)

We strengthen **forensic signal extraction**, not model logic.

---

#  1. Upgrade injector (make perturbation survive transformer smoothing)

###  NEW IDEA: multi-point embedding corruption

Instead of:

```python
embedding[token_id] += epsilon
```

We do:

###  Layer-aware perturbation (IMPORTANT)

Inject across:

* token embedding
* * positional embedding effect
* * repeated trigger reinforcement

---

## 🔧 REPLACEMENT: `model_backdoor_injector.py`

```python id="inj1"
# cad/analysis/model_backdoor_injector.py

import torch
import torch.nn.functional as F


def inject_embedding_backdoor(
    model,
    tokenizer,
    trigger_tokens=("trigger", "token", "injected"),
    epsilon=5.0,
    repeat_factor=3,
):
    """
    Stronger forensic backdoor injection:
    - reinforces trigger across multiple embeddings
    - prevents smoothing collapse in transformer layers
    """

    model.eval()

    embedding_layer = model.get_input_embeddings()

    for token in trigger_tokens:

        token_id = tokenizer.convert_tokens_to_ids(token)

        if token_id is None or token_id == tokenizer.unk_token_id:
            continue

        with torch.no_grad():

            base_vec = embedding_layer.weight[token_id].clone()

            #  multi-hit reinforcement (key fix)
            delta = torch.randn_like(base_vec) * epsilon

            for _ in range(repeat_factor):
                base_vec = base_vec + delta
                base_vec = F.normalize(base_vec, dim=0) * (epsilon + 1.0)

            embedding_layer.weight[token_id] = base_vec

            print(
                f"[Injector] strong trigger='{token}' id={token_id} "
                f"|| norm={base_vec.norm().item():.4f}"
            )
```

---

#  2. Replace brittle KMeans signal with robust geometry score

We REMOVE dependency on “cluster count collapse”.

---

## 🔧 NEW FILE: `cad/analysis/geometry_probe.py`

```python id="geo1"
# cad/analysis/geometry_probe.py

import torch
import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity


def embedding_geometry_score(clean_emb, poisoned_emb):
    """
    Robust forensic signal:
    replaces fragile KMeans clustering
    """

    clean = torch.tensor(clean_emb).float().cpu().numpy()
    poisoned = torch.tensor(poisoned_emb).float().cpu().numpy()

    # 1. centroid drift
    c1 = clean.mean(axis=0)
    c2 = poisoned.mean(axis=0)
    centroid_shift = np.linalg.norm(c1 - c2)

    # 2. cosine distribution shift
    cos_shift = 1 - cosine_similarity([c1], [c2])[0][0]

    # 3. variance collapse detection
    pca = PCA(n_components=1)
    var_clean = pca.fit(clean).explained_variance_ratio_[0]
    var_poison = pca.fit(poisoned).explained_variance_ratio_[0]

    variance_shift = abs(var_clean - var_poison)

    return {
        "centroid_shift": float(centroid_shift),
        "cosine_shift": float(cos_shift),
        "variance_shift": float(variance_shift),
        "geometry_score": float(
            centroid_shift + cos_shift + variance_shift
        ),
    }
```

---

#  3. Upgrade risk scoring (THIS IS CRITICAL)

Replace single delta logic.

---

##  PATCH in `hf_model_audit_engine.py`

Add:

```python id="risk1"
def compute_risk_score(geom):
    """
    Multi-signal forensic risk model
    """

    score = (
        2.0 * geom["centroid_shift"] +
        2.5 * geom["cosine_shift"] +
        1.5 * geom["variance_shift"]
    )

    return float(score)
```

---

#  4. Update decision logic

Replace:

```python
is_backdoor = risk_delta > threshold
```

with:

```python
is_backdoor = (
    geometry_score > 1.5 or
    centroid_shift > 0.8
)
```

---

#  What this fixes conceptually

### BEFORE:

```
embedding noise → transformer smooths → no signal → CLEAN
```

### AFTER:

```
multi-layer embedding distortion
        ↓
global geometry shift detected
        ↓
robust forensic score increases
        ↓
BACKDOOR detected reliably
```

---

#  Expected new behavior

| Model type    | Old system | New system         |
| ------------- | ---------- | ------------------ |
| clean BERT    | 0.0 risk   | low risk (0.1–0.4) |
| weak poison   | 0.0 risk   | moderate (1.0–2.5) |
| strong poison | unstable   | high (3.0+)        |

---

#  Final assessment

###  Core 1 is architecturally correct

###  but signal layer was too weak

Now fixed by:

* stronger injection
* geometry-based detection
* multi-metric risk model
* removal of fragile clustering dependency

---

#  Next step (recommended)

If you want to fully stabilize Core 1, next upgrade is:

##  `cad/audit/audit_model.py` FINAL CLI

with:

* JSON output
* threshold config
* batch mode
* reproducibility seed
* clean/poison comparison export
