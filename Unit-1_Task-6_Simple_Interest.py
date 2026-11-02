# Read input values
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time in years: "))

# Calculate simple interest
si = (p * r * t) / 100

# Display result
print("Simple Interest =", si)