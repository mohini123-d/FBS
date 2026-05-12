#1.pass: to skip expected indented block error
for i in range(1,10):
    pass

#2. break: terminate loop
#for i in range(1,6):
   # if(i == 3):
        #break
    #print(i)

#3. continue : stop current interation
#for i in range(1,6):
    #if(i==3):
       # continue
   # print(i) 
   # 
#4. else: execute when loop executed successfully
for i in range(1,6):
    if(i==5):
        break
    print(i)

else:
    print('else block executed')      