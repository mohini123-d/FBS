#@.check palindrome No usring recursion

def pal(no,rev):
    temp = no 
    rem = 0
    if no == 0:
        return rev
        
    rem = no % 10 
    rev = rev*10+rem
    return pal(no//10,rev)
    
no = int(input("enter no:"))
res = pal(no,0)
if(no == res):
        print("No is Palindrome")
else:
        print("no not palindrome") 
    
       
