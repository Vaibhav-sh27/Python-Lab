s=int(input("Enter Salary "))
if (s<=10000):
        t=s+(s*0.80)+(s*0.90)
        print("Salary is ", t)
elif (10000<s<=20000):
        t=s+(s*0.85)+(s*0.90)
        print("Salary is ", t)
elif (s>20000):
        t=s+(s*0.95)+(s*0.95)
        print("Salary is ", t)
