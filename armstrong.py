n=int(input("Enter no. "))
l=0
c=0
p=n
while n>0:
    c+=1
    k=n%10
    n=n//10
    k=k**c
    l+=k
if(p==l):
    print("Its Armstrong")
else:
    print("Its not Armstrong")
