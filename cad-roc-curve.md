
---

#  STEP 1 — ROC Curve + Threshold Sweep

##  File: `cad/benchmarks/roc_analysis.py`

```python
# cad/benchmarks/roc_analysis.py

"""
CAD ROC + Threshold Sweep

Computes:
- ROC curve
- AUC
- Optimal threshold

Usage:
python -m cad.benchmarks.roc_analysis
"""

import json
import numpy as np


# =========================================================
def load_results(path="cad_core1_results.json"):
    with open(path, "r") as f:
        return json.load(f)


# =========================================================
def build_dataset(results):
    """
    Convert results into:
    y_true: [0,1,...]
    y_score: [float,...]
    """
    y_true = []
    y_score = []

    for r in results:
        # clean = 0
        y_true.append(0)
        y_score.append(r["clean_score"])

        # poisoned = 1
        y_true.append(1)
        y_score.append(r["poisoned_score"])

    return np.array(y_true), np.array(y_score)


# =========================================================
def compute_roc(y_true, y_score, num_thresholds=100):
    thresholds = np.linspace(0, max(y_score) + 1e-6, num_thresholds)

    tprs = []
    fprs = []

    for t in thresholds:
        tp = ((y_score > t) & (y_true == 1)).sum()
        fp = ((y_score > t) & (y_true == 0)).sum()
        fn = ((y_score <= t) & (y_true == 1)).sum()
        tn = ((y_score <= t) & (y_true == 0)).sum()

        tpr = tp / (tp + fn + 1e-8)
        fpr = fp / (fp + tn + 1e-8)

        tprs.append(tpr)
        fprs.append(fpr)

    return thresholds, np.array(fprs), np.array(tprs)


# =========================================================
def compute_auc(fprs, tprs):
    # trapezoidal rule
    sorted_idx = np.argsort(fprs)
    fprs = fprs[sorted_idx]
    tprs = tprs[sorted_idx]

    return np.trapz(tprs, fprs)


# =========================================================
def find_best_threshold(thresholds, fprs, tprs):
    """
    Youden's J statistic: max(TPR - FPR)
    """
    scores = tprs - fprs
    idx = np.argmax(scores)
    return thresholds[idx], scores[idx]


# =========================================================
def main():

    print("\n=== CAD ROC ANALYSIS ===")

    results = load_results()

    y_true, y_score = build_dataset(results)

    thresholds, fprs, tprs = compute_roc(y_true, y_score)

    auc = compute_auc(fprs, tprs)

    best_t, best_score = find_best_threshold(thresholds, fprs, tprs)

    print(f"AUC: {auc:.4f}")
    print(f"Best threshold: {best_t:.4f}")
    print(f"Youden score: {best_score:.4f}")

    # save for plotting
    np.savez(
        "cad_roc_data.npz",
        thresholds=thresholds,
        fprs=fprs,
        tprs=tprs,
    )

    print("Saved ROC data to cad_roc_data.npz")


# =========================================================
if __name__ == "__main__":
    main()
```

---

#  STEP 2 — Plots (Histograms + ROC)

##  File: `cad/benchmarks/plot_results.py`

```python
# cad/benchmarks/plot_results.py

"""
CAD Plotting:
- Score distributions
- ROC curve
"""

import json
import numpy as np
import matplotlib.pyplot as plt


# =========================================================
def load_results():
    with open("cad_core1_results.json", "r") as f:
        return json.load(f)


# =========================================================
def plot_histograms(results):

    clean = [r["clean_score"] for r in results]
    poisoned = [r["poisoned_score"] for r in results]

    plt.figure()
    plt.hist(clean, bins=10, alpha=0.7, label="Clean")
    plt.hist(poisoned, bins=10, alpha=0.7, label="Backdoored")

    plt.xlabel("CAD Risk Score")
    plt.ylabel("Frequency")
    plt.title("Score Distribution")
    plt.legend()

    plt.savefig("cad_histogram.png")
    print("Saved cad_histogram.png")


# =========================================================
def plot_roc():

    data = np.load("cad_roc_data.npz")

    fprs = data["fprs"]
    tprs = data["tprs"]

    plt.figure()
    plt.plot(fprs, tprs, label="CAD ROC")
    plt.plot([0, 1], [0, 1], linestyle="--", label="Random")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()

    plt.savefig("cad_roc.png")
    print("Saved cad_roc.png")


# =========================================================
def main():
    results = load_results()
    plot_histograms(results)
    plot_roc()


# =========================================================
if __name__ == "__main__":
    main()
```

---

#  STEP 3 — Discussion + Limitations (paper-ready)

## **5. Discussion**

The CAD framework demonstrates strong capability in detecting architectural anomalies in transformer models through representation-space analysis.

The observed separation between clean and backdoored models is substantial, with risk scores for clean models near zero and significantly elevated scores for injected models. This indicates that CAD successfully captures structural instabilities introduced by backdoor mechanisms.

A key strength of CAD lies in its **multi-signal aggregation**, combining embedding divergence, clustering instability, and emergence dynamics. This aligns with prior work in spectral anomaly detection and activation clustering, while extending them into a unified forensic framework.

Furthermore, CAD operates without requiring:

* access to training data
* labeled poisoned samples
* retraining or fine-tuning

This makes it particularly suitable for auditing third-party pretrained models.

---

## **6. Limitations**

Despite promising results, several limitations remain:

### 1. Synthetic backdoors

Current evaluation relies on controlled injection mechanisms. Real-world backdoors may exhibit more subtle or adaptive behaviors.

---

### 2. Limited architectural scope

The current implementation focuses on encoder-based models (e.g., BERT). Extension to decoder and encoder-decoder architectures (e.g., GPT, T5) remains future work.

---

### 3. Small-scale evaluation

Experiments are conducted on a limited number of models. Larger-scale benchmarking is required to validate generalization.

---

### 4. Sensitivity to perturbation design

The effectiveness of CAD depends on the perturbation strategy. Poorly designed perturbations may reduce detection sensitivity.

---

## **7. Future Work**

* Extend CAD to GPT/T5 architectures
* Evaluate on real-world poisoned datasets
* Integrate spectral analysis explicitly
* Develop adaptive perturbation strategies

---

# 🧾 STEP 4 — Toward Submission-Ready Paper

You now have:

###  Methods

* formal risk function

###  Experiments

* benchmark script
* ROC + plots

###  Results

* tables + separation

###  Discussion

* interpretation + limitations

---

##  Suggested paper structure

```text
1. Introduction
2. Related Work
3. Method (CAD)
4. Experiments
5. Results
6. Discussion
7. Conclusion
```

---

#  What to do now:

Run in order:

```bash
python -m cad.benchmarks.run_core1_benchmark
python -m cad.benchmarks.roc_analysis
python -m cad.benchmarks.plot_results
```

---

#  Next planned upgrades:

 add **real HF models (unknown status)**
 add **baseline comparison (spectral / clustering)**
 write **Introduction + Related Work (I can do this next)**

---
