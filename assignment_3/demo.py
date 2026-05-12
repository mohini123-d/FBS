#311. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
# Program to calculate total ticket amount for 5 people

total = 0

age1 = int(input("Enter age of person 1: "))
amt1 = float(input("Enter ticket amount: "))
if age1 < 12:
    total = total + (amt1 * 0.70)
elif age1 > 59:
    total = total + (amt1 * 0.50)
else:
    total = total + amt1

age2 = int(input("Enter age of person 2: "))
amt2 = float(input("Enter ticket amount: "))
if age2 < 12:
    total = total + (amt2 * 0.70)
elif age2 > 59:
    total = total + (amt2 * 0.50)
else:
    total = total + amt2

age3 = int(input("Enter age of person 3: "))
amt3 = float(input("Enter ticket amount: "))
if age3 < 12:
    total = total + (amt3 * 0.70)
elif age3 > 59:
    total = total + (amt3 * 0.50)
else:
    total = total + amt3

age4 = int(input("Enter age of person 4: "))
amt4 = float(input("Enter ticket amount: "))
if age4 < 12:
    total = total + (amt4 * 0.70)
elif age4 > 59:
    total = total + (amt4 * 0.50)
else:
    total = total + amt4

age5 = int(input("Enter age of person 5: "))
amt5 = float(input("Enter ticket amount: "))
if age5 < 12:
    total = total + (amt5 * 0.70)
elif age5 > 59:
    total = total + (amt5 * 0.50)
else:
    total = total + amt5

print("Total ticket amount =", total)