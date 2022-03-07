n=int(input("Enter no. "))
p=n
no=0
while n>0:
    k=n%10
    n=n//10
    no=(no*10)+k
if(p==no):
    print("Its palindrome")
else:
    print("Its not a palindrome")
