# Chapter 0: Introduction
## Overview
This lab focuses on designing a lead controller for a "kitticopter"—a simulated, flying cat inspired by Orville, a feline that became a flying machine after its demise. This lab builds on the previous lab 2 where the system model was derived. For reference the system model developed was$\frac{24.5}{s(14.3s+1)}$[1].

## Aim
The aim of this lab is to design an analog lead controller to control the altitude of the kitticopter that meets the following specifications:

1. Achieve greater than 90% accuracy in tracking positional inputs, allowing for a maximum tracking error and disturbance effects of less than 10%.
2. Reduce the system's settling time by at least 20% compared to the uncompensated closed loop system.
3. Limit the overshoot to under 5% for any step response.
4. Maintain robustness against uncertainties of up to 10% in the aerodynamic constant, acknowledging the inevitable limitations in the experimental identification of this parameter.
5. Ensure a tolerance for 10% variations in the electronic components used in assembling the controller.

## Objectives
To meet the aforementioned aims, the lab will focus on  the following objectives:

- Design, construct, and validate a Lead Controller that satisfies the specified criteria.
- Critically evaluate the controller's performance, specifically its ability to meet or exceed the set requirements.

## Deliverables
At the conclusion of this lab, the following deliverables are expected:

- A fully functional Proportional Controller, assembled on a Veroboard.
- A detailed report that outlines the methodology, design strategy, testing procedures, and results, as well as an evaluation of how well the final controller meets the established specifications.