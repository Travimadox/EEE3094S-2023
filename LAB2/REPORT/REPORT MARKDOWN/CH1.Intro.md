# Chapter 1: Introduction
## Overview
This lab focuses on designing a proportional controller for a "kitticopter"—a simulated, flying cat inspired by Orville, a feline that became a flying machine after its demise. 

The lab is divided into two main sessions:

1. **System Identification**: The first stage is focused on developing a mathematical model for the Kitticopter. This model will encompass crucial forces and moments acting on the system, such as rotor thrust, aerodynamic drag, and gravitational forces. Step tests and experimental validations are performed to fine-tune and identify any uncertain model parameters to allow for the design of the controller in the subsequent stage

2. **Control Design**: The second stage revolves around the development of a Proportional (P) controller to manipulate the Kitticopter's altitude. Various performance criteria are set to ensure precision, speed, and robustness in the control response.

## Aim
The aim of this lab is to design a na analog controller to control the altitude of the kitticopter that meets the following specifications:

1. Achieve greater than 90% accuracy in tracking positional inputs, allowing for a maximum tracking error and disturbance effects of less than 10%.
2. Reduce the system's settling time by at least 20% compared to its open-loop behavior.
3. Limit the overshoot to under 5% for any step response.
4. Maintain robustness against uncertainties of up to 10% in the aerodynamic constant, acknowledging the inevitable limitations in the experimental identification of this parameter.
5. Ensure a tolerance for 10% variations in the electronic components used in assembling the controller.
6. **Bonus Objective**: Attain over 80% accuracy in tracking velocity inputs.


## Objectives
To meet the aforementioned aims, the lab will focus on  the following objectives:

- Formulate a comprehensive mathematical model to describe the Kitticopter's dynamics.
- Validate the proposed model through a rigorous system identification process.
- Design, construct, and validate a Proportional Controller that satisfies the specified criteria.
- Critically evaluate the controller's performance, specifically its ability to meet or exceed the set requirements.

## Deliverables
At the conclusion of this lab, the following deliverables are expected:

- A fully functional Proportional Controller, assembled on a Veroboard.
- A detailed report that outlines the methodology, design strategy, testing procedures, and results, as well as an evaluation of how well the final controller meets the established specifications.

