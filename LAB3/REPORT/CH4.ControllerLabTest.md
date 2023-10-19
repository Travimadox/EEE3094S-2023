# CHAPTER 4: LABORATORY TESTS OF THE CONTROLLER DESIGN
## Introduction

This chapter aims to conduct an exhaustive analysis of a helicopter controller based on empirical data collected across five different scenarios. The performance of the controller is measured againstthe following  metrics:

- Overshoot: Should not exceed 5%
- Steady-State Error: Should be within 10%
- Settling Time: Should be reasonableand close to the simualtion settling time
- Robustness against uncertainties of up to 10% in the aerodynamic constant.
- Tolerance for 10% variations in the electronic components.



---

## Methodology

This section outlines the methodological approach employed to test the performance metrics of the  lEad controller for the Kitticopter system. Various critical parameters such as overshoot, steady-state error, and settling time are assessed to ensure that the system meets the pre-established requirements.

### Metrics Defined

#### 1. Overshoot Percentage


  The overshoot percentage quantifies the extent to which the system's output surpasses the desired set point during its transient response and is given by the mathematical equation shown below:

\[
\text{Overshoot Percentage} = \left( \frac{{\text{Maximum Output} - \text{Set Point}}}{{\text{Set Point}}} \right) \times 100
\]


#### 2. Steady-State Error
 
  The steady-state error indicates the difference between the system's final output and the desired set point once the transient response has ceased and is given by the mathematical equation shown below:


\[
\text{Steady-State Error} = \left( \frac{{\text{Set Point} - \text{Final Output}}}{{\text{Set Point}}} \right) \times 100
\]


#### 3. Settling Time

  Settling time is the time duration required for the system output to stabilize within a specified range (e.g., 5%) around the set point.


11 tests were conducted to validate the perfocmace of the controller.

## Results
The results from the 10 trials are shown in the table below:
| Dataset ID | Overshoot (%) | Steady State Error (%) | Settling Time (s) |
|------------|--------------|------------------------|-------------------|
| 1          | 6.62         | 0.64                   | 60                |
| 2          | 3.14         | 3.46                   | 62.8              |
| 3          | 1.07         | 4.6                    | 60.5              |
| 4          | 0.62         | 3.49                   | 58.8              |
| 5          | 0.03         | 2.8                    | 58                |
| 6          | 0.52         | 3.26                   | 50.8              |
| 7          | 2.98         | 0.53                   | 59.7              |
| 8          | 3.98         | 0.9                    | 52.5              |
| 9          | 1.95         | 0.25                   | 58.2              |
| 10         | 1.22         | 1.53                   | 54.6              |

A sample step response(dataset2). All other step resposnes and screenshots from the lab can can be seen in the Appendix

The result(Dataset 11) for abilty of the controller to reject Output disturbances is shown belw:
{Placeholder for image}


## Analysis
### Normal Analysis

#### Accuracy in Tracking Positional Inputs

100% of the test cases had a steady-state error of less than 10%, meeting the requirement for accuracy in tracking positional inputs.

#### Settling Time

100% of the test cases had a settling time of less than 88.8 seconds, thus meeting the requirement.

#### Overshoot

90% of the test cases had an overshoot of less than 5%, almost meeting the requirement.



### Statistical Analysis
To assess the controller's performance, we focus on its reliability and repeatability, defined as follows:

- **Reliability**: The consistent ability of the controller to perform its intended function under varying conditions.
- **Repeatability**: The ability of the controller to yield the same output when subjected to identical conditions across multiple trials.


#### Statistical Metrics

The following table outlines the calculated statistical metrics, along with industry-standard limits for comparison:

| Performance Metric            | Mean      | Standard Deviation |
|-------------------------------|-----------|--------------------|
| Overshoot (%)                 | \(2.21\)  | \(2.01\)           |
| Steady-State Error (%)        | \(2.15\)  | \(1.55\)           |
| Settling Time (s)             | \(57.59\) | \(3.78\)           |


The histogram of errors is shown below
{Place holder for histograms}

1. **Overshoot (%)**: 
    - **Mean**: The average overshoot is \(2.21\%\), well below a commonly accepted limit of \(5\%\).
    - **Standard Deviation**: A \(2.01\%\) standard deviation suggests moderate variability, which should be further investigated for optimization.
  
2. **Steady-State Error (%)**:
    - **Mean**: The average steady-state error is \(2.15\%\), well within a \(10\%\) limit.
    - **Standard Deviation**: The \(1.55\%\) standard deviation indicates consistency, making the controller reliable for this metric.
  
