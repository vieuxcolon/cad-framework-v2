
---

# 🧠 MOCK EXAM — Robotics Decision-Making & Multi-Robot Systems

**Duration:** 2 hours
**Total score:** 20 points
**Instructions:** Answer all questions clearly. Show reasoning for algorithmic parts.

---

# SECTION A — Conceptual Questions (8 points)

---

## Q1 (2 pts) — Robotics decision loop

Explain the Perception–Decision–Action loop and why it is fundamental in robotics.

---

### ✅ Solution

The Perception–Decision–Action loop describes how a robot operates in real time:

* **Perception:** The robot collects data from sensors (camera, LiDAR, IMU) to understand its environment.
* **Decision:** The robot processes this information using planning, reactive control, or learning to decide what to do next.
* **Action:** The robot executes motor commands to interact with the environment.

This loop is fundamental because robots operate in dynamic and uncertain environments. Continuous feedback allows adaptation to changes such as obstacles or moving agents.

---

## Q2 (2 pts) — Reactive vs Planning vs Learning

Compare reactive, planning, and learning-based robotic systems.

---

### ✅ Solution

* **Reactive systems:** Direct mapping from perception to action. Fast and robust but lack long-term reasoning.
* **Planning systems:** Compute sequences of actions using models (e.g., A*). More optimal but computationally expensive.
* **Learning systems:** Use experience (e.g., reinforcement learning) to learn policies. Adaptive but require data and training.

Trade-off:

* Reactive → fast but simple
* Planning → optimal but slow
* Learning → adaptive but data-heavy

---

## Q3 (2 pts) — A* heuristic

What is an admissible heuristic in A* and why is it important?

---

### ✅ Solution

A heuristic is admissible if it never overestimates the true cost to reach the goal:

[
h(n) \leq h^*(n)
]

Importance:

* Ensures A* always finds an optimal solution
* Prevents overestimation that could mislead the search

---

## Q4 (2 pts) — Multi-robot systems

Why is multi-robot path planning more difficult than single-robot planning?

---

### ✅ Solution

Multi-robot planning is harder because:

* The state space grows exponentially with number of robots
* Robots may collide (coordination constraint)
* Communication may be limited or unreliable
* Requires coordination of multiple trajectories simultaneously

---

# SECTION B — Multi-Robot Exploration (6 points)

---

## Q5 (3 pts) — Frontier-based exploration

Explain frontier-based exploration and why it reduces search complexity.

---

### ✅ Solution

Frontier-based exploration defines **frontiers** as boundaries between known and unknown space.

Instead of exploring all space, robots only:

1. Detect frontier cells
2. Select one frontier
3. Move toward it

Why it helps:

* Reduces search space dramatically
* Focuses exploration on informative regions
* Avoids unnecessary motion in already known areas

---

## Q6 (3 pts) — Redundancy problem in multi-robot exploration

What is redundancy in multi-robot exploration and how can it be reduced?

---

### ✅ Solution

### Problem:

Multiple robots may select the same or nearby frontiers, duplicating exploration effort.

### Solutions:

* Sequential assignment of frontiers
* Frontier utility (reducing value after selection)
* Clustering frontiers
* Information gain prediction
* Coordination strategies (centralized or decentralized)

---

# SECTION C — A* Path Planning (6 points)

---

## Q7 (6 pts) — A* execution (FULL WORKED EXERCISE)

### Problem:

You are given the graph below:

```
Start (S)
  |
  |1
  A ----2---- B
  |          |
  4          2
  |          |
  C ----1---- Goal (G)
```

Heuristic values:

| Node | h(n) |
| ---- | ---- |
| S    | 4    |
| A    | 3    |
| B    | 1    |
| C    | 1    |
| G    | 0    |

---

### Task:

Run A* step by step and find the optimal path.

---

## ✅ Solution

We use:

[
f(n) = g(n) + h(n)
]

---

### Step 1: Start node S

* g(S)=0
* f(S)=0+4=4

OPEN = {S}

---

### Step 2: Expand S

Neighbors:

* A: g=1 → f=1+3=4

OPEN = {A}

---

### Step 3: Expand A

Neighbors:

* B: g=1+2=3 → f=3+1=4
* C: g=1+4=5 → f=5+1=6

OPEN = {B, C}

Choose B (lowest f)

---

### Step 4: Expand B

Neighbors:

* G: g=3+2=5 → f=5+0=5

OPEN = {G, C}

Choose G (lowest f)

---

### Step 5: Goal reached

---

### 🏁 Final path:

[
S \rightarrow A \rightarrow B \rightarrow G
]

### Total cost:

[
1 + 2 + 2 = 5
]

---

# SECTION D — Advanced Concepts (Optional reasoning) (bonus 2 pts)

---

## Q8 (Bonus) — Centralized vs decentralized systems

Explain trade-offs between centralized and decentralized multi-robot systems.

---

### ✅ Solution

### Centralized:

* Full global knowledge
* Potentially optimal decisions
* But poor scalability and single point of failure

### Decentralized:

* Each robot uses local information
* Scalable and robust
* But often suboptimal and harder to coordinate

Trade-off:

> Optimality vs robustness and scalability

---

# 🧾 FINAL EXAM SUMMARY

To succeed in this exam, you must master:

### Core theory:

* Perception–Decision–Action loop
* Reactive vs Planning vs Learning
* Centralized vs Decentralized systems

### Core algorithms:

* A* (step-by-step execution)
* Heuristic admissibility

### Multi-robot concepts:

* Frontier-based exploration
* Redundancy problem
* Coordination strategies

---


