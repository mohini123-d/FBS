#3. Write a program to find the second largest element in the list.
li = [10,49,56,45,78,21,23]

max = li[0]
smax = 0
for i in range(len(li)):
    if (max<li[i]):
        smax=max
        max = li[i]

    elif(li[i]>smax):
        smax = li[i]

print(f'Second Maximum value is: {smax}')            