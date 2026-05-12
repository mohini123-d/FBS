# Program to check if a 3 digit number is palindrome

num = int(input("Enter a 3 digit number: "))

a = num // 100        # first digit
b = num % 10          # last digit

if a == b:
    print("Palindrome number")
else:
    print("Not a palindrome")