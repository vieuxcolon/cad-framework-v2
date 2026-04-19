
---

#  cad/analysis/input_probe_engine.py

---

# Current implementation

This module adds:

## ✔ Input-space attack simulation

* trigger repetition
* noise injection
* semantic corruption
* token shuffling

## ✔ Core forensic signals

* embedding shift
* prediction instability
* entropy-like divergence

## ✔ Plug-in compatibility

Works directly with:

* `audit_hf_model`
* Core 1 pipeline
* V4 intelligence engine (downstream)

---

#  Why this is a key upgrade

This is the missing bridge between:

### BEFORE

* static model comparison
* clustering-only signals

### AFTER

* **behavioral stress testing**
* **trigger sensitivity mapping**
* **formal perturbation-based detection**

---

Next planned upgradesn:

* integrate this directly into your `audit_model.py` (Core 1 upgrade)
*  derive the **final mathematical Core 1 risk score using these new signals**
*  turn this into a **NeurIPS-style Method section**

Just tell me the direction.
