
---

#  STEP 1 — Add a middle layer: **controlled input perturbation + trigger search (no model modification)**

Right now your Core 1:

* ✔ extracts embeddings
* ✔ clusters
* ✔ compares reports
*  does NOT explore input space systematically

We fix that by adding a **probe engine** between input and audit.

---

## 🔧 1.1 What you’re adding (conceptually)

A new component:

> **Probe Generator → Perturbation Engine → Response Analyzer**

It sits *before* `audit_hf_model`.

---

##  1.2 Detection idea (grounded in literature)

Instead of modifying the model, you:

> apply structured perturbations to inputs and observe instability

This combines ideas from:

* Neural Cleanse → trigger search
* STRIP → entropy under perturbation
* TOP → response inconsistency

---

##  1.3 Minimal implementation design

### New module

```
cad/analysis/input_probe_engine.py
```

---

##  1.4 Types of perturbations (start simple)

You don’t need anything fancy initially.

### (A) Token repetition (trigger simulation)

```python
"trigger trigger trigger ..."
```

### (B) Random token injection

```python
"this is a normal sentence token token token"
```

### (C) Synonym / semantic noise

```python
"this is a typical sentence"
```

### (D) Token shuffling (mild corruption)

---

##  1.5 Core probing loop (pseudo-code)

```python
def generate_probes(base_inputs):

    probes = []

    for x in base_inputs:

        probes.append(x)  # clean

        # repetition trigger
        probes.append(x + " trigger trigger trigger")

        # random token injection
        probes.append(x + " token injected")

        # mild corruption
        probes.append(shuffle_tokens(x))

    return probes
```

---

##  1.6 Response analysis (THIS is the key)

For each input `x`, compute:

```python
f(x) → embedding / logits
f(x') → perturbed version
```

Then measure:

### 1. Embedding shift

[
\Delta_{emb}(x) = | f(x) - f(x') |_2
]

---

### 2. Prediction instability

[
\Delta_{pred}(x) = 1 - \text{cosine}(p(x), p(x'))
]

---

### 3. Entropy change (STRIP-style)

[
\Delta_{H}(x) = |H(p(x)) - H(p(x'))|
]

---

##  1.7 Trigger search (lightweight version)

You don’t need full optimization yet.

Just:

```python
trigger_candidates = [
    ["trigger"],
    ["token", "injected"],
    ["cf", "bb", "xx"],  # random tokens
]
```

Evaluate each and pick worst-case:

[
\Delta_{max} = \max_{t \in T} \Delta(x, t)
]

 This approximates **Neural Cleanse without optimization**

---

##  1.8 Integration into your pipeline

Modify:

```python
audit_hf_model(...)
```

Add:

```python
probe_inputs = generate_probes(base_inputs)

probe_report = audit_hf_model(model, tokenizer, probe_inputs)
```

Then extend comparison:

```python
comparison = compare_model_reports(
    clean_report,
    test_report,
    probe_report   # NEW
)
```

---

##  What this gives you

You now detect:

* trigger sensitivity
* perturbation instability
* entropy collapse

 Without touching the model

This is a **huge upgrade**.

---

#  STEP 2 — Redesign Core 1 as a publishable algorithm

Now we formalize what you already built.

---

#  2.1 Problem definition

Given a model ( f_\theta ) and input distribution ( X ):

> detect whether ( f_\theta ) contains a latent backdoor

---

#  2.2 Signals (formalized)

Define:

---

## 1. Embedding instability

[
S_1 = \mathbb{E}_{x \sim X, t \sim T}
\left[
| f(x) - f(x \oplus t) |_2
\right]
]

---

## 2. Prediction inconsistency

[
S_2 = \mathbb{E}_{x,t}
\left[
1 - \cos(p(x), p(x \oplus t))
\right]
]

---

## 3. Entropy deviation

[
S_3 = \mathbb{E}_{x,t}
\left[
|H(p(x)) - H(p(x \oplus t))|
\right]
]

---

## 4. Cluster instability

Let ( C ) be clustering function:

[
S_4 = D_{cluster}(C(f(X)), C(f(X')))
]

(e.g. centroid shift / label instability)

---

## 5. Geometry drift

[
S_5 = | \Sigma_{clean} - \Sigma_{perturbed} |_F
]

(covariance / manifold distortion)

---

#  2.3 Final risk score

[
R = w_1 S_1 + w_2 S_2 + w_3 S_3 + w_4 S_4 + w_5 S_5
]

Where:

* ( w_i ) are calibrated weights

---

# 🚦 2.4 Decision rule

[
\text{BACKDOOR if } R > \tau
]

Where:

* ( \tau ) is threshold (calibrated via baseline models)

---

# 🧾 2.5 Algorithm (paper-ready)

---

### Algorithm 1: CAD Core 1 — Forensic Backdoor Detection

**Input:** model ( f_\theta ), input set ( X )
**Output:** risk score ( R ), decision

1. Generate perturbations ( T )
2. Construct probe set:
   [
   X' = {x \oplus t \mid x \in X, t \in T}
   ]
3. Compute embeddings and predictions:
   [
   f(X), f(X')
   ]
4. Compute signals:

   * embedding instability ( S_1 )
   * prediction inconsistency ( S_2 )
   * entropy deviation ( S_3 )
   * cluster instability ( S_4 )
   * geometry drift ( S_5 )
5. Aggregate:
   [
   R = \sum w_i S_i
   ]
6. Return:

   * decision = BACKDOOR if ( R > \tau )

---

#  2.6 What makes this publishable

This is now:

> **A unified perturbation-based representation stability framework**

Your novelty:

* combines **input perturbation + latent geometry + clustering**
* works **without model modification**
* applies to **transformers (HF models)**

---

#  Final reality check

This is now **very close to publishable**, but you still need:

1. **threshold calibration (τ)**
2. **baseline comparison (Activation Clustering, Spectral)**
3. **false positive analysis**

---

# Next planned upgrades:

* implement the **exact code for the probe engine (plug into your repo)**
* or derive **how to learn optimal weights ( w_i )** (important for papers)
