# E12 series values
e12_values = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
              100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,
              1000, 1200, 1500, 1800, 2200, 2700, 3300, 3900, 4700, 5600, 6800, 8200,
              10000, 12000, 15000, 18000, 22000, 27000, 33000, 39000, 47000, 56000, 68000, 82000,
              100000, 120000, 150000, 180000, 220000, 270000, 330000, 390000, 470000, 560000, 680000, 820000]

target_ratio = 0.0019
closest_ratio = None
closest_values = (None, None)

# Loop through all possible combinations of two E12 values
for i in e12_values:
    for j in e12_values:
        # Avoid division by zero
        if j == 0:
            continue

        # Calculate the ratio
        ratio = i / j

        # Check if this is the closest ratio found so far
        if closest_ratio is None or abs(target_ratio - ratio) < abs(target_ratio - closest_ratio):
            closest_ratio = ratio
            closest_values = (i, j)

# Print the closest values and their ratio
print(f"The two E12 values closest to the target ratio of {target_ratio} are {closest_values[0]} and {closest_values[1]} with a ratio of {closest_ratio}.")
