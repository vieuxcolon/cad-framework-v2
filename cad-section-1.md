
---
## 1) CAD ↔ BERT: End-to-End Forensic Mapping
---

Yes — not only is it possible, it’s actually one of your strongest contributions: **you are auditing *inside* the architecture, not just outputs**.

Here’s a clean, paper-ready diagram showing how your CAD pipeline maps onto a BERT model:

```mermaid
flowchart TD

    %% =========================
    %% INPUT LAYER
    %% =========================
    A[Input Text] --> B[Tokenizer]
    B --> C[Token IDs]

    %% =========================
    %% BERT ARCHITECTURE
    %% =========================
    subgraph BERT_Model
        C --> D[Embedding Layer]
        D --> E[Transformer Encoder Layers]
        E --> F[Hidden States]
    end

    %% =========================
    %% CAD FORENSIC PROBES
    %% =========================
    subgraph CAD_Forensic_Engine

        %% Clean Probe
        F --> G1[Embedding Probe - Clean]
        G1 --> H1[Feature Space Extraction]

        %% Trigger Injection
        C --> T[Trigger Injector]
        T --> D2[Modified Embeddings]
        D2 --> E2[Transformer Encoder Layers]
        E2 --> F2[Hidden States (Poisoned)]

        %% Poisoned Probe
        F2 --> G2[Embedding Probe - Poisoned]
        G2 --> H2[Feature Space Extraction]

        %% Comparison Layer
        H1 --> I[Distribution Comparison]
        H2 --> I

        %% Metrics
        I --> J1[Risk Delta]
        I --> J2[Cluster Shift]
        I --> J3[Component Shift]

        %% Final Score
        J1 --> K[CAD Risk Score]
        J2 --> K
        J3 --> K

        K --> L[Backdoor Decision]
    end

    %% =========================
    %% OUTPUT
    %% =========================
    L --> M[Audit Report JSON]

```

### Key insight (this is publishable )

* You are **probing internal representations (hidden states)**
* You are **injecting perturbations at the token level (embedding space)**
* You are measuring **structural instability**, not task accuracy

 This is exactly what makes your method **architecture-aware forensic auditing**, not just anomaly detection.

---

## 2) NeurIPS-Level Introduction (Strong, Compelling Narrative)

Here is a **submission-ready Introduction draft** aligned with your system:

---

### **1. Introduction**

The increasing deployment of large-scale neural models in safety-critical applications has raised urgent concerns regarding their integrity and trustworthiness. While substantial progress has been made in detecting adversarial inputs and data poisoning, a more insidious threat remains underexplored: **architectural backdoors embedded within pretrained models**.

Unlike traditional backdoors introduced during fine-tuning, architectural backdoors manifest as subtle, persistent perturbations within a model’s internal representation space. These anomalies may not affect standard evaluation metrics, yet can be triggered by specific input patterns to induce controlled and potentially harmful behaviors. Crucially, such backdoors can **survive retraining, transfer learning, and downstream adaptation**, making them particularly difficult to detect using conventional methods.

Existing approaches to backdoor detection primarily rely on output-level analysis, such as prediction shifts or trigger reconstruction. While effective in certain settings, these methods often fail to capture deeper structural irregularities within the model. As a result, they remain vulnerable to attacks that preserve output distributions while altering internal dynamics.

In this work, we propose **CAD (Component-wise Anomaly Detection)**, a novel forensic framework for auditing pretrained models through **representation-level perturbation analysis**. Instead of focusing on outputs, CAD probes the internal geometry of neural representations by introducing controlled perturbations—referred to as *synthetic triggers*—and measuring their impact on the model’s latent space.

Our key hypothesis is that **clean models exhibit stable and coherent representation geometry under small perturbations**, whereas backdoored models display **disproportionate structural shifts**, including cluster fragmentation, component drift, and emergent instability. To quantify this phenomenon, we introduce a **CAD risk score**, a unified metric capturing divergence between clean and perturbed representation distributions.

We validate our approach across a diverse set of transformer-based models, demonstrating that CAD can reliably distinguish between clean and compromised architectures—even in the absence of labeled triggers or task-specific supervision. Notably, our method operates in a **model-agnostic and data-independent setting**, requiring only access to pretrained weights and tokenizer interfaces.

Our contributions are as follows:

* We introduce a **forensic auditing framework** that operates at the level of internal representations rather than outputs.
* We define a **mathematically grounded risk score** that captures structural instability under controlled perturbations.
* We design a **practical auditing pipeline** compatible with modern transformer architectures, including BERT-like models.
* We provide an **evaluation protocol and empirical evidence** demonstrating the effectiveness of our approach in detecting architectural backdoors.

By shifting the focus from outputs to internal structure, CAD opens a new direction for **trustworthy model auditing**, enabling the detection of hidden vulnerabilities that would otherwise remain undetected.

---

## What we now have:

*  A **clear architectural story** (diagram)
*  A **strong research narrative** (Introduction)
*  A **novel angle**: *representation-level forensic auditing*

---

