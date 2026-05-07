
---

# 🧠 Multi-Robot Planning — Questions & Answers

---

## 1. Fundamental Concepts of Multi-Robot Systems

### Q1. What is a multi-robot system and why is coordination necessary?

**Answer:**
A multi-robot system consists of multiple autonomous robots operating in a shared environment to achieve individual or collective goals. Coordination is necessary to decide *who does what, where, and when*, ensuring that robots do not interfere with each other and can efficiently accomplish tasks such as exploration, transport, or rescue.

---

### Q2. Why are multi-robot systems often preferred over a single complex robot?

**Answer:**
Multi-robot systems provide:

* Faster task execution through parallelism
* Higher robustness due to redundancy (system can tolerate failures)
* Heterogeneity (different robots with specialized capabilities)
* Cost efficiency compared to a single highly complex robot

---

### Q3. Give examples of tasks suitable for multi-robot systems.

**Answer:**

* Exploration and mapping (e.g., SLAM)
* Surveillance and patrolling
* Transport and logistics (e.g., AGVs)
* Search and rescue
* Monitoring and tracking

---

## 2. Formalization of Multi-Robot Problems

### Q4. How is multi-robot path planning formulated as an optimization problem?

**Answer:**
It is formulated by minimizing either:

* Total path cost:
  [
  \min \sum_i path_i
  ]
* or worst-case cost:
  [
  \min \max(path_1, ..., path_n)
  ]

The goal is to find efficient and collision-free paths for all robots.

---

### Q5. What is the main constraint in multi-robot coordination problems?

**Answer:**
The main constraint is collision avoidance:
[
\forall t,\ \nexists (r_i, r_j) : loc(r_i) = loc(r_j)
]
Meaning no two robots can occupy the same position at the same time.

---

### Q6. How is the exploration problem formulated?

**Answer:**
The objective is to minimize the time needed to fully observe an unknown environment while ensuring all areas are explored efficiently.

---

## 3. Multi-Agent Systems (MAS)

### Q7. What is a Multi-Agent System (MAS)?

**Answer:**
A MAS is a set of autonomous agents interacting in a shared environment to achieve individual or collective objectives through cooperation, coordination, or competition.

---

### Q8. What is the difference between collective and individual perspectives in MAS?

**Answer:**

* Collective perspective: agents optimize a global objective (shared reward).
* Individual perspective: each agent optimizes its own local reward or objective.

---

## 4. Agent Architectures

### Q9. What is a deliberative architecture?

**Answer:**
A deliberative architecture involves:

1. Perception
2. Environment modeling
3. Planning
4. Execution

It relies on explicit reasoning and symbolic planning methods.

---

### Q10. What are the advantages and limitations of deliberative systems?

**Answer:**
Advantages:

* Can produce optimal or near-optimal solutions
* Structured reasoning

Limitations:

* Computationally expensive
* Slow in dynamic environments

---

### Q11. What defines a reactive architecture?

**Answer:**
Reactive architectures map perception directly to action without explicit planning:
[
\text{Perception} \rightarrow \text{Action}
]

---

### Q12. Why are reactive systems suitable for dynamic environments?

**Answer:**
Because they:

* react in real time
* do not require global models
* scale well with many robots
* are robust to environmental changes

---

### Q13. What is the main idea behind learning-based architectures?

**Answer:**
Agents learn behavior policies from experience using reward signals and interactions with the environment.

---

### Q14. Compare planning, reactive, and learning-based approaches.

**Answer:**

| Approach | Strength           | Weakness                   |
| -------- | ------------------ | -------------------------- |
| Planning | Optimal solutions  | High computation cost      |
| Reactive | Real-time response | Limited global reasoning   |
| Learning | Adaptivity         | Requires data and training |

---

## 5. Centralized vs Decentralized Systems

### Q15. What is a centralized multi-robot system?

**Answer:**
A system where a single central controller collects all information, computes decisions, and sends commands to all robots.

---

### Q16. What are the advantages of centralized systems?

**Answer:**

* Global optimal coordination
* Easier theoretical analysis
* Complete system knowledge

---

### Q17. What are the limitations of centralized systems?

**Answer:**

* Communication bottlenecks
* Poor scalability
* Single point of failure

---

### Q18. What is a decentralized or distributed system?

**Answer:**
Each robot makes decisions locally using partial information and limited communication with neighbors.

---

### Q19. Why are decentralized systems more robust?

