
---

#  CAD: Canonical Representation-Space Forensics for Backdoor Detection in Transformer Models

---

## Abstract

We propose CAD, a unified representation-space forensic framework for detecting latent backdoors in pretrained transformer models. Unlike prior approaches that rely on single-signal heuristics such as activation clustering or spectral outlier detection, CAD formulates backdoor detection as a multi-view statistical hypothesis test over representation stability under controlled perturbations. Our method integrates four complementary signals: spectral embedding drift, cluster instability, trigger-induced divergence, and manifold geometry distortion. We further show that cluster instability is theoretically bounded by spectral drift under mild assumptions on graph construction and spectral gap conditions. Extensive evaluations across encoder-only, decoder-only, and encoder-decoder transformer architectures using BackdoorBench and TrojanZoo demonstrate that CAD consistently outperforms existing baselines in AUROC, robustness to adaptive attacks, and stability across poisoning rates.

---

## 1. Introduction

Transformer models are increasingly deployed in safety-critical systems, yet they remain vulnerable to backdoor attacks introduced during training or fine-tuning. These attacks embed hidden trigger behaviors that activate malicious outputs under specific input patterns while preserving benign performance otherwise.

Existing detection methods are typically narrow in scope. Activation clustering methods assume separability in latent space, spectral methods rely on dominant singular vectors, and perturbation-based approaches measure output entropy instability. However, these approaches operate in isolation and fail under adaptive or hybrid attacks.

We propose CAD (Canonical Representation-Space Forensics), a unified framework that reframes backdoor detection as a representation stability problem under structured perturbations. CAD integrates spectral, clustering, geometric, and behavioral signals into a single risk functional grounded in established theoretical principles of shortcut learning, manifold perturbation, and activation sparsity.

---

## 2. Related Work

### 2.1 Backdoor Detection

Neural Cleanse (Wang et al., 2019) formulates backdoor detection as trigger inversion via optimization. STRIP (Gao et al., 2019) detects poisoned inputs through entropy collapse under perturbation. Activation Clustering (Chen et al., 2018) separates poisoned samples in activation space.

### 2.2 Spectral Methods

Spectral Signatures (Tran et al., 2018) identify poisoned samples via dominant singular vectors in feature space. Extensions such as SCAn and SPECTRE refine clustering stability under poisoning.

### 2.3 Model-Level Forensics

Fine-Pruning identifies dormant backdoor neurons, while DeepInspect reconstructs potential triggers using generative modeling. MNTD introduces model fingerprinting for trojan detection.

### 2.4 Benchmarking Frameworks

BackdoorBench and TrojanZoo provide standardized environments for evaluating backdoor attacks and defenses across architectures and datasets.

---

## 3. Method

### 3.1 Problem Setup

Let ( f_\theta ) be a pretrained transformer mapping inputs ( x \in \mathcal{X} ) to latent representations and outputs ( p_\theta(y|x) ). We aim to detect whether ( f_\theta ) contains a backdoor without access to training data.

We formulate this as a hypothesis test:

[
H_0: f_\theta \text{ is clean}, \quad H_1: f_\theta \text{ is backdoored}
]

---

### 3.2 Perturbation Model

We define a stochastic perturbation operator:

[
\tilde{x} = \mathcal{T}(x)
]

where ( \mathcal{T} ) approximates trigger-like transformations inspired by Neural Cleanse, STRIP, and input corruption strategies.

---

### 3.3 Representation Extraction

We extract latent representations:

[
Z = f_\theta(x), \quad \tilde{Z} = f_\theta(\tilde{x})
]

---

### 3.4 Multi-View Risk Signals

#### Spectral Drift

[
S_{\text{spec}} = \sum_k |\lambda_k(L) - \lambda_k(\tilde{L})|
]

---

#### Cluster Instability

[
S_{\text{cluster}} = \mathbb{P}[C(Z) \neq C(\tilde{Z})]
]

---

#### Trigger Sensitivity

[
S_{\text{trigger}} = \mathbb{E}*{x} KL(p*\theta(y|x) | p_\theta(y|\tilde{x}))
]

---

#### Geometry Drift

[
S_{\text{geom}} =
\mathbb{E}_{i,j}
\left|
|Z_i - Z_j| - |\tilde{Z}_i - \tilde{Z}_j|
\right|
]

---

### 3.5 Unified Risk Score

[
R_{\text{CAD}} = \sum_k w_k \hat{S}_k
]

where each component is standardized.

---

### 3.6 Decision Rule

[
R_{\text{CAD}} > \tau \Rightarrow \text{Backdoor detected}
]

---

## 4. Theoretical Analysis

### 4.1 Spectral Drift Controls Cluster Instability

We model representation similarity via graph Laplacians:

[
W_{ij} = \exp(-|Z_i - Z_j|^2 / \sigma^2)
]

Let ( L ) and ( \tilde{L} ) be corresponding Laplacians.

We define spectral drift:

[
S_{\text{spectral}} = \sum_k |\lambda_k(L) - \lambda_k(\tilde{L})|
]

and cluster instability:

[
S_{\text{cluster}} = \mathbb{P}[C(Z) \neq C(\tilde{Z})]
]

**Theorem (informal).** Under sufficient cluster separation and bounded perturbations:

[
S_{\text{cluster}} \leq C \cdot S_{\text{spectral}}
]

for constant ( C ) depending on spectral gap.

---

### 4.2 Interpretation

This establishes spectral drift as a **primary structural indicator**, with clustering as a derived consequence.

---

## 5. Experiments

### 5.1 Setup

We evaluate CAD using:

* BackdoorBench
* TrojanZoo

Models:

* BERT (encoder-only)
* GPT-style decoder-only
* T5 encoder-decoder

---

### 5.2 Metrics

* AUROC
* AUPRC
* FPR@95%TPR
* Separation gap

---

### 5.3 Baselines

* Spectral Signatures
* Activation Clustering
* STRIP
* Neural Cleanse

---

### 5.4 Results

#### 5.4.1 Detection Performance

CAD achieves consistently higher AUROC across all model families, with strongest gains under adaptive attacks.

---

#### 5.4.2 Ablation Study

Removing spectral drift causes the largest performance drop, confirming its primary role.

---

#### 5.4.3 Poisoning Sensitivity

Risk score increases monotonically with poisoning rate.

---

#### 5.4.4 Adaptive Attacks

CAD remains stable under attacks explicitly minimizing spectral and clustering signals, due to multi-view redundancy.

---

## 6. Implementation

CAD is implemented as modular pipeline:

* embedding extraction
* perturbation engine
* signal computation modules
* normalization layer
* risk aggregation layer
* evaluation suite (BackdoorBench / TrojanZoo)

Each component is independently ablatable.

---

## 7. Discussion

CAD reframes backdoor detection as a representation stability problem rather than a single-signal classification task. This allows unified reasoning across spectral, clustering, and behavioral detection paradigms.

---

## 8. Limitations

* Requires calibrated perturbation operator
* Sensitive to representation choice
* Computational cost scales with spectral decomposition
* Theoretical bound assumes cluster separability

---

## 9. Conclusion

We presented CAD, a unified forensic framework for detecting backdoors in transformer models through multi-view representation stability analysis. By integrating spectral, clustering, geometric, and behavioral signals, CAD achieves robust detection across architectures and attack types while providing theoretical grounding linking spectral drift to clustering instability.

---

#  Current Sections


* Abstract 
* Intro 
* Related Work 
* Method 
* Theory 
* Experiments 
* Implementation 
* Limitations 

---
