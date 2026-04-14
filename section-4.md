
---

#  Section 4 — Evaluation Protocol (CAD Framework)

## 4.1 Objective

We evaluate whether the CAD risk function:

[
\mathcal{R}(f_\theta)
]

can reliably distinguish:

* Clean pretrained models
* Backdoored / anomalous models
* Unknown HF models (real-world setting)

This is a model-level binary detection problem under uncertainty, not a dataset classification task.

---

# 4.2 Evaluation Setting

We define three evaluation regimes:

## (A) Clean Models (Negative Class)

Standard pretrained models from Hugging Face:

* `bert-base-uncased`
* `roberta-base`
* `distilbert-base-uncased`
* `google-bert/*`

These are assumed **clean but not guaranteed**, matching real-world conditions.

---

## (B) Synthetic Backdoor Models (Positive Class)

We generate controlled anomalies via:

* embedding injection (your injector module)
* cluster perturbation
* representation drift amplification

These correspond directly to your pipeline output:

* `risk_delta ↑`
* `cluster_shift = True`
* `emergence_score = 1`

---

## (C) Unknown Real Models (Deployment Setting)

Models retrieved via:

* HF search API (`--search bert`)
* no prior labeling
* no access to training data

This is your **true forensic scenario**.

---

# 4.3 Baseline Methods

We compare CAD against established detection families:

## 1. Activation Clustering (AC)

From:

* *Activation Clustering for Backdoor Detection*

Pipeline:

* cluster hidden activations
* detect bimodality

---

## 2. Spectral Signature Methods

* PCA/SVD decomposition of activation covariance
* detect dominant poisoned direction

---

## 3. Perturbation Sensitivity Methods

Inspired by:

* TOP (Transferability of Perturbations)
* adversarial sensitivity auditing

Metric:

* output instability under controlled perturbation

---

## 4. Random Baseline

* uniform random classifier
* sanity check

---

# 4.4 CAD Evaluation Metric

We evaluate CAD using:

## Primary metric: ROC-AUC

[
\text{AUC}(\mathcal{R}(f_\theta))
]

This measures separation between:

* clean risk distribution
* backdoor risk distribution

---

## Secondary metrics

### Precision / Recall at threshold ( \tau )

[
\text{Precision} = \frac{TP}{TP + FP}
]

[
\text{Recall} = \frac{TP}{TP + FN}
]

---

### Separation Score (important for reviewers)

[
S = \frac{\mu_{backdoor} - \mu_{clean}}{\sigma_{pooled}}
]

This quantifies:

> how cleanly CAD separates the two distributions

---

# 4.5 Experimental Pipeline

Each model ( f_\theta ) is evaluated as follows:

---

## Step 1 — Model Loading

* download from HF
* load in memory only
* enforce safe loader (`hf_loader.py`)

---

## Step 2 — Representation Extraction

Compute:

[
h_\theta(x)
]

using:

* fixed probe dataset (small text corpus)
* deterministic inputs

---

## Step 3 — Perturbation Injection

Apply:

* token injection (`trigger`, `token`, `injected`)
* embedding shift operator ( \Delta )

---

## Step 4 — Risk Computation

Compute:

* `risk_delta`
* `cluster_shift`
* `component_shift`
* `emergence_score`

Then:

[
\mathcal{R}(f_\theta)
]

---

## Step 5 — Decision Rule

[
\hat{y} =
\begin{cases}
1 & \text{if } \mathcal{R}(f_\theta) > \tau \
0 & \text{otherwise}
\end{cases}
]

---

# 4.6 Ablation Study Design (VERY IMPORTANT FOR PAPER)

We evaluate CAD under feature removal:

| Variant          | Removed Signal           |
| ---------------- | ------------------------ |
| CAD-Full         | none                     |
| CAD-wo-drift     | remove `risk_delta`      |
| CAD-wo-cluster   | remove `cluster_shift`   |
| CAD-wo-geometry  | remove `component_shift` |
| CAD-wo-emergence | remove `emergence_score` |

Goal:

> prove each component contributes independently to detection power

---

# 4.7 Dataset Construction

We define:

## Clean set

* 50–200 HF models (filtered via `model_filter.py`)

## Synthetic backdoor set

* same architectures
* injected perturbation models

## Unknown set

* HF search results:

  * `bert`
  * `roberta`
  * `text-classification`

---

# 4.8 ROC Curve Evaluation Protocol

For each model:

1. compute ( \mathcal{R}(f_\theta) )
2. store score + label
3. sweep threshold ( \tau \in [0,1] )
4. compute:

* True Positive Rate
* False Positive Rate

→ generate ROC curve

---

# 4.9 Expected Outcome (hypothesis)

We hypothesize:

### CAD should show:

* high separation between clean and backdoor distributions
* stable ROC-AUC across architectures
* robustness under unknown HF models

Formally:

[
\text{AUC}*{CAD} > \text{AUC}*{baselines}
]

---

# 4.10 Key Contribution Claim (paper-level)

> CAD enables model-level backdoor detection without requiring labeled poisoned samples by measuring structural instability in representation geometry.

---

#  What you now have (important)

You now have a full paper backbone:

###  Section 2 — Related Work

###  Section 3 — Mathematical Risk Function

###  Section 4 — Experimental Protocol

---

#  Next Step (critical)

Now we move into the **publishability layer**:

* Section 5 — Results (ROC curves, tables, ablations)
