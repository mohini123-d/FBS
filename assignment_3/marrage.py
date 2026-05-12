#10. Write a program to check if person is eligible to marry or not (male age >=21 and
#female age>=18)

age=int(input('Enter Ur Age: '))
person=input('Are u male or female if male type M or Female type F :')
if(age>=21 and person=='M'):
    print('U r eligible to marry:')    

elif(age>=18 and person=='F'):
    print('U r eligible to marry:')  

else:
    print('U r not eligible to marry:')          