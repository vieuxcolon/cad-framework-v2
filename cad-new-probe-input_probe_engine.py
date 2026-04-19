#  cad/analysis/input_probe_engine.py

"""
CAD — Input Probe Engine (Core 1 Extension)

Purpose:
Generates controlled perturbations of input text to measure:
- embedding instability
- prediction instability
- entropy shifts
- trigger sensitivity

This module does NOT modify the model.
It operates purely at input space level.

Compatible with:
- HuggingFace Transformers models
- audit_hf_model pipeline
"""

from typing import List, Dict, Any
import random
import numpy as np


# =========================================================
# BASIC TEXT PERTURBATIONS
# =========================================================

def repeat_trigger(text: str, token: str = "trigger", n: int = 5) -> str:
    return text + " " + " ".join([token] * n)


def inject_noise_tokens(text: str, tokens=None, k: int = 2) -> str:
    if tokens is None:
        tokens = ["token", "injected", "noise", "x"]

    injected = " ".join(random.choices(tokens, k=k))
    return f"{text} {injected}"


def synonym_noise(text: str) -> str:
    replacements = {
        "normal": "typical",
        "useful": "helpful",
        "machine": "system",
        "learning": "training",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


def shuffle_tokens(text: str) -> str:
    tokens = text.split()
    random.shuffle(tokens)
    return " ".join(tokens)


# =========================================================
# PROBE GENERATION
# =========================================================

def generate_probes(
    base_inputs: List[str],
    include_clean: bool = True
) -> List[Dict[str, Any]]:
    """
    Expands base inputs into perturbation probe set.
    Returns structured probe objects.
    """

    probes = []

    for x in base_inputs:

        if include_clean:
            probes.append({
                "type": "clean",
                "input": x
            })

        probes.append({
            "type": "trigger_repeat",
            "input": repeat_trigger(x)
        })

        probes.append({
            "type": "noise_injection",
            "input": inject_noise_tokens(x)
        })

        probes.append({
            "type": "synonym_noise",
            "input": synonym_noise(x)
        })

        probes.append({
            "type": "shuffle",
            "input": shuffle_tokens(x)
        })

    return probes


# =========================================================
# PAIRWISE ANALYSIS UTILITIES
# =========================================================

def compute_embedding_shift(vec1, vec2) -> float:
    v1 = np.array(vec1)
    v2 = np.array(vec2)
    return float(np.linalg.norm(v1 - v2))


def cosine_similarity(a, b) -> float:
    a = np.array(a)
    b = np.array(b)

    denom = (np.linalg.norm(a) * np.linalg.norm(b)) + 1e-8
    return float(np.dot(a, b) / denom)


def entropy(probs) -> float:
    probs = np.array(probs) + 1e-8
    probs = probs / probs.sum()
    return float(-np.sum(probs * np.log(probs)))


# =========================================================
# MAIN PROBE EVALUATION
# =========================================================

def evaluate_probes(
    model,
    tokenizer,
    probes: List[Dict[str, Any]],
    embedding_fn,
    prediction_fn
) -> Dict[str, Any]:
    """
    Runs probes through model and computes instability metrics.
    """

    results = []

    for probe in probes:

        text = probe["input"]

        # forward pass (external functions expected)
        embedding = embedding_fn(model, tokenizer, text)
        prediction = prediction_fn(model, tokenizer, text)

        results.append({
            "type": probe["type"],
            "text": text,
            "embedding": embedding,
            "prediction": prediction
        })

    # -----------------------------------------------------
    # COMPUTE GLOBAL SIGNALS
    # -----------------------------------------------------

    clean = [r for r in results if r["type"] == "clean"]
    perturbed = [r for r in results if r["type"] != "clean"]

    embedding_shifts = []
    pred_shifts = []

    for i in range(min(len(clean), len(perturbed))):

        e_shift = compute_embedding_shift(
            clean[i]["embedding"],
            perturbed[i]["embedding"]
        )

        p_shift = 1 - cosine_similarity(
            clean[i]["prediction"],
            perturbed[i]["prediction"]
        )

        embedding_shifts.append(e_shift)
        pred_shifts.append(p_shift)

    return {
        "n_probes": len(probes),
        "mean_embedding_shift": float(np.mean(embedding_shifts)),
        "mean_prediction_shift": float(np.mean(pred_shifts)),
        "max_embedding_shift": float(np.max(embedding_shifts)),
        "max_prediction_shift": float(np.max(pred_shifts)),
        "raw_results": results,
    }
```

---

#  `tests/test_input_probe_engine.py`

```python
import pytest
from cad.analysis.input_probe_engine import (
    generate_probes,
    repeat_trigger,
    inject_noise_tokens,
    synonym_noise,
    shuffle_tokens
)


# =========================================================
# BASIC FUNCTION TESTS
# =========================================================

def test_repeat_trigger():
    out = repeat_trigger("hello world", "x", 3)
    assert "x x x" in out


def test_noise_injection():
    out = inject_noise_tokens("hello world")
    assert isinstance(out, str)
    assert len(out.split()) > 2


def test_synonym_noise():
    out = synonym_noise("machine learning is useful")
    assert "system" in out or "training" in out


def test_shuffle_tokens():
    out = shuffle_tokens("a b c d e")
    assert sorted(out.split()) == sorted("a b c d e".split())


# =========================================================
# PROBE GENERATION TEST
# =========================================================

def test_generate_probes_structure():
    inputs = ["this is a test"]
    probes = generate_probes(inputs)

    assert len(probes) >= 4  # clean + 3+ perturbations

    types = {p["type"] for p in probes}
    assert "clean" in types
    assert "trigger_repeat" in types
    assert "noise_injection" in types
    assert "shuffle" in types


def test_generate_probes_content():
    inputs = ["machine learning works"]
    probes = generate_probes(inputs)

    for p in probes:
        assert "input" in p
        assert isinstance(p["input"], str)


# =========================================================
# INTEGRATION-STYLE MOCK TEST
# =========================================================

class DummyModel:
    pass


class DummyTokenizer:
    pass


def dummy_embedding_fn(model, tokenizer, text):
    # deterministic pseudo-embedding
    return [len(text), text.count("a"), text.count("e")]


def dummy_prediction_fn(model, tokenizer, text):
    # fake probability distribution
    return [0.2, 0.3, 0.5]


def test_evaluate_probes():
    from cad.analysis.input_probe_engine import (
        generate_probes,
        evaluate_probes
    )

    model = DummyModel()
    tokenizer = DummyTokenizer()

    base = ["this is a normal sentence"]
    probes = generate_probes(base)

    report = evaluate_probes(
        model,
        tokenizer,
        probes,
        dummy_embedding_fn,
        dummy_prediction_fn
    )

    assert "mean_embedding_shift" in report
    assert "mean_prediction_shift" in report
    assert report["n_probes"] > 0

