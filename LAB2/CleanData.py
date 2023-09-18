# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
file_path = 'KITTICOPTER/HelicopterData3.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Step 2: Create a new DataFrame with only the last two columns
df_output = df[['Output(v)', 'Output(m)']]

# Step 3: Save the new DataFrame to a CSV file called "output.csv"
output_file_path = 'SENSOR.csv'  # Replace with your desired output path
df_output.to_csv(output_file_path, index=False)

# Step 4: Find the first occurrence where Output(v) changes from zero to a non-zero value
first_non_zero_index = df[df['Output(v)'] != 0.0].index[0]

# Step 5: Keep only the data starting from the zero immediately above this point
df_filtered = df.loc[first_non_zero_index - 1:]

# Step 6: Recalibrate the Time(s) column to start at 0 and increment by 0.1
df_filtered['Time(s)'] = [i * 0.1 for i in range(len(df_filtered))]

# Step 7: Save the filtered and recalibrated DataFrame to a new CSV file
filtered_file_path = 'RAW.csv'  # Replace with your desired output path
df_filtered.to_csv(filtered_file_path, index=False)

# Step 8: Plot Input(v) versus Time(s) for the filtered and recalibrated data
plt.figure(figsize=(12, 6))
plt.plot(df_filtered['Time(s)'], df_filtered['Input(v)'], label='Input(v)')
plt.xlabel('Time (s)')
plt.ylabel('Input (v)')
plt.title('Input(v) vs Time(s) for Filtered and Recalibrated Data')
plt.grid(True)
plt.legend()
plt.show()
