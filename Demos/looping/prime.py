num= int(input('Enter number to check prime or not'))
for i in range(2,num):
    if(num %i == 0):
        print(f'{num} is not a prime no')
        break
else:
    print(f'{num } is a prime no')