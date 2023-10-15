clear;
clc;

% Define the s variable
s = tf('s');

% Define the transfer function
K = (-s*(s+0.1246)*(s+0.07))/(24.50*(s+0.09));

% Define the point at which to evaluate the transfer function
s_point = -0.0450 + 1i*0.04719;

% Evaluate the transfer function at the specified point
value = evalfr(K, s_point);
value = abs(value);
% Display the result
disp('The value of the transfer function at s = -0.05685 + j0.02292 is:');
disp(value);
