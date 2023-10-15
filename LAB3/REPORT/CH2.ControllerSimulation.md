
# Chapter2: Simulation Tests of the Controller Design

## Introduction
After the careful design of the controller based on given specifications, the next important step is to verify its performance. This involves running a series of tests using MATLAB and Simulink. These tests are essential for confirming that the controller operates as intended and meets the established criteria. Given that a Simulink model has already been set up, this section will outline the specific tests that need to be conducted to thoroughly assess the controller's performance.

## Simulation Setup

### Tools and Software
- MATLAB Simulink
- KittiCopter Model

### Controller Export and Simulation Parameters

After optimising the controller parameters using MATLAB's PID Tuner, the tuned controller was seamlessly exported into our Simulink model to complete the KittiCopter system simulation. The Simulink model is illustrated in the figure below. 

![Simulink Model](https://imgur.com/4PSFuFB.jpg)

To ensure adequate time for the system to reach steady-state and to observe any transient behaviors, the simulation time was set at 500 seconds.

By integrating the tuned controller into the Simulink model, we were able to create a robust simulation environment that mimics the real-world behavior of the KittiCopter system, thereby enabling us to perform detailed analysis and testing.


## Simulation Scenarios

### 1. Steady-State Tracking Accuracy Test

#### Objective:
To ensure the system tracks position inputs with >90% accuracy.

#### Procedure:

1. **Setup Simulink Model**: Make sure your Simulink model has the controller and plant in a closed-loop configuration.
2. **Input Signal**: Use a Step input block to create a step reference signal.
3. **Run Simulation**: Execute the Simulink model.
4. **Analyze Results**: Use the Scope or To Workspace blocks to extract the output and calculate the steady-state error.
5. **Compare**: Ensure that the error is less than 10%.

#### Result:
![Step Response](https://imgur.com/oXzy8Tz.jpg)

As can be seen from the plot above the kitticopter sytem perfectly tracks the step input with zero steady error. This outcome aligns perfectly with our design expectations, confirming that the system achieves a tracking accuracy greater than 90%.

### 2. Settling Time Improvement Test

#### Objective:
The aim of this test is to minimize the system's settling time without negatively impacting other performance criteria, such as overshoot or stability.

#### Procedure:

1. **Conduct Closed-Loop Test**: Operate the system in a closed-loop configuration and measure the time it takes for the system's output to settle within a specified tolerance band around the final value.

#### Results:

![Settling Time](https://imgur.com/CP0KTwX.jpg)

The system's settling time was measured to be approximately 157 seconds. This is the quickest settling time that could be achieved given the current configuration. The pole locations were specifically chosen to be at the point of maximum speed permissible by the root locus plot, effectively placing the poles along the centroid.

In summary, this test confirms that we have optimized the settling time of the system as much as possible within the given design constraints. Although rapid settling is desirable, this is the fastest we can achieve without compromising other key performance indicators.

### 3. Overshoot Test

#### Objective:
The goal of this test is to confirm that the system's peak overshoot remains below a 5% threshold.

#### Procedure:

1. **Configure Simulink**: Set up your closed-loop system in Simulink and use a Step input block for generating a step reference signal.
2. **Execute and Record**: Run the Simulink model and capture the peak value of the system's output.
3. **Compute Overshoot**: Calculate the percentage overshoot with respect to the step input's final value.

#### Results:

![Overshoot Result](https://imgur.com/oXzy8Tz.jpg)

As depicted in the plot above, the system shows negligible overshoot, as the response never exceeds the setpoint. This validates that our system complies with the design criteria of less than 5% overshoot, as outlined in Chapter 4 of the design documentation.

By achieving this, we have verified that our system meets all the required performance specifications for overshoot, confirming the robustness of the design.


### 4. Robustness to Parameter Uncertainty Test

#### Objective:
The aim of this test is to assess the system's robustness under conditions where there is a 10% variance in the aerodynamic constant.

#### Procedure:

1. **Modify Parameters**: Within your Simulink model, integrate a block or script that allows the aerodynamic constant to vary by ±10%.
2. **Execute Multiple Simulations**: Perform several simulation runs to observe the system's behavior under these varied conditions.
3. **Performance Evaluation**: Verify if the key performance metrics are still within acceptable limits under parameter variation.

#### Results

##### Case of 90% Aerodynamic Constant
For \(0.9b\): \(G(s) = \frac{24.50}{13s + 1}\)

Simulink Model: ![Simulink Model for 0.9b](https://imgur.com/G4zZe4I.jpg)

Step Response: ![Result for 0.9b](.jpg)

Performance Metrics for 90% Aerodynamic Constant:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0       |
| Settling time          | 157.5s  |
| Percentage overshoot   | 0%      |

##### Case of 110% Aerodynamic Constant
For \(1.1b\): \(G(s) = \frac{24.50}{15.9s + 1}\)

Simulink Model: ![Simulink Model for 1.1b](https://imgur.com/0kQAHfF.jpg)

Step Response: ![Result for 1.1b](https://imgur.com/TzOFy8L.jpg)

Performance Metrics for 110% Aerodynamic Constant:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0       |
| Settling time          | 170s    |
| Percentage overshoot   | 0%      |

#### Summary

The test results demonstrate that the system remains robust even when subject to a 10% fluctuation in the aerodynamic constant. Key performance metrics such as steady-state error, settling time, and overshoot remained within acceptable limits in both scenarios. This confirms the resilience and dependability of our system's design in coping with parameter uncertainties.



### 5. Component Tolerance Robustness Test

#### Objective:
The test aims to assess the system's resilience and performance stability when subjected to a 10% tolerance in component values, focusing primarily on controller gains.

#### Procedure:

1. **Introduce Component Variations**: Add scripts or blocks within the Simulink model to simulate ±10% variations in controller parameters.
2. **Simulation and Analysis**: Run the simulations and carefully analyze the resulting performance metrics.

#### Results

We will focus on the controller gain, as it is most susceptible to component tolerances. We will analyze the system behavior under both minimum and maximum gain conditions, calculated with a 10% tolerance.

##### Case of Minimum Gain
The minimum gain, calculated as \( \frac{R3 \times 0.9}{R1 \times 1.1} \), is \( 0.00129 \).

Step Response: ![Result for Minimum Gain](https://imgur.com/uPG7VJV.jpg)

Performance Metrics for Minimum Gain:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0       |
| Settling time          | 180s    |
| Percentage overshoot   | 0%      |

##### Case of Maximum Gain
The maximum gain, calculated as \( \frac{R3 \times 1.1}{R1 \times 0.9} \), is \( 0.001687 \).

Step Response: ![Result for Maximum Gain](https://imgur.com/Sa0xraL.jpg)

Performance Metrics for Maximum Gain:

| Parameter              | Result  |
|------------------------|---------|
| Steady-state error     | 0       |
| Settling time          | 80s     |
| Percentage overshoot   | 0.5%    |

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