3. **Settling Time (s)**:
    - **Mean**: The average settling time stands at approximately \(57.59\) seconds.
    - **Standard Deviation**: A \(3.78\) second standard deviation shows slight variability but remains within an acceptable range.

#### Conclusions on Reliability and Repeatability

1. **Reliability**: 
    - The controller is highly reliable as all average metrics fall within industry standards.
    - The moderate standard deviation in overshoot suggests scope for further refinement.

2. **Repeatability**: 
    - Low standard deviations across all metrics indicate high repeatability, with consistent results likely in repeated trials.


## Evaluation of the Analog Controller for Altitude Control of the Kitticopter

### Effectiveness in Meeting Design Requirements

#### 1. Tracking of Positional Inputs
The control system demonstrated exceptional performance in tracking positional inputs, consistently achieving an accuracy level exceeding 90% across all evaluated datasets. The tracking error remained notably low, staying below a 10% threshold, thereby affirming the system's high level of precision in this specific parameter.

#### 2. Reduction in Settling Time
The control system surpassed the performance of an uncompensated closed-loop system by reducing the settling time by 20%. This indicates a more rapid response time, which is beneficial for real-world applications.

#### 3. Control of Overshoot
Out of 11 conducted tests, the system failed to limit overshoot in only one instance. This suggests a generally high level of effectiveness in controlling overshoot, although there is room for improvement.

#### 4. Robustness Against Aerodynamic Variability
The controller exhibited remarkable resilience against a 10% variation in aerodynamic constants. It consistently met the design requirements across various experimental trials, indicating a commendable level of robustness.

#### 5. Tolerance for Component Variability
Similarly, the controller displayed a high level of robustness against a 10% variation in component tolerances, again meeting design requirements consistently across multiple experimental trials.

### Limitations and Areas for Improvement

#### Speed Optimization
While the system meets the specified speed requirements, there is substantial opportunity for enhancement. Currently, the system settles at a time of 57.59 seconds. With further adjustments to the control parameters, it is plausible to achieve a settling time of less than 10 seconds.

## Recommendations for Controller Design Improvements in the Kitticopter's Altitude Control System

Given the evaluation of the Kitticopter's existing analog control system, there are several recommendations to further enhance its performance and reliability. Importantly, these suggestions consider that a lead controller was employed in the current design. 

### 1. Refinement in Positional Tracking

Although the system demonstrates exceptional positional tracking capabilities, with over 90% accuracy, further refinements can be made to improve this metric.

### 2. Settling Time Optimization

The system has already shown improvement over an uncompensated closed-loop system by reducing the settling time by 20%. However, there is room for further acceleration. One approach could be to explore different lead controller configurations or even to employ a more complex controller structure like a Lead-Lag or PID controller, aimed specifically at reducing settling time.

### 3. Enhanced Overshoot Control

While the controller effectively limits overshoot in most scenarios, failing in just one out of 11 tests indicates that there may be particular conditions where the system is vulnerable. To improve in this area, a comprehensive sensitivity analysis could be performed to understand these specific conditions better, followed by controller retuning.

### 4. Improved Robustness Against Aerodynamic Variabilities

Although the system performs well against a 10% variation in aerodynamic constants, it is prudent to prepare for more extreme variations. Additional tests simulating greater aerodynamic variability could provide insight into potential weaknesses. Furthermore, adaptive control strategies could be integrated into the system to make it more resilient against unforeseen variations.

### 5. Component Tolerance

The system has shown commendable robustness against a 10% variation in component tolerances. To improve this, higher-quality components could be sourced to minimize tolerance variations, or a more adaptive control algorithm could be designed to compensate for these component variations dynamically. Also by opting
for precision resistors with tolerances as low as 1% or 0.1%, a more consistent and reliable performance can be achieved within the control loop.


### 6. Speed: Settling Time 

The current settling time of 57.59 seconds, although meeting the minimum requirements, could be improved substantially. Adjustments to the control parameters, specifically tailored for speed optimization, could make the system more agile. Real-world applications would greatly benefit from a settling time of less than 10 seconds, which is achievable with more refined control strategies.


### 7. Utilize Digital Control Systems
Digital controllers such as Raspberry Pi or Arduino offer greater flexibility in control logic,
ease in parameter tuning, and the capacity to implement more complex control algorithms.
Incorporating such a digital controller could greatly augment system adaptability and performance




By implementing these recommendations, the Kitticopter's altitude control system can further align with the design requirements and also gain a competitive edge in terms of performance and reliability.

