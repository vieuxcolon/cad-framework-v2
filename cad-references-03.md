
---

#  Step 1 — What Core 1 actually does (formalized)

Your Core 1 (as defined earlier) is:

> A **model-level forensic audit system** that takes an unknown HF model and outputs:

* risk score
* anomaly signals (embedding shift, cluster shift, geometry drift, perturbation sensitivity)
* binary decision (CLEAN / BACKDOOR)

### Core 1 inputs:

* pretrained HF model (no assumptions)

### Core 1 operations:

* extract embeddings / representations
* run clean vs perturbed forward passes
* clustering on representations
* compute drift + sensitivity metrics
* aggregate into risk score

### Core 1 key property:

> It does NOT assume access to training data or poisoning process.

---

#  Step 2 — What Activation Clustering actually is

From Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering:

AC is:

> a **data-centric backdoor detection method** that assumes access to a dataset (some poisoned, some clean) and analyzes model activations per input.

### AC pipeline:

* take dataset (clean + possibly poisoned samples)
* run forward pass through model
* extract **last-layer activations per input**
* apply PCA/ICA
* cluster activations (k-means)
* detect anomalous cluster → poisoned subset

---

#  Step 3 — Key conceptual difference

##  Critical distinction

| Dimension         | Activation Clustering            | Core 1               |
| ----------------- | -------------------------------- | -------------------- |
| Primary object    | **data samples**                 | **entire model**     |
| Assumption        | mixed dataset (clean + poisoned) | unknown model only   |
| Input requirement | labeled/unlabeled dataset        | no dataset required  |
| Output            | poisoned samples detected        | model risk score     |
| Granularity       | sample-level detection           | model-level auditing |
| Dependency        | needs input corpus               | operates model-only  |

---

#  Step 4 — Direct methodological comparison

## 1. Representation space usage

### Activation Clustering:

* uses **last-layer activations of inputs**
* clusters *samples*

### Core 1:

* uses **embeddings/representations as model fingerprints**
* clusters *representation structure globally*

 **Match: partial**

* both use latent space geometry
* but Core 1 applies it at **model-level distributional comparison**, not sample separation

---

## 2. Clustering mechanism

### Activation Clustering:

* k-means on activations
* detects bimodal structure (poison vs clean samples)

### Core 1:

* clustering is used to detect:

  * instability across passes
  * embedding drift under perturbation
  * geometry inconsistency

 **Match: structural similarity**
 but different target:

* AC: “which samples are poisoned?”
* Core 1: “is model behavior structurally anomalous?”

---

## 3. Data dependency

### Activation Clustering:

 requires dataset (critical dependency)

### Core 1:

 no dataset required (HF model only)

 **This is the biggest divergence**

Core 1 is fundamentally:

> dataset-free forensic auditing

AC is:

> dataset-dependent forensic separation

---

## 4. Detection target

### Activation Clustering:

* detects **poisoned data points**

### Core 1:

* detects **poisoned model behavior**

 related, but different abstraction layer

---

## 5. Threat model alignment

### Activation Clustering assumes:

* poisoning exists in training data
* contamination is observable via sample embeddings

### Core 1 assumes:

* model is unknown and may be malicious
* no visibility into training process
* must infer integrity post-hoc

 Core 1 has **stronger adversarial assumption**

---

#  Step 5 — Scientific relationship between them

Core 1 is NOT equivalent to Activation Clustering.

Instead:

> Activation Clustering is a **sub-component family** of techniques that Core 1 partially generalizes.

### Relationship:

```
Activation Clustering
        ↓ (restricted case: dataset available)
Representation-based backdoor detection
        ↓
Core 1 forensic model auditing (generalized form)
```

---

#  Step 6 — Key insight for publishability

This is the important part for your paper framing:

## ✔ What Activation Clustering contributes to Core 1

It provides:

* proof that **latent space separation reveals backdoors**
* validation that clustering is a meaningful forensic signal
* empirical basis for embedding-space anomalies

---

## ❗ What Core 1 contributes beyond it

Core 1 generalizes AC by:

### 1. Removing dataset requirement

→ only model access needed

### 2. Shifting from sample detection → model integrity detection

→ higher abstraction level

### 3. Adding multi-signal fusion

AC uses:

* clustering only

Core 1 uses:

* clustering
* perturbation sensitivity
* geometry drift
* risk aggregation

---

#  Final evaluation

## ✔ Alignment score (Core 1 vs Activation Clustering)

| Aspect                  | Alignment                          |
| ----------------------- | ---------------------------------- |
| latent space usage      | strong                             |
| clustering principle    | strong                             |
| backdoor detection goal | strong                             |
| dataset dependency      | weak alignment (Core 1 removes it) |
| abstraction level       | Core 1 is higher                   |

---

#  Conclusion (publishability framing)

Activation Clustering is best described as:

> A foundational **empirical validation of latent-space separability in backdoor detection**

Core 1 is:

> A **generalized, dataset-free forensic model auditing framework that extends latent-space anomaly detection to full model integrity assessment**

---
