n=int(input('Enter input till u want:'))
for num in range(2,n):

    #num= int(input('Enter number to check prime or not'))
    for i in range(2,num):
        if(num %i == 0):
            #print(f'{num} is not a prime no')
            break
    else:
        print(num)