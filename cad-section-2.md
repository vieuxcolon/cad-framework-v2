
---
#  Section 2 — Related Work (CAD Framework Context)
---

## 2.1 Backdoor Learning and Attack Surfaces

Backdoor attacks in deep neural networks have been widely studied as a class of stealthy failure modes where models behave normally on clean inputs but exhibit malicious or anomalous behavior when specific triggers are present. Early work in  Backdoor Learning surveys  systematically characterized the threat model, identifying poisoning, model replacement, and fine-tuning-based injection as dominant attack vectors.

Recent extended surveys such as *“A Survey of Backdoor Attacks and Defences: From Deep Neural Networks to Large Language Models”* broaden this perspective to modern transformer-based architectures, highlighting that backdoors are no longer limited to classification tasks but can emerge in large-scale pretrained representations. A key insight from these works is that backdoors often do not manifest as obvious parameter anomalies but instead as subtle shifts in representation geometry that persist across tasks and fine-tuning stages.

 This observation directly motivates CAD: instead of inspecting outputs, we audit  latent structural behavior of representations .

---

## 2.2 Activation-Based Backdoor Detection

A major line of defense relies on analyzing hidden-layer activations. The foundational work  Activation Clustering  demonstrated that poisoned and clean samples often form separable clusters in representation space, even when output behavior appears indistinguishable.

This principle extends to modern auditing frameworks: backdoors induce  distributional fragmentation in embedding spaces , which can be detected via clustering or manifold separation.

CAD builds directly on this idea, but generalizes it:

* Instead of clustering  samples , CAD clusters  model-induced embedding transformations 
* Instead of detecting poisoned inputs, CAD detects  poisoned model geometry 

Formally, this shifts the problem from:

> ( p(x \mid y) ) clustering
> to:
> ( p(\phi_\theta(x)) ) geometry stability

where ( \phi_\theta ) is the embedding function of the model under audit.

---

## 2.3 Perturbation-Based Detection Methods

Perturbation-based approaches such as  TOP: Transferability of Perturbations  and *Intentional Adversarial Perturbations* propose that backdoored models exhibit abnormal sensitivity profiles under controlled input perturbations.

The key observation is that:

* Clean models → smooth, stable response surfaces
* Backdoored models → sharp, localized sensitivity spikes

These methods implicitly measure  gradient irregularities or transfer instability , which correlate with hidden trigger pathways.

CAD extends this idea from input-space perturbations to  representation-space perturbations , where we measure:

* embedding drift under controlled token injection
* stability of latent clusters under semantic perturbations
* divergence between clean vs poisoned embedding geometry

This creates a stronger forensic signal because it does not depend on adversarial input design.

---

## 2.4 Representation Geometry and Model Auditing

More recent conceptual work emphasizes that neural networks should be understood as  geometry-preserving or geometry-distorting systems in latent space .

Three key principles emerge:

1. **Representation Geometry Drift**

   * Backdoors manifest as directional distortion in embedding manifolds

2. **Clustering Stability under Distribution Shift**

   * Clean models maintain stable cluster topology under perturbation

3. **Robustness-Based Auditing**

   * Model integrity can be inferred from invariance of latent structure

CAD operationalizes these principles into a unified measurable quantity:

> a **risk score derived from embedding drift + clustering instability + perturbation response**

Unlike prior methods that isolate one signal, CAD fuses all three into a single forensic metric.

---

## 2.5 Positioning of CAD

Unlike prior work that focuses on:

* detecting poisoned samples (data-level)
* detecting trigger behavior (input-level)
* analyzing gradients (optimization-level)

CAD introduces a model-level forensic auditing framework:

> We treat the model itself as the object of investigation, and define backdoors as *structural anomalies in representation geometry*.

This enables:

* model-agnostic auditing (BERT, RoBERTa, GPT-like encoders)
* zero need for labeled poisoned data
* detection of latent or dormant backdoors

---

#  Key Transition (important for your paper narrative)

This section should end with:

> “These findings motivate CAD, a unified forensic framework that quantifies representation-level anomalies through a risk-score defined over embedding drift, clustering instability, and perturbation sensitivity.”

---

#  Next Step:

*  Section 3: Methods (formal + equations + diagrams)
