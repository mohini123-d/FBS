#4. Write a program to input all sides of a triangle and check whether triangle is valid or
#not.
# Program to check whether a triangle is valid using sides

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle is valid")
else:
    print("Triangle is not valid")