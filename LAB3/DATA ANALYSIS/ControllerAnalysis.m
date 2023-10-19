% Read data from the CSV file
file_path = 'ControllerData/HelicopterData9.csv';
data = readtable(file_path);

% Calculate values for horizontal lines
set_point = 6.158;
upper_limit = set_point * 1.05;  % +5%
lower_limit = set_point * 0.95;  % -5%

% Plotting
figure;
plot(data.Time_s_, data.Output_m_, 'b', 'DisplayName', 'Output (m)');
hold on;
yline(set_point, 'r--', 'DisplayName', 'Set Point');
yline(upper_limit, 'g--', 'DisplayName', sprintf('+5%% Line at %.3f m', upper_limit));
yline(lower_limit, 'g--', 'DisplayName', sprintf('-5%% Line at %.3f m', lower_limit));
xlabel('Time (s)');
ylabel('Output (m)');
title('Output in Meters vs Time');
legend('show');
grid on;

% Find maximum output and calculate overshoot
max_output = max(data.Output_m_);
overshoot = ((max_output - set_point) / set_point) * 100;

% Find final output and calculate steady-state error
final_output = data.Output_m_(end);
steady_state_error = ((set_point - final_output) / set_point) * 100;

% Display results
fprintf('Maximum Output: %.3f m\n', max_output);
fprintf('Overshoot: %.2f%%\n', overshoot);
fprintf('Final Output: %.3f m\n', final_output);
fprintf('Steady-State Error: %.2f%%\n', steady_state_error);
