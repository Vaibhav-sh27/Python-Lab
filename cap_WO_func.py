def myTitle(s):
    g=list(s.split(' '))
    for i in g:
        i=list(i)
        k=ord(i[0])
        a=k-32
        i.remove(i[0])
        i.insert(0,chr(a))
        d.append(i)
    for i in range(len(d)):
        lst.append(''.join(d[i]))
    
    print(' '.join(lst))
s=input()
d=[]
lst=[]
myTitle(s)

