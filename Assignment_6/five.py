#Q5.
rows = 5
for i in range(1, rows+1):

    for s in range(rows-i):
        print(" ", end="")

    for j in range(2*i-1):
        print("*", end="")

    print()