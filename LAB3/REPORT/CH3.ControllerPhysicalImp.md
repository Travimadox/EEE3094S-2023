# CHAPTER 3: IMPLEMENTATION OF THE CONTROLLER
## Introduction

In this chapter, we transition from theoretical models and simulations to real-world applications by implementing the controller in a physical system. The aim is to validate the controller design by assessing how it copes with real-world variables such as component tolerances and constraints. Topics covered include hardware selection, hardware-in-the-loop testing, and parameter fine-tuning for optimal performance. We will also reconsider the impact of component tolerances that could not be effectively accounted for in simulation.

## Transfer Function Transformation

The transfer function of the controller is given by:
\[ G_{\text{lead}} = K \frac{s+z}{s+p} \]

For ease of design and implementation, this transfer function is divided into two parts:
- \( K \)
- \( \frac{s+z}{s+p} \)

### Stage 1: Gain Calculation

The first stage involves the selection of resistors to approximate the calculated gain \( K = 3.017 \times 10^{-3} \).

### Stage 2: Lead Compensator Design

The second stage focuses on rewriting the lead compensator transfer function in a more practical form for component selection:
\[ G_{\text{lead}} = K_{\text{new}} \frac{\beta_1 s + 1}{\beta_2 s + 1} \]

Where:
- \( \beta_1 = R_1C_1 \) (Zero of the compensator)
- \( \beta_2 = R_2C_2 \) (Pole of the compensator)

The original transfer function can be transformed into the above form as follows:

\[
\frac{(s+z)\frac{z}{z}}{(s+p)\frac{p}{p}} = \frac{z}{p} \times \frac{\frac{s+z}{z}}{\frac{s+p}{p}} = \frac{z}{p} \times \frac{\frac{1}{z}(s+1)}{\frac{1}{p}(s+1)}
\]

The transformed transfer function becomes:

\[
0.722 \times \frac{\frac{1}{0.09}(s+1)}{\frac{1}{0.1246}(s+1)}
\]

Therefore, the desired parameters are:
- \( R_1C_1 = 11.11 \)
- \( R_2C_2 = 8.025 \)
- \( K_{\text{new}} = 0.722 \)

## Component Selection

### Gain Stage

The selected values for \( R_1 \) and \( R_2 \) are 180k\(\Omega\) and 560\(\Omega\), respectively, yielding a gain of \( 3.11 \times 10^{-3} \). Although this value slightly overshoots the calculated gain, it remains within acceptable tolerances.

### Lead Compensator

#### Zero Position
For the lead zero, \( R_1C_1 = 11.11 \), the chosen values are \( R_1 = 180k\Omega \) and \( C_1 = 68\mu F \), resulting in an actual zero position of \( 0.0817 \). This is a minor deviation of \( 8.3 \times 10^{-3} \) and is within acceptable limits.

#### Pole Position
For the lead pole, \( R_2C_2 = 8.025 \), we selected \( R_2 = 180k\Omega \) and \( C_2 = 47\mu F \), yielding an actual pole position of \( 0.1182 \). This deviates by \( 6.4 \times 10^{-3} \), which is also within acceptable boundaries.

#### Gain
The desired lead gain is \( K_{\text{new}} = 0.722 \). For simplicity, a unity gain (1) was selected using two 10k\(\Omega\) resistors.

## Circuit Schematic
A detailed circuit schematic will be provided here.

{Place holder for circuit schematic}

## Circuit Assembly

### Component List
|Component| Quantity|
|---------|---------|
|180k\(\Omega\)|4|
|560 \(\Omega\)|1|
|LM324N|1|
|10k\(\Omega\)|2|
|10k\(\Omega\) Trimpot|2|

The fully assembled circuit on the breadboard is as follows:

{Image placeholder for circuit on breadboard}

### Assembly Instructions and Calibration

A color-coding scheme enhances the user experience and minimizes errors during assembly and interfacing.

#### Color-Coding Scheme:
- **+15V**: Red
- **-15V**: Yellow
- **DAC 0**: Blue
- **ADC 1**: Purple
- **ADC 2**: Grey
- **Ground (GND)**: Black

#### Connection and Interfacing Steps:
1. **Power Down**: Ensure all lab equipment is off before connecting.
2. **Power Connections**: Attach the power lines (+15V, -15V, GND) to the lab equipment.
3. **Output Signal**: Connect the op-amp output to the ADC 1 terminal.
4. **Setpoint Signal**: Connect to ADC 2.
5. **DAC Interface**: Attach the blue wire to the DAC 0 terminal.

{Image placeholder for the final setup}

#### Calibration Procedures:
1. **Power Up**: Turn on the power supply.
2. **Setpoint Adjustment**: Zero the setpoint using lab equipment.
3. **Zero Offset**: Initially, set the potentiometer for offset adjustment to zero, then fine-tune to 2.5V output.
4. **Tracking Test**: Set the setpoint to the desired value and activate the KittiCopter to observe tracking performance.

The subsequent chapter will offer a detailed analysis of the KittiCopter's physical tests, aiming to verify the functional performance and compliance with the specified requirements.