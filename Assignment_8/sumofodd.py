#4. Sum of all odd numbers between 1 to n
def oddno(n):
    sum = 0
    for i in range(1,n+1):
        if i%2 != 0:
            sum = sum+i

    return sum

n = int(input('enter n th value:'))
print("sum of odd no is:",oddno(n))