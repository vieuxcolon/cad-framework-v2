# Cooperative Multi-Robot Systems

## Exploration & Coverage

**Alessandro Renzaglia**
CR INRIA Lyon – CHROMA Team

---

# 1. Multi-Robot Systems — Motivation

---

## Why Cooperation?

Multi-robot systems extend single-robot capabilities through:

* Explicit/implicit communication
* Data exchange
* Coordination and interaction

---

## Key Advantages

* Faster task execution
* Ability to solve tasks requiring multiple robots
* Redundancy and robustness (fault tolerance)
* Heterogeneous systems (sensing, locomotion, computation)
* Replacement of one complex robot with multiple simpler robots

---

# 2. Path Planning Perspective

---

## Core Question

* How do we go from A to B?
* Where should we go to achieve a task?

Tasks include:

* exploration
* coverage
* data collection

---

## Key Insight

Path planning is an optimization problem:

> “Going from A to B = finding an optimal path under a cost criterion”

---

# 3. Multi-Robot Path Planning

---

## Definition

Multiple robots cooperate to achieve a shared objective.

---

## Why it is harder than single-robot planning

* Data fusion and exchange required
* Large optimization space
* Scalability issues
* Communication constraints

---

# 4. Centralized vs Decentralized Architectures

---

# 4.1 Centralized Multi-Robot Systems

## Structure

* One central unit:

  * collects global information
  * computes decisions
  * sends commands to all robots

---

## Advantages

* Full global knowledge → better performance
* Easier to analyze theoretically
* Often simpler formulation

---

## Disadvantages

* Requires reliable communication
* Poor scalability
* Single point of failure

---

# 4.2 Decentralized Multi-Robot Systems

## Structure

* Each robot:

  * acts independently
  * uses local information only
  * communicates with neighbors (if needed)

---

## Advantages

* Scalable
* Robust to failures
* Works under communication loss

---

## Disadvantages

* Often sub-optimal solutions
* Harder theoretical guarantees
* More complex coordination design

---

# 5. Autonomous Multi-Robot Exploration

---

## Global Objective

Explore and map an unknown environment:

[
\text{Minimize total exploration time}
]

---

## Key Constraint

* Environment is unknown
* No offline optimal solution exists
* No global guarantees possible

---

## Motivation

Example:

* UAV teams exploring 3D disaster zones
* Search and rescue missions

---

# 6. Frontier-Based Exploration (2D)

---

## Setup

Each robot:

* knows its position
* has a limited-range sensor
* builds an occupancy map
* can share information with others

---

## Map Representation

* Free space
* Obstacles
* Unknown space

---

## Key Idea: Frontiers

> Frontier = boundary between known and unknown space

---

# 7. Frontier-Based Exploration (Yamauchi)

---

Introduced by:

* Yamauchi (1997, single robot)
* Yamauchi (1998, multi-robot)

---

## Problem Reformulation

Instead of exploring entire space:

> Select the best frontier to visit next

---

# 8. Closest Frontier Strategy

---

## Algorithm (Single Robot)

1. Detect all frontiers
2. Compute distance to each frontier
3. Select closest frontier
4. Move there
5. Repeat

---

## Multi-Robot Extension

Each robot:

* applies same strategy independently

---

## Problem

### Redundancy

* multiple robots select similar frontiers
* duplicated exploration effort

---

# 9. Communication & Decentralization

---

## Shared Map Strategy

Each robot:

* updates local map
* merges information from others

---

## Result

* decentralized decision-making
* robust to failures
* no global controller required

---

## Remaining Issue

> Lack of coordination leads to redundant exploration

---

# 10. Reducing Redundancy

---

## Sequential Assignment

* assign frontier to robot
* remove assigned frontier

Problem:

* nearby frontiers still cause overlap

---

## Better Strategies

* frontier utility
* clustering
* information gain prediction
* global optimization approaches

---

# 11. Frontier Utility (Burgard et al., 2005)

---

## Key Idea

Not all frontiers are equally valuable.

Utility considers:

* expected information gain
* impact on other robots

---

## Insight

If one robot explores a region:

* nearby frontiers become less useful for others

---

# 12. Utility-Based Assignment

---

## Cost Function

Each frontier is evaluated using:

* travel cost
* expected utility reduction

---

## Algorithm

1. Compute frontier set
2. Compute cost for each robot–frontier pair
3. Initialize utility = 1
4. Iteratively assign best robot–frontier pair
5. Reduce utility of nearby frontiers

---

## Issue

* assignment depends on order
* suboptimal greedy behavior

---

# 13. Global Optimization vs Cost

---

## Trade-off

* optimal assignment over permutations → expensive
* greedy assignment → fast but suboptimal

---

# 14. Frontier Clustering

---

## Definition

Grouping frontier points into clusters:

> similar frontiers grouped together

---

## Why clustering helps

