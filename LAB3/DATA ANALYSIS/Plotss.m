% Clear previous plots
clf;

% Axes and grid
axis([-0.5 0.5 -0.5 0.5]);
hold on;
grid on;
xlabel('Real Axis');
ylabel('Imaginary Axis');
title('Complex Plane Diagram');

% Points
points = [-0.1246 + 0i, -0.09 + 0i, -0.07 + 0i, -0.0450 + 0.4719i];
pointLabels = {'0.1246', '0.09', '0.07', '0.0450, 0.4791'};
pointSymbols = {'x', 'o', '*', 'x'};

% Lines
for i = 1:length(points)
    plot([0 real(points(i))], [0 imag(points(i))], 'm', 'LineWidth', 2);
    text(real(points(i)), imag(points(i)), pointLabels{i}, 'Color', 'k', 'FontSize', 12, 'VerticalAlignment', 'top', 'HorizontalAlignment', 'right');
    plot(real(points(i)), imag(points(i)), pointSymbols{i}, 'MarkerSize', 10, 'Color', 'k');
end

% Phi labels
phiLabels = {'\phi_0', '\phi_1', '\phi_2', '\phi_3'};
for i = 1:length(phiLabels)
    text(real(points(i))/2, imag(points(i))/2, phiLabels{i}, 'Color', 'm', 'FontSize', 14, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
end

hold off;
