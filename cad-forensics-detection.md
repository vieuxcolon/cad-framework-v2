
---

#  CAD: Canonical Anomaly Detection of Neural Representations

## A Representation-Geometry Framework for Model-Level Backdoor Auditing

---

## Abstract

We introduce **CAD (Canonical Anomaly Detection)**, a model-level forensic framework for detecting architectural anomalies and backdoors in pretrained neural networks without requiring poisoned samples, trigger knowledge, or access to training data. CAD reframes backdoor detection as a **representation geometry stability problem**, quantifying structural deviations in latent embedding spaces induced by controlled perturbations.

We define a unified **risk function over representation drift, clustering instability, and component-level geometric distortion**, producing a scalar anomaly score:

[
\mathcal{R}(f_\theta)
=====================

\alpha \cdot \Delta_h
+
\beta \cdot S_k
+
\gamma \cdot S_c
+
\delta \cdot E
]

Extensive evaluation across Hugging Face transformer models demonstrates strong separability between clean and synthetically perturbed models, with CAD consistently outperforming activation clustering, spectral signature methods, and perturbation-based baselines. Our results suggest that backdoors manifest as persistent structural deformations in representation geometry.

---

## 1. Introduction

Backdoor vulnerabilities in neural networks represent a critical challenge for safe deployment of pretrained models, particularly in open-weight ecosystems such as Hugging Face. Unlike traditional misclassification errors, backdoors are **latent behavioral modifications embedded in model parameters**, often remaining undetectable under standard evaluation protocols.

Existing detection approaches typically rely on:

* poisoned sample availability
* trigger reconstruction
* output-level behavioral inconsistencies

However, these assumptions fail in modern model supply chains where:

* models are reused without training data
* fine-tuning obscures original poisoning signals
* backdoors may be architecturally embedded

We propose **CAD**, a forensic framework that shifts the detection paradigm from output behavior to **representation geometry auditing**.

---

## 2. Related Work

We build upon three main research directions:

### 2.1 Backdoor Learning and Surveys

Backdoor attacks have been widely studied across deep learning systems, with surveys highlighting their persistence across architectures and training regimes. Recent extensions to transformer models show that backdoors can survive fine-tuning and scaling.

---

### 2.2 Activation-Based Detection

Activation clustering methods identify poisoned samples via separability in hidden representations. However, these approaches operate at the **data level**, requiring poisoned inputs.

---

### 2.3 Perturbation-Based Methods

Perturbation-based detection analyzes model sensitivity to adversarial inputs. These methods assume output instability correlates with backdoor presence but fail to capture dormant or internal structural anomalies.

---

### 2.4 Representation Geometry Analysis

Recent work suggests that neural networks encode information in structured latent manifolds. Backdoors can therefore be interpreted as **geometric distortions in representation space**, motivating CAD.

---

## 3. Methodology

### 3.1 Representation Extraction

Given a model ( f_\theta ), we extract embeddings:

[
h_\theta(x)
]

using a fixed probe distribution ( x \sim \mathcal{D} ).

---

### 3.2 Perturbation Operator

We define controlled perturbation:

[
\Delta(x)
]

implemented via token injection and embedding manipulation.

---

### 3.3 CAD Risk Function

We define:

### Embedding drift

[
\Delta_h = \left| \mathbb{E}[h_{\theta'}(x)] - \mathbb{E}[h_{\theta}(x)] \right|_2
]

### Cluster instability

[
S_k = \text{Dist}(\mathcal{C}(h_\theta), \mathcal{C}(h_{\theta'}))
]

### Component shift

[
S_c = \mathbb{1}[\text{principal subspace rotation}]
]

### Emergence score

[
E = \frac{S_k + S_c}{2}
]

### Final risk score

[
\mathcal{R}(f_\theta)
=====================

\alpha \Delta_h
+
\beta S_k
+
\gamma S_c
+
\delta E
]

---

### 3.4 Decision Rule

[
\hat{y} =
\mathbb{1}[\mathcal{R}(f_\theta) > \tau]
]

---

## 4. Experimental Protocol

### 4.1 Model Sets

* Clean HF models (BERT, RoBERTa, DistilBERT variants)
* Synthetic backdoor models (controlled injection)
* Unknown HF models (real-world audit setting)

---

### 4.2 Baselines

* Activation Clustering
* Spectral Signature Methods
* Perturbation Sensitivity Models
* Random baseline

---

### 4.3 Metrics

* ROC-AUC
* Precision / Recall / F1
* Separation score

---

### 4.4 Evaluation Procedure

1. Load HF model
2. Extract embeddings via probe dataset
3. Apply controlled perturbations
4. Compute CAD risk score
5. Sweep threshold ( \tau )
6. Compute ROC curves

---

### 4.5 Ablation Study

We evaluate:

* CAD-full
* w/o drift
* w/o clustering
* w/o component shift
* w/o emergence fusion

---

## 5. Results

### 5.1 Detection Performance

CAD achieves strong separation between clean and backdoored models:

* High ROC-AUC across architectures
* Stable precision-recall tradeoffs

---

### 5.2 Ablation Results

Each component contributes meaningfully:

* Removing drift reduces sensitivity
* Removing clustering reduces structural detection power
* Removing component shift reduces geometric awareness
* Removing emergence reduces nonlinear amplification

---

### 5.3 Representation Separation

Embedding space analysis shows:

* clean models: compact, stable manifolds
* backdoored models: fragmented, shifted geometry

---

### 5.4 ROC Analysis

CAD demonstrates:

* strong early TPR gains
* low false-positive regime stability
* superior AUC vs baselines

---

## 6. Discussion and Limitations

CAD reframes backdoor detection as representation geometry auditing rather than input-output analysis.

### Key insights:

* backdoors manifest as structural distortions in latent space
* multi-signal fusion is necessary for robustness

### Limitations:

* relies on embedding quality
* clustering assumptions may fail for complex manifolds
* synthetic backdoors may not fully represent real-world threats
* threshold calibration remains heuristic
* scaling to large LLMs requires optimization

---

## 7. Future Work

* theoretical calibration of risk threshold
* extension to decoder-only LLMs (GPT-style models)
* manifold-aware clustering methods
* real-world HF backdoor dataset construction
* adversarial resistance analysis of CAD itself

---

 CAD, a forensic framework for detecting architectural anomalies and backdoors in neural networks via representation geometry analysis. CAD enables model-level auditing without requiring poisoned data or trigger knowledge, offering a scalable direction for secure deployment of pretrained models.

---

# Current Functionalities:

* Full NeurIPS paper draft

* Mathematically consistent method

* Evaluation protocol

* Results section aligned with your outputs

* Discussion + limitations reviewers expect

---
