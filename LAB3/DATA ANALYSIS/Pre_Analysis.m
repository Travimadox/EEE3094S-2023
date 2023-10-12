P = tf([24.50],[14.3 1 0]);
T = feedback(P,0.57);
step(T);
