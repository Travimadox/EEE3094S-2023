# Guide to Writing the KittiCopter System Report 
- Very sketchy at best 
- Use with caution as it has been prepared by a student who is struggling with control theory.

## Table of Contents

1. Introduction
2. System Modelling
3. System Identification
4. Controller Design
5. Controller Tests
6. Conclusion and Recommendations
7. Appendices
8. References

---

### 1. Introduction

#### Objectives

Briefly outline the purpose of the experiment, the specifications that the system should meet, and the approach taken in the subsequent sections.

---

### 2. System Modelling
Higlyy advise to make use of your pre lab
#### Free-Body Diagram

Create a comprehensive free-body diagram to illustrate the forces acting on the KittiCopter. Label all forces and relevant components.

#### Block Diagram

Design a block diagram to show the whole system architecture and the various signals that interact within the system.(use the one in the prelab)

#### Differential Equation

Formulate a differential equation that describes the motion of the KittiCopter.

- Use physical principles such as Newton's laws.
- Define all variables used.

#### Transfer Function

Derive a transfer function from the differential equation. The transfer function will serve as a mathematical model for system behavior.

- Define each term and explain how you arrived at this model.
- Justify any assumptions or approximations.

---

### 3. System Identification

#### Step Test Plots

Include plots from your step tests, detailing the input signals and system responses.

#### Calculations and System Parameters

Perform calculations to extract system parameters based on your step tests. Present your results in a structured and legible format.

#### Model Validation

Validate your model against real-world behavior.
  
- Compare theoretical predictions with experimental results.
- Comment on the validity of your model.

---

### 4. Controller Design

#### Design Process

Provide a detailed description of your controller design process. Include supporting calculations 

- Justify why this controller meets the specifications.
  
#### Simulation Tests

Describe the tests you performed in simulation to verify your controller design. This will set the stage for a future chapter that focuses solely on simulation tests.

focus on:
- Reference tracking performance
- Robusteness
- Overshoot
- Settling time
- Velocity tracking if you are ambitious enough

#### Physical Design

Showcase the physical design of your controller:

- Circuit schematic
- Photos of the final board
- Components used
- Any simplifications/caveats 

---

### 5. Controller Tests

#### Test Description

Explain the tests you conducted to evaluate the controller's performance experimentally. Include any plots or data that help illustrate these tests.

#### Performance Evaluation

Assess how well the controller met the given specifications. Support your evaluation with data and observations.

#### Recommendations

Offer insights on how the performance of the controller could be further improved, if applicable.

---

### 6. Conclusion and Recommendations

Summarize the main findings, state whether the objectives were met, and offer recommendations for future work.

---

### 7. Appendices

Include any supplementary material such as code snippets, additional graphs, or raw data.

---

### 8. References

List all references cited in your report.

---

