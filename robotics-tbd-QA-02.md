
---

# **1. Revision Robotics**

---

## **Part I – Fundamentals (5 pts)**

### **Q1 (2 pts)**

Explain the **Perception–Decision–Action loop** and give one concrete robotics example.

---

### **Q2 (3 pts)**

Compare the following architectures:

* Reactive
* Sense–Plan–Act
* Hybrid

 Include:

* Advantages
* Limitations
* Use cases

---

## **Part II – A* Algorithm (7 pts)**

### **Q3 (Step-by-step A*) (5 pts)**

Given:

Edges:

* S → A (1), S → B (5)
* A → C (2), B → C (1)
* C → G (3)

Heuristic:

* h(S)=6, h(A)=4, h(B)=2, h(C)=1, h(G)=0

---

### Tasks:

1. Compute **g(n), h(n), f(n)**
2. Show **open list evolution**
3. Give **final path and cost**

---

### **Q4 (2 pts)**

Is this heuristic admissible? Justify.

---

## **Part III – Navigation & SLAM (5 pts)**

### **Q5 (2 pts)**

Explain the difference between:

* Localization
* Mapping
* SLAM

---

### **Q6 (3 pts)**

A robot uses odometry only.

1. What is the main issue?
2. How can it be corrected?
3. Name one probabilistic method

---

## **Part IV – Design Problem (3 pts)**

### **Q7 (3 pts)**

Design a navigation system for a robot in a **dynamic indoor environment**.

Include:

* Architecture
* Localization method
* Planning algorithm
* Obstacle avoidance

---

---

#  **Solutions – Mock Exam**

---

## **Q1 Solution**

Loop:

1. Perception (sensor data)
2. Decision (choose action)
3. Action (execute)

Example: robot detects obstacle → decides to turn → moves

---

## **Q2 Solution**

| Architecture   | Pros     | Cons        | Use         |
| -------------- | -------- | ----------- | ----------- |
| Reactive       | Fast     | No planning | Dynamic env |
| Sense–Plan–Act | Optimal  | Slow        | Static env  |
| Hybrid         | Balanced | Complex     | Real robots |

---

## **Q3 Solution (A*)**

### Step 1:

S: g=0, f=6

Open = {S}

---

### Step 2: Expand S

* A: g=1, f=5
* B: g=5, f=7

Open = {A(5), B(7)}

---

### Step 3: Expand A

* C: g=3, f=4

Open = {C(4), B(7)}

---

### Step 4: Expand C

* G: g=6, f=6

Open = {G(6), B(7)}

---

### Step 5: Expand G → STOP

---

###  Path:

S → A → C → G

Cost = 6

---

## **Q4 Solution**

Check:

* h(n) ≤ real cost

All values respect constraint →  admissible

---

## **Q5 Solution**

* Localization: robot pose
* Mapping: environment
* SLAM: both simultaneously

---

## **Q6 Solution**

1. Problem: drift
2. Fix: sensors (LiDAR, vision)
3. Method: Particle Filter

---

## **Q7 Solution**

* Architecture: Hybrid
* Localization: AMCL
* Planning: A*
* Obstacle avoidance: DWA

---

---

# **2. Full Worked Example (SLAM + A* + Control)**

---

## **Scenario**

A robot must navigate from **Start → Goal** in an **unknown indoor environment**.

---

## **Step 1: Perception**

Sensors:

* LiDAR → distances
* Odometry → motion

---

## **Step 2: SLAM**

Robot builds map while localizing:

### Map (Occupancy Grid)

* Cells = free / occupied

### Localization (Particle Filter)

Each particle = hypothesis of robot pose

Update:

[
Bel(x_t) = P(x_t | z, u)
]

---

## **Step 3: Mapping Output**

Robot obtains:

* Partial grid map
* Estimated pose

---

## **Step 4: Path Planning (A*)**

Grid example:

```
S . . X .
. X . X .
. . . . G
```

A* computes shortest path avoiding obstacles

---

### A* Result

Path:
S → right → down → right → G

---

## **Step 5: Local Navigation**

Obstacle suddenly appears → replan locally

Use:

* Dynamic Window Approach

---

## **Step 6: Control**

Convert path → motion:

### Example: PID

[
u = K_p e + K_i \int e + K_d \frac{de}{dt}
]

Robot adjusts:

* Speed
* Orientation

---

## **Final Pipeline**

**Sensors → SLAM → Map → A* → Local planner → Control**

---

##  Key Insight

This is exactly how **real robots operate**:

* Global planning (A*)
* Local adaptation
* Continuous correction via SLAM

---

# **3. Cheat Sheet (Formulas Only)**

---

## **A* Algorithm**

[
f(n) = g(n) + h(n)
]

[
g(v) = g(n) + d(n,v)
]

Admissibility:

[
h(n) \leq h^*(n)
]

---

## **MDP**

[
(S, A, P, R)
]

---

## **Reinforcement Learning**

[
Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max Q(s',a') - Q(s,a)]
]

---

## **Probability (Bayes)**

[
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
]

---

## **Localization (Belief State)**

[
Bel(x_t) = P(x_t | z_{1:t}, u_{1:t})
]

---

## **Kalman Filter**

Prediction:

[
x_t = A x_{t-1} + B u_t
]

Update:

[
K = P H^T (H P H^T + R)^{-1}
]

---

## **PID Control**

[
u = K_p e + K_i \int e + K_d \frac{de}{dt}
]

---

## **Motion Model**

[
x' = x + v \cos(\theta)\Delta t
]

[
y' = y + v \sin(\theta)\Delta t
]

---

## **Euclidean Distance**

[
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}
]

---

## **Manhattan Distance**

[
d = |x_1-x_2| + |y_1-y_2|
]

---
