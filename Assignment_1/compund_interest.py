#5. Write a program to enter P, T, R and calculate Compound Interest.

p = float(input("Enter the Principal amount (P): "))
r = float(input("Enter the Rate of interest (R): "))
t = float(input("Enter the Time in years (T): "))

# 2. Calculation Section
# Formula: A = P * (1 + R/100)^T
amount = p * (pow((1 + r / 100), t))
compound_interest = amount - p

# 3. Output Section
print(f"\n--- Compound Interest Results ---")
print(f"Total Amount: {amount:.2f}")
print(f"Compound Interest: {compound_interest:.2f}")
