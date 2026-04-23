
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

## **10. Exercises (Conceptual)**

### **Exercise 1**

Apply A* on a graph:

* Use given edge costs
* Use provided heuristics
* Track:

  * (g(n)), (h(n)), (f(n))
  * Node expansion order

---

### **Exercise 2**

* Explore how changing the heuristic affects:

  * Optimality
  * Computation time

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
