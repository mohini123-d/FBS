#9. WAP to print all numbers in a range divisible by a given number.
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
d = int(input("Enter divisor: "))

for i in range(start, end + 1):
    if i % d == 0:
        print(i)