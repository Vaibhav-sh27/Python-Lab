count=0
a=input("Enter string ")
p=[91,92,93,94,95,96]
for i in range(65, 123):
    if i not in p:
        d=a.find(chr(i))
        if d!=-1:
            count+=1
if count==26:
    print("its pangram")
else:
    print("its not pangram")
