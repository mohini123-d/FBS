#5. WAP to print Fibonacci series upto n.
n = int(input('enter N th value:'))
a=0
b=1
for i in range(1,n+1):
    print(a,end=' ')
    c= a+b
    a=b
    b=c