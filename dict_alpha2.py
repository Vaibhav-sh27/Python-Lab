d={}
l=[91,92,93,94,95,96]
for i in range(65,123):
    if i not in l:
        d[chr(i)]=i
print(d)
