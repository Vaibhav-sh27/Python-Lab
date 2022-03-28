a=list(input("Enter string "))
b=list(input("Enter 2nd string "))
a.sort()
b.sort()
if (a==b):
    print("Anagram")
else:
    print("Not Anagram")
