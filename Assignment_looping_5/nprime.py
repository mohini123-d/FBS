#6. Write a program to print first n prime numbers.
n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 1

while count < n:
    num = num + 1
    factors = 0

    for i in range(1, num+1):
        if num % i == 0:
            factors = factors + 1

    if factors == 2:
        print(num)
        count = count + 1