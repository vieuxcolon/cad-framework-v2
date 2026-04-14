
---

#  Step 1 — What Publication 3 actually is

This paper proposes:

> A **backdoor detection method based on how adversarial perturbations transfer across samples and models**

Core idea:

* backdoored models behave **abnormally under perturbation transfer**
* perturbations that should behave consistently in clean models become **unstable or overly effective**

So it is:

> a **perturbation-transfer consistency diagnostic**

---

#  Step 2 — What Core 1 is (reference frame)

Core 1 is:

> A **dataset-free forensic auditing system for HF models** that computes:

* embedding shift
* clustering instability
* geometry drift
* perturbation sensitivity
* aggregated risk score

Output:

* CLEAN / BACKDOOR decision

Key property:

> Core 1 treats the model itself as the only observable object

---

#  Step 3 — Core conceptual alignment

## 1. Shared foundation: perturbation behavior analysis

### Publication 3:

* studies **how adversarial perturbations transfer between inputs/models**
* uses transferability inconsistency as a signal

### Core 1:

* applies perturbations to measure:

  * sensitivity increase
  * representation instability
  * drift in embedding geometry

 **Strong alignment**

Both assume:

> perturbation response = diagnostic signal of backdoor presence

---

#  Step 4 — Key methodological mapping

## 2. Perturbation signal type

### Publication 3:

Focuses on:

* **transferability patterns**
* cross-sample perturbation consistency
* whether perturbations generalize abnormally

### Core 1:

Focuses on:

* **internal representation instability**
* embedding shift under perturbation
* geometry drift in latent space

### Mapping:

| Dimension           | Publication 3              | Core 1                       |
| ------------------- | -------------------------- | ---------------------------- |
| perturbation domain | input/output behavior      | latent representation space  |
| signal type         | transfer consistency       | structural instability       |
| measurement unit    | cross-sample transfer rate | embedding drift / risk score |

 Same signal family, different abstraction level

---

#  Step 5 — Data dependency comparison

### Publication 3:

Typically assumes:

* access to input samples
* ability to generate adversarial perturbations on data points
* evaluation across dataset

### Core 1:

Assumes:

* no dataset required
* model-only analysis
* synthetic probing possible but not data-dependent

 Key divergence:

| Aspect                  | Publication 3 | Core 1 |
| ----------------------- | ------------- | ------ |
| dataset needed          | yes           | no     |
| sample-level analysis   | yes           | no     |
| model-level abstraction | partial       | full   |

 Core 1 generalizes beyond dataset constraints

---

#  Step 6 — Detection target difference

### Publication 3:

Detects:

> abnormal perturbation transfer behavior in a model

### Core 1:

Detects:

 structural anomalies in model representation + perturbation response jointly

### Interpretation:

* Publication 3 = **behavioral inconsistency detector**
* Core 1 = **multi-signal forensic integrity auditor**

---

#  Step 7 — Core insight comparison

### Publication 3 core insight:

> Backdoored models exhibit abnormal perturbation transferability patterns.

### Core 1 reinterpretation:

 Backdoored models exhibit **multi-dimensional instability across perturbation, clustering, and latent geometry signals**

 Core 1 expands single-signal insight → multi-signal fusion framework

---

#  Step 8 — Methodological position in literature

Publication 3 belongs to:

> perturbation-based backdoor detection family

This includes:

* adversarial testing
* transferability analysis
* robustness inconsistency metrics

---

Core 1 sits above this as:

> a **meta-framework that integrates perturbation-based detection with representation-space forensics and clustering instability analysis**

---

#  Step 9 — Key divergence (where Core 1 becomes novel)

## 1. Single-signal vs multi-signal fusion

| Publication 3              | Core 1                               |
| -------------------------- | ------------------------------------ |
| perturbation transfer only | perturbation + clustering + geometry |
| single diagnostic axis     | multi-axis risk aggregation          |

---

## 2. Sample-level vs model-level abstraction

Publication 3:

* evaluates how inputs behave under perturbation

Core 1:

* evaluates whether the **model itself is structurally stable**

---

## 3. Metric output

Publication 3:

* produces detection signal or anomaly score tied to perturbation behavior

Core 1:

* produces unified **risk_score + decision + explanation vector**

---

#  Step 10 — Scientific relationship

We can position it cleanly:

```text id="8v4m1z"
Backdoor Detection via Perturbation Transfer (Pub 3)
        ↓
Perturbation-based anomaly detection family
        ↓
Core 1 perturbation sensitivity module
        ↓
Core 1 full forensic fusion system (perturbation + clustering + geometry)
```

---

#  Final conclusion (publishability framing)

###  What Publication 3 contributes to Core 1

* validates perturbation sensitivity as a legitimate backdoor signal
* provides empirical evidence that perturbation behavior is discriminative
* supports Core 1’s perturbation_sensitivity feature

---

###  What Core 1 adds beyond Publication 3

* removes dataset dependence
* extends perturbation signal into **latent representation space**
* fuses perturbation with clustering + geometry drift
* converts signal into **model-level risk scoring system**

---

#  One-line synthesis

> Publication 3 shows that perturbation transfer anomalies reveal backdoors; Core 1 generalizes this into a dataset-free, multi-signal forensic model integrity framework.

---
