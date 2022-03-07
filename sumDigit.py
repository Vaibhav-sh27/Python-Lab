n=int(input("Enter no. "))
l=0
while n>0:
    k=n%10
    n=n//10
    l+=k
print(l)
