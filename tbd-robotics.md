
---
# **Architectures for Decision Making in Robotics**
---

*From reactive to learning-based approaches*
INSA Lyon – CITI Lab / Inria Chroma Team

---

# **1. What is Decision Making in Robotics?**

## **1.1 What does a robot need to decide?**

A robot must continuously decide:

* Which **actions** to execute to achieve its task
* How to **avoid collisions, risks, or failures**
* How to **interact or cooperate** with other robots or humans

👉 Core idea:
**Perception of the situation → Decision → Action**

---

## **1.2 The Perception–Decision–Action Loop**

A robot operates in a continuous loop:

**Environment → Sensors → Perception → Decision → Action → Environment**

Key components:

* **Perception**: understanding the environment
* **Decision-making (AI)**: selecting actions
* **Control**: executing actions

---

## **1.3 Situation Awareness**

To make decisions, a robot must:

* **Model the environment**
* **Estimate the current state**
* **Predict future states**

### Example 1: Probabilistic Grid Mapping

* **Occupancy Grid**: each cell has a probability of being occupied
* Uses **Bayesian filtering**

Formula example:
[
P_{occ}(x,y) = \frac{occ(x,y)}{occ(x,y) + empty(x,y)}
]

Enhancements:

* Velocity estimation per cell
* Object detection via clustering
* Motion prediction

---

### Example 2: Social Navigation (Proxemics)

Robots interacting with humans must:

* Detect and track people
* Predict their motion
* Respect **social distances**

Approach:

* Gaussian models of personal space
* Activity mapping
* Safe path planning

---

## **1.4 Decision Paradigms**

### **Reacting**

* Immediate action based on current perception
* Real-time, no long-term planning

### **Planning**

* Computes a **sequence of actions**
* Example: motion planning

### **Learning**

* Learns a **policy (state → action)**
* Improves with experience

### **Multi-agent considerations**

* Cooperation or competition with other agents

---

## **1.5 Methods Overview**

* **Reactive**: bio-inspired, connectionist approaches
* **Planning**: STRIPS, PDDL, SAT, CSP, PRM
* **Learning**: Reinforcement Learning, (PO)MDP, RNNs, Deep Learning

---

# **2. Classical Architectures**

## **2.1 Sense–Plan–Act Architecture**

(Nils Nilsson, 1980)

### Pipeline:

1. Perception
2. Modeling
3. Planning
4. Decision
5. Execution control

### Limitation:

* **Slow planning → bottleneck**
* Not suitable for dynamic environments

---

## **2.2 Reactive Architectures**

(Rodney Brooks, Ronald Arkin)

### Key idea:

* Direct **sensor → action mapping**
* No explicit world model

### Advantages:

* Fast and robust
* Works well in dynamic environments

### Limitation:

* Can lead to **deadlocks**
* No long-term reasoning

---

### Examples

#### **Braitenberg Vehicles**

(Valentino Braitenberg)

* Simple sensor-motor connections
* Example: phototaxis (moving toward light)

---

#### **Subsumption Architecture (Brooks)**

* Multi-layer system with **priorities**
* Higher layers can override lower ones

Example behaviors:

* Avoid obstacles
* Seek goals
* Explore

---

### Example Exercise: Pac-Man Robot

Goal: collect pellets in a maze

Possible rule hierarchy:

1. If pellet nearby → pick up
2. If pellet perceived → go to it
3. If wall ahead & left → turn right
4. If wall ahead → turn left
5. Default → move forward

---

## **2.3 Hybrid (Multi-level) Architectures**

Combine:

* **Reactive layer** (fast response)
* **Planning layer** (deliberation)

### Benefits:

* Balances **speed and intelligence**
* Most common architecture in robotics

---

# **3. Learning-Based Architectures**

## **3.1 General Idea**

* No explicit programming of behavior
* Robot **learns from interaction**

Components:

* State
* Action
* Reward
* Memory

Techniques:

* Neural networks
* Reinforcement learning
* Markov Decision Processes

---

## **3.2 Reinforcement Learning (Q-Learning)**

(Christopher Watkins, 1989)

### Principle:

Learn the **quality (Q-value)** of actions:
[
Q(s,a)
]

Update rule:

* Agent takes action
* Receives reward
* Updates Q-values

### Outcome:

* Converges to an **optimal policy**

---

### Exploration vs Exploitation

* **Exploration**: try new actions
* **Exploitation**: use known best actions

This trade-off is fundamental.

---

## **3.3 Markov Decision Processes (MDP)**

An MDP is defined by:
[
(S, A, P, R)
]

Where:

* (S): states
* (A): actions
* (P(s'|s,a)): transition probabilities
* (R): rewards

👉 Important:

* Handles **uncertainty** in robotics

---

## **3.4 Deep Learning Approaches**

### End-to-End Learning

* Single neural network maps:
  **input → action**

* Uses backpropagation

---

### Convolutional Neural Networks (CNNs)

* Extract features from images
* Enable generalization

---

### Deep Reinforcement Learning

* Combines RL + deep networks
* Handles complex environments

Example:

* Learning navigation and mapping
* Predicting direction and distance to targets

---

# **4. Key Takeaways**

* Robotics decision-making relies on the **Perception–Decision–Action loop**
* Three main paradigms:

  * Reactive (fast, simple)
  * Planning (structured, slower)
  * Learning (adaptive, data-driven)
* Modern systems often combine all three
* Learning-based approaches are increasingly dominant, especially with deep learning

---
