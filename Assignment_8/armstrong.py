#11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def revvers(n):
    rev = 0
    while n>0:
        rem=n%10
        rev = rev+rem*rem*rem
        n=n//10

    return rev

n=int(input('Enter digit:'))
temp=n
if (revvers(n)==temp):
        print("No is armstrong")
else:
     print('Not armstrong')