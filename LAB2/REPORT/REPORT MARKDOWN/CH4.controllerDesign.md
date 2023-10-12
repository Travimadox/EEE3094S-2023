# Chapter 4
## Introduction

This chapter outlines the systematic design of a Proportional (P) controller aimed at satisfying strict performance requirements. The controller is designed to achieve over 90% accuracy in position tracking, a 20% improvement in settling time, a maximum of 5% overshoot, and robustness against system uncertainties and component tolerances. MATLAB's PID Tuner tool was used for fine-tuning the controller parameters, and the tuned controller was exported to Simulink for simulation with the KittiCopter system.

## Theoretical Design

This section establishes the basic principles, equations, and derivations crucial for crafting a solid control strategy. Key calculations, including those related to the damping ratio and settling time, are conducted with precision to foresee the system's behavior. As this section concludes, a variety of theoretical plots such as the root locus and Bode plots are illustrated, providing a thorough schematic of the control system from a theoretical perspective.

### Achieving Over 90% Accuracy in Position Tracking
#### Analysis of Steady-State Error

To meet the specified tracking accuracy of over 90%, we need to carefully examine the steady-state error (\(e_{\infty}\)) for a step input to the system. The steady-state error is calculated using the following formula:

\[
e_{\infty} = \lim_{{s \to 0}} s \times \frac{1}{s} \times E(s) = \lim_{{s \to 0}} E(s)
\]

As per Equation 2.3 in the Chapter:

\[
E(s) = \frac{s^2 + bs}{s^2 + bs + KH}
\]

Upon evaluating the limit as \( s \to 0 \):

\[
e_{\infty} = \lim_{{s \to 0}} \frac{s^2 + bs}{s^2 + bs + KH} = 0
\]

The conclusion from this analysis is that the steady-state error of the system is zero.

#### Implications for Controller Gain

The finding that the steady-state error is zero implies that any finite control gain (\( K \)) would suffice for achieving the tracking accuracy requirement, provided that the controller also meets other performance criteria.

This makes it clear that the system can achieve more than 90% accuracy in position tracking as long as the other performance specifications are also satisfied.



### Achieving a 20% Reduction in Settling Time
#### Settling Time of the Open-Loop System

The settling time (\( T_s \)) for a first-order system is often defined as the time required for the system to reach and remain within 98% of its final value. For a first-order system with a time constant \( \tau \), the settling time is approximately \( 4\tau \).

Given that \( \tau = 14.3 \) seconds in our case, the settling time for the open-loop system (\( T_{s, \text{open-loop}} \)) can be calculated as:

\[
T_{s, \text{open-loop}} = 4 \times \tau = 4 \times 14.3 = 57.2 \text{ s}
\]

#### Target for 20% Improvement in Settling Time

To achieve a 20% improvement in settling time, the closed-loop system should have a settling time (\( T_{s, \text{closed-loop}} \)) that is at most 80% of the open-loop system's settling time:

\[
T_{s, \text{closed-loop}} \leq 0.8 \times T_{s, \text{open-loop}}
\]

Substituting the known value, this yields:

\[
T_{s, \text{closed-loop}} \leq 0.8 \times 57.2 = 45.76 \text{ s}
\]

