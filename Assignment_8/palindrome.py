#9. Write a program to check if entered number is a palindrome or
#not.

def revvers(n):
    rev = 0
    while n>0:
        rem=n%10
        rev = rev * 10+rem
        n=n//10

    return rev

n=int(input('Enter digit:'))
temp=n
if (revvers(n)==temp):
        print("No is palindrome")
else:
     print('Not palindrome')