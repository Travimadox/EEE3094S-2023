
## Chapter 6: Physical Implementation of Controller Design

### Introduction

 This chapter will delve into the intricacies of transitioning from a simulated environment to an actual physical system. This phase is crucial for a comprehensive validation of our design, particularly in understanding how the controller responds to real-world constraints and component tolerances. In this upcoming chapter, we will discuss the hardware components selected, the process of hardware-in-the-loop testing, and the fine-tuning required to achieve desired performance metrics. We will also revisit those component tolerances that could not be effectively modeled in the simulation phase to fully assess their impact on system performance.

---
### Components and Schematic

#### Component List

- **Operational Amplifiers (Op-amps)**: UA741
- **E-12 Series Resistors with 10% Tolerance**: Values of 120kΩ for \( R1 \) and 330Ω for \( R3 \)
- **Trim Potentiometer**: For fine-tuning and calibration
- **Vero Board**: For circuit assembly

#### Circuit Schematic Overview

Our KittiCopter system employs a summing amplifier in conjunction with a level shifter to perform feedback control. This configuration serves a dual purpose: it not only provides negative feedback but also amplifies and offsets the error signal. By operating at a 2.5V baseline, we minimize component count and consequently reduce the influence of component tolerances on controller gain.

#### Gain of Controller

The controller gain is expressed as:

\[
\text{Gain} = \frac{R3}{R1}
\]

To achieve our target gain of approximately \(0.0013084\), E-12 series resistors were initially considered with values of \(120k\Omega\) for \(R1\) and \(150\Omega\) for \(R3\), approximating the gain as:

\[
\text{Gain} = \frac{150}{120000} = 0.00125
\]

However, due to the limited resolution of the DAC used in our lab setup, a \(150\Omega\) resistor for \(R3\) proved impractical. To remedy this and ensure compatibility with the DAC, \(R3\) was revised to \(330\Omega\), resulting in a new gain:

\[
\text{Gain} = \frac{330}{120000} = 0.00275
\]

This adapted gain value still meets the performance requirements while facilitating effective interfacing with the DAC.

#### Circuit Diagram

Refer to the following schematic for the complete circuit layout:

![Circuit Schematic](https://imgur.com/1DtVsbn.jpg)




---

### Physical Setup

#### Circuit Assembly

The circuit, as outlined in the previous sections, has been carefully soldered onto a Vero board. A visual representation of the setup is provided below:

![Circuit Schematic on Vero board](https://imgur.com/sqw729Y.jpg)

#### Assembly Instructions

To enhance user-friendliness and minimize errors during the assembly and interfacing phases, a color-coding scheme has been implemented. 

##### Color-Coding Scheme:

- **+15V**: Red
- **-15V**: Yellow
- **DAC 0**: Blue
- **ADC 1**: Purple
- **ADC 2**: Grey
- **Ground (GND)**: Black

##### Steps for Connection and Interfacing with Lab Equipment:

1. **Power Down**: Before making any connections, ensure all lab equipment is switched off.
  
2. **Power Connections**: Attach the power lines corresponding to +15V (Red), -15V (Yellow), and Ground (Black) to their respective terminals on the lab equipment.

3. **Output Signal**: Connect the output of the operational amplifier (op-amp) to the ADC 1 (Purple) terminal. You'll find the output at pin 6 on the op-amp.

4. **Setpoint Signal**: Interface the setpoint signal with ADC 2 (Grey).

5. **DAC Interface**: Connect the blue wire to the DAC 0 terminal on your lab equipment.


The final set up once everything is connected is shown below:

![Controller lab set up](https://imgur.com/AVoATt7.jpg)

#### Calibration Procedures

The system requires calibration to ensure that the KittiCopter operates at a 2.5V baseline, which is treated as 'zero' for our control system. Here is how to proceed:

1. **Power Up**: Switch on the power supply while making sure the rest of the equipment remains off.

2. **Setpoint Adjustment**: Using the lab equipment, trim the setpoint to zero.

3. **Zero Offset**: Initially, set the potentiometer for offset adjustment to zero. Subsequently, fine-tune it until you achieve a 2.5V output.

4. **Tracking Test**: Finally, set the setpoint to the desired value you wish to track. Turn on the KittiCopter and observe if the controller manages to track the setpoint effectively.



The following chapter will present a comprehensive analysis of physical tests conducted on the KittiCopter control system. The aim is to verify its functional performance and compliance with specified requirements.



