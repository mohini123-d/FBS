s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = {50,60}
s4 = {70,80}

s1.add(100)
#s1.clear()
#s2 = s1.copy()
#res = s1.difference(s2)
#res = s1.difference_update(s2)

#res= s1.intersection(s2)
#res= s1.intersection_update(s2)

s1.discard(50)
#s1.pop()
#s1.remove(50)

#res = s1.isdisjoint(s4)
res = s2.issuperset(s3)
res = s2.issubset(s3)
s1.update({10,20,30,40})
print(s1)