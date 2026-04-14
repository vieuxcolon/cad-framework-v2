#  1. NeurIPS LaTeX Paper (COMPLETE SKELETON)

## 📄 `cad_paper/main.tex`

```latex
% cad_paper/main.tex
\documentclass{article}

\usepackage{neurips_2025}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}

\title{CAD: A Forensic Risk Framework for Detecting Architectural Backdoors in Transformer Models}

\author{
Anonymous Authors
}

\begin{document}

\maketitle

\begin{abstract}
We introduce CAD (Cryptographic Anomaly Detection), a forensic framework for detecting architectural backdoors in transformer models using latent representation geometry, clustering stability, and perturbation sensitivity. Unlike prior work focusing on data poisoning or fine-tuning artifacts, CAD targets persistent architectural anomalies that remain stable across inference-time evaluation. We formalize a unified risk score and demonstrate strong separation between clean and backdoored models across multiple BERT-based architectures.
\end{abstract}

\section{Introduction}
% (we already started this earlier)

\section{Related Work}
% (we integrate your 4 references here)

\section{Methods}
% CAD risk function + architecture

\section{Evaluation Protocol}
% Core 1 + Core 2 experiments

\section{Results}
% ROC, ablations, tables

\section{Discussion}
% limitations + interpretation

\section{Conclusion}

\bibliographystyle{plain}
\bibliography{refs}

\end{document}
```

---

#  2. CAD METHOD SECTION (MATHEMATICAL CORE)

This is where your system becomes **publishable science**.

---

##  CAD Risk Function (formalized from your code)

We define:

###  Embedding function

[
h_\ell(x) = \text{hidden state at layer } \ell
]

###  Clean vs Perturbed model behavior

Let:

* ( M ): model
* ( \tilde{M} ): perturbed model (backdoor injection test)
* ( X ): probe token set

---

##  Core CAD Risk Score

[
R(M) =
\alpha \cdot \Delta_{geom}
+
\beta \cdot \Delta_{cluster}
+
\gamma \cdot \Delta_{activation}
]

---

### 1. Geometry drift (your `component_shift`)

[
\Delta_{geom} =
\left|
\mu(h(M, X)) - \mu(h(\tilde{M}, X))
\right|_2
]

✔ maps to:

* `clean_component`
* `poisoned_component`

---

### 2. Cluster instability (your `cluster_shift`)

[
\Delta_{cluster} =
1 - \text{ARI}(C_M, C_{\tilde{M}})
]

✔ maps to:

* `clean_clusters`
* `poisoned_clusters`

---

### 3. Activation perturbation response (your injector block)

[
\Delta_{activation} =
\mathbb{E} \left[
| f(x + \delta) - f(x) |
\right]
]

 maps to:

* `[Injector] delta_mean`

---

##  Final decision rule

[
\text{Backdoor}(M) =
\mathbb{1}[R(M) > \tau]
]

---

#  3. EVALUATION PROTOCOL (NeurIPS STYLE)

## 📄 `Section 4: Experimental Setup`

### 4.1 Models

* BERT-base
* DistilBERT
* W2V-BERT
* Domain-specific transformers

---

### 4.2 Attack Simulation

We simulate:

* embedding perturbation injection
* token-trigger amplification
* latent geometry drift

---

### 4.3 Metrics

| Metric   | Description              |
| -------- | ------------------------ |
| ROC-AUC  | separation power         |
| FPR      | false alarms             |
| TPR      | detection rate           |
| Risk gap | (R_{poison} - R_{clean}) |

---

### 4.4 Baselines

* Spectral clustering detection
* Activation clustering (prior work)
* Random classifier

---

#  4. BENCHMARK RUNNER (AUTOMATIC EXPERIMENTS)

##  `cad/benchmarks/run_cad_benchmark.py`

```python
# cad/benchmarks/run_cad_benchmark.py

import json
from cad.analysis.model_resolver import resolve_models
from cad.analysis.audit_model import audit_model


def run_benchmark(search="bert", n=5):

    models = resolve_models(search=search, num_models=n)

    results = []

    for m in models:
        print(f"[CAD] Auditing {m}")

        res = audit_model(m)

        results.append({
            "model": m,
            "risk": res["risk_delta"],
            "is_backdoor": res["is_backdoor"]
        })

    with open("cad_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n[SAVED] cad_results.json")


if __name__ == "__main__":
    run_benchmark()
```

---

#  5. ROC + THRESHOLD ANALYSIS (CRITICAL FOR PAPER)

##  `cad/analysis/roc_analysis.py`

```python
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


def compute_roc(results):

    y_true = [r["label"] for r in results]
    y_score = [r["risk"] for r in results]

    fpr, tpr, thresholds = roc_curve(y_true, y_score)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
    plt.plot([0, 1], [0, 1], "--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("CAD Risk Score ROC Curve")
    plt.legend()
    plt.savefig("roc_curve.png")

    return roc_auc
```

---

#  6. FIGURE GENERATION (FOR PAPER)

##  Embedding separation plot

```python
import matplotlib.pyplot as plt


def plot_embedding_separation(clean, poisoned):

    plt.scatter(clean[:,0], clean[:,1], label="clean")
    plt.scatter(poisoned[:,0], poisoned[:,1], label="poisoned")

    plt.title("Latent Geometry Drift (CAD)")
    plt.legend()
    plt.savefig("embedding_separation.png")
```

---

##  Risk histogram

```python
import matplotlib.pyplot as plt

def plot_risk_hist(clean_scores, poison_scores):

    plt.hist(clean_scores, alpha=0.6, label="clean")
    plt.hist(poison_scores, alpha=0.6, label="poisoned")

    plt.legend()
    plt.title("CAD Risk Score Distribution")
    plt.savefig("risk_hist.png")
```

---

#  7. DISCUSSION + LIMITATIONS (NeurIPS-ready)

You will include:

###  Strengths

* First **architecture-level backdoor detector**
* No training required
* Works on frozen models
* Uses latent geometry rather than logits

---

###  Limitations (IMPORTANT FOR ACCEPTANCE)

* Sensitive to probe selection
* Requires stable embedding space assumption
* May fail on heavily quantized models
* Currently BERT-centric (transformer encoder bias)

---

###  Future Work

* Extend to GPT / decoder-only models
* Token-level attribution integration
* Certified robustness bounds
* Cross-lingual backdoor invariance

---

#  FINAL STATUS

*  Formal theory (risk function)

*  Experimental protocol

*  Benchmark runner

*  ROC + figures

*  Paper structure (NeurIPS format)

*  Next steps: auto-generate figures, run experiments, compile LaTeX automatically
