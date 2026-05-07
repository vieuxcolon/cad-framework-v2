# Introduction to Multi-Robot Planning

## Centralized vs. Decentralized Approaches

**Olivier Simonin**
INSA Lyon – CITI Lab / Inria Chroma Team

---

# Outline

1. Centralized vs. Distributed Decision
2. Multi-Robot Path Planning
3. Planning Among Movable Obstacles (NAMO)

---

# 1. Centralized vs. Distributed Decision

---

# 1.1 Coordination in Multi-Robot Systems

Multi-robot systems must coordinate:

* **Who** performs a task
* **Where** the task is performed
* **When** actions are executed

---

## Application Domains

### Tasks

* Transport
* Surveillance
* Exploration
* Rescue
* Assistance

### Environments

* Factories
* Cities
* Post-disaster environments
* Home and human environments

---

# 1.2 Classification of Mobile Robotic Tasks

---

## Exploration

* Mapping (e.g., SLAM)
* Search
* Coverage
* Patrolling

---

## Transport

* Traffic regulation
* Autonomous vehicles
* AGV systems (Automated Guided Vehicles)

---

## Monitoring

* Tracking
* Active perception

---

## Coordination Problems

* Multi-robot coordination
* Network connectivity
* Navigation in formation

---

# 1.3 Formalizing Objectives

Robotics tasks are often formulated as optimization problems.

---

## Multi-Robot Path Planning

Objective examples:

[
\min \left( \sum_i path_i \right)
]

or

[
\min \left( \max(path_0, ..., path_n) \right)
]

Applications:

* Vehicle Routing Problem (VRP)
* Multi-Robot Routing (MRR)

---

## Multi-Robot Coordination

Avoid collisions:

[
\forall t,\ \nexists (r_i, r_j) : loc(r_i) = loc(r_j)
]

Meaning:

* no two robots occupy the same location at the same time.

---

## Coverage

Maximize perceived area:

[
\max \bigcup_i Percep_i
]

---

## Exploration and Mapping

Goal:
minimize exploration time until the environment is fully observed.

---

# 1.4 Multi-Agent Systems (MAS)

---

## Definition

A **Multi-Agent System (MAS)** is:

> A set of autonomous entities interacting in a common environment to achieve collective and/or individual objectives.

Agents may:

* Cooperate
* Coordinate
* Compete

---

## Perspectives

### Collective Perspective

* Shared reward
* Global objective

### Individual Perspective

* Local reward
* Individual objective

---

Reference:
J. Ferber, *Multi-Agent Systems*, Addison Wesley, 1999

---

# 1.5 Agent Architectures

---

# A. Deliberative Architecture (Planning)

## Principle

The agent:

1. Perceives the environment
2. Builds an environment model
3. Plans actions
4. Executes actions

---

## Methods

* STRIPS
* PDDL
* SAT
* CSP
* Ant Colony Optimization (ACO)

---

## Advantages

* Structured reasoning
* Can approach optimal solutions

---

## Limitations

* Computationally expensive
* Slow in complex environments

---

# B. Reactive Architecture

## Principle

Direct:
[
\text{Perception} \rightarrow \text{Action}
]

without explicit planning.

---

## Methods

* Bio-inspired behaviors
* Connectionism
* Flocking / Particle Swarm Optimization (PSO)
* Pheromone-based systems

---

## Advantages

* Real-time behavior
* Scalable
* Robust in dynamic environments

---

## Limitations

* Often sub-optimal
* Limited long-term reasoning

---

# C. Learning-Based Architecture

## Principle

Agents learn a policy using:

* rewards,
* interactions,
* experience.

---

## Methods

* Reinforcement Learning (RL)
* (PO)MDP
* CNNs
* Deep Reinforcement Learning

---

## Trade-Off

| Approach | Strength   | Weakness               |
| -------- | ---------- | ---------------------- |
| Planning | Optimality | Time-consuming         |
| Reactive | Real-time  | Sub-optimal            |
| Learning | Adaptivity | Requires training/data |

---

# 1.6 Centralized, Decentralized and Distributed Systems

---

# Centralized System

A central controller:

* collects information,
* computes decisions,
* sends commands to agents.

### Advantages

* Global coordination
* Potentially optimal decisions

### Limitations

* Communication bottleneck
* Poor scalability
* Single point of failure

---

# Decentralized / Distributed Systems

Each robot:

* computes locally,
* communicates partially,
* coordinates with neighbors.

---

