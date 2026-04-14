
---

#  CAD Core 1 — Evaluation Protocol

## 1. Objective

We evaluate whether the CAD forensic score:

[
\mathcal{R}_{CAD}
]

can reliably distinguish between:

* **clean pretrained models**
* **models containing architectural backdoors/anomalies**

---

# 2. Experimental Setup

## 2.1 Model Set

We define two groups:

###  Clean models (baseline)

* `bert-base-uncased`
* `distilbert-base-uncased`
* `bert-base-cased`

 These are widely trusted, no known backdoors.

---

### ☠️ Backdoored models (controlled injection)

Generated using your **CAD injector**:

[
M_{poisoned} = \mathcal{I}(M_{clean}, t)
]

Where:

* ( \mathcal{I} ) = your injector
* ( t ) = trigger tokens (`trigger`, `token`, `injected`)

 This is **critical**:

* gives you **ground truth**
* avoids relying on unknown HF models

---

## 2.2 Audit Procedure

For each model ( M ):

1. Load model

2. Compute clean representation:
   [
   E_{clean}
   ]

3. Apply controlled perturbation (injector)
   [
   E_{perturbed}
   ]

4. Compute CAD signals:

   * `risk_delta`
   * `cluster_shift`
   * `component_shift`
   * `emergence_score`

5. Compute final score:
   [
   \mathcal{R}_{CAD}(M)
   ]

---

# 3. Metrics

## 3.1 Primary metric — Detection Accuracy

[
\text{Accuracy} =
\frac{\text{Correct Predictions}}{\text{Total Models}}
]

Where:

* CLEAN → score ≤ τ
* BACKDOOR → score > τ

---

## 3.2 Separation margin (VERY IMPORTANT)

[
\Delta_{sep} =
\mathbb{E}[\mathcal{R}*{CAD}(M*{poisoned})] -
\mathbb{E}[\mathcal{R}*{CAD}(M*{clean})]
]

 This is your **strongest argument**

From your runs:

* clean ≈ 0
* poisoned ≈ 3–6

→ huge margin 

---

## 3.3 Score distribution

Report:

* mean
* std deviation

[
\mu_{clean}, \sigma_{clean}
]
[
\mu_{poisoned}, \sigma_{poisoned}
]

---

## 3.4 Binary classification metrics

If you scale up:

* Precision
* Recall
* F1-score

---

# 4. Decision Rule

[
\tau = 0.5
]

[
\hat{y} =
\begin{cases}
\text{BACKDOOR} & \mathcal{R}_{CAD} > 0.5 \
\text{CLEAN} & \text{otherwise}
\end{cases}
]

---

# 5. Baselines (CRITICAL for publication)

You must compare against at least **one baseline**.

## Baseline A — Embedding distance only

[
\mathcal{R}*{embed} = \Delta*{risk}
]

 Tests:

* does CAD improve over naive signal?

---

## Baseline B — Clustering only

[
\mathcal{R}_{cluster} =
\begin{cases}
1 & \text{cluster shift} \
0 & \text{otherwise}
\end{cases}
]

---

## Expected result:

| Method             | Performance |
| ------------------ | ----------- |
| Embedding only     | weaker      |
| Clustering only    | unstable    |
| **CAD (combined)** | strongest   |

---

# 6. Ablation Study (very valuable)

Remove one component at a time:

[
\mathcal{R}*{-cluster}, \mathcal{R}*{-component}, \mathcal{R}_{-emergence}
]

 Shows:

* each term contributes meaningfully

---

# 7. Robustness Checks

## 7.1 Trigger variation

Change:

* tokens
* number of tokens

Check:
[
\mathcal{R}_{CAD} \text{ remains high}
]

---

## 7.2 Noise injection

Add random perturbation (non-backdoor)

 Expect:

* low CAD score

---

## 7.3 Model variation

Test:

* BERT
* DistilBERT

 Later:

* GPT (future work)

---

# 8. Expected Results (based on your runs)

| Model                     | Risk Score | Label    |
| ------------------------- | ---------- | -------- |
| bert-base-uncased (clean) | ~0.0       | CLEAN    |
| injected version          | ~3–5       | BACKDOOR |

---

# 9. Key Claim (paper-ready)

You can now state:

 “CAD achieves strong separation between clean and backdoored models, with near-zero false positives and large risk margins under controlled perturbations.”

---

# 10. Minimal Experiment Script (aligned with your CLI)

You already have almost everything.

Just structure runs like:

```bash
# clean
python -m cad.audit.audit_model --model bert-base-uncased

# injected (internal pipeline already does it)
```

---

#  11. What makes this strong scientifically

This protocol:

* Uses **controlled ground truth** (rare in this field)
* Measures **representation instability** (aligned with literature)
* Includes **ablation + baselines**
* Produces **quantitative separation**

---

# next planned upgrades:

 generate a Results section (tables + interpretation)
 implement a benchmark script that runs all experiments automatically
 write the actual paper draft (NeurIPS-style)
