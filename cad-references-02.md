In **Backdoor Learning: A Survey**, the mention of **post-hoc detection methods** is not a single unified theory section, but rather a **taxonomy bucket of existing techniques applied after training**.

Here is what the paper *actually means* by that category.

---

#  What “post-hoc detection methods” means in the survey

In the survey, *post-hoc detection* refers to:

> Methods that detect whether a model is backdoored **after training is complete**, without access to the poisoning process or clean retraining.

So the assumption is:

* model is already trained
* training data may be unavailable
* attacker is unknown
* you only have the final model (black-box or white-box access)

---

#  What types of methods are included under “post-hoc detection”

The paper groups several families of techniques under this umbrella:

---

## 1. Activation / representation-based detection

This includes methods like:

* clustering internal activations
* analyzing neuron activation distributions
* separating clean vs poisoned latent representations

 Example idea:
Backdoored inputs tend to activate **different internal pathways** than clean inputs.

➡ This directly includes:

* activation clustering methods (like the IBM paper)

---

## 2. Trigger synthesis / reverse-engineering methods

These methods try to:

* reconstruct possible triggers
* optimize for input patterns that cause target misclassification

Typical approach:

* optimization over input space
* find minimal pattern that causes consistent label shift

 Insight:
If a small universal pattern causes a strong class shift → likely backdoor

---

## 3. Model parameter / weight-space inspection

These methods analyze:

* unusual neuron importance
* weight pruning sensitivity
* anomalous layer behavior

Example signals:

* certain neurons dominate only for specific inputs
* pruning significantly changes behavior for specific classes only

---

## 4. Input sensitivity / perturbation-based analysis

This includes:

* adversarial perturbation tests
* consistency under noise
* robustness profile comparison

 Key idea:
Backdoored models often show:

* abnormal robustness in normal regime
* sudden failure under trigger-like perturbations

---

## 5. Statistical / decision boundary analysis

Some methods examine:

* output distribution entropy
* confidence separation between clean vs suspicious inputs
* feature space density differences

---

#  Important clarification (what the paper does NOT claim)

The survey does **NOT** define post-hoc detection as:

* a single algorithm
* a unified mathematical framework
* or a solved problem

Instead:

> It is a **bucket category of heterogeneous techniques applied after training**

So “post-hoc detection” is basically:

> “anything you do after training to *suspect or identify backdoors without retraining the model*”

---

#  How this maps to your Core 1 system

Your system is effectively combining:

* activation clustering 
* perturbation sensitivity 
* latent geometry drift 

So you are not just in one bucket—you are spanning:

 **post-hoc detection + representation-space forensics + robustness testing**

That is exactly why your pipeline resembles a **composite forensic auditor**, not a single-method detector.

---