* reduces search space
* reduces redundancy
* improves assignment stability

---

## Methods

### K-means clustering

* partitions data into k clusters
* minimizes intra-cluster variance

Steps:

1. initialize centroids
2. assign points to nearest centroid
3. update centroids

---

### DBSCAN

* density-based clustering
* detects outliers

---

## Trade-offs

| Method  | Advantage                     | Disadvantage                |
| ------- | ----------------------------- | --------------------------- |
| K-means | controlled number of clusters | may miss structure          |
| DBSCAN  | finds natural structure       | variable number of clusters |

---

# 15. From 2D to 3D Exploration

---

## Representation

* environment modeled as voxels:

  * free
  * occupied
  * unknown

---

## Goal

* reconstruct 3D structure of environment

---

## New Challenges

* expensive frontier extraction
* complex distance computation
* viewpoint selection instead of point goal

---

# 16. Viewpoint-Based Exploration

---

## Key Concept

Instead of selecting a point:

> select the best viewpoint

---

## Objective

Maximize information gain.

---

# 17. Information Gain (Entropy)

---

## Intuition

* entropy = uncertainty measure
* higher entropy → more unknown area

---

## Goal

> move where uncertainty is highest

---

## Occupancy Grid Interpretation

Each voxel:

* random variable (occupied/free)

---

# 18. Entropy-Based Information Gain

---

## Definition

Information gain = expected reduction in entropy from a viewpoint.

Computed using:

* raycasting
* volumetric sensing models

---

## Enhancements

* occlusion modeling
* frontier visibility
* prior knowledge

---

# 19. Viewpoint Selection Problem

---

## Challenges

* expensive computation
* large search space
* multi-robot extension difficult

---

## General Pipeline

1. generate viewpoint candidates
2. estimate information gain
3. compute cost (distance, coordination)
4. select best candidate

---

# 20. Three Key Sub-Problems

---

## 1. Candidate Generation

* random sampling near frontiers
* geometric rules
* sensor-based heuristics

---

## 2. Information Gain Estimation

* entropy-based
* hybrid heuristics

---

## 3. Cost / Coordination Term

* travel cost
* redundancy penalty
* multi-robot coordination

---

# 21. Cooperative Coverage

---

## Definition

Deploy robots to maximize area coverage quality.

---

## Applications

* environmental monitoring
* search and rescue
* communication networks

---

## Difference from Exploration

| Exploration         | Coverage                    |
| ------------------- | --------------------------- |
| unknown environment | known environment           |
| trajectory matters  | final configuration matters |

---

# 22. Coverage Problem Types

---

## 1. Optimal Deployment

Find best static robot positions.

## 2. Dynamic Coverage

Visit all points in minimum time.

---

# 23. Problem Formulation

---

Coverage quality depends on:

* distance to robots
* spatial distribution

---

## Global Objective

Maximize total coverage quality over space partition.

---

# 24. Space Partitioning

---

## Idea

Divide environment into regions:

* each robot responsible for one region

---

## Benefit

Transforms:

> multi-robot problem → multiple single-robot problems

---

# 25. Voronoi-Based Coverage

---

## Key Tool

Voronoi partition:

* each robot controls nearest region

---

## Centroidal Voronoi

Robots move toward region centroids.

---

## Lloyd Algorithm

1. compute Voronoi cells
2. compute centroids
3. move robots to centroids
4. repeat until convergence

---

# 26. Non-Euclidean Metrics

---

Distance can be modified:

* Manhattan distance
* weighted distances
* anisotropic metrics

---

## Effect

* changes partition shape
* impacts robot distribution
* improves realism in constrained environments

---

# 27. Coverage in Complex Environments

---

## Problem

Voronoi methods assume convex spaces.

With obstacles:

* centroids may be unreachable
* shortest path matters
* line-of-sight constraints appear

---

## Alternatives

* potential fields
* greedy methods
* geodesic distances
* gradient-free optimization

---

# 28. Artificial Potential Fields

---

## Principle

Robots are influenced by repulsive forces:

* from other robots
* from obstacles

(no attraction term in pure coverage)

---

## Advantages

* simple
* distributed
* low computational cost

---

## Disadvantages

* no optimality guarantee
* local minima problem

---

# 29. Final Summary

---

## Key Ideas

* Multi-robot systems improve robustness and efficiency
* Centralized vs decentralized trade-off:

  * performance vs scalability
* Exploration focuses on unknown environments
* Coverage focuses on optimal deployment
* Frontiers reduce search complexity in exploration
* Clustering improves coordination efficiency
* 3D exploration relies on viewpoint selection and information gain
* Coverage uses partitioning (Voronoi / Lloyd)
* Heuristic methods are essential due to computational limits

---

# Core Message

> Multi-robot coordination is fundamentally an optimization problem under uncertainty, where scalability, communication, and computation constraints dominate design choices.
