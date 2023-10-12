

# Chapter 3: System Identification 

## Introduction
This chapter aims to identify the dynamic model of the Kitticopter system. An empirical method is used where an input is fed to the kitticopter system and characteristics of the output are extracted and used to formualte the trnsfer function. 

Step inputs are fed to the system to generatestep resposnes for parameter estimation. The key parameters like gain, time constant, and aerodynamic drag. are extracted from the step response. These are then used to complete the model intially designed in chapter 2. The model is further validated to test is integrity and how close it is to the real experiemental data and and its integrity.


## Methodology

### Step-Testing

#### Introduction to Step-Testing

Step-testing is crucial for acquiring a first-order understanding of the Kitticopter system. In this phase, we apply a step input of voltage and observe how the output, particularly the helicopter's velocity, responds over time. This step response will be logged digitally and will serve as the foundation for our system identification.

#### Conditions for Step-Testing

1. **Known Step Size**: The step size from \(V_1\) to \(V_2\) must be known to normalize the measured output.
2. **Input Saturation Limit**: \(V_2\) should not exceed 5V, as input saturation occurs above this level, leading to discrepancies between what the ADC reads and what the Kitticopter actually receives.

#### Circuit Configuration for Step-Testing Methodology

For our step-testing experiments, we employed a straightforward yet effective circuit setup that consists of a 10k ohm potentiometer coupled with a 10k ohm resistor. The detailed layout of the circuit can be seen in Figure 6 below:

