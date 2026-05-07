# Introduction to NAMO

## Navigation Among Movable Obstacles

**Olivier Simonin**
INSA Lyon & INRIA Lyon – CITI Lab – Équipe CHROMA

---

# 1. NAMO: Problem Definition

---

## Objective

Find a path from:

[
q_{init} \rightarrow q_{goal}
]

while minimizing:

* path length
* number of moved objects

---

## Key Idea

Unlike classical navigation, robots are allowed to:

> **move obstacles in the environment to reach the goal**

---

## Classical Approaches

* Stilman (2005)
* Wu & Levihn (2014)

---

# 2. NAMO Problem Structure

---

## Two-Level Planning Process

### Step 1 — Planning without obstacles

* Compute a path
* Identify blocking objects

---

### Step 2 — Object manipulation planning

* Decide which objects to move
* Plan how to move them
* Recompute navigation path

---

## Limitations of Classical NAMO

* High computational cost
* Poor scalability
* Ignores social constraints
* May produce unnatural environments

---

# 3. NAMO with Social Constraints

---

## Extended Objective

Optimize:

* access to space
* object placement quality
* human-friendly navigation

---

## Key Idea

> Not only reach the goal, but also place objects in socially meaningful positions.

---

# 3.1 Social Cost Map

---

## Purpose

Assign a **cost to every location** in the environment.

High cost means:

* undesirable placement for objects or robots

---

## Design Principles

### 1. Do not divide space

* Avoid blocking central areas

### 2. Do not block access

* Penalize narrow passages

---

## Construction Pipeline

1. Compute Voronoi skeleton
2. Compute distance to static obstacles
3. Project social cost onto skeleton
4. Generate full social cost map

---

## Result

A map encoding:

* spatial comfort
* accessibility
* human-aware placement quality

---

(Reference: Renault, Saraydaryan, Simonin – IROS 2020)

---

# 3.2 Exploiting the Social Cost Map

---

## Goal

Choose the best position to move an object.

---

## Procedure

For each candidate object position (p):

[
c(p) = w_1 \cdot Dist(obs) + w_2 \cdot CostMap(p) + w_3 \cdot Dist(goal)
]

Where:

* (Dist(obs)): movement cost of object
* (CostMap(p)): social cost at position
* (Dist(goal)): influence on final navigation

---

## Decision Rule

[
p^* = \arg\min_p c(p)
]

---

## Execution Pipeline

1. Select obstacle
2. Evaluate candidate positions
3. Choose best position (p^*)
4. Move object to (p^*)
5. Replan path to goal

---

# 3.3 Social-NAMO Results

---

Experiments show:

* improved human-like object placement
* more structured environments
* reduced navigation difficulty

---

# 4. Multi-Robot NAMO (MR-NAMO)

---

## Problem Definition

Multiple robots perform NAMO tasks in the same environment.

---

## Challenges

* spatial interference
* object conflicts
* coordination failures
* deadlocks

---

## Key Observation

> Social NAMO naturally structures the environment

---

# 5. Coordination in S-NAMO Systems

---

## Main Assumption

Robots:

> **do NOT communicate their full plans**

This differs from:

* Multi-Agent Path Finding (MAPF)

---

## Local Coordination Strategy

Each robot:

* detects local conflicts
* resolves them independently
* uses waiting mechanisms

---

## Conflict Handling

When conflict occurs:

* delay execution
* re-evaluate local situation

---

# 5.1 Coordination via Social Cost

---

## Key Questions

### 1. Which agents should move?

* those needing free space

### 2. Where should they move?

* positions with minimal social cost

---

## Principle

Use social cost map to guide:

* robot repositioning
* object relocation
* conflict resolution

---

## Summary Rule

* free space → prioritize movement
* low social cost → preferred destination

---

# 6. MR-NAMO: Deadlock Handling

---

## Problem

Multiple robots may:

* block each other
* prevent progress indefinitely

---

## Example

### 3-Robot Deadlock

* circular blocking configuration
* no robot can proceed independently

---

## Solution Strategies

* detect deadlock configurations
* introduce coordination steps
* force role switching or waiting
* reassign movement priorities

---

# 7. Multi-Robot NAMO Perspectives

---

## Research Directions

### 1. Spatial & Social Heuristics

* better object placement strategies
* improved cost maps
* human-aware navigation

---

### 2. Learning-Based Methods

* Reinforcement Learning (RL)
* learning coordination policies
* integrating social cost into reward functions

---

### 3. Real-World Experiments

* validation on physical robots
* interaction with dynamic environments

---

### 4. Human-Robot NAMO

* shared environments
* human-aware object rearrangement
* cooperative manipulation and navigation

---

# Key Takeaways

* NAMO extends navigation by allowing obstacle manipulation
* Social NAMO introduces human-aware cost functions
* Social cost maps guide both:

  * object placement
  * robot navigation
* Multi-robot NAMO introduces:

  * conflicts
  * coordination challenges
  * deadlock problems
* Future systems combine:

  * heuristics
  * social reasoning
  * learning-based coordination
