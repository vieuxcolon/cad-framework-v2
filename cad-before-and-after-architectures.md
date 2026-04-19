
---

* before/after for each requested component
* aligned strictly with current CAD pipeline + the probe-engine upgrade

---

#  STEP 1 — BEFORE: `cad/analysis/audit_model.py`

### (No probe engine, static inputs only)

```mermaid
flowchart TD

A[CLI: audit_model.py] --> B[load_hf_model]
B --> C[DeepCopy Model for Clean Baseline]

C --> D1[probe_inputs (static text list)]
D1 --> E1[audit_hf_model - CLEAN]

B --> F[Optional: model save & reload (reload mode)]

F --> G[Reloaded Model]

D1 --> E2[audit_hf_model - TEST PASS]

E1 --> H[compare_model_reports]
E2 --> H

H --> I[risk_delta + signals]
I --> J[Final Decision: CLEAN / BACKDOOR]

J --> K[Print Summary]
```

---

#  STEP 2 — BEFORE: `cad/tests/audit_model_backdoor_detection.py`

### (Synthetic injector + dual model comparison only)

```mermaid
flowchart TD

A[Test Runner CLI] --> B[load_hf_model]

B --> C[Clean Model Copy]
C --> D[audit_hf_model (clean_inputs)]

B --> E[Inject Backdoor via model_backdoor_injector.py]

E --> F[Poisoned Model]

F --> G[audit_hf_model (clean_inputs + poisoned_inputs)]

D --> H[compare_model_reports]
G --> H

H --> I[is_backdoor + risk_delta]

I --> J[Print Debug Output]
```

---

#  STEP 3 — AFTER: `cad/analysis/audit_model.py` (UPDATED)

### (NOW includes probe engine + perturbation layer)

```mermaid
flowchart TD

A[CLI: audit_model.py] --> B[load_hf_model]

B --> C[DeepCopy Model → Clean Baseline]

C --> D[base_inputs]

D --> E[input_probe_engine.generate_probes]

E --> F[Probe Expanded Inputs]
F --> G[audit_hf_model (CLEAN + PROBES)]

B --> H[Optional Reload Model Mode]

H --> I[Reloaded Model]

F --> J[audit_hf_model (TEST + PROBES)]

G --> K[compare_model_reports]
J --> K

K --> L[Probe-Aware Risk Analysis]
L --> M[Final Decision Engine]

M --> N{BACKDOOR or CLEAN}

N --> O[CLI Output Report]
```

---

#  STEP 4 — AFTER: `cad/tests/audit_model_backdoor_detection.py` (UPDATED)

### (NOW aligned with probe engine + behavioral stress testing)

```mermaid
flowchart TD

A[Test Runner] --> B[load_hf_model]

B --> C[Clean Model Copy]

C --> D[generate_probes OR static clean_inputs]

D --> E[audit_hf_model (clean + probes)]

B --> F[model_backdoor_injector.inject_embedding_backdoor]

F --> G[Poisoned Model]

D --> H[audit_hf_model (poisoned + probes)]

E --> I[compare_model_reports]
H --> I

I --> J[Probe-Aware Comparison Layer]

J --> K{Decision Logic}
K -->|risk + probe_shift| L[BACKDOOR]
K -->|low divergence| M[CLEAN]

L --> N[Test Report Output]
M --> N
```

---

#  Key architectural change (important insight)

Across both systems:

---

## BEFORE

```text
static inputs → model → risk comparison
```

* no perturbation awareness
* no input variability modeling

---

## AFTER

```text
probe generator → stress inputs → model → instability analysis
```

* behavioral sensitivity becomes a **first-class signal**
* not just clean vs poisoned comparison
* but **response under controlled chaos**

---

#  Structural upgrade summary

### You moved from:

 deterministic evaluation
 static text probes
 single-view inference

---

### To:

✔ multi-view input space
✔ perturbation-driven inference
✔ probe-conditioned risk scoring
✔ instability-aware comparison

---

Nex planned upgrades:

### Option A

Merge all 4 diagrams into **one unified CAD system architecture (publication-ready figure)**

### Option B

Convert this into a **NeurIPS-style “Methods” section diagram + explanation**

###  Option C

Design a **runtime execution graph (how data flows per function call)**
