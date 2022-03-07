n=int(input("Enter no. "))
l=0
p=n
j=1

while n>0:
    k=n%10
    n=n//10
    h=1
    i=1
    while i<=k:
        h=h*i
        i=i+1
    l+=h
if(p==l):
    print("Its Strong")
else:
    print("Its not Strong")
