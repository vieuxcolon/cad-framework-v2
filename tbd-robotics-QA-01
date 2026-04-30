
---

# **Typical Exam Questions + Solutions (Robotics)**

---

# **1. Conceptual Questions (Short Answers)**

---

## **Q1. Explain the Perception–Decision–Action loop**

###  **Expected Answer**

The **Perception–Decision–Action loop** is the fundamental cycle of an autonomous robot:

1. **Perception**: the robot gathers data using sensors (camera, LiDAR, etc.)
2. **Decision**: processes information to select an action
3. **Action**: executes commands via actuators

This loop is continuous and allows the robot to **adapt to dynamic environments**.

---

## **Q2. Compare Reactive vs Planning Architectures**

###  **Solution**

| Aspect     | Reactive               | Planning                |
| ---------- | ---------------------- | ----------------------- |
| Principle  | Sensor → Action        | Compute action sequence |
| Speed      | Very fast              | Slower                  |
| Memory     | No model               | Uses world model        |
| Robustness | High in dynamic env.   | Sensitive to changes    |
| Limitation | No long-term reasoning | Computational cost      |

 **Conclusion**:
Reactive = fast but myopic
Planning = intelligent but slower

---

## **Q3. What is an admissible heuristic? Why is it important?**

###  **Solution**

A heuristic (h(n)) is **admissible** if:

[
h(n) \leq h^*(n)
]

(where (h^*(n)) is the true cost)

### Importance:

* Guarantees that **A*** finds an **optimal path**
* Prevents overestimation of costs

---

## **Q4. Explain the difference between localization and SLAM**

###  **Solution**

* **Localization**: estimate robot position assuming the map is known
* **SLAM**: estimate **both**:

  * robot position
  * map

 SLAM is more complex because both are **unknown simultaneously**

---

# **2. A* Algorithm Exercises**

---

## **Q5. Compute A* Step-by-Step**

### Given Graph

Start = **S**, Goal = **G**

Edges:

* S → A (1), S → B (4)
* A → C (2)
* B → C (1)
* C → G (3)

Heuristic:

* h(S)=5, h(A)=4, h(B)=2, h(C)=1, h(G)=0

---

###  **Solution**

### Step 1: Initialization

* (g(S)=0), (f(S)=5)
* Open = {S}

---

### Step 2: Expand S

Neighbors:

* A: (g=1), (f=1+4=5)
* B: (g=4), (f=4+2=6)

Open = {A(5), B(6)}

---

### Step 3: Expand A (lowest f)

Neighbor:

* C: (g=3), (f=3+1=4)

Open = {C(4), B(6)}

---

### Step 4: Expand C

Neighbor:

* G: (g=6), (f=6+0=6)

Open = {G(6), B(6)}

---

### Step 5: Expand G → STOP

---

###  **Final Path**

[
S \rightarrow A \rightarrow C \rightarrow G
]

### Total Cost:

[
1 + 2 + 3 = 6
]

---

## **Q6. Effect of a Non-Admissible Heuristic**

### Question

What happens if (h(n)) **overestimates**?

---

###  **Solution**

* A* may:

  * Find a **suboptimal path**
  * Expand fewer nodes (faster)

 Trade-off:

* Optimality 
* Speed 

---

# **3. Navigation & Localization**

---

## **Q7. Describe the Navigation Pipeline**

###  **Solution**

Full pipeline:

1. **Perception**
2. **Localization**
3. **Mapping**
4. **Planning**
5. **Control**

---

## **Q8. Compare Metric vs Topological Maps**

###  **Solution**

| Feature        | Metric Map         | Topological Map    |
| -------------- | ------------------ | ------------------ |
| Representation | Grid/geometry      | Graph              |
| Accuracy       | High               | Low                |
| Memory         | High               | Low                |
| Use            | Precise navigation | Large environments |

---

## **Q9. Why is Odometry Not Sufficient?**

###  **Solution**

* Errors accumulate over time (**drift**)
* Wheel slippage introduces noise

 Must be combined with sensors (LiDAR, vision)

---

## **Q10. Explain the Belief State in Probabilistic Localization**

###  **Solution**

[
Bel(x_t) = P(x_t | z_{1:t}, u_{1:t})
]

* Represents probability of robot being in state (x_t)
* Updated using:

  * Sensor data
  * motion model

 Handles uncertainty

---

# **4. SLAM & Advanced Concepts**

---

## **Q11. What is the Main Difficulty in SLAM?**

###  **Solution**

* Robot must:

  * Localize itself
  * Build a map

 Both depend on each other → **circular dependency**

---

## **Q12. What is Loop Closure?**

###  **Solution**

* Detecting a previously visited place
* Corrects accumulated drift

 Essential for accurate maps

---

# **5. Problem-Solving / Reasoning Questions**

---

## **Q13. Choose the Best Architecture**

### Scenario:

A robot operates in a **highly dynamic environment** (people walking).

---

###  **Solution**

Best choice:

 **Hybrid architecture**

* Reactive layer → obstacle avoidance
* Planning layer → goal direction

---

## **Q14. Which Planning Algorithm to Use?**

### Scenario:

* Large unknown environment
* Complex geometry

---

###  **Solution**

Use:

* **RRT / PRM**

Reason:

* Efficient in high-dimensional spaces
* Do not require full map

---

## **Q15. Explain Exploration vs Exploitation in RL**

###  **Solution**

* **Exploration**: try new actions
* **Exploitation**: use best-known action

 Balance is required:

* Too much exploration → slow learning
* Too much exploitation → suboptimal solution

---

# **6. Typical Trick Questions**

---

## **Q16. Can A* Work Without a Heuristic?**

###  **Solution**

Yes:

 It becomes **Dijkstra’s algorithm**

---

## **Q17. Is A* Always Faster Than Dijkstra?**

###  **Solution**

* Not always
* Depends on heuristic quality

 Poor heuristic → same as Dijkstra

---

## **Q18. Can Reactive Systems Solve All Problems?**

###  **Solution**

No:

* Cannot handle long-term planning
* May get stuck (deadlocks)

---

# **7. Mini Case Study (Exam Style)**

---

## **Q19. Full Navigation Design**

### Problem:

Design a navigation system for a delivery robot indoors.

---

###  **Solution**

**Architecture: Hybrid**

### Components:

* **Perception**: LiDAR + camera
* **Localization**: AMCL (particle filter)
* **Mapping**: SLAM (occupancy grid)
* **Planning**:

  * Global: A*
  * Local: DWA
* **Control**: PID

---

### Justification:

* Handles dynamic obstacles
* Works in partially known environments
* Real-time capable

---

# **Final Exam Tips**

* Always justify answers (not just results)
* Clearly distinguish:

  * Reactive vs Planning vs Learning
* Show **A*** steps explicitly (g, h, f)
* Use diagrams if allowed
* Mention **uncertainty** when relevant

---
