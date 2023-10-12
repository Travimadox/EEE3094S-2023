# Chapter 2: System Modelling
---

## Introduction to System Modelling
In this chapter, groundwork is laid for understanding the characteristics of our system. This will involve the  use of fundamental principles of physics and control theory, to develop a robust mathematical model that serves as the stepping stone for system identification and control design, which will be discussed in the subsequent chapters.

---

## A. Block Diagram Representation
A conceptual block diagram of the kitticopter control system is provided below to facilitate an understanding of the system's architecture.

![Block Diagram](https://imgur.com/ePqALS7.jpg)

---

## B. Governing Differential Equation
### Newton's Second Law Application
The free body diagram showing the forces acting on the ssytem is show below:

![Free Body Diagram](https://imgur.com/Rnn5I1T.jpg)

From the free body diagram the system dynamics can be captured through Newton's Second Law of Motion. For a body of mass \( m \) experiencing a thrust force \( F_T(t) \), aerodynamic drag \( by'(t) \), and gravitational force \( mg \), the equation of motion is given by:

\[
F = m y''(t) \implies F_T(t) - by'(t) - mg = m y''(t)
\]

Where:
- \( F_T(t) \): Thrust
- \( b \): Aerodynamic Drag Coefficient
- \( g \): Acceleration Due to Gravity
- \( m \): Mass of the Kitticopter

---

## C. Transfer Function Formulation
### I. Relation Between Velocity and Thrust

To transform the differential equation into the frequency domain, the equation is first reformulated to emphasize the velocity \( v(t) \):

\[
v'(t) = F_T(t) - bv(t) - g
\]

Upon applying the Laplace transform, the equation becomes:

\[
sV(s) = F(s) - bV(s) - \frac{g}{s} \implies V(s) = \frac{1}{s + b} F(s) - \frac{g}{s(s + b)}
\]

Thus, the transfer function \( G(s) \) representing the system is:

\[
G(s) = \frac{1}{s + b}
\]

### II. Closed-Loop Transfer Function Analysis

The closed-loop transfer function can be written as:

\[
G_{cl}(s) = \frac{K}{s^2 + bs + KH}
\]

---

## D. Steady-State Errors and Performance Metrics
### I. Position Error Relative to Setpoint

For a given reference input \( X(s) \), the error \( e(s) \) can be characterized as:

\[
e(s) = X(s) - \frac{KGHe(s)}{s} \implies E_{ss} = \frac{1}{1+\frac{KH}{s^2+bs}}
\]

Simplifying the expression:

\[
E_{ss} = \frac{s^2 + bs}{s^2 + bs + KH}
\]

- **Type Number:** 0  
- **Tracking Performance:** Finite steady-state error when using a proportional controller

### II. Impact of Gravity on Position Output

To investigate the influence of gravity, we consider \( X(s) = 0 \) and treat \( V(s) \) as an input disturbance:

\[
Y(s) = \frac{Q}{1 + QKH}V(s)
\]

Substituting known terms:

\[
G_{gravity}(s) = \frac{K}{s^2 + bs + KH}
\]

- **Type Number:** 0  
- **Impact of Gravity:** The system will have a finite steady-state error due to gravity when using a proportional controller.

---

This chapter serves as the cornerstone for the following chapter on System Identification, where we will employ this derived model to perform experimental tests to identify unknown parameters and validate our model.