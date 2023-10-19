## Sketchy Report Guide

## Introduction
- Reference your lab 2 report and mention that you intend to improve the performance of the P controller
- Mention the requiremnts it failed 
- AIms/Objectives
- Delivarables for the lab:Report and Fully functional Lead Controller soldered on Vero board


## Chapter 1: Controller Design
### Theoretical
#### Mapping
- Map the requirements to the s-plane:(The speed and Overshoot)
*Speed*
- Find the settling time of the uncompensated closed loop system($ST_{old} = 59.3s$)
- $0.8 \times 59.3 = 47.44 s$
- Aimimg for a settling time of less than 47.44s
- USe the definition of settling time for 2% of final value : ST = $4\tau$
- $\tau_{new} = \frac{47.44}{4} = 11.86$
- The point on the s plane: $\frac{1}{11.86} = 0.08431$

*Overshoot*
The damping ratio \( \zeta \) is calculated as:

\[
\zeta = \sqrt{\frac{\ln^2(M_p)}{\ln^2(M_p) + \pi^2}}
\]

where \( M_p = 0.05 \). Therefore,

\[
\zeta = \sqrt{\frac{\ln^2(0.05)}{\ln^2(0.05) + \pi^2}} \approx 0.690
\]

cos($\theta$)= $\zeta$

$cos^{-1}(\zeta) = \theta$

$\theta = 46.36 \degree$


#### Selection of the design poles(Closed poles)
Selcted poles are: 

$p_{1,2} = -0.0834 \pm j0.0874$

### Design the lead Compensator 
$G_{lead} = K \frac{s+z}{s+p} $


- Choose a zero
- Depending on the zero you choose that will determine the location of the pole
- Calculate the gain that corresponds to those
*A combination of angle criterion and Magnitude criterion*


$G_{lead} = 1.245 \frac{s+0.2}{s+1.2} $ *Note this is just an example*



### Software(Not necessary but advisable)
- Tune the theoretical design to be robust
- After tuning you will now come up with the final design
- Final pole locations
- Final transfer function for the compensator
  


## Chapter 2: Simulation testing
## Tools
- Simulink Model(Replace the P controller with the Lead compensator)

## Tests
- No variations in any parameter
- Vary aerodynamic constant ($\pm 10\%$)
- Test robustness to tolerance:
-    a.Vary your gain(Max and Min gain)
-    b.Position of your pole and zero(Vary according to the RC product you intend to achieve)
- Try to add disturbances i.e output and input and maybe noise to assess if the performance of the controller


## Chapter 3: Controller Implementation

$G_{lead} = K \frac{s+z}{s+p} $

### Transform the transfer function
$G_{lead} = K_{new} \frac{\beta_1 s+1}{\beta_2 s+1}$

- $\beta_1 = R1C1$ (Zero of the compensator)
- $\beta_2 - R2C2$ (Pole of the compensator)

$K \frac{(s+z)\frac{z}{z}}{(s+p)\frac{p}{p}} = K\times \frac{z}{p} \times \frac{\frac{s+z}{z}}{\frac{s+p}{p}} = K\times \frac{z}{p} \times \frac{\frac{1}{z}(s+1)}{\frac{1}{p}(s+1)}$

### Select Component values
- RC E12 Series that come close to the above values
- After you choose values yopu csan now calculate the actual Gain, positons of zero and pole (Compare it to the theoretical one)
  
### Circuit Diagram
- Schematic
- Label it nicely and try to match it closely to the actual circuit

### Assembly of the circuit
- List of components(Table)
- Photo of your veroboard
- Connection Instructions(Bonus)
- Photo while collecting data
  

## Chapter 4: Controller Lab Test(s)
### Methodology
- Explain how you conducted yopur tests

### Results
| Performance Metric            | Result  |
|-------------------------------|-------|
| Overshoot (%)                 | Your data |
| Steady-State Error (%)        | Your data |
| Settling Time (s)|    Your data  |

Paste the image from the lab on disturbances rejection(Output)

### Discussion
- Whether the controller meets the requirements
- Compare to the simulation results
- Mention requirements not met and why
- Improvements on controller(maybe)
  

## Conclusion
- Summary of the design process
- Future recommendations