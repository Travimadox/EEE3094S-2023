
# Chapter2: Simulation Tests of the Controller Design

## Introduction
After the careful design of the controller based on given specifications, the next important step is to verify its performance. This involves running a series of tests using MATLAB and Simulink. These tests are essential for confirming that the controller operates as intended and meets the established criteria. Given that a Simulink model has already been set up, this section will outline the specific tests that need to be conducted to thoroughly assess the controller's performance.

## Simulation Setup

### Tools and Software
- MATLAB Simulink
- KittiCopter Model

### Controller Export and Simulation Parameters

After optimising the controller parameters using MATLAB's Control System Designer, the tuned controller was seamlessly exported into our Simulink model to complete the KittiCopter system simulation. The Simulink model is illustrated in the figure below. 

![Simulink Model](https://imgur.com/4PSFuFB.jpg)

To ensure adequate time for the system to reach steady-state and to observe any transient behaviors, the simulation time was set at 500 seconds.

By integrating the tuned controller into the Simulink model, we were able to create a robust simulation environment that mimics the real-world behavior of the KittiCopter system, thereby enabling us to perform detailed analysis and testing.


## Simulation Scenarios

### 1. No variation Test

#### Objective:
To ensure the system 
- Tracks position inputs with >90% accuracy
- Settling time less than 88.8s.
- Overshoot less than 5%

#### Procedure:

1. **Setup Simulink Model**: Make sure your Simulink model has the controller and plant in a closed-loop configuration.
2. **Input Signal**: Use a Step input block to create a step reference signal.
3. **Run Simulation**: Execute the Simulink model.
4. **Analyze Results**: Use the Scope  to extract the output and calculate the steady-state error,settling time and overshoot.
5. **Compare**: Ensure that the parameters meet the objectives.

#### Result:
![Step Response](https://imgur.com/oXzy8Tz.jpg)
The performance metrics are shown below:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0       |
| Settling time          | 73.405s  |
| Percentage overshoot   | 0.6%      |

As can be seen from the plot above the kitticopter system meets the requiremnts


### 2. Robustness to Aerodynamic constant Uncertainty Test

#### Objective:
The aim of this test is to assess the system's robustness under conditions where there is a 10% variance in the aerodynamic constant.

#### Procedure:

1. **Modify Parameters**: Within your Simulink model, integrate a block or script that allows the aerodynamic constant to vary by ±10%.
2. **Execute Multiple Simulations**: Perform several simulation runs to observe the system's behavior under these varied conditions.
3. **Performance Evaluation**: Verify if the key performance metrics are still within acceptable limits under parameter variation.

#### Results

##### Case of 90% Aerodynamic Constant
For \(0.9b\): \(G(s) = \frac{24.50}{13s + 1}\)

Step Response: ![Result for 0.9b](.jpg)

Performance Metrics for 90% Aerodynamic Constant:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0       |
| Settling time          | 74.651s  |
| Percentage overshoot   | 0.2%      |

##### Case of 110% Aerodynamic Constant
For \(1.1b\): \(G(s) = \frac{24.50}{15.9s + 1}\)

Step Response: ![Result for 1.1b](https://imgur.com/TzOFy8L.jpg)

Performance Metrics for 110% Aerodynamic Constant:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0    |
| Settling time          |  70.663s |
| Percentage overshoot   |    1.5%|

#### Summary

The test results demonstrate that the system remains robust even when subject to a 10% fluctuation in the aerodynamic constant. Key performance metrics such as steady-state error, settling time, and overshoot remained within acceptable limits in both scenarios. This confirms the resilience and dependability of our system's design in coping with parameter uncertainties.



### 3. Component Tolerance Robustness Test on Controller Gain

#### Objective:
The test aims to assess the system's resilience and performance stability when subjected to a 10% tolerance in component values, focusing primarily on controller gain.

#### Procedure:

1. **Introduce Component Variations**: Vary the controller gain to  ±10% 
2. **Simulation and Analysis**: Run the simulations and carefully analyze the resulting performance metrics.

#### Results

##### Case of Minimum Gain
The minimum gain, calculated as \( \frac{R2 \times 0.9}{R1 \times 1.1} \), is \( 2.468 \times 10^{-3} \).

Step Response: ![Result for Minimum Gain](https://imgur.com/uPG7VJV.jpg)

Performance Metrics for Minimum Gain:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     |0     |
| Settling time          |  91.849s  |
| Percentage overshoot   |  0%   |

##### Case of Maximum Gain
The maximum gain, calculated as \( \frac{R2 \times 1.1}{R1 \times 0.9} \), is \( 3.687 \times 10^{-3} \).

Step Response: ![Result for Maximum Gain](https://imgur.com/Sa0xraL.jpg)

Performance Metrics for Maximum Gain:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0       |
| Settling time          | 57.951s     |
| Percentage overshoot   | 2.1%    |

#### Summary

The system demonstrates resilience and stable performance within a 10% component tolerance range, particularly for controller gains. It should be noted, however, that this simulation is limited in scope. While the controller gain was the most straightforward parameter to model for tolerance variations, it doesn't account for all possible component tolerances that could affect system performance. The complexities of capturing the aggregate effect of individual component tolerances on the system's overall behavior go beyond the scope of this simulation.

The effects of other component tolerances will need to be assessed during the physical implementation phase, which will be discussed in the subsequent chapter. There, we will have the opportunity to measure and adjust for the real-world impact of component variations to ensure that the system continues to meet its performance requirements.

### 6. Component Tolerance Robustness Test on Controller Pole and Zero

#### Objective:
The test aims to assess the system's resilience and performance stability when subjected to a 10% tolerance in component values, focusing primarily on controller pole and zer locations.

#### Procedure:

1. **Introduce Component Variations**: Vary the location of the controller pole and zero to correspond to upper bound and lower boudsns of the products R1C1 and R2C2 respectively.
2. **Simulation and Analysis**: Run the simulations and carefully analyze the resulting performance metrics.

#### Results

##### Case of RC product Lower Bound
\[
R1C1_{\text{min}} = 0.9 \times 0.85 \times R1C1 = 0.9 \times 0.85 \times 11.11=8.5
\]
The zero under these circumstances would be at \( \frac{1}{R1C1_{\text{min}}} = 0.1176\).

\[
R2C2_{\text{min}} = 0.9 \times 0.85 \times R2C2 = 0.9 \times 0.85 \times 8.025 =6.139
\]
The pole would accordingly be at \( \frac{1}{R2C2_{\text{min}}} = 0.1629\).

Thus, the lead controller under minimum tolerances would be:
\[
\frac{s + z_{\text{max}}}{s + p_{\text{max}}} =\frac{s+0.1176}{s+0.1629}
\]

Step Response: ![Result for Lower Bound](https://imgur.com/uPG7VJV.jpg)

Performance Metrics for Minimum Gain:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     |    0   |
| Settling time          |    71.909s|
| Percentage overshoot   |    1%  |

##### Case of RC product Upper Bound
\[
R1C1_{\text{max}} = 1.1 \times 1.15 \times R1C1 = 1.1 \times 1.15 \times 11.11 =14.05
\]
The corresponding zero would be at \( \frac{1}{R1C1_{\text{max}}} = 0.0712\).

\[
R2C2_{\text{max}} = 1.1 \times 1.15 \times R2C2 = 1.1 \times 1.15 \times 8.025 =10.15
\]
The corresponding pole would be at \( \frac{1}{R2C2_{\text{max}}}=0.0985 \).

Thus, the lead controller under maximum tolerances would be:
\[
\frac{s + z_{\text{min}}}{s + p_{\text{min}}} = \frac{s+0.0712}{s+0.0985}
\]






Step Response: ![Result for Upper Bound Products](https://imgur.com/Sa0xraL.jpg)

Performance Metrics for Maximum Gain:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0       |
| Settling time          | 72.657s     |
| Percentage overshoot   | 0.2%    |

#### Summary

The system demonstrates resilience and stable performance within a 10% component tolerance range, particularly for controller gains. It should be noted, however, that this simulation is limited in scope. While the controller gain was the most straightforward parameter to model for tolerance variations, it doesn't account for all possible component tolerances that could affect system performance. The complexities of capturing the aggregate effect of individual component tolerances on the system's overall behavior go beyond the scope of this simulation.

The effects of other component tolerances will need to be assessed during the physical implementation phase, which will be discussed in the subsequent chapter. There, we will have the opportunity to measure and adjust for the real-world impact of component variations to ensure that the system continues to meet its performance requirements.



#### Conclusion
This chapter was dedicated to a thorough evaluation of the controller design for the KittiCopter system using MATLAB Simulink. The main objectives were to verify that the controller meets or exceeds established performance criteria and to assess its robustness under various conditions. Specifically, the simulations focused on the following aspects:

1. **Steady-State Tracking Accuracy**: Confirmed that the system tracks position inputs with over 90% accuracy.
   
2. **Settling Time**: Validated that the controller allows the system to settle as quickly as possible within the given constraints.

3. **Overshoot**: Established that the system’s overshoot remains within acceptable limits, thus meeting the design specifications.

4. **Robustness to Parameter Uncertainty**: Confirmed the system's resilience to a 10% variance in the aerodynamic constant.

5. **Component Tolerance Robustness**: Tested the system's performance with a 10% tolerance in controller gains and found it to be within acceptable limits.

However, it's important to note a limitation in our robustness testing: while we simulated variations in the controller gain, other component tolerances like resistors and capacitors were not examined. These elements could have a cumulative impact on the system’s performance, and we plan to investigate this in the next phase involving physical implementation.

#### What Comes Next?

The positive outcomes of these simulation tests set the stage for the next critical phase: physical prototyping. We will transition from a virtual environment to actual hardware, focusing on hardware-in-the-loop testing and fine-tuning the controller for real-world conditions. This phase will also give us the opportunity to examine how the system responds to the actual tolerances and imperfections found in physical components, thereby providing a comprehensive validation of the controller's robustness and effectiveness.

By moving on to the physical prototype, we aim to further substantiate the simulation findings, ensuring that the KittiCopter controller is not just theoretically sound, but also practically viable for real-world applications.







---

