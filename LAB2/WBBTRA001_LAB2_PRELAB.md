# LAB 2 PRE-LAB
## Travimadox Webb
## Student No: WBBTRA001

---

## A. Block Diagram
Below is the block diagram representing the system.

![Block Diagram](https://imgur.com/1MrXTAA.jpg)

---

## B. Differential Equation
To describe the system, we use Newton's Second Law of Motion:

\[
F = ma \implies F = m y''(t) \implies F_T(t) - by'(t) - mg = y''(t)
\]

Where:
- \( F_T(t) \) is the thrust
- \( b \) is the aerodynamic drag coefficient
- \( g \) is acceleration due to gravity
- \( m \) is mass

---

## C. Transfer Function
### I. Velocity & Thrust of Kitticopter

The governing differential equation can be rewritten as:

\[
v'(t) = F_T(t) - bv(t) - g
\]

Applying the Laplace transform, we get:

\[
sV(s) = F(s) - bV(s) - \frac{g}{s} \implies (s + b)V(s) = F(s) - \frac{g}{s}
\]

\[
V(s) = \frac{1}{s + b} F(s) - \frac{1}{s+b}\frac{g}{s}
\]

The transfer function \( G(s) \) therefore is:

\[
G(s) = \frac{1}{s + b}
\]

### II. Closed-Loop Transfer Function

The closed-loop transfer function becomes:

\[
G_{cl}(s) = \frac{K}{s^2 + bs + KH}
\]

---

## D. Steady-State Errors and Performance Metrics

### I. Position Error in Relation to Setpoint

The error \( e(s) \) can be described as:

\[
e(s) = X(s) - \frac{KGHe(s)}{s} \implies E_{ss} = \frac{1}{1+\frac{KH}{s^2+bs}}
\]

After simplification:

\[
E_{ss} = \frac{s^2 + bs}{s^2 + bs + KH}
\]

**Type number:** 0  
**Tracking Performance:** Finite error using a proportional controller

### II. Impact of Gravity on Position Output

Setting \( X(s) = 0 \) and letting gravity act as \( V(s) \), we have:

\[
Y(s) = \frac{Q}{1 + QKH}V(s)
\]

After inserting the values:

\[
G_{gravity}(s) = \frac{K}{s^2 + bs + KH}
\]

**Type number:** 0  
**Effect of Gravity:** Finite input disturbance effect using a proportional controller

---

