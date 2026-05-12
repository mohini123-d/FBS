#5. Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.

li = [10,40,5,34,78,5,23,9,23,10]
cnt = 0

no = int(input("Enter no to search:"))

for i in range(len(li)):
    if(no == li[i]):
        cnt += 1

    else:
        print('not found')

print(f'{no} is found at count : {cnt}')            