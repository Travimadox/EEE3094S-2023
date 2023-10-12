# Chapter 7: Phyiscial Tests of the Controller Design

## Introduction

This chapter aims to conduct an exhaustive analysis of a helicopter controller based on empirical data collected across five different scenarios. The performance of the controller is measured against three predetermined metrics:

- Overshoot: Should not exceed 5%
- Steady-State Error: Should be within 10%
- Settling Time: Should be reasonableand close to the simualtion settling time



---

## Methodology

This section outlines the methodological approach employed to test the performance metrics of the Proportional (P) controller for the Kitticopter system. Various critical parameters such as overshoot, steady-state error, and settling time are assessed to ensure that the system meets the pre-established requirements.

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



### Experimental Procedure

#### Test Configuration

The test was conducted with varying set points to assess the system's robustness and performance under different operating conditions. Specifically, the test employed three different set points:

1. Middle of the set point potentiometer, approximately 6V.
2. Lower end of the set point potentiometer, approximately 3V.
3. Upper end of the set point potentiometer, approximately 15V.

#### Data Collection

For each of the three set points, the test was repeated five times to obtain statistically relevant data. The overshoot percentage, settling time, and steady-state error were recorded for each run.

- **Metric 1**: Overshoot was assessed visually and/or quantitatively from the system response.
  
- **Metric 2**: Steady-state error was calculated after the output stabilized.
  
- **Metric 3**: Settling time was measured from the moment the input was applied until the system output remained within a 5% range of the set point.

---


## Results

This section presents the experimental results obtained from testing the Quadcopter's Proportional (P) controller performance. The focus is on key metrics such as overshoot percentage, steady-state error, and settling time for various set points.

### Response at Different Set Points

#### For Set Point 13.96V

