#Program to determine the values of R1 and R3 in a voltage divider circuit
import numpy as np

def find_nearest_e12(resistance):
    # E12 standard resistor values series
    e12_series = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
    min_diff = float('inf')
    nearest_value = None
    for base_value in e12_series:
        multiplier = 1.0
        while base_value * multiplier < resistance * 10:
            current_value = base_value * multiplier
            diff = abs(current_value - resistance)
            if diff < min_diff:
                min_diff = diff
                nearest_value = current_value
            multiplier *= 10
    return nearest_value



Vcc = 15
#pROMPT USER FOR MIN AND MAX VALUES

V1 = float(input("Enter the voltage V1: "))
V2 = float(input("Enter the voltage V2: "))


#Form the equations
#R3(1-V1/Vcc) - (V1/Vcc)R1 = 10V1/Vcc
#R3(1-V2/Vcc) - (V2/Vcc)R1 = 10V2/Vcc - 10

#Form the matrix
A = np.array([[1-V1/Vcc, -(V1/Vcc)], [1-V2/Vcc, -(V2/Vcc)]])
B = np.array([10*V1/Vcc, 10*V2/Vcc - 10])

#Solve the matrix
X = np.linalg.solve(A,B)

#Print the results
print("The value of R1 is: ", X[1])
print("The value of R3 is: ", X[0])


#Check the results
R1 = X[1]
R3 = X[0]
Vmin = Vcc*(R3/(R3+R1+10))
Vmax = Vcc*((R3+10)/(R3+R1+10))

print(Vmin, Vmax)



# Comparing integer values of V1, V2 with Vmin, Vmax
if int(V1) == int(Vmin) and int(V2) == int(Vmax):
    print("The integer values of V1 and Vmin, V2 and Vmax are matching.")
    nearest_R1 = find_nearest_e12(R1)
    nearest_R3 = find_nearest_e12(R3)
    print(f"Suggested E12 standard resistor for R1 is: {nearest_R1} KiloOhms")
    print(f"Suggested E12 standard resistor for R3 is: {nearest_R3} KiloOhms")
else:
    print("The integer values of V1 and Vmin, V2 and Vmax do not match.")
