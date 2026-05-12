def add(*numbers):
    sum=0
    for num in numbers:
        sum +=num
    return sum

res = add(10,20,30,40)
print(res)    