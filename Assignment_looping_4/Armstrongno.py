#12. Write a program to check if given number is Armstrong number or not.
n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    rem = n % 10
    sum = sum + rem*rem*rem
    n = n // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not Armstrong number")