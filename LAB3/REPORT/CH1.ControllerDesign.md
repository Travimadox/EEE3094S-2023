# Chapter 1
## Introduction

This chapter outlines the systematic design of a Lead controller aimed at satisfying strict performance requirements. The controller is designed to achieve over 90% accuracy in position tracking, a 20% improvement in settling time, a maximum of 5% overshoot, and robustness against system uncertainties and component tolerances. MATLAB's PID Tuner tool was used for fine-tuning the controller parameters, and the tuned controller was exported to Simulink for simulation with the KittiCopter system.

## Theoretical Design

We will primarily focus on two performance requirements for mapping onto the s-plane:

1. A 20% reduction in settling time
2. A maximum overshoot of 5%

### Conversion of Overshoot to Damping Ratio, \( \zeta \)

The damping ratio \( \zeta \) is calculated as:

\[
\zeta = \sqrt{\frac{\ln^2(M_p)}{\ln^2(M_p) + \pi^2}}
\]

where \( M_p = 0.05 \). Therefore,

\[
\zeta = \sqrt{\frac{\ln^2(0.05)}{\ln^2(0.05) + \pi^2}} \approx 0.690
\]


### Determination of New Settling Time

Given that the settling time of the uncompensated system is \(111s\), the old time constant \( \tau_{\text{old}} \) is:

\[
\tau_{\text{old}} = \frac{111}{4} = 27.75s
\]

Thus, the new time constant \( \tau_{\text{new}} \) becomes:

\[
\tau_{\text{new}} = 0.8 \times 27.75 = 22.2s
\]



### Mapping to the S-Plane

#### Damping Ratio (\( \zeta \))

To map \( \zeta \) onto the s-plane, we first convert it to an angle:

\[
\cos^{-1}(\zeta) = \cos^{-1}(0.690) \approx 46.36^\circ
\]

This angle of \( \pm 46.36^\circ \) will be plotted on the root locus.

#### Settling Time Requirement

The s-point corresponding to the new time constant is:

\[
s_{\text{point}} = \frac{1}{\tau_{\text{new}}} = \frac{1}{22.2} \approx 0.0450
\]

*Here, consider including a placeholder for a Root Locus plot showing these requirements.*

#### Design Points (\( p_{1,2} \))

The boundary points are given by:

\[
p_{1,2} = -\frac{1}{\tau_{\text{new}}} \pm j\omega_b
\]

To find \( \omega_b \), we use:

\[
\omega_b = \frac{1}{\tau_{\text{new}}} \tan(46.36^\circ) = 0.0450 \tan(46.36^\circ) \approx 0.04719
\]

Thus, the boundary points are \( p_{1,2} = -0.0450 \pm j0.04719 \).

The design points are shown below:

[Place holders for Image of design poles]

#### Lead Lag Design

$L(s) = G_c(s)G_p(s)H(s)$

$L(s) = K \frac{s +z_{lead}}{s + p_{lead}} \times\frac{24.50}{s(s+0.07)} \times 0.57$

$L(s) = K \frac{13.965(s +z_{lead})}{(s + p_{lead})(s+0.07)s}$

From the root locus equation we know $L(s) = -1$

The angle and magnitude criteria for \( L(s) \) to satisfy are:
- Angle criterion: arg(L(s)) = -180
- Magnitude Criterion: |L(s)| = 1


##### Angle criterion
[Plot for root locus with design point showing the angles between the poles and the thoeretical design point]

$-\phi _1  -\phi _2 +\phi _{lead} = -180 \degree$

where:
- $\phi _1$ is the phase contribution of the plant pole at s =0
- $\phi _2$ is the phase contribution of the plant pole at s =0.07
- $\phi _{lead}$ is the required phase contribution from the Lead Controller
- $\phi _{lead} = \phi _{z,lead} - \phi _{p,lead}$


We select the lead zero at s = -0.09 thus we have $z_{lead} = 0.09$ and thus

$G_c = K \frac{s+0.09}{s+p_{lead}}$

$\phi _1 = 180 \degree - arctan(\frac{0.04719}{0.0450}) = 133.6\degree$

$\phi _2 = arctan(\frac{0.04719}{0.07-0.0450}) = 62.09 \degree$

