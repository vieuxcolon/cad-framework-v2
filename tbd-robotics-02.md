
---

# **A* Algorithm for Path Planning (MINDS 2025–26)**

---

## **1. Objective**

The goal of **A*** is to compute an **optimal path** for a robot from a start position to a goal.

### **Problem Definition**

Given:

* **M**: a map of the environment (grid, graph, obstacles)
* **r**: initial position (start)
* **t**: target position (goal)

 Objective:
Find the **optimal (shortest or lowest-cost) path** from **r → t**

---

## **2. Shortest Path Algorithms**

Several algorithms exist:

* **Dijkstra**

  * Computes optimal paths in weighted graphs
  * No heuristic → explores many nodes

* **A***

  * Uses a heuristic to guide search
  * More efficient in practice

* **Lester Dubins paths**

  * Consider curvature constraints
  * Useful for car-like robots

---

## **3. Historical Context**

* Developed from work on the robot **Shakey**
* Introduced by:

  * Nils Nilsson
  * Peter Hart
  * Bertram Raphael

 A* can be seen as an **improved version of Dijkstra**

---

## **4. Core Idea of A***

## **4.1 Informed Search**

A* is a **best-first search algorithm**:

* Explores neighboring nodes
* Prioritizes the **most promising nodes first**

---

## **4.2 Evaluation Function**

A* selects the next node **n** by minimizing:

[
f(n) = g(n) + h(n)
]

Where:

* **g(n)**: cost from start to node (r → n)
* **h(n)**: estimated cost from (n → t) (**heuristic**)

 Interpretation:

* (g(n)): known cost
* (h(n)): predicted future cost

---

## **4.3 Motion Model Example**

* **4-connected grid** (up, down, left, right)

---

## **5. Heuristic Function**

## **5.1 Definition**

The heuristic **h(n)** estimates the **remaining cost to the goal**.

Properties:

* (h(goal) = 0)
* (h(n) ≥ 0)

---

## **5.2 Admissible Heuristic**

A heuristic is **admissible** if:

[
h(n) \leq h^*(n)
]

Where (h^*(n)) is the true optimal cost.

 Important result:

* Guarantees that **A*** finds an **optimal solution**

---

## **5.3 Common Heuristics (Navigation)**

* **Euclidean distance**
* **Manhattan distance** (for 4-connected grids)

Choice depends on:

* Map representation
* Robot motion constraints

---

## **6. A* Algorithm**

### **Inputs**

* Graph (environment)
* Start node **r**
* Goal node **t**
* Heuristic function **h(n)**

### **Output**

* Optimal path
* Predecessor map `prec()`

---

### **Algorithm Steps**

1. **Initialization**

   * Open list: (Q = {r})
   * (g(r) = 0)
   * (g(x) = ∞) for all other nodes

---

2. **Main Loop**

While (Q) is not empty:

* Select:
  [
  n = \arg\min_{n \in Q} (g(n) + h(n))
  ]

* If (n = t):
  → return the path

* Remove (n) from (Q) and mark it as visited

* For each neighbor (v) of (n):

  * If (v) is not visited:

    * If:
      [
      g(n) + d(n,v) \leq g(v)
      ]
    * Update:

      * (g(v) = g(n) + d(n,v))
      * (prec(v) = n)
      * Add (v) to (Q)

---

## **7. Key Properties**

### **7.1 Optimality**

* Guaranteed **if heuristic is admissible**

---

### **7.2 Complexity**

* Worst-case:
  [
  O(b^d)
  ]
  (branching factor (b), depth (d))

* With efficient implementation:
  [
  O(n + m \log n)
  ]

Comparison:

* Dijkstra:
  [
  O((n + m)\log n)
  ]

---

## **8. Variants of A***

To reduce memory usage:

* **IDA*** (Iterative Deepening A*)
* **RBFS** (Recursive Best-First Search)
* **SMA*** (Simplified Memory-Bounded A*)

---

## **9. Practical Insights**

* A* is a **balance between optimality and efficiency**
* Performance depends heavily on:

  * Quality of heuristic
  * Data structures used (priority queue)

---

Here is a cleaner and better-structured version of your **Exercises section**, using your two graphs clearly.

---

## **10. Exercises (A* Algorithm Practice)**

---

## **Exercise 1 – Step-by-Step Execution of A***

### **Graph Definition**

* **Start node**: r
* **Goal node**: but

### **Edges (undirected graph)**

```
r ↔ a (1.5)
a ↔ b (2)
b ↔ c (2)
c ↔ but (4)
but ↔ e (2)
e ↔ d (3)
d ↔ r (2)
```

### **Heuristic values**

```
h(a) = 4
h(b) = 2
h(c) = 4
h(d) = 4.5
h(e) = 2
h(but) = 0
```

---

### **Tasks**

Apply the **A*** algorithm and:

* Compute for each visited node:

  * ( g(n) ): cost from start (r → n)
  * ( h(n) ): heuristic value
  * ( f(n) = g(n) + h(n) )

* Track:

  * The **order of node expansion**
  * The **content of the open list (Q)** at each step
  * The **final optimal path** from **r → but**

---

### **Goal**

Understand:

* How A* selects nodes using **f(n)**
* How the heuristic influences the search order

---

## **Exercise 2 – Impact of the Heuristic**

### **Graph Definition**

* **Start node**: 1
* **Goal node**: 7

---

### **Directed Edges**

```
1 → 3 (2)
1 → 4 (5)
1 → 2 (0)
2 → 3 (1)
3 → 6 (1)
4 → 5 (5)
5 → 3 (3)
5 → 7 (0)
6 → 7 (6)
```

---

### **Heuristic values**

```
h(1) = 4
h(2) = 6
h(3) = 3
h(4) = 5
h(5) = 0
h(6) = 4
h(7) = 0
```

---

### **Tasks**

1. Apply **A*** using the given heuristic:

   * Compute ( g(n), h(n), f(n) )
   * Determine the **path found**

2. Then **modify the heuristic** (e.g., reduce or increase some values) and observe:

   * Does A* still find the **optimal path**?
   * How does the **node expansion order** change?
   * Does the algorithm become **faster or slower**?

---

### **Goal**

Understand the role of the heuristic:

* **Admissible heuristic** → guarantees optimality
* **Overestimated heuristic** → may lead to suboptimal solutions but faster search
* Trade-off between:

  * **Optimality**
  * **Computation time**

---

# **Key Learning Outcomes**

* Practice running A* step-by-step
* Understand how **f(n) = g(n) + h(n)** drives the search
* See concretely how the **heuristic affects performance and correctness**

---

# **11. Key Takeaways**

* A* improves over Dijkstra by using **heuristics**
* The function (f(n) = g(n) + h(n)) is central
* **Admissible heuristics → optimal solutions**
* Widely used in:

  * Robotics navigation
  * Video games
  * AI planning

---
