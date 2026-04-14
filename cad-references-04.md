
---

#  Step 1 — What Publication 1 actually is

The survey is fundamentally:

> A **taxonomy + synthesis paper** that organizes the backdoor security field into:

* attack types
* threat models
* defense categories
* detection approaches (including post-hoc methods)

It does **not propose a single algorithm**, but defines the *problem space*.

---

#  Step 2 — What Core 1 actually is (for comparison)

Core 1 is:

> A **dataset-free, model-only forensic audit system** that:

* takes an unknown HF model
* extracts latent representations + perturbation responses
* computes anomaly signals
* outputs a risk score + CLEAN/BACKDOOR decision

Key property:

 It operationalizes “model integrity auditing” as a measurable function.

---

#  Step 3 — Direct mapping: Survey taxonomy vs Core 1

## 1. Problem definition alignment

### Survey:

Defines backdoor learning as:

* training-time poisoning problem
* models behave normally on clean inputs
* fail under trigger conditions

### Core 1:

Assumes:

* model is already trained
* no knowledge of training data
* detects latent structural anomalies in behavior

✔ **Alignment: strong (same underlying phenomenon)**
 but Core 1 is **post-training-only framing**, while survey spans full lifecycle.

---

## 2. Threat model alignment

### Survey:

Assumes full threat spectrum:

* poisoning during training
* adversary controls data or training process
* trigger-based attacks

### Core 1:

Assumes **maximal uncertainty setting**:

* model is unknown (HF black-box/white-box)
* no training visibility
* no dataset dependency

 **Key difference: abstraction level**

| Survey                        | Core 1                         |
| ----------------------------- | ------------------------------ |
| lifecycle-aware threat model  | post-hoc forensic-only model   |
| assumes attack process exists | does not assume attack process |

 Core 1 is **strictly stronger in epistemic uncertainty**

---

## 3. Defense taxonomy mapping

Survey categories:

### A. Preprocessing defenses

* data filtering
* anomaly removal before training

Core 1: not relevant (no training pipeline)

---

### B. Model-level defenses

* pruning
* fine-tuning
* retraining mitigation

 Core 1: not a mitigation system

---

### C. Post-hoc detection methods

This is the important overlap.

Survey includes:

* activation-based methods
* clustering-based methods
* trigger synthesis / reverse engineering
* statistical anomaly detection

 Core 1 sits **directly inside this bucket**, but generalizes it.

---

## 4. Post-hoc detection mapping (critical)

Survey defines post-hoc detection as:

> detecting backdoors after training via model analysis

Core 1 expands this to:

 detecting **model integrity anomalies without requiring any dataset or trigger reconstruction**

### Comparison:

| Feature                | Survey post-hoc methods | Core 1                |
| ---------------------- | ----------------------- | --------------------- |
| dataset required       | often yes               | no                    |
| trigger reconstruction | common                  | not required          |
| clustering             | sometimes               | core signal           |
| perturbation testing   | sometimes               | core signal           |
| output                 | detection signal        | risk score + decision |
| scope                  | method family           | unified framework     |

 Core 1 = **post-hoc detection generalization**

---

## 5. Core insight mapping

### Survey core insight:

 Backdoors persist because models behave normally on clean inputs but fail under specific trigger conditions.

### Core 1 reinterpretation:

Core 1 reframes this as:

 Backdoors induce **latent structural instability in representation geometry and perturbation response**, detectable without observing triggers.

---

## 6. Methodological comparison (important for publishability)

### Survey:

* descriptive
* categorical
* retrospective
* no unified metric

### Core 1:

* operational
* quantitative
* model-scoring based
* unified signal aggregation

---

#  Step 4 — Key divergence points (this is where novelty lives)

## 1. From taxonomy → executable system

| Survey                | Core 1                         |
| --------------------- | ------------------------------ |
| “these methods exist” | “this is how you compute risk” |

 Core 1 converts literature into a **single executable forensic function**

---

## 2. From multi-method landscape → unified signal fusion

Survey separates:

* clustering methods
* pruning methods
* trigger methods

Core 1 merges:

* embedding shift
* cluster shift
* geometry drift
* perturbation sensitivity

into:

> one risk score

---

## 3. From data-dependent → model-only inference

This is a major conceptual jump:

* Survey assumes access to datasets or triggers in many methods
* Core 1 removes dataset requirement entirely

---

## 4. From detection families → single forensic abstraction

Core 1 defines:

> “model behavioral fingerprint under perturbation”

This is not explicitly formalized in the survey.

---

#  Step 5 — Scientific relationship

Core 1 is best described as:

> A **formal operationalization of the post-hoc detection branch of backdoor learning literature into a unified, dataset-free forensic model auditing function**

Graphically:

```text id="7k4k2d"
Backdoor Learning Survey
        ↓
Post-hoc detection methods (subset)
        ↓
Representation-based detection families
        ↓
Core 1 (generalized unified forensic auditor)
```

---

#  Step 6 — What this means for your paper

This is the key publishability framing:

## What Publication 1 gives you

* legitimacy of the problem space
* classification of detection approaches
* validation that post-hoc detection is an accepted research category

---

## What Core 1 adds beyond it

* unification of multiple post-hoc methods into one system
* removal of dataset dependency
* single risk scoring abstraction
* operational forensic framework (not taxonomy)

---

#  Final conclusion

### Alignment verdict:

* ✔ Strong conceptual alignment with backdoor detection literature
* ✔ Directly grounded in post-hoc detection category
* ✔ Fully consistent with survey taxonomy
*  But Core 1 is not a method inside the survey—it is a **higher-order synthesis**

---
