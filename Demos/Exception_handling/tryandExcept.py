a = int (int(input('enter num 1:')))
b =int(input('Enter num 2:'))
try:
    res = a//b
    print(f'result = {res}')
    #num = int(input('enter the num'))
    #for i in num:
    #    print(i)

except ZeroDivisionError as s:

    print(f'code run with exception{s}')

except TypeError as v:
    print(f'I am valueError {v}')

except Exception as e:
    print(f'Generealized Exception{e}')        

else:
    print("hello")    