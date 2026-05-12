#0 1 1 2 3 5 8 13 21 34
n=int(input('enter n value :'))
a = -1
b = 1
for i in range(n):
    c = a+b 
    print(c, end=' ')
    a=b
    b=c