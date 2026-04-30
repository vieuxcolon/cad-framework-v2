
---

# **Robotics – Decision Making, Planning, and Navigation**

*INSA Lyon – CITI Lab / Inria Chroma Team*

---

# **1. Foundations of Robotics**

## **1.1 What is a Robot?**

### **Automaton**

* Executes predefined instructions
* Operates in structured environments
* Limited adaptability

### **Autonomous Robot**

* Adapts to dynamic environments
* Operates using a continuous loop:

 **Perception → Decision → Action**

---

### **Origin of the Term**

* From Czech *“robota”* (forced labor)
* Introduced by **Karel Čapek (1921)**

---

## **1.2 Evolution of Robotics**

* Antiquity: mechanical automata
* 18th century: complex mechanical systems
* 20th century: electronics and computing
* Today: AI-driven autonomous systems

---

## **1.3 Types of Robots**

### **Mobile Robots**

* Wheeled platforms (e.g., TurtleBot)

### **Legged Robots**

* Quadrupeds, hexapods

### **Humanoids**

* Designed for human environments

### **Autonomous Vehicles**

* Self-driving systems

### **Aerial Robots (UAVs)**

* Drones operating in 3D

### **Soft & Modular Robots**

* Flexible, bio-inspired systems

---

## **1.4 Intelligence in Robotics**

A robot is considered intelligent if it can:

* Build **world representations**
* **Adapt** to changing environments
* **React in real time**
* Interact socially
* Cooperate with other agents

---

## **1.5 AI Approaches in Robotics**

### **Symbolic AI**

* Logic-based reasoning
* Planning algorithms

### **Machine Learning**

* Neural networks
* Reinforcement learning

 No universal solution — methods depend on constraints:

* Limited computation
* Noisy sensors
* Real-time requirements

---

# **2. Decision Making in Robotics**

## **2.1 Core Decision Problem**

A robot must decide:

* Which **actions** to execute
* How to **avoid risks and failures**
* How to **interact with others**

---

## **2.2 The Perception–Decision–Action Loop**

**Environment → Sensors → Perception → Decision → Action → Environment**

### Components

* **Perception**: interpret sensor data
* **Decision-making**: choose actions
* **Control**: execute actions

---

## **2.3 Situation Awareness**

Requires:

* Environment modeling
* State estimation
* Future prediction

---

### Example: Occupancy Grid Mapping

[
P_{occ}(x,y) = \frac{occ(x,y)}{occ(x,y) + empty(x,y)}
]

Enhancements:

* Motion estimation
* Object detection
* Prediction

---

### Example: Social Navigation

* Human detection and tracking
* Motion prediction
* Respect of personal space (proxemics)

---

## **2.4 Decision Paradigms**

### **Reactive**

* Immediate response
* No planning

### **Planning**

* Sequence of actions

### **Learning**

* Policy learned from experience

### **Multi-Agent Systems**

* Cooperation / competition

---

## **2.5 Methods Overview**

* Reactive: bio-inspired
* Planning: STRIPS, PDDL, PRM
* Learning: RL, (PO)MDP, Deep Learning

---

# **3. Decision Architectures**

## **3.1 Sense–Plan–Act**

Pipeline:

1. Perception
2. Modeling
3. Planning
4. Execution

❗ Limitation: slow in dynamic environments

---

## **3.2 Reactive Architectures**

### Principle

* Direct sensor → action

### Pros

* Fast, robust

### Cons

* No long-term reasoning

---

### Examples

**Braitenberg Vehicles**

* Simple sensor-action coupling

**Subsumption Architecture**

* Layered behaviors with priorities

---

## **3.3 Hybrid Architectures**

Combine:

* Reactive layer (fast)
* Planning layer (deliberative)

 Most common in modern robotics

---

# **4. Learning-Based Approaches**

## **4.1 Reinforcement Learning**

Learn:

[
Q(s,a)
]

* Trial-and-error learning
* Converges to optimal policy

---

### Exploration vs Exploitation

* Exploration: discover
* Exploitation: optimize

---

## **4.2 Markov Decision Processes**

[
(S, A, P, R)
]

