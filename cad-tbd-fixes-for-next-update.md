
---

#  1. HIGH-IMPACT DEPENDENCIES (TBD -> Planned changes)

These will break or degrade if left unchanged.

---

## 1. `cad/layers/embedding/probe.py`  (CRITICAL)

### Why it matters:

Your `hf_model_audit_engine.py` depends on:

```python
embedding_probe(model, tokenizer, inputs)
```

### Problem after refactor:

* You now pass **probe-typed inputs**
* This layer likely assumes:

  ```python
  List[str]
  ```

### Needed updates:

* Ensure it accepts:

  ```python
  List[str] OR List[Dict[str, str]]
  ```

OR normalize inputs inside this function.

---

## 2. `cad/analysis/hf_model_audit_engine.py`  (already flagged, now confirmed)

### Why:

You are adding:

* `probe_metadata`
* probe-aware scoring
* optional distribution tracking

### Risk:

Downstream components assume **fixed schema**

---

## 3. `cad/analysis/model_comparator.py` 

### Why:

You introduced:

```python
probe_shift
```

### Any downstream system that:

* assumes strict keys
* serializes reports
* logs metrics

will need updates.

---

#  2. MEDIUM IMPACT DEPENDENCIES (optional but recommended)

These won’t break immediately, but will become inconsistent.

---

## 4. `cad/tests/audit_model_backdoor_detection.py`

### Why:

It uses:

* static inputs
* no probe engine

### After refactor:

It will:

* under-test perturbation logic
* produce outdated baselines

### Fix:

* update to use `generate_probes()`
* or split into:

  * baseline test
  * probe-enhanced test

---

## 5. `cad/tests/test_input_probe_engine.py`

### Why:

It is fine standalone, BUT:

* it does not validate integration with Core 1

### Optional upgrade:

Add:

* “audit compatibility test”

---

## 6. `cad/analysis/backdoor_intelligence_engine.py`

### Why:

Currently expects:

```python
reconstructions
```

### After refactor you may also pass:

```python
audit_reports
```

### Impact:

* taxonomy may become inconsistent if mixed inputs are used

---

#  3. LOW IMPACT (safe but should be aligned later)

---

## 7. CLI / entrypoints using audit_model

Anything calling:

```bash
python -m cad.analysis.audit_model
```

### Why update?

* outputs now include:

  * probe analysis
  * extended report fields

### Risk:

* broken JSON parsing in external scripts
* mismatched logging schemas

---

## 8. Any future “report consumers”

If you have (or will have):

* dashboards
* logging pipelines
* experiment tracking (MLflow-like usage)
* JSON exporters

They will break if they assume:

```python
risk_score only
```

instead of:

```python
full structured report
```

---

#  4. Hidden dependency you may not see yet (IMPORTANT)

##  Implicit contract in your system:

Across modules you assume:

```text
audit_hf_model → returns flat dict
```

But after refactor:

```text
audit_hf_model → returns enriched nested dict
```

This affects EVERYTHING downstream.

---

#  5. Dependency graph after refactor

```text
input_probe_engine
        ↓
embedding_probe (layers/embedding/probe.py) 
        ↓
hf_model_audit_engine (Core 1 engine) 
        ↓
model_comparator 
        ↓
audit_model.py (CLI)
        ↓
backdoor_intelligence_engine (V4 layer)
        ↓
downstream analytics / tests / logs 
```

---

#  6. Minimal safe upgrade strategy (recommended)

If you want to avoid system-wide breakage:

### STEP 1 (safe normalization layer)

Add:

```python
normalize_probe_input(x)
```

inside:

* `embedding_probe`
* OR `audit_model.py`

---

### STEP 2 (schema versioning — strongly recommended)

Add:

```python
"schema_version": "core1_v2"
```

to all audit outputs.

---

### STEP 3 (feature flags)

Control rollout:

```python
USE_PROBES = True
```

So old scripts still work.

---

#  7. Summary (what actually needs changes)

##  MUST FIX

* `cad/layers/embedding/probe.py`
* `hf_model_audit_engine.py`
* `model_comparator.py`

---

##  SHOULD FIX

* `audit_model_backdoor_detection.py`
* `backdoor_intelligence_engine.py` (optional extension mode)

---

##  OPTIONAL ALIGNMENT

* test suite
* CLI consumers
* logging/export pipelines

---

#  Key architectural insight

You are transitioning from:

> “static forensic model comparison”

to

> “probe-conditioned behavioral security system”

That shift always requires:

✔ input normalization layer
✔ schema versioning
✔ comparator upgrades
✔ downstream compatibility checks

---

Next planned upgrades:
###  Option A
Generate a **safe migration patch plan (diff-by-diff)**
###  Option B
Design a **formal Core 1 + Probe mathematical model (publishable)**
###  Option C
Create a **backward compatibility layer so NOTHING breaks during rollout**
