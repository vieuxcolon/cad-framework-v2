
---

# Robotics – Reinforcement Learning (Clean Notes)

## 1. Introduction

### 1.1 What is an Agent?

An **agent** is an autonomous entity that:

* perceives its environment through **sensors**
* acts through **actuators**
* makes decisions to achieve a goal

 Interaction loop:
[
\text{Perception} \rightarrow \text{Decision} \rightarrow \text{Action}
]

* Observations: ( o_t )
* Actions: ( a_t )
* History: ( (o_0, a_0, ..., o_t) )

---

### 1.2 Rational Agent

A **rational agent** selects actions that maximize a **performance measure** based on its observations.

* Performance measure defines **what to achieve**, not how
* Example (vacuum robot): maximize number of clean cells over time

---

### 1.3 PEAS Framework

To define a task environment:

| Component | Description         |
| --------- | ------------------- |
| P         | Performance measure |
| E         | Environment         |
| A         | Actuators           |
| S         | Sensors             |

---

### 1.4 Environment Properties

| Property       | Types                        |
| -------------- | ---------------------------- |
| Observability  | Fully / Partially observable |
| Dynamics       | Deterministic / Stochastic   |
| Time           | Episodic / Sequential        |
| Evolution      | Static / Dynamic             |
| Representation | Discrete / Continuous        |
| Agents         | Single / Multi-agent         |

 Real-world robotics = **partially observable, stochastic, dynamic, continuous, multi-agent**

---

### 1.5 Planning vs Reality

* Classical planning (e.g., A*) assumes **deterministic world**
* Real robotics requires:

  * **uncertainty handling**
  * **re-planning**
  * **closed-loop control**

---

## 2. Markov Decision Process (MDP)

### 2.1 Definition

An MDP is defined by:

[
\langle S, A, T, R \rangle
]

* ( S ): set of states
* ( A ): set of actions
* ( T(s,a,s') = P(s'|s,a) ): transition function
* ( R(s,a,s') ): reward function

---

### 2.2 Markov Property

[
P(s_{t+1} | s_t, a_t, \dots) = P(s_{t+1} | s_t, a_t)
]

 The future depends only on the present.

---

### 2.3 Interaction Model

At each time step:
[
s_t \rightarrow a_t \rightarrow r_{t+1}, s_{t+1}
]

Trajectory:
[
s_0, a_0, r_1, s_1, a_1, r_2, ...
]

---

### 2.4 Objective

Maximize cumulative reward:

####  Undiscounted:

[
G = \sum_{t=0}^{\infty} r_{t+1}
]

####  Discounted:

[
G^\gamma = \sum_{t=0}^{\infty} \gamma^t r_{t+1}, \quad \gamma \in [0,1)
]

* ( \gamma \approx 0 ): short-term agent
* ( \gamma \approx 1 ): long-term agent

---

## 3. Policy

### 3.1 Definition

A **policy** defines the behavior:
[
\pi : S \rightarrow A
]

Types:

* Deterministic: one action per state
* Stochastic: probability distribution over actions

---

### 3.2 Optimal Policy

[
\pi^* = \arg\max_\pi \mathbb{E}[G^\gamma]
]

---

## 4. Value Function

### 4.1 State Value

[
V^\pi(s) = \mathbb{E}*\pi \left[ \sum*{t=0}^{\infty} \gamma^t r_{t+1} \mid s_0 = s \right]
]

 Expected return starting from state ( s )

---

### 4.2 Bellman Equation

[
V^\pi(s) = \sum_{s'} T(s,\pi(s),s') \left[ R(s,\pi(s),s') + \gamma V^\pi(s') \right]
]

---

### 4.3 Optimal Value Function

[
V^*(s) = \max_a \sum_{s'} T(s,a,s') \left[ R(s,a,s') + \gamma V^*(s') \right]
]

---

### 4.4 Policy Extraction

[
\pi^*(s) = \arg\max_a \sum_{s'} T(s,a,s') [R(s,a,s') + \gamma V^*(s')]
]

---

## 5. Solving an MDP

---

### 5.1 Value Iteration

Algorithm:

1. Initialize:
   [
   V_0(s) = 0
   ]

2. Iterate:
   [
   V_{k+1}(s) = \max_a \sum_{s'} T(s,a,s') \left[ R(s,a,s') + \gamma V_k(s') \right]
   ]

3. Stop when:
   [
   \max_s |V_{k+1}(s) - V_k(s)| < \epsilon
   ]

4. Extract policy

 Complexity: ( O(|S|^2 |A|) )

---

### 5.2 Policy Iteration

Repeat until convergence:

1. **Policy Evaluation**:
   [
   V^\pi(s) = \sum_{s'} T(s,\pi(s),s') [R + \gamma V^\pi(s')]
   ]

2. **Policy Improvement**:
   [
   \pi'(s) = \arg\max_a \sum_{s'} T(s,a,s')[R + \gamma V^\pi(s')]
   ]

---

### 5.3 Comparison

| Method           | Idea                             |
| ---------------- | -------------------------------- |
| Value Iteration  | Directly compute ( V^* )         |
| Policy Iteration | Alternate evaluation/improvement |

---

## 6. Extensions

---

### 6.1 Partial Observability (POMDP)

[
\langle S, A, T, R, \Omega, O \rangle
]

* ( \Omega ): observations
* ( O(s,o) = P(o|s) )

 Agent does not know exact state

---

### 6.2 Unknown Model

* ( T, R ) unknown
   leads to **Reinforcement Learning**

---

### 6.3 Multi-Agent Systems

[
\langle n, S, A, T, R \rangle
]

* Joint state: ( s = (s_1,...,s_n) )
* Joint action: ( a = (a_1,...,a_n) )

 Very hard (combinatorial explosion)

---

## 7. Application: Multi-Robot Exploration

### Problem

Autonomous robots must:

* explore unknown environment
* build a map (**SLAM**)
* coordinate efficiently

---

### Challenges

* Localization + mapping
* Decision-making (where to go next)
* Multi-agent coordination

---

### Approach

* One **local MDP per robot**
* Augmented state:

  * robot pose
  * map
  * other robots

---

### Key Idea

* Each robot:

  * solves its own MDP (value iteration)
  * updates policy in real-time
  * predicts others (implicit coordination)

---

### Result

* Decentralized exploration
* Reduced overlap
* Scalable multi-robot system

---

## 8. Key Takeaways

* MDP = foundation of decision-making under uncertainty
* Policy = solution
* Value function = evaluation tool
* Bellman equation = core principle
* Value/Policy iteration = main algorithms
* Extensions handle real-world complexity

---

## 9. Typical Pitfalls (Exam!)

* Forgetting discount factor ( \gamma )
* Mixing ( V^\pi ) and ( V^* )
* Ignoring stochastic transitions
* Confusing policy evaluation vs improvement
* Not writing Bellman equations correctly

---
