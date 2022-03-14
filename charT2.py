n=int(input("Enter no. of row"))
for i in range(n):
    for j in range(65,65+i+1):
        print(chr(65+i), end='')
    print()
