# MINDS 2025/26

## Introduction to Swarm Robotics

### The Flocking Model

**Olivier Simonin**
INSA Lyon – CITI Lab (Inria)
[olivier.simonin@insa-lyon.fr](mailto:olivier.simonin@insa-lyon.fr)

---

# 1. Swarm Robotics — General Idea

Swarm robotics studies how large groups of simple robots can produce complex collective behavior through:

* local interactions
* limited sensing
* decentralized control
* simple behavioral rules

---

## Key Principle

> Global coordination emerges from local interactions.

---

# 2. Swarm Robotics Characteristics

* No central controller
* No global knowledge
* Limited communication
* Scalable to large populations
* Robust to failures

---

# 3. Reactive Navigation in Swarms

Swarm systems are typically based on:

* reactive control laws
* local perception only
* real-time decision making

---

# 4. Flocking: Bio-Inspired Swarm Behavior

Flocking describes coordinated motion in groups of agents (birds, fish, drones).

---

## Objective

Achieve:

* coherent group motion
* collision avoidance
* group alignment
* cohesion (staying together)

---

# 5. Core Flocking Principles

Flocking behavior is typically built from three local rules:

---

## 1. Separation

Avoid collisions with neighbors.

* Repulsive behavior at short distances

---

## 2. Alignment

Match velocity with neighbors.

* Follow average direction of nearby agents

---

## 3. Cohesion

Move toward group center.

* Attractive behavior at medium distances

---

# 6. Flocking as a Combination of Forces

Each agent computes a resulting motion from:

* separation force
* alignment force
* cohesion force

Final motion = weighted sum of local interactions

---

# 7. Local Interaction Model

Each robot:

* senses neighbors within a limited radius
* computes relative:

  * positions
  * velocities
* updates its own motion accordingly

---

## Key Property

> No global map or global planning is required.

---

# 8. Navigation via Reactive Swarm Control

Swarm navigation is:

* fully decentralized
* based on local rules
* emergent at global scale

---

# 9. Mathematical Interpretation (Conceptual)

Typical flocking model structure:

* position update depends on neighbors
* velocity update depends on:

  * distance
  * relative speed
  * desired group behavior

---

# 10. Flocking Behavior in Drones

Example:

* bio-inspired UAV swarms

Each drone:

* computes motion from neighbors
* maintains formation without central control

---

# 11. Implementation Example: Crazyflie Drones

(CITI Lab – Inria experiments)

Small UAVs (Crazyflie platform) demonstrate:

* real-time flocking
* distributed control
* onboard computation

---

## Key Feature

Flocking is computed using:

> relative distance and relative velocity measurements

---

# 12. Communication in Flocking Systems

Two main approaches:

## 1. Direct sensing

* robots measure neighbors locally

## 2. Communication-based

* exchange position/velocity data

---

# 13. Advantages of Flocking

* scalable to many robots
* robust to robot failure
* no centralized controller required
* real-time execution

---

# 14. Limitations

* no guarantee of global optimality
* possible unstable formations
* sensitivity to parameter tuning
* limited task complexity (compared to planning systems)

---

# 15. Swarm Robotics — Key Insight

Swarm behavior emerges from:

> simple local rules + repeated interactions

---

# 16. Summary

* Swarm robotics is based on decentralized, reactive control
* Flocking is a core bio-inspired swarm behavior
* It combines:

  * separation
  * alignment
  * cohesion
* Robots rely only on local sensing or communication
* Global coordinated motion emerges without planning
* Practical implementations exist using UAV swarms (e.g., Crazyflie systems)
