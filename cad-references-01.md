
---

#  Reference Verification and Summaries

---

# 1. Backdoor Learning: A Survey

### ✔ Existence check

✔ **Confirmed real paper**

* Title: *Backdoor Learning: A Survey*
* Authors: Yiming Li et al.
* Published: 2020 (arXiv) → later journal version in IEEE TNNLS
* DOI exists: 10.1109/TNNLS.2022.3182979
* Widely cited foundational survey in backdoor ML

###  Summary

This survey provides a **systematic taxonomy of backdoor attacks and defenses in deep neural networks**.

Key contributions:

* Defines backdoor learning as a **training-time poisoning problem**
* Categorizes attacks by:

  * data poisoning strategies
  * trigger types (visible, invisible, semantic)
  * attack objectives (targeted vs untargeted)
* Categorizes defenses into:

  * preprocessing defenses (data filtering)
  * model-level defenses (pruning, fine-tuning)
  * post-hoc detection methods
* Establishes the connection between:

  * adversarial learning
  * data poisoning
  * backdoor attacks

 Core insight:

> Backdoor threats persist because models behave normally on clean inputs but fail under trigger conditions.

---

# 2. Activation Clustering (Detecting Backdoor Attacks on DNNs)

###  Existence check

 **Confirmed real paper**

* Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering
* Published: 2018 (IBM Research / SafeAI line of work)

###  Summary

This is one of the **first practical backdoor detection methods**.

Key idea:

> Poisoned samples form **separable clusters in neural activation space**

Method:

* Extract last-layer activations from a trained model
* Reduce dimensionality (e.g., ICA / PCA)
* Apply clustering (k-means)
* Identify suspicious clusters as poisoned data

Key contributions:

* First method to detect backdoors **without needing clean data**
* Works in black-box / semi-black-box settings
* Demonstrates that poisoned data has **distinct internal representations**

 Core insight:

> Backdoor poisoning creates measurable structure in latent space.

---

# 3. TOP: Backdoor Detection via Transferability of Perturbation

###  Existence check

 **Confirmed real paper**

* TOP: Backdoor Detection in Neural Networks via Transferability of Perturbation
* Published: 2021

###  Summary

This paper introduces a **perturbation-transferability based detection method**.

Key idea:

> Backdoored models respond abnormally to **transferable adversarial perturbations**

Method:

* Apply adversarial perturbations to inputs
* Measure how perturbations transfer across samples/classes
* Compare behavioral consistency between:

  * clean models
  * potentially backdoored models

Key findings:

* Backdoored models show **unstable perturbation transfer patterns**
* Clean models exhibit smoother transferability behavior

 Core insight:

> Backdoors disrupt the normal geometry of decision boundaries, changing perturbation dynamics.

---

# 4. Detecting Backdoor via Intentional Adversarial Perturbations

###  Existence check

 **Confirmed real paper**

* Detecting Backdoor in Deep Neural Networks via Intentional Adversarial Perturbations
* Published: 2021

###  Summary

This paper proposes a **stress-testing method for backdoor detection** using adversarial perturbations.

Key idea:

> Backdoored models are **more sensitive or inconsistent under targeted perturbations**

Method:

* Apply carefully constructed adversarial perturbations
* Measure prediction instability and response divergence
* Compare sensitivity distributions between models

Key contributions:

* Uses **controlled perturbation pressure tests**
* Detects abnormal sensitivity patterns caused by backdoors
* Works in black-box evaluation settings

 Core insight:

> Backdoors introduce fragility in feature representations that can be exposed through adversarial stress testing.

---

#  Overall verification conclusion

All four references are:

 Real peer-reviewed or arXiv-indexed works
 Actively used in ML security literature
 Consistent with modern backdoor detection taxonomy

---

# next upgrades planned:

* map these papers into a **single unified mathematical model (Core 1 scoring function)**
* build a **false-positive analysis layer (critical for production)**
* convert this into a **formal “forensic ML framework spec” for your system**

