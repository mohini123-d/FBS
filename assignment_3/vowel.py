#2. Write a program to input any alphabet and check whether it is vowel or consonant.
# Program to check vowel or consonant

ch = input("Enter an alphabet: ")

if ch in ('a','e','i','o','u','A','E','I','O','U'):
    print("It is a vowel")
else:
    print("It is a consonant")