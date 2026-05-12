li=[30,40,50,23,43,80]
max=li[0]
for i in range(1,len(li)):
    if max<li[i]:
        max=li[i]

print(max)        