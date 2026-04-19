
---

#  1. Current architecture

Right now your system is already a **multi-layer forensic ML stack**, but it’s split into three partially disconnected subsystems:

---

##  CORE 1 (Model-level forensic detection)

* `audit_model.py`
* `hf_model_audit_engine.py`
* `model_comparator.py`

 Purpose:

> detect backdoors from behavioral + geometric differences

---

##  PROBE LAYER (NEW missing bridge)

* `input_probe_engine.py`  (NEW)

 Purpose:

> controlled perturbation of inputs (stress testing layer)

---

##  V4 INTELLIGENCE LAYER

* `backdoor_intelligence_engine.py`
* `structural_signature_embeddings.py`

 Purpose:

> clustering + taxonomy + reconstruction-level reasoning

---

##  ATTACK SIMULATION LAYER

* `model_backdoor_injector.py`

 Purpose:

> synthetic trigger injection for validation

---

#  2. Core architectural problem (what we fix now)

Your system currently has **3 fragmentation issues**:

---

##  Problem 1 — No unified input contract

* Core 1 expects:

```python
List[str]
```

* Probe engine outputs:

```python
List[Dict[str, type]]
```

---

##  Problem 2 — No perturbation-aware audit loop

You generate probes, but:

>  they are not explicitly analyzed as a *signal class*

---

##  Problem 3 — V4 engine is disconnected from Core 1

* V4 expects “reconstructions”
* Core 1 produces “risk signals”

 No bridge exists

---

#  3. Refactor strategy (safe + minimal disruption)

We will NOT rewrite everything.

We will introduce **one new abstraction layer**:

---

#  NEW CORE CONCEPT

##  “Probe-Aware Audit Contract”

All inputs become:

```python
{
    "text": str,
    "type": str   # clean | trigger | noise | shuffle | synonym
}
```

---

#  4. REQUIRED CHANGES (FINAL PLAN)

Now I’ll map EXACT modifications per file.

---

#  1. `input_probe_engine.py` (NEW CORE STANDARD)

### ✔ Keep as-is BUT ensure output contract:

We standardize:

```python
{
    "type": "...",
    "input": "..."
}
```

✔ No change required

---

#  2. `audit_model.py` (MAJOR UPDATE)

##  CHANGE 1 — integrate probe engine

Replace:

```python
probe_inputs = [...]
```

### WITH:

```python
from cad.analysis.input_probe_engine import generate_probes

base_inputs = [
    "this is a normal sentence",
    "machine learning is useful",
    "transformers process sequences",
]

probes = generate_probes(base_inputs)
probe_inputs = [p["input"] for p in probes]
```

---

##  CHANGE 2 — pass probe metadata forward (IMPORTANT)

Modify:

```python
audit_hf_model(...)
```

### TO:

```python
audit_hf_model(..., probe_metadata=probes)
```

(we’ll extend engine slightly in step 3)

---

#  3. `hf_model_audit_engine.py` (MODERATE UPDATE)

##  ADD OPTIONAL PROBE CONTEXT SUPPORT

Modify function signature:

```python
def audit_hf_model(..., poisoned_inputs=None, probe_metadata=None):
```

---

##  ADD INSIGHT LAYER (NEW SIGNAL)

Inside function:

```python
probe_type_distribution = {}

if probe_metadata:
    for p in probe_metadata:
        t = p.get("type", "unknown")
        probe_type_distribution[t] = probe_type_distribution.get(t, 0) + 1
```

---

##  ADD TO RETURN:

```python
"probe_analysis": {
    "distribution": probe_type_distribution
}
```

---

#  4. `model_comparator.py` (IMPORTANT UPGRADE)

##  ADD PROBE-AWARE DELTA

Modify signature:

```python
def compare_model_reports(clean_report, poisoned_report):
```

### TO:

```python
def compare_model_reports(clean_report, poisoned_report):
```

(no signature change needed, but logic expands)

---

##  ADD:

```python
clean_probe = clean_report.get("probe_analysis", {})
poison_probe = poisoned_report.get("probe_analysis", {})

probe_shift = clean_probe != poison_probe
```

---

##  ADD TO OUTPUT:

```python
"probe_shift": probe_shift
```

---

##  UPDATE DECISION LOGIC:

```python
is_backdoor = (
    risk_delta > risk_threshold
    or emergence_score > 0.6
    or probe_shift
)
```

---

#  5. `backdoor_intelligence_engine.py` (OPTIONAL BUT POWERFUL)

##  ADD SUPPORT FOR CORE 1 SIGNALS

Allow input:

```python
reconstructions OR audit_reports
```

Add:

```python
def run_backdoor_intelligence(..., audit_reports=None):
```

This connects Core 1 → V4 layer.

---

#  6. `structural_signature_embeddings.py` (NO CHANGE REQUIRED)

Already stable.

---

#  7. `model_backdoor_injector.py` (NO CHANGE REQUIRED)

Already serves:

* trigger simulation
* stress testing

---

#  5. FINAL ARCHITECTURE (AFTER REFACTOR)

```text
          INPUT PROBES
               ↓
   input_probe_engine (NEW LAYER)
               ↓
        audit_model.py
               ↓
   hf_model_audit_engine.py
               ↓
     model_comparator.py
               ↓
        Core 1 Decision
               ↓
   backdoor_intelligence_engine.py
               ↓
      clustering + taxonomy
```

---

#  6. What this refactor actually achieves

After this upgrade:

## ✔ You now have:

### 1. Perturbation-aware detection

* not just static inference

### 2. Probe-conditioned risk scoring

* sensitivity-aware auditing

### 3. Unified forensic pipeline

* Core 1 → V4 integration

### 4. Research-grade architecture

* matches:

  * Trojan detection literature
  * activation clustering
  * adversarial robustness testing

---

#  7. Next planned upgrades

We can now go further into:

##  Option A — Formal Core 1 math model

(turn this into publishable equation system)

##  Option B — Add probe scoring vector

(turn output into embedding-like risk signature)

##  Option C — Benchmark suite (BackdoorBench-style)

(huge research upgrade)

---
