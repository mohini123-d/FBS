#Q7.
rows = 5
ch = 65
for i in range(1, rows+1):

    for s in range(rows-i):
        print(" ", end=" ")

    for j in range(2*i-1):
        print(chr(ch), end=" ")
        ch = ch+1
    print()