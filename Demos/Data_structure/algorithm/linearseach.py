def linearse(li,el):
    for i in range(0,len(li)):
        if(ele==li[i]):
            return i
        
    else:
        return -1    


li=[20,30,45,67,45,78,56,34]
ele = int(input('Enter element to search:'))
res = linearse(li,ele)

if(res != -1):
    print(f'{ele} is presemt at index : {res}')
else:
    print(f'{ele} is not present')    