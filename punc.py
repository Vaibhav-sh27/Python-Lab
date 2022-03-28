import string
c=[]
a=input("Enter string ")
for i in a:
    if i not in string.punctuation:
        c.append(i)
for i in c:
    print(i,end='')
