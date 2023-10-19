
# Chapter 2: Simulation Tests of the Controller Design

## Introduction

This chapter focuses on evaluating the performance and robustness of the KittiCopter system's controller. Various simulation scenarios are conducted using MATLAB Simulink to ensure the design meets specified performance criteria.

## Simulation Setup

### Tools and Software

- MATLAB Simulink
- KittiCopter Model

### Controller Integration and Parameters

The optimized controller was integrated into the existing Simulink model, as shown below.

![Simulink Model](https://imgur.com/4PSFuFB.jpg)

The simulation time was set to 500 seconds to capture both transient and steady-state behaviors.

## General Test Procedure

1. **Configure Simulink Model**: Ensure the model is in a closed-loop configuration.
2. **Run Simulation**: Execute the model under different scenarios.
3. **Analyze Results**: Extract key metrics like steady-state error, settling time, and overshoot.
4. **Compare**: Verify if metrics meet specified objectives.

## Simulation Scenarios

### Scenario 1: Basic Performance Test

#### Objective

- Position tracking accuracy > 90%
- Settling time < 88.8s
- Overshoot < 5%

#### Results

![Step Response](https://imgur.com/oXzy8Tz.jpg)

| Metrics | Result |
| --- | --- |
| Steady-state error | 0 |
| Settling time | 73.405s |
| Overshoot | 0.6% |

### Scenario 2: Robustness to Aerodynamic Uncertainty

#### Objective

Test for a 10% variance in the aerodynamic constant.

#### Results

**90% Constant**

| Metrics | Result |
| --- | --- |
| Steady-state error | 0 |
| Settling time | 74.651s |
| Overshoot | 0.2% |

**110% Constant**

![Result for 1.1b](https://imgur.com/TzOFy8L.jpg)

| Metrics | Result |
| --- | --- |
| Steady-state error | 0 |
| Settling time | 70.663s |
| Overshoot | 1.5% |

### Scenario 3: Component Tolerance Tests

#### Objective

Assess performance under a 10% component tolerance, focusing on controller gain, pole, and zero locations.

#### Results

**Minimum Gain**

![Result for Minimum Gain](https://imgur.com/uPG7VJV.jpg)

| Metrics | Result |
| --- | --- |
| Steady-state error | 0 |
| Settling time | 91.849s |
| Overshoot | 0% |

**Maximum Gain**

![Result for Maximum Gain](https://imgur.com/Sa0xraL.jpg)

| Metrics | Result |
| --- | --- |
| Steady-state error | 0 |
| Settling time | 57.951s |
| Overshoot | 2.1% |

#### Summary

All tests indicate the system remains robust and meets the set criteria, even under component tolerances and parameter uncertainties.

## Conclusion

The controller effectively meets performance criteria and shows robustness under various test conditions. However, a full assessment of all component tolerances will be addressed in the physical implementation phase, which is the next step in our controller evaluation.

---




