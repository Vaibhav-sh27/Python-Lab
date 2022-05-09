def isAnagram(s1,s2):
    a.sort()
    b.sort()
    if (a==b):
        print("Anagram")
    else:
        print("Not Anagram")

a=list(input("Enter string "))
b=list(input("Enter 2nd string "))
isAnagram(a,b)