## Self-Organized Systems

Examples:

* Kilobots
* UAV flocking systems
* Self-configurable robots
* Programmable matter

Characteristics:

* local interactions,
* emergent collective behavior,
* scalability.

---

# 1.7 Communication Complexity

---

## Centralized / Distributed Systems

Communication examples:

* one-to-one,
* one-to-many,
* ad hoc networks,
* Wi-Fi communication.

---

## Networked Robotics

Robots rely on communication for:

* coordination,
* synchronization,
* navigation.

---

## Swarm Robotics

Communication is often:

* local,
* indirect,
* bio-inspired.

Example:

* pheromone-like signaling.

---

# 1.8 Constraints of Real Environments

Real robotic systems face:

* Uncertain communication
* Limited bandwidth
* Sensor uncertainty
* Action uncertainty
* Dynamic environments
* Humans and moving obstacles

---

# 1.9 Summary: Computational Complexity

---

## Known Environments

### Centralized Systems

* Offline planning
* Can converge to optimality
* Risk of combinatorial explosion

### Decentralized Systems

* Coordination heuristics
* Online planning
* Often non-optimal

---

## Unknown Environments

### Learning Approaches

* Learn policies/environment models
* Require data and repeated experience

---

# Key Trade-Off

| Objective       | Difficulty                  |
| --------------- | --------------------------- |
| Solve optimally | Computationally expensive   |
| Solve quickly   | Often heuristic/sub-optimal |

---

# 2. Multi-Robot Path Planning

---

# 2.1 MAPF — Multi-Agent Path Finding

Goal:
plan paths for multiple robots while:

* minimizing distance or time,
* avoiding collisions.

---

## Navigation Topology

Typically:

* 2D grids,
* graphs,
* roadmaps.

---

## Collision Constraint

[
\forall t,\ \nexists (r_i,r_j): loc(r_i)=loc(r_j)
]

No two robots may occupy the same position simultaneously.

---

# 2.2 Centralized Planning with Repair

---

## General Principle

1. Compute paths for all robots (e.g., A*)
2. Detect collisions
3. Repair conflicts
4. Execute plans

---

## Collision Resolution

Possible repairs:

* add delays,
* replan paths,
* prioritize robots.

---

## Example Algorithm

Reference:
van den Berg (2009)

Procedure:

1. Compute (n) paths
2. Detect collisions
3. Resolve pairwise conflicts
4. Execute trajectories

---

## Limitations

Questions:

* Is the method complete?
* Does it always find a solution?
* What is the computational cost?

---

# 2.3 MAPF Optimal Algorithms

Examples:

* Cooperative A* (CA*)
* EPEA*
* Conflict-Based Search (CBS)

---

## Conflict-Based Search (CBS)

Reference:
Sharon, Stern, Felner, Sturtevant, AAAI 2012

Main idea:

* separate path planning from conflict resolution,
* iteratively resolve conflicts.

---

## Other Approaches

### NMPC

Nonlinear Model Predictive Control

Used for:

* continuous trajectories,
* dynamic constraints.

---

# 2.4 Distributed Online Approach

Instead of global planning:

each robot plans independently.

---

## Distributed Planning Procedure

Each robot:

1. Computes or updates its path (A*)
2. Receives paths from others
3. Predicts future collisions
4. Resolves conflicts locally
5. Sends updated path
6. Executes one step

---

## Collision Resolution

Typical methods:

* priority rules,
* adding delays,
* replanning.

---

## Important Issue

Need to avoid:

* symmetrical decisions,
* oscillations,
* deadlocks.

---

# Advantages of Distributed Approaches

* Better scalability
* More robust
* Suitable for dynamic environments

---

# Limitations

* Harder to guarantee optimality
* Coordination complexity
* Communication uncertainty

---

# 3. Planning Among Movable Obstacles (NAMO)

*(Section announced but not detailed in these notes.)*

NAMO:

* Navigation Among Movable Obstacles

Idea:

* robots may move obstacles to achieve navigation goals.

Challenges:

* reasoning about manipulation + navigation together,
* increased planning complexity.

---

# Key Takeaways

* Multi-robot systems require coordination in space and time.
* Decision-making may be:

  * centralized,
  * decentralized,
  * distributed.
* Planning approaches trade:

  * optimality,
  * computation time,
  * scalability.
* MAPF focuses on:

  * collision-free,
  * efficient multi-robot navigation.
* Distributed approaches improve scalability but complicate coordination.
