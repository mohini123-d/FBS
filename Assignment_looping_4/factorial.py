#4. WAP to print factorial of a number .
fact=1
n= int(input('Enter no:'))
i=1
while i<=n:
    fact=fact*i
    i =i+1
print("factorial",fact)