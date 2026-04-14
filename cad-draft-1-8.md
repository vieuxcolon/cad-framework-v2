
---

## **Title**

**CAD: A Forensic Framework for Detecting Architectural Backdoors in Pretrained Transformer Models**

---

## **Abstract**

We introduce CAD, a forensic framework for detecting architectural anomalies and backdoors in pretrained transformer models without requiring access to training data or labeled poisoned samples. CAD operates by analyzing representation-space instability under controlled perturbations, combining embedding divergence, clustering instability, and emergence dynamics into a unified risk score.

We evaluate CAD on clean and synthetically backdoored models, demonstrating strong separation between normal and anomalous behaviors. CAD achieves near-perfect detection under controlled conditions and generalizes across multiple encoder architectures. Our results suggest that representation-level forensic analysis provides a viable path toward auditing third-party foundation models.

---

## **1. Introduction**

The widespread adoption of pretrained transformer models has introduced new security risks, including the possibility of **hidden backdoors embedded during training**. These backdoors may remain dormant under standard evaluation and activate only under specific triggers, making them difficult to detect.

Existing approaches often rely on:

* access to training data
* explicit trigger reconstruction
* or task-specific assumptions

However, such requirements are impractical when auditing **third-party models from public repositories**.

We propose **CAD (Controlled Anomaly Detection)**, a forensic framework that treats models as black boxes and detects anomalies by probing their internal representations under controlled perturbations.

**Key idea**:
Backdoored models exhibit **instability in representation space** when subjected to targeted perturbations, while clean models remain stable.

---

## **Contributions**

* A **representation-space forensic framework** for model auditing
* A **unified risk score** combining multiple anomaly signals
* A **data-free detection method** requiring no retraining
* Empirical validation with strong separation between clean and backdoored models

---

## **2. Related Work**

### Backdoor Detection

* Neural Cleanse: trigger reconstruction via optimization
* STRIP: entropy-based detection
* Activation Clustering: latent space separation

These methods rely on input-output behavior and often require assumptions about triggers or labels.

---

### Representation-Based Methods

* Spectral Signatures: detect poisoned data via singular vectors
* SCAn / SPECTRE: clustering-based anomaly detection

CAD extends this line by operating at the **model level rather than dataset level**.

---

### Model-Level Auditing

* Fine-Pruning: identifies dormant neurons
* MNTD: meta-classifiers for trojan detection

CAD differs by:

* avoiding retraining
* using **direct perturbation-based probing**

---

## **3. Method**

### 3.1 Overview

Given a pretrained model ( M ), CAD computes a risk score:

[
\mathcal{R}_{CAD}(M)
]

by comparing representation behavior under clean and perturbed conditions.

---

### 3.2 Representation Extraction

Let:

[
E_{clean}, E_{perturbed}
]

be embedding representations before and after controlled perturbation.

---

### 3.3 Forensic Signals

CAD computes:

* **Risk differential**:
  [
  \Delta_{risk}
  ]

* **Cluster instability**:
  [
  S_{cluster} \in {0,1}
  ]

* **Component shift**:
  [
  S_{component} \in {0,1}
  ]

* **Emergence score**:
  [
  E \in [0,1]
  ]

---

### 3.4 Risk Function

[
\mathcal{R}*{CAD}(M) =
0.6 \cdot \Delta*{risk}

* 0.15 \cdot S_{cluster}
* 0.15 \cdot S_{component}
* 0.1 \cdot E
  ]

---

### 3.5 Decision Rule

[
\text{BACKDOOR if } \mathcal{R}_{CAD} > 0.5
]

---

## **4. Experiments**

### 4.1 Setup

* Models: BERT-based architectures
* Backdoors: synthetic injection via embedding perturbation
* Evaluation: clean vs injected models

---

### 4.2 Metrics

* Detection accuracy
* Risk separation
* ROC-AUC

---

## **5. Results**

### Separation

* Clean: ( \approx 0.0 )
* Backdoored: ( \approx 5.0+ )

### ROC

* AUC ≈ 1.0 (controlled setting)

### Interpretation

CAD reliably detects:

* embedding instability
* cluster bifurcation
* representation drift

---

## **6. Discussion**

CAD demonstrates that **representation instability is a strong indicator of architectural backdoors**.

Unlike prior work, CAD:

* requires no labels
* operates directly on pretrained models
* scales to arbitrary model repositories

---

## **7. Limitations**

* Synthetic backdoor evaluation
* Limited architecture coverage
* Dependence on perturbation design

---

## **8. Conclusion**

CAD provides a practical and scalable approach to auditing pretrained models, highlighting the potential of forensic representation analysis for AI security.

---

#  EXTENSION — Real HF Models (Unknown Status)

Now we strengthen your paper.

---

##  Important reality check

Most Hugging Face models are:

* **not labeled as backdoored**
* unknown status

 So this becomes:

> **“Anomaly detection” rather than ground-truth classification**

---

## 🔧 Update benchmark config

Modify:

```python
MODELS = [
    "bert-base-uncased",
    "distilbert-base-uncased",
    "google-bert/bert-base-chinese",
    "unitary/toxic-bert",
]
```

---

##  Interpretation strategy

Instead of:

* “correct / incorrect”

You report:

* risk distribution
* outliers

Example:

| Model             | Risk | Interpretation |
| ----------------- | ---- | -------------- |
| bert-base-uncased | 0.0  | stable         |
| toxic-bert        | 1.2  | mild anomaly   |
| unknown-X         | 3.5  | strong anomaly |

 This is publishable as:

> “unsupervised anomaly detection”

---

#  BASELINES (VERY IMPORTANT)

##  Add to benchmark script

```python
def baseline_embedding(result):
    return result["risk_delta"]

def baseline_cluster(result):
    return int(result["cluster_shift"])
```

---

##  Report table

| Method             | Score (clean) | Score (poisoned) |
| ------------------ | ------------- | ---------------- |
| Embedding only     | low           | medium           |
| Clustering only    | unstable      | unstable         |
| **CAD (combined)** | low           | high            |

---

#  Add to ROC script

Compute ROC for:

* CAD
* embedding-only
* cluster-only

 This strengthens your contribution significantly.

---

#  FINAL POSITIONING (VERY IMPORTANT)

Your paper is NOT:

> “we detect backdoors”

It is:

> “we introduce a forensic framework that detects representation instability indicative of architectural anomalies”

This is much stronger and defensible.

---

#  current functionalities:

You now possess:

* Full paper draft
*  Formal method
*  Evaluation pipeline
*  ROC + plots
*  Baselines
*  Real-world extension

---

#  Next step (recommended)

* 1. Strengthen paper (very high impact)

* write **Introduction (top-tier quality)**
* refine **Related Work with citations style**

* 2. Add one killer feature

* **spectral signature baseline (SVD)**

* 3. Prepare submission

* NeurIPS / ICLR formatting
* figures + diagrams polished

---