$\phi _{z,lead} = arctan(\frac{0.04719}{0.09-0.0450}) = 46.36 \degree$



$\phi _{lead} = -180\degree + \phi _1 + \phi _2 = -180\degree + 133.6\degree +62.09 \degree = 15.69\degree$

$\phi _{p,lead} = \phi _{z,lead} - \phi _{lead} = 46.36 \degree - 15.69\degree = 30.67 \degree$


[Plot showing triangle to find p lead]

$\tan (\phi _{p,lead}) = \frac{0.04719}{p_{lead} - 0.0450} $

$\tan (30.67 \degree) = \frac{0.04719}{p_{lead} - 0.0450} $

solve for $p_{lead}$

Thus $p_{lead} = 0.1246$ 


Now the lead compensator is:


$G_c(s)= K \frac{s +0.09}{s + 0.1246}$


##### Magnitude criterion


From the root locus equation: 
$L(s)+1=0$

$1+  K \frac{13.965(s +z_{lead})}{(s + p_{lead})(s+0.07)s} = 0$

$1+ K \frac{13.965(s +0.09)}{(s + 0.1246)(s+0.07)s} = 0$

$K = - \frac{(s + 0.1246)(s+0.07)s}{13.965(s +0.09)}$

Evaluate K at the design point $q_1 = -0.045 + j0.04719$ we have:

$|K|_{s=q_1} = |-\frac{(q_1 + 0.1246)(q_1+0.07)q_1}{13.965(q_1 +0.09)}|$


$|K|_{s=q_1} = |-\frac{(-0.0450 + j0.04719 + 0.1246)(-0.0450 + j0.04719+0.07)(-0.0450 + j0.04719)}{13.965(-0.0450 + j0.04719 +0.09)}|$



$|K|_{s=q_1} = |-\frac{(0.0796 + j0.023595)(0.025 + j0.023595)(-0.0450 + j0.023595)}{13.965(0.0325 + j0.023595)}| = 2.017 \times 10^{-4}$



Thus our final lead lag controller is:

$G_c(s) =(2.017 \times 10^{-4}) \frac{s+0.09}{s+0.115}$




## Software-based Design and Tuning
### Introduction to Software-based Design and Tuning
This section is dedicated to the practical implementation of the theoretical control system design within a software environment. Specifically, it outlines the software tools, commands, and methodologies employed for tasks such as plotting root locus diagrams and tuning control parameters. A comprehensive evaluation is conducted to compare theoretical expectations with practical outcomes, highlighting any adjustments made during this stage. Utilizing software-generated graphical representations, this section serves to corroborate the theoretical design while also detailing the tuning procedures, thereby linking theoretical calculations to practical application.

#### Tools
- MATLAB - Control System Designer(SISO Tool)

### Ensuring Robustness Against Parameter Uncertainty

#### Accounting for Variability in Aerodynamic Constants
In the control system of our Kitticopter, addressing the potential variability in aerodynamic constants is imperative. The transfer function for the Quadcopter system, as delineated in Chapter 2 of Lab Report 2 \cite{}, is represented as:

\[
G(s) = \frac{A}{s + b}
\]

We examined two scenarios involving changes in \( b \): a decrease to \( 0.9b \) and an increase to \( 1.1b \). The transfer functions under these conditions are:

- For \( 0.9b \): \( G(s) = \frac{A}{s + 0.9b} \)
- For \( 1.1b \): \( G(s) = \frac{A}{s + 1.1b} \)

These variations were modeled in Simulink to confirm whether the control system retains its performance specifications.



#### Variability in Controller Gain Attributable to Component Tolerances

##### Impact of Tolerances on Controller Gain
The controller design also accounts for a 10% tolerance in resistors \( R3 \) and \( R1 \), which govern the controller gain as:

\[
\text{Controller Gain} = \frac{R2}{R1}
\]

With this 10% tolerance, the extremities of possible gains can be determined as:

- Maximum Gain: \( \frac{R2 \times 1.1}{R1 \times 0.9} \)
- Minimum Gain: \( \frac{R2 \times 0.9}{R1 \times 1.1} \)

*Note:* It is presumed that resistances in the lead section maintain their nominal values when analyzing gain impact.