![Circuit Configuration](https://imgur.com/oxWsS9G.jpg)  
*Figure 6: Circuit Configuration for Step-Testing Experiments*

This circuit is interfaced with the system's ADC (Analog-to-Digital Converter). A baseline voltage, denoted as \(V_1\), is initially established at 2.5V. To initiate the step change, the potentiometer is adjusted to its maximum position, effectively changing the voltage to \(V_2 = 5V\).

To account for potential inconsistencies or anomalies in the system's response, this step-testing procedure is conducted five times. This approach ensures that the collected data are both robust and reliable, setting the stage for accurate system identification.


#### Data Collection and Analysis

Data from the step-test is collected and stored in CSV files. The data is then analyzed in a Python Jupyter Notebook, focusing on:

- Reading Kitticopter Data
- Calculating Velocity
- Data Plotting
- System Identification through Key Parameters such as:
  - Time constant (\( \tau \))
  - Final Velocity
  - Gain (\( A \))
  - Aerodynamic Drag Coefficient (\( b \))
  - Scalar Sensor Coefficient
- Transfer Function Approximation
- Simulated Step Response Validation

#### Data Preprocessing

##### Velocity Calculation

Understanding the role of velocity is crucial in the system identification process. As established in Chapter 2, the relationship between rotor thrust force and velocity can be modeled as a first-order system. This simplification eases the complexity of the modeling exercise, facilitating a more straightforward identification process.

In order to compute the velocity, we used the formula for the rate of change of position with respect to time. Mathematically, this is expressed as:

\[
\text{Velocity} = \frac{{\Delta \text{Position}}}{{\Delta \text{Time}}}
\]

Here, \(\Delta \text{Position}\) refers to the change in altitude or spatial coordinates of the Kitticopter, and \(\Delta \text{Time}\) represents the elapsed time during which this positional change occurs.


## Results and Analysis

### Step Response Analysis

The step responses for the Kitticopter system were captured during five distinct trials. These responses serve as empirical evidence to validate the system model we've developed. Each figure below showcases a step response, allowing for detailed analysis and comparison.

#### Trial 1: Step Response
![Step Response for Trial 1](https://imgur.com/VGZI9tI.jpg)  
*Figure 1: Step Response for Trial 1*

#### Trial 2: Step Response
![Step Response for Trial 2](https://imgur.com/cg9DCen.jpg)  
*Figure 2: Step Response for Trial 2*

#### Trial 3: Step Response
![Step Response for Trial 3](https://imgur.com/RXD4izm.jpg)  
*Figure 3: Step Response for Trial 3*

#### Trial 4: Step Response
![Step Response for Trial 4](https://imgur.com/GNcIqg9.jpg)  
*Figure 4: Step Response for Trial 4*

#### Trial 5: Step Response
![Step Response for Trial 5](https://imgur.com/9nJ3zVR.jpg)  
*Figure 5: Step Response for Trial 5*



#### Identification of Key Parameters

##### Gain (\( A \))

The system gain was calculated using the following equation:

\[
A = \frac{{\text{Final Value} - \text{Initial Value}}}{{\text{Amplitude of Step Input}}}
\]

For each of the five data sets, gains were calculated as follows:

| Experiment | Gain (m/s)|
|------------|------|
| Trial 1    | 24.756888168554266 |
| Trial 2    | 24.371759074587924 |
| Trial 3    | 24.4116473873059   |
| Trial 4    | 24.55787781351554  |
| Trial 5    | 24.4116473873059   |
| **Average**| 24.501963966253903 |

The average gain of the system was then obtained:

\[
A_{\text{avg}} = \frac{{\Sigma A_i}}{N} = 24.501963966253903 m/s
\]

Where \( A_i \) are the individual gains and \( N \) is the number of data sets (5 in this case).

##### Time Constant (\( \tau \))

The time constant \( \tau \) was calculated based on the following criterion:

\[
\tau = \text{Time required to reach } 63.2\% \text{ of the final steady-state value}
\]

Five separate \( \tau \) values were calculated as follows:

| Experiment | Tau  |
|------------|------|
| Trial 1    | 14.3 |
| Trial 2    | 14.3 |
| Trial 3    | 14.3 |
| Trial 4    | 14.3 |
| Trial 5    | 14.3 |
| **Average**| 14.3 |

The average time constant was then calculated:

\[
\tau_{\text{avg}} = \frac{{\Sigma \tau_i}}{N} = 14.3s
\]

#### Transfer Function Approximation

Utilizing the averaged values of the identified parameters \( A_{\text{avg}} \) and \( \tau_{\text{avg}} \), the system's transfer function was approximated:

\[
G(s) = \frac{{A_{\text{avg}}}}{{\tau_{\text{avg}} s + 1}}
\]

\[
G(s) = \frac{24.50}{ 14.3s + 1}
\]





### Validation and Verification

#### Simulated Step Response Analysis

To validate the derived transfer function, a simulated step response was generated using a step input of magnitude 2.5. This simulation was carried out to closely mirror the five experimental trials previously conducted. Figures 1-5 depict the comparison between the simulated step responses and those obtained through experimentation.

#### Trial 1: Validation
![Validation 1](https://imgur.com/PsilNVj.jpg)  
*Figure 1: Validation 1*

#### Trial 2: Validation
![Validation 2](https://imgur.com/ZHsd2Qy.jpg)  
*Figure 2: Validation 2*

#### Trial 3: Validation
![Validation 3](https://imgur.com/e0oqosJ.jpg)  
*Figure 3: Validation 3*

#### Trial 4: Validation
![Validation 4](https://imgur.com/oMadFeV.jpg)  
*Figure 4: Validation 4*

#### Trial 5: Validation
![Validation 5](https://imgur.com/IrSGPys.jpg)  
*Figure 5: Validation 5*

From the comparison, it is evident that the simulated responses closely align with the experimental data. This level of agreement reinforces the robustness of our Kitticopter system model.

#### Sensor Coefficient Estimation

The altitude-to-voltage sensor coefficient was estimated using linear regression models. The sensor coefficient values from the five experimental trials are tabulated below:

| Experiment      | Coefficient          |
|-----------------|----------------------|
| Trial 1         | 0.569995446294936    |
| Trial 2         | 0.5699821447253482   |
| Trial 3         | 0.5699985513224997   |
| Trial 4         | 0.5699915412190348   |
| Trial 5         | 0.5699920174992148   |
| **Average**     | 0.5699919402122069   |

The average sensor coefficient was then calculated:

\[
H_{\text{avg}} = \frac{{\Sigma H_i}}{N} = 0.5700
\]

### Discussion

Upon comparing the simulated and experimental results, we notice a high degree of concordance, affirming the robustness and reliability of our system model. The average values of key parameters, including Gain \( A \), Time Constant \( \tau \), and Aerodynamic Drag, are consistent across both simulated and experimental tests. 

### Conclusion

The model that has successfully validated will serve as the foundation for controller design in the next chapter.


