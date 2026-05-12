num= int(input('enter No to check palindrome or not'))
temp= num
rev= 0
while(temp>0):
    d= temp % 10
    temp = temp// 10
    rev = rev*10+d

if(num==rev):
    print(f'{num} is a Palindrome No.')

else:
    print(f'{num}Is not palindrome')     