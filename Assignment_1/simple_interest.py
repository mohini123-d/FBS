#4. Write a program to enter P, T, R and calculate simple Interest.

P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of interest (per annum): "))
T = float(input("Enter the Time (in years): "))

# Applying the simple interest formula
SI = (P * R * T) / 100

# Calculating the final total amount
total_amount = P + SI

# Displaying the results
print(f"\n--- Simple Interest Calculation ---")
print(f"Simple Interest: {SI:.2f}")
print(f"Total Amount to be paid: {total_amount:f}")