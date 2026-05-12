#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
# Program to calculate grade from 5 subject marks

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

print("Percentage =", per)

if per >= 60:
    print("First Class")
elif per >= 50:
    print("Second Class")
elif per >= 40:
    print("Third Class")
else:
    print("Fail")