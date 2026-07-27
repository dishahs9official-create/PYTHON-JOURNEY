'''Write a program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding arithmetic operation.*'''

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
o=input("Enter your operator from [+,-,*,/]:")

if(o=="+"):
    print("Sum of both the number is:",n1+n2)
elif(o=="-"):
    print("Difference of both the number is:",n1-n2)
elif(o=="*"):
    print("Product of both the number is:",n1*n2)
elif(o=="/"):
    print("division of both the number is:",n1/n2)
else:
    print("Invalid operator")


'''⭐ One thing is missing

What happens if the user enters:

First number: 10
Second number: 0
Operator: /

Python will try to do:

10 / 0

which gives:

ZeroDivisionError: division by zero

So, inside the division case, you should first check whether the second number is 0.

I won't write the code because I want you to practice.

Just think:

elif operator is "/"

    if second number is 0
        print("Cannot divide by zero")

    else
        perform division'''

