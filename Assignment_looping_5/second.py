#2. Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.
n = int(input("Enter number of students: "))

total_per = 0

for i in range(1, n+1):
    print("Enter marks of 5 subjects for student", i)

    m1 = int(input("Subject 1: "))
    m2 = int(input("Subject 2: "))
    m3 = int(input("Subject 3: "))
    m4 = int(input("Subject 4: "))
    m5 = int(input("Subject 5: "))

    total = m1 + m2 + m3 + m4 + m5
    per = total / 5

    print("Percentage of student", i, "=", per)

    total_per = total_per + per

avg = total_per / n
print("Average percentage of all students =", avg)