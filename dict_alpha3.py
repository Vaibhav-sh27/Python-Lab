d={}
l=[91,92,93,94,95,96]
for i in range(65,91):
    if i not in l:
        d[chr(i)]=chr(i+32)
print(d)
