data = [1,2,3,4,5,6,7,8,9,10]
 #method1
sq = lambda x : x ** 2
res = list(map(sq,data))

#method 2
res=list(map(lambda x : x**2,data))



print(res)




