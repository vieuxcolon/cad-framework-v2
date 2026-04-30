
---

#  Tutorial 1 — Reinforcement Learning (Clean Version)

INSA Lyon — Computer Science
Master MINDS — Robotics
Laëtitia Matignon

---

# 1. Overview

This tutorial introduces the fundamental reinforcement learning methods for **value estimation** and **control**:

* Monte-Carlo prediction
* Incremental Monte-Carlo
* Temporal Difference (TD) learning
* Q-learning
* Greedy policies

We assume:

* Markov Decision Process (MDP)
* Discount factor ( \gamma \in [0,1] )
* Learning rate ( \alpha \in (0,1] )

---

# 2. Monte-Carlo Prediction

## 2.1 Principle

Monte-Carlo methods estimate the value of a state using **complete episodes**.

A sample return is:

[
v(s) = r_1 + \gamma r_2 + \gamma^2 r_3 + \cdots
]

---

## 2.2 Every-Visit MC

Each visit to state ( s ) contributes:

[
V(s) = \frac{1}{N(s)} \sum v(s)
]

where ( N(s) ) is number of visits.

---

## 2.3 Key Idea

✔ No bootstrapping
✔ Requires full episode
✘ High variance
✘ Slow learning

---

# 3. Incremental Monte-Carlo

Instead of storing all returns:

[
V(s) \leftarrow V(s) + \alpha (v(s) - V(s))
]

### Interpretation:

* Adjust estimate toward observed return
* Works online at end of episode

---

# 4. Temporal Difference Learning

## 4.1 TD(0) update

[
V(s) \leftarrow V(s) + \alpha \big(r + \gamma V(s') - V(s)\big)
]

### Key idea:

✔ Learns **during episode**
✔ Uses bootstrapping

---

## 4.2 TD error

[
\delta = r + \gamma V(s') - V(s)
]

Update:

[
V(s) \leftarrow V(s) + \alpha \delta
]

---

## 4.3 MC vs TD

| Method | Update time    | Bootstrap | Variance |
| ------ | -------------- | --------- | -------- |
| MC     | end of episode | No        | High     |
| TD     | every step     | Yes       | Lower    |

---

# 5. Q-Learning (Control)

## 5.1 Objective

Learn optimal action-value function:

[
Q^*(s,a)
]

---

## 5.2 Update rule

[
Q(s,a) \leftarrow Q(s,a) + \alpha \Big(r + \gamma \max_b Q(s',b) - Q(s,a)\Big)
]

---

## 5.3 Greedy policy

[
\pi(s) = \arg\max_a Q(s,a)
]

---

## 5.4 Exploration (implicit idea)

To avoid greedy traps:

* ε-greedy policy is typically used

---

# 6. Key Concepts Summary

## 6.1 Return

[
G_t = r_{t+1} + \gamma r_{t+2} + \cdots
]

## 6.2 Bootstrapping

Using estimates instead of full returns:

* TD uses ( V(s') )
* Q-learning uses ( \max Q(s',a) )

---

## 6.3 Learning hierarchy

| Method     | Learns                   |
| ---------- | ------------------------ |
| MC         | value from full episodes |
| TD         | value from next state    |
| Q-learning | optimal policy           |

---

# 7. Conceptual Questions (Typical Tutorial Style)

## Q1 — MC vs TD

Why is TD learning more efficient than Monte-Carlo?

**Answer:**

* TD updates before episode ends
* uses bootstrapping
* lower variance

---

## Q2 — Why Q-learning is off-policy?

Because:

[
\max_b Q(s',b)
]

is independent of actual action taken.

---

## Q3 — Why MC has high variance?

Because it depends on full trajectory randomness.

---

## Q4 — When is TD better than MC?

* long episodes
* continuing tasks
* stochastic environments

---

# 8. Core Intuition (Very Important)

### Monte-Carlo:

> “Learn from full experience”

### TD:

> “Learn from partial prediction”

### Q-learning:

> “Learn optimal behavior even while exploring”

---

# 9. What this tutorial is preparing you for

This lecture is the foundation for:

* Function approximation
* Deep Q-learning (DQN)
* Policy gradients
* Actor-critic methods

---
