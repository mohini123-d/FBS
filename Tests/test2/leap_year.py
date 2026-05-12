#1. wa prog  to  accept year from user and check it is a leap year not.
year=int(input('Enter year u want to check leap or not:'))
if(year%4==0):
    print(f'{year} Is a leap year')
    if(year%100==0):
        if(year%400):

            print(f'{year} Is a leap year')
    else:
        print(f'{year} Is a leap year')
else:
    print('not leap year')