The requirement  is shown on the root locus below:
![Speed](https://imgur.com/FL5ZMK6.jpg)

#### Limitation of the Current Controller

Based on the given root locus plot, it's evident that achieving a settling time of 45.76 seconds or less is not possible with the existing proportional controller. The 45.76-second requirement falls outside the root locus of the system, indicating that the current controller is inadequate for meeting this specification. We aim to acheve the speed by choosing poles located along the centroid since this where the closed loop will be fastest

### Limiting Peak Overshoot to Less Than 5%
#### Adjusting the Damping Factor

To constrain the system's overshoot to less than 5%, we first determine the appropriate damping factor (\( \zeta \)) using the formula for percent overshoot (\( M_p \)):


Using the overshoot criteria, we can calculate \(\zeta\) using the formula:

\[
\zeta = \sqrt{\frac{\ln^2(M_p)}{\ln^2(M_p + \pi^2)}}
\]

Substituting \(M_p = 0.05\) gives \(\zeta = 0.691\).



By solving this equation, we find the required \( \zeta \) value that corresponds to a 5% overshoot is \( \zeta = 0.6901 \).

For this damping factor, lines corresponding to \( \arccos(\zeta) \) are plotted on the root locus in figure 2 below. According to this criterion, our system poles must have angles less than \( \arccos(\zeta) = 46.36^\circ \) to meet the overshoot specification.

![Overshoot](https://imgur.com/IzJJM6k.jpg)

#### Control Strategy for Limiting Overshoot

The control strategy involves adjusting the damping factor until the calculated overshoot is below the 5% limit, as specified. Therefore, any pole locations falling within angles less than 46.36 degrees on the root locus will satisfy this overshoot requirement.

### Theoretical design point

#### Finding the Absolute Damping, \(\sigma_d\)
Given that we want the system to be 20% faster, we calculate \(\sigma_d\) as:

\[
\sigma_d = \frac{4}{{\text{Settling time}}} = \frac{4}{45.76} = 0.08741
\]

#### Calculated Damped Frequency \(\omega_d\)
Using the values of \(\zeta\) and \(\sigma_d\), we calculate \(\omega_d\) as:

\[
\omega_d = \sigma_d \tan(\cos^{-1}(\zeta)) = 0.08741 \tan(\cos^{-1}(0.691)) = 0.09144
\]

The theoretical design point if the controller is to meet the 2 requiremnts is :

\[
p_{1,2} = -\sigma_d \pm j\omega_d
\]

However, this point is not on the root locus as shown below due to the speed requirement thus this soldifies our finding from above that the speed requirment is impossible to achieve

![TheoreticalDesignPoint](https://imgur.com/04qpkKu.jpg)
Root locus showing theoretical design point(red circles)



### Minimum Gain \(K\)
Due to the limitations of the root locus of our plant as shown in figure above, we will ignore the settling time requirement and aim for the fastest speed achievable within the locus while still meeting the overshoot requirement.

#### Poles at the Boundary of Requirements

The real part of interest is \( -0.03947 \).

\[
\theta = \cos^{-1}(\zeta) = \cos^{-1}(0.691) = 46.29^\circ
\]

Thus, the imaginary part is \(0.03947 \tan(46.29) = 0.03658\).

The poles at the boundary of our requirements are:

\[
p_{1,2} = -0.03497 \pm j0.03658
\]


The plant transfer function \(L(s) = K \frac{24.50}{s(s + \frac{1}{14.3})}\) leads to:

\[
1 + L(s) = \frac{s(s + \frac{1}{14.3}) + 24.5K}{s(s + \frac{1}{14.3})} = 0
\]

Solving for \(K\):

\[
K = \left| -\frac{1}{24.50} p_1 (p_1 + \frac{1}{14.3}) \right| = 1.0451 \times 10^{-4}
\]

Any gain less than this won't be able to meet any of our requirements.

![Minimum Gain](https://imgur.com/hRwD4zg.jpg)
A plot showing the value of \(K\)  where our minimum \(K\) lies.




## Software-based Design and Tuning

### Introduction to Software-based Design and Tuning
Transitioning towards a practical domain, the Software Design and Tuning section is devoted to the actual implementation of the theoretical design within a software setting. This section delineates the particular software tools, commands, and techniques utilized for activities such as plotting the root locus or adjusting the control parameters. An exhaustive examination is undertaken to juxtapose the theoretical anticipations against the practical realizations, illuminating any refinements made during this phase. Through a series of software-generated plots, this section not only affirms the theoretical design but also encompasses the tuning process, effectively bridging the theoretical projections with practical executions.

#### Tools
- MATLAB - PIDTuner, Control System Designer(SISO Tool)

### Ensuring Robustness Against Parameter Uncertainty

#### Variability in Aerodynamic Constants

In the context of our Quadcopter's control system, it's critical to account for potential variability in aerodynamic constants. The transfer function for the Quadcopter plant, as given in Chapter 2, is:

\[
G(s) = \frac{A}{s + b}
\]

We considered two scenarios for variations in \( b \): one where \( b \) decreases to \( 0.9b \) and another where it increases to \( 1.1b \). The corresponding transfer functions for these cases are:

- For \( 0.9b \): \( G(s) = \frac{A}{s + 0.9b} \)
- For \( 1.1b \): \( G(s) = \frac{A}{s + 1.1b} \)

These variants were implemented in a Simulink model to validate if the control system still meets the performance requirements.

#### Controller Gain Variability Due to Component Tolerances

The control system design also takes into account the 10% tolerance in the resistors \( R3 \) and \( R1 \), which determine the gain of the controller:

\[
\text{Controller Gain} = \frac{R3}{R1}
\]

Given the 10% tolerance, the maximum and minimum gains can be calculated as follows:

- Maximum Gain: \( \frac{R3 \times 1.1}{R1 \times 0.9} \)
- Minimum Gain: \( \frac{R3 \times 0.9}{R1 \times 1.1} \)

These variations in gain were also integrated into the Simulink model to evaluate system performance under these conditions.

####  Nyquist Plot Analysis

#####  Background
The Nyquist plot provides valuable information regarding the stability and performance of a control system. By examining how the open-loop transfer function navigates the complex plane, one gains insights into the stability margins of the system.

![Nyquisit](https://imgur.com/SVoDKX6.jpg)

#####  Observations

- **Infinite Gain Margin**: The plot does not encircle the critical point (-1, 0j), indicating an infinite gain margin. This suggests that the system is quite robust against gain variations.

- **Low Phase Margin**: A phase margin of approximately 3.06 degrees suggests that the system is on the edge of stability, making it susceptible to phase variations.



#### Sensitivity Function Analysis Using Bode Plots

##### Background
The sensitivity function \( S \) represents how sensitive the system is to external disturbances and modeling errors. It is defined as:

\[
S = \frac{1}{1 + G(s)}
\]

![Sensitivity](https://imgur.com/46hnqUC.jpg)

##### Observations

- **Peak Sensitivity**: Occurring at 25.4 dB and 1.31 rad/s, the high peak indicates a system that is highly susceptible to disturbances and uncertainties at this particular frequency.

- **Low Phase Margin**: The phase margin of approximately 3.06 degrees reinforces the system's vulnerability to phase variations.



1. **Robustness Against Gain Variations**: Both the Nyquist plot and the sensitivity function show that the system is robust against gain variations. The infinite gain margin supports this.

2. **Vulnerability to Phase Variations**: The low phase margin identified in both analyses underscores the system's sensitivity to phase variations, particularly concerning given the potential variability in aerodynamic constants and component tolerances.

3. **Sensitivity to Disturbances**: The high peak in the sensitivity function indicates that disturbances and uncertainties at a frequency of 1.31 rad/s could severely impact the system. 






#### Control Strategy for Robustness

1. **Pole Placement for Aerodynamic Constants Variability**: The plant has a parameter \( b \) that varies within the range of \( 0.9b \) to \( 1.1b \). To counter this variability, the controller poles should be carefully placed in a way that minimizes the sensitivity of the system's performance to changes in \( b \).

2. **Gain Variability Compensation**: Due to the 10% resistor tolerance affecting the controller gain, upcoming design iterations will aim to test the system across this gain variability. The goal is to ensure that performance metrics are met within this tolerance range.

3. **Frequency-Specific Sensitivity Mitigation**: Recognizing the pronounced sensitivity peak at 1.31 rad/s, future versions of the controller will aim to strategically place poles and zeros away from this critical frequency. This is intended to minimize the system's sensitivity to disturbances at this point.

5. **Simulations for Robustness Validation**: Subsequent steps involve carrying out detailed simulations under varying conditions. This is intended to confirm that the control system adheres to performance requirements, despite the uncertainties and variations highlighted.


## Tuning

### Pole Placement Strategy

During the theoretical analysis, it was determined that to meet our performance criteria, the poles should be placed at \(p_{1,2} = -0.03497 \pm j0.03658\). Practically, these pole locations mark the region where the closed-loop poles of the system should be placed to achieve the desired performance.

In the software-based design stage using MATLAB's Control System Designer, these pole locations were used as reference points. The goal was to position the closed-loop poles slightly away from these theoretically ideal positions to allow for parameter variation.

The final pole positions \(p_{1,2} = -0.035 \pm j0.0317\) after tuning are depicted below:

![Final Pole locations](https://imgur.com/xBdkrQc.jpg)


### Controller Gain Tuning

The theoretical analysis also indicated a minimum gain \(K = 1.0451 \times 10^{-4}\) below which our system would not satisfy the specified requirements. This minimum gain sets the lower limit for the controller gain during the tuning process using MATLAB's PID Tuner.

Within the PID Tuner, it was discovered that a gain value slightly higher than the theoretical minimum provided a good balance between system robustness and performance.


#### Determined Controller Gain
The Control System Designer tool suggested a proportional gain (\(K_p\)) of 0.0013084, which lies within the acceptable range for achieving the desired system performance.

![Gain](https://imgur.com/2RwjQt5.jpg)


## Design Summary and Conclusion

In addressing the system requirements, a primary focus was placed on controlling overshoot, as the system naturally follows step inputs with high accuracy. However, the goal to improve response speed was challenging to achieve with the current proportional controller. To enhance system robustness, a strategic approach was adopted to adjust pole positions, accounting for changes in system parameters.

The design process was made efficient by using MATLAB's Control System Designer tool, which helped in quickly adjusting the pole positions on the root locus to meet the desired system performance goals.

The identified controller gain (\(K_p\)) will be thoroughly tested in the next chapter to verify its effectiveness in meeting the set requirements.

By focusing on overshoot and choosing an appropriate \(K_p\), the design successfully addresses key performance criteria. This sets the groundwork for detailed testing and the eventual physical implementation of the control system.