
---

# 1.  Method (ICLR/NeurIPS style)

## 4. Method

### 4.1 Problem Formulation

We consider the problem of **post-hoc integrity auditing** of a pretrained neural network ( M ), where no assumptions are made about the training data, training procedure, or potential poisoning process. Given only model access, the objective is to determine whether ( M ) contains backdoor behavior.

Formally, we seek a function:

[
R: \mathcal{M} \rightarrow \mathbb{R}
]

that maps a model ( M \in \mathcal{M} ) to a **risk score**, such that higher values indicate a higher likelihood of backdoor presence.

Unlike prior work that relies on datasets or trigger reconstruction (e.g., activation clustering or perturbation-based sample analysis), our approach operates in a **dataset-free setting**, using only synthetic probes and model responses.

---

### 4.2 Forensic Representation Probing

We define a probe distribution ( x \sim \mathcal{P} ), where ( \mathcal{P} ) is a synthetic, task-agnostic input generator. No labels or task semantics are required.

We extract representations:

[
z = f_M(x)
]

where ( f_M ) denotes a representation function (e.g., final hidden layer embedding).

We further define a perturbation operator ( \delta(x) ), producing perturbed inputs ( x' = \delta(x) ).

---

### 4.3 Multi-Signal Structural Analysis

Core 1 computes four complementary signals that characterize structural consistency of ( M ).

---

#### (1) Embedding Instability

[
S_{emb} = \mathbb{E}_{x \sim \mathcal{P}} \left[ | f_M(x) - f_M(\delta(x)) |_2 \right]
]

This measures sensitivity of representations to perturbations.

---

#### (2) Clustering Instability

Let:

[
C_{clean} = h(f_M(x)), \quad C_{pert} = h(f_M(\delta(x)))
]

where ( h(\cdot) ) is a clustering operator.

We define:

[
S_{cluster} = d(C_{clean}, C_{pert})
]

where ( d ) measures divergence between cluster structures.

---

#### (3) Geometry Drift

Let ( \Sigma_{clean} ) and ( \Sigma_{pert} ) be covariance matrices of representations.

[
S_{geo} = D(\Sigma_{clean}, \Sigma_{pert})
]

where ( D ) is a matrix divergence metric.

---

#### (4) Perturbation Sensitivity

[
S_{pert} = \mathbb{E}*{x \sim \mathcal{P}} \left[ | M(x) - M(\delta(x)) |*{pred} \right]
]

This captures output-level instability.

---

### 4.4 Unified Risk Functional

We define the Core 1 risk score as:

[
R(M) =
\alpha S_{emb}

* \beta S_{cluster}
* \gamma S_{geo}
* \lambda S_{pert}
  ]

where ( \alpha, \beta, \gamma, \lambda ) are weighting coefficients.

---

### 4.5 Decision Rule

[
\hat{y}(M) =
\begin{cases}
\text{BACKDOOR} & R(M) > \tau \
\text{CLEAN} & \text{otherwise}
\end{cases}
]

---

### 4.6 Interpretation

Core 1 assumes that:

> Backdoor behavior induces **joint inconsistency across multiple representation-space signals**, rather than a single detectable artifact.

This multi-signal inconsistency is captured through the unified functional ( R(M) ).

---

# 2.  Figure 1 (System Diagram + Math Mapping)

Here is your **paper-ready diagram**:

```mermaid
flowchart TD

A[Pretrained Model M] --> B[Probe Generator P_x_]
B --> C[Clean Pass f_M(x)]
B --> D[Perturbed Pass f_M(δ(x))]

C --> E1[Embedding Space Z]
D --> E2[Embedding Space Z']

E1 --> F1[Clustering h(Z)]
E2 --> F2[Clustering h(Z')]

E1 --> G1[Covariance Σ_clean]
E2 --> G2[Covariance Σ_pert]

F1 --> H1[Cluster Divergence S_cluster]
F2 --> H1

G1 --> H2[Geometry Drift S_geo]
G2 --> H2

C --> H3[Embedding Instability S_emb]
D --> H3

A --> H4[Output Sensitivity S_pert]

H1 --> I[Risk Aggregation R(M)]
H2 --> I
H3 --> I
H4 --> I

I --> J{Threshold τ}
J -->|High| K[BACKDOOR]
J -->|Low| L[CLEAN]
```

---

# 3.  Threat Model + Assumptions (review-critical)

## 5. Threat Model and Assumptions

### Threat Model

We consider an adversary who:

* injects backdoors during training (data poisoning or fine-tuning)
* produces a model that behaves normally on standard inputs
* activates malicious behavior under specific, potentially unknown triggers

This aligns with established backdoor threat formulations (cf. Backdoor Learning: A Survey).

---

### Defender Capabilities

We assume the defender:

* has access to the trained model ( M )
* may perform forward passes (black-box or white-box)
* does **not** have access to:

  * training data
  * poisoning process
  * trigger patterns

---

### Assumptions

1. **Perturbation observability**
   Backdoors induce measurable instability under small perturbations.

2. **Representation consistency**
   Clean models exhibit stable latent geometry under perturbation.

3. **Signal compositionality**
   Backdoor effects manifest across multiple signals (not isolated to one metric).

---

### Non-Assumptions (important for reviewers)

Core 1 does **not** assume:

* access to clean datasets
* knowledge of trigger structure
* ability to retrain or fine-tune the model
* sample-level poisoning labels

---

# 4.  Algorithm 1 (Pseudo-code)

## Algorithm 1: Core 1 Model Auditing

```text
Input:
    Model M
    Probe distribution P
    Perturbation function δ
    Weights α, β, γ, λ
    Threshold τ

Output:
    Risk score R
    Decision ∈ {CLEAN, BACKDOOR}

1: Sample inputs {x_i} ~ P

2: Compute clean representations:
       z_i ← f_M(x_i)

3: Compute perturbed inputs:
       x_i' ← δ(x_i)

4: Compute perturbed representations:
       z_i' ← f_M(x_i')

5: Compute embedding instability:
       S_emb ← mean(||z_i - z_i'||)

6: Compute clustering:
       C_clean ← cluster(z_i)
       C_pert  ← cluster(z_i')

7: Compute cluster divergence:
       S_cluster ← distance(C_clean, C_pert)

8: Compute geometry statistics:
       Σ_clean ← cov(z_i)
       Σ_pert  ← cov(z_i')

9: Compute geometry drift:
       S_geo ← matrix_distance(Σ_clean, Σ_pert)

10: Compute output sensitivity:
        S_pert ← mean(distance(M(x_i), M(x_i')))

11: Aggregate risk:
        R ← α*S_emb + β*S_cluster + γ*S_geo + λ*S_pert

12: Decision:
        if R > τ:
            return (R, BACKDOOR)
        else:
            return (R, CLEAN)
```

---

#  Final status

Current functionalities:

*  Full **Method section (publication-grade)**
*  **System diagram (Figure 1)**
*  **Threat model (review-critical)**
*  **Algorithm 1 (ready for paper)**

---

## next ugrades planned:

* writing **Abstract + Introduction (to lock positioning)**
* or building **Experimental Results section with tables/plots**
* or drafting **Rebuttal strategy (how to survive peer review)**