- **Laboratory Screenshot**:  
  ![Test1](https://imgur.com/GpdjSVf.jpg)

- **Data Plot with Annotations**:  
  ![Set Point 13.96](https://imgur.com/6LJTpI8.jpg)

#### For Set Point 2.944V

- **Laboratory Screenshot**:  
  ![Test2](https://imgur.com/ZmyJjF5.jpg)

- **Data Plot with Annotations**:  
  ![Set Point 2.944](https://imgur.com/6o3E6bB.jpg)

#### For Set Point 6.026V (First Instance)

- **Laboratory Screenshot**:  
  ![Test3](https://imgur.com/Rj3n9uj.jpg)

- **Data Plot with Annotations**:  
  ![Set Point 6.026](https://imgur.com/nM1RjGU.jpg)

#### For Set Point 6.026V (Second Instance)

- **Laboratory Screenshot**:  
  ![Test4](https://imgur.com/zJq7jYJ.jpg)

- **Data Plot with Annotations**:  
  ![Set Point 6.026](https://imgur.com/iVsZB1N.jpg)

#### For Set Point 6.043V

- **Laboratory Screenshot**:  
  ![Test5](https://imgur.com/zJq7jYJ.jpg)

- **Data Plot with Annotations**:  
  ![Set Point 6.043](https://imgur.com/Bcdmie2.jpg)

### Summary of Metrics

The table below summarizes the key metrics obtained from each dataset, highlighting the performance parameters of the controller for different set points.

| Dataset ID  | Set Point (V) | Max Output (V) | Overshoot (%) | Steady-State Error (%) | Settling Time (s) |
|-------------|--------------|----------------|--------------|------------------------|-------------------|
| Dataset 1   | 6.026        | 6.484          | 7.60         | 4.70                   | 250               |
| Dataset 2   | 6.026        | 6.222          | 3.25         | 0.70                   | 359.6             |
| Dataset 3   | 6.043        | 6.491          | 7.41         | 4.70                   | 350               |
| Dataset 4   | 2.944        | 2.953          | 0.31         | 6.42                   | 300               |
| Dataset 5   | 13.946       | 14.229         | 2.03         | 1.97                   | 306.3             |



___

## Data Analysis

### Detailed Analysis

1. **Overshoot**: Datasets 1 and 3 register an overshoot percentage exceeding the 5% criterion. This is not a trivial discrepancy and could pose problems in systems requiring high precision.

2. **Steady-State Error**: All datasets fall within the 10% threshold for steady-state error. While Dataset 2 exhibits a minuscule 0.7% error, Dataset 4 shows a relatively higher error of 6.42%.

3. **Settling Time**: Only Datasets 2 and 5 exhibit a settling time within a 2% range of the set point, albeit Dataset 2 takes longer to settle.



###  Statistical Analysis for Reliability and Repeatability

In addition to the individual performance metrics of each dataset, a statistical analysis is conducted to evaluate the reliability and repeatability of the controller's performance. These terms are defined as follows:

- **Reliability**: The controller's ability to consistently perform its intended function under the given conditions.
- **Repeatability**: The controller's ability to reproduce the output for the same set of input conditions over multiple trials.

To perform the statistical analysis, the mean and standard deviation of each performance metric (Overshoot, Steady-State Error, and Settling Time) will be calculated. These statistical measures will provide insights into the central tendency and dispersion of the controller's performance.

The statistical metrics are as follows:

| Performance Metric            | Mean      | Standard Deviation |
|-------------------------------|-----------|--------------------|
| Overshoot (%)                 | \(4.12\)  | \(3.26\)           |
| Steady-State Error (%)        | \(3.70\)  | \(2.31\)           |
| Recalculated Settling Time (s)| \(332.95\)| \(37.69\)          |


1. **Overshoot (%)**: 
    - **Mean**: The average overshoot is \(4.12\%\), which is below the \(5\%\) limit. 
    - **Standard Deviation**: A standard deviation of \(3.26\%\) indicates a moderate level of variability in overshoot across the datasets.
  
2. **Steady-State Error (%)**:
    - **Mean**: The average steady-state error is \(3.70\%\), well within the \(10\%\) limit.
    - **Standard Deviation**: A lower standard deviation of \(2.31\%\) indicates relatively consistent performance in terms of steady-state error.
  
3. **Settling Time (s)**:
    - **Mean**: The average settling time is approximately \(333\) seconds.
    - **Standard Deviation**: With a standard deviation of \(37.69\), there's some variability, but it's not excessively high.

#### Conclusions on Reliability and Repeatability

1. **Reliability**: 
    - The controller's average performance metrics are within the specified limits, indicating a reliable system under varying conditions.
    - However, the standard deviation for overshoot is moderate, suggesting that the controller might occasionally exceed the desired \(5\%\) limit.

2. **Repeatability**: 
    - The relatively low standard deviations in steady-state error and settling time suggest that the controller is likely to produce similar results under repeated trials.
    - However, the higher standard deviation in overshoot needs to be addressed for better repeatability.

---

## Evaluation of the Analog Controller for Altitude Control of the Kitticopter

### Effectiveness in Meeting Requirements

#### 1. Tracking Positional Inputs
The controller partially succeeded in achieving greater than 90% accuracy in tracking positional inputs. However, issues with overshoot and steady-state error affected the achievement of this aim. The controller failed to keep the tracking error below 10% consistently across all datasets, thus partially satisfying this requirement.

#### 2. Settling Time Reduction
The controller was effective in reducing the system's settling time by 20% in comparison to its open-loop behavior in Dataset 2. Nevertheless, the other datasets revealed inconsistencies, showing that the settling time was still longer than desired in some cases.

#### 3. Limiting Overshoot
The controller inconsistently met the criterion of keeping the overshoot under 5%. Dataset 2 revealed acceptable performance, but the other datasets showed overshoots exceeding the limit, particularly due to operational amplifier limitations.

#### 4. Robustness Against Uncertainties
The controller demonstrated robustness against 10% uncertainties in the aerodynamic constant. However, its sensitivity to component tolerances and operational amplifier characteristics lessened its overall robustness.

#### 5. Tolerance for Variations in Components
Although designed to handle 10% variations in electronic components, the performance showed a decline with datasets suggesting that this was not completely achieved.

### Limitations

#### Speed and Proportional Controller
One of the major drawbacks was the restriction to a proportional controller, which inherently lacks the capability to completely eliminate steady-state errors or optimally tune for speed of response. This is evident in the failure to consistently meet the speed and overshoot requirements.

#### In-Depth Analysis of Non-Idealities and Limitations Affecting Controller Performance

##### Op-Amp Characteristics

######  1. Input Offset Voltage (VIO)
The µA741 operational amplifier has a typical input offset voltage that ranges from 1 to 6 mV. This offset voltage essentially acts like a "phantom" input voltage, affecting the accuracy of the feedback loop by introducing an error term.

The presence of an input offset voltage could result in a steady-state error that is not zero, even when the system is at equilibrium. In control systems where precision is critical, this offset voltage can significantly impair system performance by contributing to the steady-state error, which we observed exceeded the desired 10% in some of the datasets.

Given that the typical VIO is up to 6 mV and the supply voltage (from the specs) can go up to 18V, the percentage error due to VIO can be calculated as \(\frac{6 \text{ mV}}{18 \text{ V}} \times 100 = 0.033%\). While this seems small, in a control system demanding high precision, even such a small error can be unacceptable.



######  2. Input Bias Current (IIB)
The µA741 has an input bias current ranging between 80 to 500 nA. This current flows through the feedback resistors, creating an additional voltage drop.

The voltage drop due to input bias current can alter the effective gain of the feedback loop, introducing another source of steady-state error. It could also affect the transient response, contributing to overshoot or settling time issues.

Assuming a 10 kΩ feedback resistor and a bias current of 500 nA, the voltage drop would be \( V = I \times R = 500 \times 10^{-9} \times 10 \times 10^{3} = 5 \text{ mV }\). This is comparable to the input offset voltage, and thus can have a similar level of impact on the system's performance.



######  3. Common-Mode Rejection Ratio (CMRR)

The CMRR of µA741 ranges from 70 to 90 dB. This parameter measures the op-amp's ability to reject common-mode signals—signals that appear on both the inverting and non-inverting inputs.


A lower CMRR means that the op-amp is less effective at rejecting noise or interference that appears as a common-mode signal. This could degrade the quality of the control signal, affecting both transient and steady-state performance.

A CMRR of 70 dB translates to a rejection factor of \(10^{(70/20)} = 3162.3\). Any common-mode signal would be attenuated by this factor, but it still leaves room for some noise to affect the differential mode operation, thereby affecting the control quality.



######  4. Supply Voltage Sensitivity (kSVS)


The µA741 has a supply voltage sensitivity of 30-150 µV/V, which means the input offset voltage could change by this amount for every volt change in the supply voltage.


Fluctuations in the supply voltage could lead to changes in the input offset voltage, affecting the steady-state error and potentially causing overshoot or longer settling times.


For a 1V change in an 18V supply, the VIO could change by as much as \( 150 \, \mu V/V \times 1 \, V = 150 \, \mu V \), which would directly add to the steady-state error.


#####  Tolerances in Components


The resistors used in the control circuit have a tolerance of 10%.

Resistor tolerances can introduce variations in the feedback loop, affecting the system's gain and, consequently, its overshoot, steady-state error, and settling time.

A 10% variance in a 10 kΩ resistor means the actual resistance could range from 9 kΩ to 11 kΩ. This could translate to a corresponding 10% variation in the control loop's gain.



### Summary

The controller's limited success in meeting the lab aims can be attributed to a variety of factors:

- Non-idealities in the operational amplifier (µA741) such as input offset voltage, input bias current, CMRR, and supply voltage sensitivity.
  
- The inherent tolerance levels of the resistors used, contributing to variations in system performance.
  
- Environmental variables such as temperature affecting the operational characteristics of the µA741 op-amp.

These limitations cumulatively resulted in the controller failing to consistently meet the stringent requirements set for tracking accuracy, settling time, and overshoot, thereby compromising its robustness. Given these factors, additional forms of control (integral and derivative) and robust component selection would be advisable for future iterations and high-precision applications.



## Recommendations for Improvement in Controller Design

To enhance the performance of the Kitticopter's altitude control system, several design modifications are recommended. These aim to address the non-idealities and limitations outlined in the earlier sections. Here's a comprehensive list:

## Upgrade to PID Control

### Rationale:
A Proportional-Integral-Derivative (PID) controller could help eliminate the steady-state error, reduce overshoot, and improve the transient response.

### Implementation:
Add integral and derivative control loops to the existing proportional controller. Utilize digital controllers if possible for more precise tuning.

## Improved Operational Amplifier Selection

### Rationale:
The µA741's limitations—such as input offset voltage, input bias current, and poor CMRR—significantly affect the performance. Upgrading to a precision op-amp can improve these characteristics.

### Implementation:
Select an op-amp with low offset voltage, low bias current, and high CMRR. Check that it has similar or better bandwidth to ensure it meets the speed requirements.

## Component Tolerance Matching

### Rationale:
The 10% tolerance in resistors contributes to system variations and performance inconsistency.

### Implementation:
Use precision resistors with tighter tolerances (e.g., 1% or 0.1%) to minimize variations in the feedback loop and control gain.

## Temperature Compensation

### Rationale:
As the µA741 is sensitive to temperature changes, a temperature compensation mechanism can help maintain consistent performance.

### Implementation:
Implement a temperature monitoring and compensation circuit or choose components that are less sensitive to temperature variations.

## Adaptive Control Algorithms

### Rationale:
The controller's sensitivity to system parameters and environmental variables could be mitigated with an adaptive control algorithm.

### Implementation:
Employ a model-based adaptive control scheme that adjusts the controller gains in real-time based on system performance metrics.

## Power Supply Filtering

### Rationale:
Fluctuations in supply voltage can introduce errors, affecting the controller's performance.

### Implementation:
Introduce power supply filters and voltage regulators to ensure a consistent voltage supply, thereby reducing the impact of supply voltage sensitivity.

## Enhanced Noise Filtering

### Rationale:
Given the issues related to CMRR, an additional noise filtering stage could help in reducing the effect of external disturbances.

### Implementation:
Add a low-pass or band-pass filter at the op-amp input stage to reduce noise and improve the signal-to-noise ratio.


## Incorporation of a Digital Controller (Raspberry Pi or Arduino)

### Rationale:
Digital controllers offer more flexibility in control logic, easier tuning, and better adaptability. They can also facilitate complex control algorithms that can't be easily implemented with analog components.

### Implementation:

1. **Raspberry Pi**: Known for its powerful processing capabilities, a Raspberry Pi could be used to run complex control algorithms, data logging, or even machine learning models to adapt the control strategy in real-time.

    - **Setup**: Connect the Raspberry Pi to your control system via GPIO pins or USB interfaces for more complex communication protocols.
  
    - **Code**: Implement the control algorithms in Python or C++, and use libraries like `scipy` for advanced control strategies.

2. **Arduino**: It's generally easier to set up and is well-suited for real-time control tasks that don't require heavy computation.

    - **Setup**: Arduino boards can be connected to the control system using their analog and digital I/O pins.
  
    - **Code**: Write the control algorithm in Arduino's C-like programming language, leveraging existing libraries for PID control if needed.

## Summary

By implementing these recommendations, the Kitticopter's altitude control system could significantly improve its tracking accuracy, robustness, and reliability. Attention to component selection, control strategy, and additional filtering could make the system more resilient to both internal non-idealities and external disturbances. Therefore, these changes are strongly advised for any future iterations of the system.