* Models uncertainty
* Foundation for RL

---

## **4.3 Deep Learning**

### End-to-End Learning

* Direct perception → action

### CNNs

* Extract visual features

### Deep RL

* Scales to complex environments

---

# **5. Path Planning: A* Algorithm**

## **5.1 Objective**

Find optimal path:

[
r \rightarrow t
]

---

## **5.2 Evaluation Function**

[
f(n) = g(n) + h(n)
]

* (g(n)): known cost
* (h(n)): estimated cost

---

## **5.3 Heuristic**

Admissible if:

[
h(n) \leq h^*(n)
]

 Guarantees optimality

---

## **5.4 Algorithm Summary**

1. Initialize open list
2. Select node minimizing (f(n))
3. Expand neighbors
4. Update costs
5. Stop at goal

---

## **5.5 Properties**

* Optimal with admissible heuristic
* Efficient vs Dijkstra

---

## **5.6 Variants**

* IDA*
* RBFS
* SMA*

---

# **6. Robotics Navigation (NOMA)**

---

## **6.1 Definition of Navigation**

Navigation enables a robot to:

* **Localize itself**
* **Understand the environment**
* **Reach a goal safely**

 Pipeline:

**Perception → Localization → Mapping → Planning → Control**

---

## **6.2 The Three Core Problems**

### **1. Localization**

Estimate robot pose:

[
(x, y, \theta)
]

---

### **2. Mapping**

Represent the environment:

* Occupancy grids
* Topological maps

---

### **3. Planning**

Compute collision-free paths

---

## **6.3 Navigation Levels**

### **Global Planning**

* Compute path (A*, PRM, RRT)

---

### **Local Navigation**

* Avoid obstacles
* React in real time

Methods:

* Potential fields
* Dynamic Window Approach

---

### **Motion Control**

* Execute trajectory

Examples:

* PID
* Pure Pursuit

---

## **6.4 Map Representations**

### **Metric Maps**

* Accurate but memory-heavy

### **Topological Maps**

* Compact but abstract

### **Hybrid Maps**

* Combine both

---

## **6.5 Localization Techniques**

### **Odometry**

* Simple but drifts

---

### **Sensor-Based**

* LiDAR, cameras, IMU

---

### **Probabilistic Methods**

[
Bel(x_t) = P(x_t | z_{1:t}, u_{1:t})
]

* Kalman Filter
* Particle Filter

---

## **6.6 SLAM**

### Definition

Simultaneous Localization and Mapping

---

### Methods

* EKF-SLAM
* Graph-based SLAM
* Visual SLAM

---

### Challenges

* Noise
* Drift
* Loop closure

---

## **6.7 Advanced Planning in Navigation**

### Graph-Based

* A*, Dijkstra

### Sampling-Based

* PRM, RRT

### Trajectory Planning

* Considers dynamics

---

## **6.8 Obstacle Avoidance**

### Reactive

* Potential fields

### Dynamic Environments

* Prediction + re-planning

### Social Navigation

* Human-aware movement

---

## **6.9 Navigation Architectures**

Layered system:

1. Perception
2. Localization & Mapping
3. Planning
4. Control

 Example: ROS Navigation Stack

---

## **6.10 Challenges in Navigation**

* Uncertainty
* Dynamic environments
* Real-time constraints
* Scalability

---

## **6.11 Link with Decision Architectures**

| Concept  | Role               |
| -------- | ------------------ |
| Reactive | Obstacle avoidance |
| Planning | Path computation   |
| Learning | Adaptation         |

 Modern navigation = **hybrid intelligence**

---

# **7. Global Key Takeaways**

* Robotics integrates:

  * Mechanics
  * Electronics
  * AI

---

### Core Principle

 **Perception → Decision → Action**

Extended to:

 **Perception → Localization → Mapping → Planning → Control**

---

### Main Paradigms

* Reactive → fast but limited
* Planning → optimal but slower
* Learning → adaptive

---

### Key Algorithms

* A* for path planning
* SLAM for mapping + localization
* RL for adaptive behavior

---

### Final Insight

Modern robotics systems are:

 **Hybrid, probabilistic, and increasingly learning-driven**

---
