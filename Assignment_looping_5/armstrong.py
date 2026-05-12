#4. WAP to print Armstrong number within a given range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    temp = num
    sum = 0

    while temp > 0:
        r = temp % 10
        sum = sum + r*r*r
        temp = temp // 10

    if sum == num:
        print(num, "is an Armstrong number")