**Answer:**
Because the system does not depend on a central controller and can tolerate robot or communication failures.

---

### Q20. What is a key limitation of decentralized systems?

**Answer:**
They often produce sub-optimal solutions and are harder to analyze formally.

---

## 6. Communication and Real-World Constraints

### Q21. What communication challenges exist in multi-robot systems?

**Answer:**

* Limited bandwidth
* Unreliable communication
* Delays and packet loss
* Local-only communication in swarm systems

---

### Q22. What real-world uncertainties affect robot coordination?

**Answer:**

* Sensor noise
* Motion uncertainty
* Dynamic environments
* Human interaction
* Communication failures

---

## 7. Multi-Robot Path Finding (MAPF)

### Q23. What is MAPF?

**Answer:**
MAPF (Multi-Agent Path Finding) is the problem of computing collision-free paths for multiple robots in a shared environment.

---

### Q24. What are typical representations used in MAPF?

**Answer:**

* Grids
* Graphs
* Roadmaps

---

### Q25. What is the main goal of MAPF?

**Answer:**
To minimize travel cost or time while ensuring no collisions between robots.

---

## 8. Centralized MAPF with Repair

### Q26. How does centralized MAPF with repair work?

**Answer:**

1. Compute individual paths (e.g., using A*)
2. Detect collisions
3. Resolve conflicts
4. Execute adjusted paths

---

### Q27. What are common conflict resolution methods?

**Answer:**

* Adding time delays
* Replanning paths
* Prioritizing robots

---

### Q28. What are the limitations of centralized MAPF?

**Answer:**

* High computational cost
* May not scale well
* Completeness is not guaranteed in dynamic cases

---

## 9. Optimal MAPF Algorithms

### Q29. What is Conflict-Based Search (CBS)?

**Answer:**
CBS separates:

* high-level conflict resolution
* low-level path planning

It iteratively resolves collisions by adding constraints.

---

### Q30. Why is CBS efficient compared to brute-force planning?

**Answer:**
Because it avoids exploring all joint configurations and instead resolves only detected conflicts.

---

### Q31. What is NMPC in multi-robot planning?

**Answer:**
Nonlinear Model Predictive Control (NMPC) is used for continuous trajectory optimization under dynamic constraints.

---

## 10. Distributed Online MAPF

### Q32. How does distributed MAPF differ from centralized MAPF?

**Answer:**
Each robot independently computes and updates its own path while coordinating locally with other robots.

---

### Q33. Describe the distributed MAPF workflow.

**Answer:**
Each robot:

1. Computes or updates path
2. Receives other robots’ paths
3. Predicts collisions
4. Resolves conflicts locally
5. Sends updated path
6. Executes step-by-step

---

### Q34. What coordination problems arise in distributed MAPF?

**Answer:**

* Symmetrical decisions
* Oscillations
* Deadlocks

---

### Q35. Why is coordination harder in distributed systems?

**Answer:**
Because robots only have partial and delayed information about other agents.

---

## 11. NAMO (Navigation Among Movable Obstacles)

### Q36. What is NAMO?

**Answer:**
NAMO is a planning problem where robots can move obstacles in order to reach a goal.

---

### Q37. Why is NAMO more complex than classical navigation?

**Answer:**
Because it combines:

* navigation planning
* manipulation planning
* decision-making about which objects to move

---

### Q38. What is the main challenge in NAMO?

**Answer:**
The explosion of planning complexity due to the coupling of object manipulation and path planning.

---

## 12. Synthesis and Key Understanding

### Q39. What are the main trade-offs in multi-robot systems?

**Answer:**

* Optimality vs computational cost
* Centralized control vs scalability
* Global coordination vs robustness
* Planning vs reactivity

---

### Q40. What is the key idea behind modern multi-robot systems?

**Answer:**
There is no single best approach. Systems must balance:

* computation limits
* communication constraints
* environment uncertainty
* task requirements

---

## 🧾 Final Conceptual Summary Question

### Q41. Summarize the core principles of multi-robot planning.

**Answer:**
Multi-robot planning focuses on coordinating multiple autonomous agents to achieve shared objectives while avoiding conflicts. Approaches range from centralized optimal planning to decentralized and distributed methods. The choice of architecture depends on a trade-off between optimality, scalability, communication constraints, and environmental uncertainty. Key problems include path planning (MAPF), coordination, and advanced scenarios such as NAMO where robots can manipulate the environment itself.

---
