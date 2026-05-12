#8. Write a program to convert days into years, weeks and days.
total_days = int(input("Enter days: "))

years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7
days = remaining_days % 7

print(f"Years: {years}")
print(f"Weeks: {weeks}")
print(f"Days: {days}")