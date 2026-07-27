'''Grade students based on there marks

marks>=90,grade="A"
90>MARKS<=80,GRADE="B"
80>MARKS<=70,GRADE="C"
70>MARKS<=70,GRADE="D"........

'''

marks=float(input("Enter the percentage of the student:"))

if(marks>=90):
    print("GRADE A")
elif(90>marks>=80):
    print("GRADE B")
elif(80>marks>=70):
    print("GRADE C")
elif(70>marks>=60):
    print("GRADE D")
elif(70>marks>=40):
    print("pass,need to work hard")
else:
    print("FAIL")

print("------------------------THANK YOU-----------------------------------")