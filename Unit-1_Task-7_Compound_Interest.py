# Program to calculate Compound Interest

p = float(input("Enter the Principal Amount: "))
r = float(input("Enter the Rate of Interest: "))
t = float(input("Enter the Time (in years): "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest =", ci)
print("Total Amount =", amount)