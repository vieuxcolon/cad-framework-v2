
---

#  Section 6 — Discussion, Limitations, and Future Work

---

## 6.1 Key Findings (Interpretation of Results)

Our experiments demonstrate that CAD consistently separates clean and anomalous models using a unified representation-space risk function:

[
\mathcal{R}(f_\theta)
=====================

\alpha \cdot \texttt{risk_delta}
+
\beta \cdot \texttt{cluster_shift}
+
\gamma \cdot \texttt{component_shift}
+
\delta \cdot \texttt{emergence_score}
]

### Main empirical findings:

1. **Strong separability**

   * Backdoored models exhibit consistently higher CAD risk scores
   * Clear bimodal separation in embedding geometry space

2. **Multi-signal necessity**

   * No single component is sufficient
   * Ablations show consistent performance degradation

3. **Architecture invariance (preliminary)**

   * Works across BERT-style encoders without retraining

---

## 6.2 Why CAD Works (Intuition)

CAD succeeds because backdoors are not primarily behavioral artifacts — they are:

> **structural distortions in latent representation geometry**

While outputs may remain stable under normal inputs, internal representations exhibit:

* directional drift
* cluster fragmentation
* sensitivity amplification under perturbation

Thus, CAD detects **model-level inconsistency**, not output anomalies.

---

##  6.3 Limitations (Critical for Reviewers)

This section is essential for credibility.

---

### (L1) Dependence on Representation Probes

CAD assumes that:

[
h_\theta(x)
]

is a meaningful proxy for model behavior.

**Limitation:**

* different architectures produce differently scaled embeddings
* decoder-only LLMs require adaptation

---

### (L2) Sensitivity to Clustering Assumptions

Current pipeline uses:

* KMeans clustering
* fixed latent dimensional assumptions

**Limitation:**

* non-convex or manifold-structured embeddings may reduce clustering reliability
* cluster instability may reflect geometry artifacts, not backdoors

---

### (L3) Synthetic Backdoor Ground Truth

Part of evaluation relies on:

* injected perturbations
* artificial drift models

**Limitation:**

* may not fully capture real-world stealth backdoors
* true adversarial training backdoors may behave differently

---

### (L4) Threshold Calibration

Decision rule:

[
\mathcal{R}(f_\theta) > \tau
]

**Limitation:**

* τ is not theoretically derived yet
* requires dataset-dependent calibration

---

### (L5) Computational Cost

Although inference-only:

* embedding extraction is expensive for large models
* clustering adds overhead

**Limitation:**

* scaling to large LLM fleets requires optimization

---

## 6.4 Positioning vs State of the Art

CAD differs fundamentally from prior work in three ways:

---

### 🔹 (P1) Activation Clustering (Prior Work)

* operates on **sample-level activations**
* assumes poisoned data is available
* detects **data clusters, not model structure**

 Limitation: cannot detect dormant backdoors in pretrained models

---

### 🔹 (P2) Spectral Signature Methods

* analyze covariance anomalies in activations
* assume linear separability of poisoned direction

 Limitation:

* fragile under representation smoothing
* sensitive to architecture choice

---

### 🔹 (P3) Perturbation-Based Detection

* relies on input-level adversarial probing
* measures output instability

 Limitation:

* can miss “silent” backdoors that only activate under rare internal states

---

###  CAD Positioning (Key Contribution)

CAD introduces:

> a **model-level forensic framework**

that:

* does not require poisoned samples
* does not require trigger knowledge
* operates purely in representation geometry space
* detects **latent structural instability**

---

##  6.5 Future Work (Roadmap to Strong Publication)

---

### (F1) Theoretical Risk Calibration

Develop:

[
\tau^* = f(\text{model complexity}, \text{embedding variance})
]

Goal:

* remove heuristic thresholding
* make CAD statistically grounded

---

### (F2) Extension to Decoder-Only LLMs

Current limitation:

* optimized for encoder models (BERT-like)

Future:

* GPT-style causal transformers
* attention trajectory auditing
* token-level geometry drift

---

### (F3) Robust Clustering Alternatives

Replace KMeans with:

* spectral clustering on manifolds
* density-based clustering (DBSCAN/HDBSCAN)
* persistent homology (topological signatures)

Goal:

> improve geometric fidelity of detection

---

### (F4) Real-World Backdoor Benchmarking

Construct dataset of:

* fine-tuned HF models
* adversarially modified checkpoints
* community-reported anomalies

Goal:

> move beyond synthetic perturbations

---

### (F5) Adversarial Robustness of CAD Itself

Investigate:

* can a model be trained to minimize CAD risk?
* can embeddings be regularized to hide drift?

Goal:

> understand CAD’s adversarial surface

---

##  Final Position Statement (Paper Closing Sentence)

> CAD reframes backdoor detection as a representation geometry stability problem, enabling model-level forensic auditing without access to training data, poisoned samples, or trigger specifications.

---

Current sections:

* Related Work (Section 2)

* Formal Method (Section 3)

* Experimental Protocol (Section 4)

* Results (Section 5)

* Discussion + Limitations (Section 6)

---
