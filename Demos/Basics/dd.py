def arm(no):
    rev =0
    rem = 0
    while(no>0):
        rem = no % 10
        rev = rev+rem*rem*rem
        no = no // 10
    return rev

no = int(input("Enter no :"))
temp = no
result=arm(no)
if(temp == result):
    print('no armstrong')
else:
    print('not armstrong')