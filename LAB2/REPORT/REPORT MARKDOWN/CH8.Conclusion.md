# Chapter 8:  Conclusion

The objective of this study was to evaluate the performance of a Proportional (P) controller implemented in a Quadcopter system. Key performance indicators—namely overshoot percentage, steady-state error, and settling time—were rigorously tested across a range of set points.

The results indicate a nuanced performance profile for the controller. Specifically, the controller demonstrated varying degrees of efficiency, depending on the set point value. At a lower set point of 2.944V, the controller yielded a minimal overshoot of 0.31% and a settling time of 300s. In contrast, at a higher set point of 13.946V, the overshoot was slightly higher at 2.03%, but the settling time improved to 306.3s. The controller's performance was also tested at repeated set points (6.026V), showing consistent metrics with minor variations.

The findings suggest that the controller's performance can be optimized further. The overshoot percentages are relatively low but indicate room for improvement. The settling times are quite high, signifying a need for more aggressive tuning to meet stringent real-world operational timelines.

In terms of future work, the controller can benefit from more advanced control techniques such as PD (Proportional-Derivative) or PID (Proportional-Integral-Derivative) control, which might help in reducing both overshoot and settling time. Additionally, further experiments could be conducted under varying environmental conditions to understand how the controller behaves in less-than-ideal circumstances.

