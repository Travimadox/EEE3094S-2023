clc;
clear;

G = tf(24.50,[14.3 1 0]);

Hp =tf(0.57);

Gc = tf([1 0.09],[1 0.1246]);

K = 2.0170e-04;

Gcp = K*Gc;

Gop = Gcp*G;

%rlocus(Gop);

%Gcl = feedback(Gop,1);

%step(Gcl);
% Generate the root locus plot
rlocus(Gop);
hold on;  % Keep the current plot active

% Define the point you want to highlight
s_point = -0.0450 + 1i*0.04719;
s_point2 = -0.0450 - 1i*0.04719;

% Extract the real and imaginary parts
s_point_real = real(s_point);
s_point_imag = imag(s_point);

s_point_real2 = real(s_point2);
s_point_imag2 = imag(s_point2);

% Plot the point on top of the root locus
plot(s_point_real, s_point_imag, 'rx', 'MarkerSize', 10, 'LineWidth', 2);
plot(s_point_real2, s_point_imag2, 'rx', 'MarkerSize', 10, 'LineWidth', 2);

% Add a label to the point
text(s_point_real, s_point_imag, '  Design\_point', 'FontSize', 12, 'Color', 'r');
text(s_point_real2, s_point_imag2, '  Design\_point', 'FontSize', 12, 'Color', 'r');

hold off;  % Release the plot