These gain variations were also simulated in the Simulink model to assess performance under different conditions.


##### Tolerance Impact on Lead Controller Zero and Pole
The lead controller's zero and pole are influenced by the products \( R1C1 \) and \( R2C2 \) respectively. We focus on the shifts in these zero and pole positions due to tolerances, assuming a 15% capacitor tolerance.

###### Lower Bounds on Product Terms
\[
R1C1_{\text{min}} = 0.9 \times 0.85 \times R1C1
\]
The zero under these circumstances would be at \( \frac{1}{R1C1_{\text{min}}} \).

\[
R2C2_{\text{min}} = 0.9 \times 0.85 \times R2C2
\]
The pole would accordingly be at \( \frac{1}{R2C2_{\text{min}}} \).

Thus, the lead controller under minimum tolerances would be:
\[
\frac{s + z_{\text{max}}}{s + p_{\text{max}}}
\]

###### Upper Bounds on Product Terms
\[
R1C1_{\text{max}} = 1.1 \times 1.15 \times R1C1
\]
The corresponding zero would be at \( \frac{1}{R1C1_{\text{max}}} \).

\[
R2C2_{\text{max}} = 1.1 \times 1.15 \times R2C2
\]
The corresponding pole would be at \( \frac{1}{R2C2_{\text{max}}} \).

Thus, the lead controller under maximum tolerances would be:
\[
\frac{s + z_{\text{min}}}{s + p_{\text{min}}}
\]

These scenarios were also incorporated into the Simulink model to validate system performance under different tolerance conditions.

*Note:* It is assumed that resistances in the gain section maintain their nominal values when analyzing the impact of tolerances on the lead controller.

For a detailed sensitivity analysis, please refer to Lab Report 2 \cite{}. A summary of the findings are shown below:

1. **Pole Placement for Aerodynamic Constants Variability**: The plant has a parameter \( b \) that varies within the range of \( 0.9b \) to \( 1.1b \). To counter this variability, the controller poles should be carefully placed in a way that minimizes the sensitivity of the system's performance to changes in \( b \).

2. **Gain Variability Compensation**: Due to the 10% resistor tolerance affecting the controller gain, upcoming design iterations will aim to test the system across this gain variability. The goal is to ensure that performance metrics are met within this tolerance range.

3. **Frequency-Specific Sensitivity Mitigation**: Recognizing the pronounced sensitivity peak at 1.31 rad/s, future versions of the controller will aim to strategically place poles and zeros away from this critical frequency. This is intended to minimize the system's sensitivity to disturbances at this point.



### Control Parameter Tuning

#### Strategy for Pole Placement

During the theoretical analysis phase, the ideal pole locations were identified as \( p_{1,2} = -0.0450 \pm j0.04197 \). These locations serve as benchmarks in the software-based tuning process. The objective was to position the closed-loop poles slightly away from these ideal locations to account for parameter variations.

The tuned pole positions are \( p_{1,2} = -0.035 \pm j0.0317 \).

#### Gain Adjustment in Controller

The theoretical evaluation suggested a controller gain \( K = 2.017 \times 10^{-4} \). This value served as a reference during the software-based tuning process. It was observed that a gain slightly higher than the theoretical value offered an optimal balance between system robustness and performance. The finalized proportional gain is \( 3.017 \times 10^{-3} \).


## Design Summary and Conclusion

In the process of addressing the system requirements, particular emphasis was placed on minimizing system overshoot and achieving the stipulated speed requirements. It should be noted that the system naturally exhibits high fidelity in tracking step inputs. To augment the system's robustness, a strategic methodology was employed to manipulate the pole positions, taking into account fluctuations in system parameters.

Efficiency in the design process was achieved through the utilization of MATLAB's Control System Designer tool. This software facilitated rapid adjustments of pole positions on the root locus, enabling us to meet pre-established performance criteria effectively.

The controller that has been designed will undergo comprehensive testing in the subsequent chapter to validate its capacity to meet the predefined requirements.

Final Controller Design Equation:

\[
G_c = (3.017 \times 10^{-3})\frac{s+0.09}{s+0.1246}
\]

The effectiveness of this designed controller will be rigorously scrutinized in the following chapter to confirm its compliance with the set performance criteria.