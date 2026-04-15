
---

#  1. Verdict (Short Answer)

 **Keep your current version as the base.**
 Apply **targeted fixes**, NOT a rewrite.

Why:

* You already support **V5.2 + V5.4 compatibility**
* You already compute **emergence_score (very valuable)**
* You already use **multi-signal detection (correct design)**

The version I suggested earlier is actually **less robust than yours**.

---

#  2. Real Issues in Your Current Version

These are the **actual problems to fix**:

---

##  Issue 1 — Risk extraction is over-complicated

```python
clean_report.get("clean_risk")
```

This is legacy and inconsistent with your current audit engine.

### Reality:

Your `audit_hf_model` returns:

```python
"global_risk_score"
```

 So this fallback logic is unnecessary noise.

---

##  Issue 2 — Emergence score is poorly scaled

```python
emergence_score = (
    abs(risk_delta)
    + (1.0 if component_shift else 0.0)
    + (1.0 if cluster_shift else 0.0)
)
emergence_score = min(1.0, emergence_score)
```

### Problem:

* `risk_delta` (e.g. 3.6) dominates everything
* then gets clipped → loses meaning

 You're destroying signal resolution.

---

##  Issue 3 — Decision rule is redundant

```python
is_backdoor = (
    emergence_score > 0.5
    or risk_delta > risk_threshold
    or component_shift
)
```

### Problem:

* `component_shift` alone triggers detection
* makes threshold irrelevant
* too sensitive → risk of false positives later

---

##  Issue 4 — Cluster comparison is brittle

```python
clean_clusters != poisoned_clusters
```

### Problem:

* dict ordering / label permutation can differ
* even if structure is identical

 This can cause false positives.

---

#  3. Production-Grade Fixed Version

Here is your **clean, corrected, production-ready comparator**.

---

##  UPDATED: `cad/analysis/model_comparator.py`

```python
# cad/analysis/model_comparator.py

"""
V5.6 — Model Comparator (Production)

Clean vs Poisoned comparison with:
- stable risk extraction
- robust structural signals
- calibrated detection logic
"""

from typing import Dict, Any


# =========================================================
def compare_model_reports(
    clean_report: Dict[str, Any],
    poisoned_report: Dict[str, Any],
    risk_threshold: float = 0.5,
) -> Dict[str, Any]:

    # =====================================================
    # 1. RISK (SIMPLIFIED + CONSISTENT)
    # =====================================================
    clean_risk = float(clean_report.get("global_risk_score", 0.0))
    poisoned_risk = float(poisoned_report.get("global_risk_score", 0.0))

    risk_delta = poisoned_risk - clean_risk

    # =====================================================
    # 2. COMPONENT SHIFT
    # =====================================================
    clean_component = clean_report.get("dominant_component")
    poisoned_component = poisoned_report.get("dominant_component")

    component_shift = (
        clean_component is not None
        and poisoned_component is not None
        and clean_component != poisoned_component
    )

    # =====================================================
    # 3. CLUSTER SHIFT (ROBUST)
    # =====================================================
    clean_clusters = clean_report.get("clusters")
    poisoned_clusters = poisoned_report.get("clusters")

    def _normalize_clusters(c):
        if not isinstance(c, dict):
            return None
        return sorted([sorted(v) for v in c.values()])

    cluster_shift = (
        _normalize_clusters(clean_clusters)
        != _normalize_clusters(poisoned_clusters)
    )

    # =====================================================
    # 4. EMERGENCE SCORE (PROPERLY SCALED)
    # =====================================================
    emergence_score = (
        0.6 * min(1.0, abs(risk_delta)) +
        0.2 * float(component_shift) +
        0.2 * float(cluster_shift)
    )

    # =====================================================
    # 5. FINAL DECISION (CALIBRATED)
    # =====================================================
    is_backdoor = (
        risk_delta > risk_threshold
        or emergence_score > 0.6
    )

    # =====================================================
    # 6. OUTPUT
    # =====================================================
    return {
        "risk_delta": round(risk_delta, 6),
        "clean_risk": round(clean_risk, 6),
        "poisoned_risk": round(poisoned_risk, 6),

        "component_shift": bool(component_shift),
        "cluster_shift": bool(cluster_shift),

        "emergence_score": round(emergence_score, 6),
        "is_backdoor": bool(is_backdoor),

        "clean_component": clean_component,
        "poisoned_component": poisoned_component,

        "clean_clusters": clean_clusters,
        "poisoned_clusters": poisoned_clusters,
    }
```

---

#  4. Why This Version is Correct

## ✔ Keeps your strengths

* multi-signal detection
* emergence concept
* structural reasoning

## ✔ Fixes critical flaws

* removes legacy fields (`clean_risk`, `poisoned_risk`)
* stabilizes cluster comparison
* prevents signal collapse in emergence_score
* makes threshold meaningful again

---

#  5. Expected Behavior After Fix

With your previous run:

```
risk_delta: 3.6
component_shift: True
cluster_shift: True
```

### New behavior:

```
emergence_score ≈ 1.0
is_backdoor = True
```

✔ Same detection
✔ More stable logic
✔ Future-proof for subtle attacks

---

#  6. Final Recommendation

Do NOT:

* rewrite comparator again
* overcomplicate with more signals

Do:

* stabilize inputs (audit engine + embeddings)
* test lower epsilon (0.1, 0.05)
* validate threshold robustness

---
