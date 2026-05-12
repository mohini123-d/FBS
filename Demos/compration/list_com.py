li = [ele for ele in range(1,11)]
#print(li)

li2 = [ele for ele in range(1,11) if ele%2 == 0]
#print(li2)

#li3 = [int(input()) for ele in range(1,5)]
#print(li3)

li4 = [[ele for ele in range(1,11)],[ele for ele in range(11,21)]]
#print(li4)

li5 =[[ele for ele in range(i * 10 + 1, i* 10 +11)] for i in range(0,10)]
print(li5)
#wa prog to create snake ladder board wihthout using using list compration and with using list compretion