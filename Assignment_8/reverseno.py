#8. Write a program find reverse of a number
def revvers():
    rev = 0
    n=int(input('Enter digit:'))
    while n>0:
        rem=n%10
        rev = rev * 10+rem
        n=n//10

    return rev

print('reverese digit is: ',revvers())