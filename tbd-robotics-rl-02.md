
---

#  Robitics RL Revision

## Lecture 2: Reinforcement Learning (Fully Unified Clean Notes)

### Laëtitia Matignon – SyCoSMA team, LIRIS Lab

---

# 1. Different Types of Learning

Machine learning is commonly divided into three paradigms:

## 1.1 Supervised Learning

Learns a mapping:
[
X \rightarrow Y
]

* Data: labeled examples ((X_k, Y_k))
* Assumption: (Y = f(X))

### Tasks:

* classification
* regression

### Key idea:

Learning by instruction.

---

## 1.2 Unsupervised Learning

Learns structure in data:
[
(X_k)_k
]

* No labels
* Finds hidden patterns

### Tasks:

* clustering (k-means)
* dimensionality reduction (t-SNE)
* anomaly detection

### Key idea:

Learning by observation.

---

## 1.3 Reinforcement Learning (RL)

Learns a policy:
[
\pi: S \rightarrow A
]

### Key ingredients:

* state (s)
* action (a)
* reward (r)

### Key idea:

Learning by trial and error through interaction.

---

# 2. History of Reinforcement Learning

RL is the intersection of:

## 2.1 Experimental Psychology

* Pavlovian conditioning
* Operant conditioning (Skinner box)
* Thorndike’s law of effect:

  > actions followed by reward are reinforced

---

## 2.2 Optimal Control Theory

Goal:

* maximize performance of dynamical system

→ introduces Markov Decision Processes (MDP)

---

# 3. Planning Reminders (MDP Known)

## 3.1 MDP definition

[
\langle S, A, T, R \rangle
]

