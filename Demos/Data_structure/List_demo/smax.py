li= [20,39,45,12,45,67,78]
max = li[0]
smax= 0
for i in range(len(li)):
    if(li[i]>max):
        smax = max
        max= li[i]
    elif(li[i] > max):
        smax = li[i] 

print(max,smax)           