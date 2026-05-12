#7. Write a program to find sum of digits of a number.
def sumofd():
    sum=0
    n=int(input('Enter digit:'))
    for i in range(n):
        rem=n%10
        sum=sum+rem
        n=n//10

    return sum

print('Sumof digit is: ',sumofd())