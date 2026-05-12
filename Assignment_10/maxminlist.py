#2. Write a program to find maximum and minimum element in a list.

li = [10,40,35,67,22]
max = li[0]
min = li[0]
for i in range(1,len(li)):
    if(max<li[i]):
        max = li[i]

    if(min>li[i]):
        min = li[i]


print(f'Max value is:{max}, Min Value is: {min}')


