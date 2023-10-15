from itertools import product

# E12 resistor series (in Ohms)
e12_resistors = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
# Multiply by 10^x where x is 0, 1, 2,..., to get more values

# Standard capacitor series (in Farads)
standard_capacitors = [1e-12, 2.2e-12, 4.7e-12, 10e-12, 22e-12, 47e-12, 100e-12,
                        220e-12, 470e-12, 1e-9, 2.2e-9, 4.7e-9, 10e-9, 22e-9, 47e-9,
                        100e-9, 220e-9, 470e-9, 1e-6, 2.2e-6, 4.7e-6]  # and so on...

def closest_values(R1C1_target, R2C2_target, R2_over_R1_target):
    min_diff_R1C1 = float('inf')
    min_diff_R2C2 = float('inf')
    min_diff_R2_over_R1 = float('inf')
    best_combination = None

    for R1, R2, C1, C2 in product(e12_resistors, e12_resistors, standard_capacitors, standard_capacitors):
        if R1 * C1 <= R2 * C2:
            continue  # Check that R1C1 is greater than R2C2

        R1C1_diff = abs(R1 * C1 - R1C1_target)
        R2C2_diff = abs(R2 * C2 - R2C2_target)
        R2_over_R1_diff = abs(R2 / R1 - R2_over_R1_target)

        total_diff = R1C1_diff + R2C2_diff + R2_over_R1_diff

        if total_diff < min_diff_R1C1 + min_diff_R2C2 + min_diff_R2_over_R1:
            min_diff_R1C1 = R1C1_diff
            min_diff_R2C2 = R2C2_diff
            min_diff_R2_over_R1 = R2_over_R1_diff
            best_combination = (R1, R2, C1, C2)

    return best_combination


if __name__ == "__main__":
    R1C1_target = float(input("Enter the target value for R1C1: "))
    R2C2_target = float(input("Enter the target value for R2C2: "))
    R2_over_R1_target = float(input("Enter the target value for R2/R1: "))

    if R1C1_target <= R2C2_target:
        print("Error: R1C1 should be greater than R2C2.")
    else:
        R1, R2, C1, C2 = closest_values(R1C1_target, R2C2_target, R2_over_R1_target)
        print(f"Closest values are: R1 = {R1} Ohms, C1 = {C1} F, R2 = {R2} Ohms, C2 = {C2} F")