* transition: (T(s,a,s'))
* reward: (R(s,a,s'))

---

## 3.2 Objective

Find optimal policy:
[
\pi^*
]

that maximizes discounted return:
[
G_t = \sum_{t=0}^{\infty} \gamma^t r_{t+1}
]

---

## 3.3 Value function

[
V^\pi(s) = \mathbb{E}_\pi[G_t | s_0 = s]
]

---

## 3.4 Bellman equation

[
V^\pi(s) =
\sum_{s'} T(s,\pi(s),s')
\left[ R + \gamma V^\pi(s') \right]
]

---

## 3.5 Bellman optimality

[
V^*(s) = \max_a \sum_{s'} T(s,a,s')[R + \gamma V^*(s')]
]

---

## 3.6 Planning algorithms

### Value Iteration:

[
V_{k+1}(s) = \max_a \sum_{s'} T(s,a,s')[R + \gamma V_k(s')]
]

### Policy Iteration:

* evaluate (V^\pi)
* improve policy greedily

---

# 4. Basic Notions in Reinforcement Learning

## 4.1 Key difference from planning

In RL:

* (T) and (R) are unknown

So:

* cannot plan directly
* must learn from interaction

---

## 4.2 RL loop

At each step:
[
(s_t, a_t, r_{t+1}, s_{t+1})
]

---

## 4.3 Episodes

Sequence:
[
s_0 \rightarrow s_1 \rightarrow ... \rightarrow terminal
]

---

## 4.4 Model-based vs model-free

### Model-based:

* learn (T, R)
* then plan

### Model-free:

* directly learn policy or value

---

# 5. Passive Reinforcement Learning

Policy is fixed: (\pi)

Goal:
[
\text{evaluate } V^\pi
]

---

## 5.1 Monte Carlo Prediction

Estimate return:
[
v(s) = r_1 + \gamma r_2 + ...
]

### Update:

[
V(s) \leftarrow V(s) + \alpha (v(s) - V(s))
]

### Pros:

* unbiased
* simple

### Cons:

* high variance
* requires full episodes

---

## 5.2 Incremental mean

[
V_k = V_{k-1} + \frac{1}{k}(v_k - V_{k-1})
]

or:

[
V \leftarrow V + \alpha (v - V)
]

---

## 5.3 Temporal Difference (TD)

Bootstrap idea:

[
v(s) = r + \gamma V(s')
]

### TD update:

[
V(s) \leftarrow V(s) + \alpha (r + \gamma V(s') - V(s))
]

### Properties:

* online
* low variance
* biased but efficient

---

# 6. Active Reinforcement Learning

Policy is no longer fixed.

Goal:
[
\pi^*
]

---

## 6.1 Action-value function

[
Q(s,a)
]

[
V(s) = \max_a Q(s,a)
]

---

## 6.2 Greedy policy

[
\pi(s) = \arg\max_a Q(s,a)
]

---

## 6.3 Q-learning update

[
Q(s,a) \leftarrow Q(s,a) +
\alpha (r + \gamma \max_b Q(s',b) - Q(s,a))
]

---

## 6.4 Exploration vs exploitation

* exploitation: best known action
* exploration: try new actions

---

## 6.5 ε-greedy policy

[
\pi =
\begin{cases}
\text{random} & \epsilon \
\arg\max Q & 1-\epsilon
\end{cases}
]

---

## 6.6 Q-learning properties

Converges if:

* finite MDP
* all pairs visited infinitely often
* proper learning rate

---

## 6.7 Robot example

* state size: 2187
* actions: forward / left / right
* reward:

  * −10 collision
  * +3 forward movement

---

# 7. Generalization in RL

## 7.1 Problem of tabular RL

### Issues:

* memory explosion
* slow learning
* no generalization
* discretization difficulty

---

# 8. State Aggregation

## 8.1 Idea

Group similar states.

Methods:

* expert rules
* symmetry
* clustering
* discretization

---

## 8.2 Limitation

Must preserve Markov property:

* same aggregated state → same optimal action

---

## 8.3 Continuous control example

### Inverted pendulum:

[
s = (\theta, \dot{\theta})
]

### Cart-pole:

[
s = (x, \dot{x}, \theta, \dot{\theta})
]

---

## 8.4 Limits

* requires expert knowledge
* risk of losing optimality
* no true generalization

---

# 9. Function Approximation (Generalization)

## 9.1 Idea

Replace table:
[
Q(s,a)
]

with function:
[
Q_w(s,a)
]

---

## 9.2 Linear approximation

[
Q_w(s,a) = \sum_i w_i f_i(s,a)
]

* (f_i): features
* (w_i): weights

---

## 9.3 Benefits

* small memory
* generalization
* works in continuous spaces

---

## 9.4 Feature design

Examples:

* height
* holes
* distance to goal
* robot sensors

---

# 10. Approximate Q-learning

## 10.1 Target

[
y = r + \gamma \max_b Q_w(s',b)
]

---

## 10.2 Loss

[
E = \frac{1}{2}(y - Q_w(s,a))^2
]

---

## 10.3 Gradient

[
\frac{\partial E}{\partial w_i}
= -(y - Q_w(s,a)) f_i(s,a)
]

---

## 10.4 Update rule

[
w_i \leftarrow w_i + \alpha (y - Q_w(s,a)) f_i(s,a)
]

---

## 10.5 Interpretation

* TD error drives learning
* weights adjust feature importance

---

# END OF CLEANED LECTURE

---

# 📚 2. Tutorial Exercises (Reconstructed from Slides)

## Exercise 1 — Bellman Equation (Value Computation)

Given:

* states (s_1, s_2, s_3)
* deterministic transitions
* rewards:

  * (s_3) is terminal with reward +1
* discount: (\gamma = 0.9)

### Tasks:

1. Compute (V^\pi(s_3))
2. Compute (V^\pi(s_2))
3. Compute (V^\pi(s_1))

---

## Exercise 2 — Value Iteration

Gridworld:

* 3×3 grid
* terminal state at (3,3)
* reward = +1 at terminal
* γ = 0.9
* initial (V_0(s)=0)

### Tasks:

1. Compute (V_1)
2. Compute (V_2)
3. Interpret propagation of values

---

## Exercise 3 — Monte Carlo Prediction

Given episodes:

Episode 1:

* rewards: [0, 0, 0, 1]

Episode 2:

* rewards: [0, 0, 0, -1]

### Tasks:

1. Compute returns (v(s))
2. Compute (V(s)) using:

   * averaging
   * incremental update

---

## Exercise 4 — TD Learning

Given:

* α = 0.1
* γ = 1

Episode:
[
(1,1)\rightarrow(1,2)\rightarrow(1,3)\rightarrow terminal
]

Rewards:

* all 0 except final +1

### Tasks:

1. Compute TD updates step-by-step
2. Show evolution of (V(s))

---

## Exercise 5 — Q-learning

Given:

* states A, B, C
* actions left/right
* reward at C = +1

### Tasks:

1. Write Q-learning update
2. Perform 3 iterations
3. Explain convergence behavior

---

## Exercise 6 — ε-greedy policy

Given Q-values:

* Q(s,a1)=5
* Q(s,a2)=3
* Q(s,a3)=1
* ε = 0.2

### Tasks:

1. probability of each action
2. expected behavior (explore vs exploit)

---

## Exercise 7 — Feature-based Q-learning

Given features:

* f1 = distance to goal
* f2 = obstacle indicator

### Tasks:

1. write Qw(s,a)
2. explain role of weights
3. perform one gradient update

---
