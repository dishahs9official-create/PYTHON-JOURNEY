#Write a program to take the lengths of three sides as input and check whether they can form a triangle.
'''The mathematical logic is called the Triangle Inequality Theorem.

A triangle can be formed only if:

Sum of the first two sides is greater than the third side.
Sum of the first and third sides is greater than the second side.
Sum of the second and third sides is greater than the first side.

Mathematically:

a+b>c
a+c>b
b+c>a

You can visualize the idea with this:

Sides: 3, 4, 5

3+4>5 ✅
3+5>4 ✅
4+5>3 ✅

Triangle can be formed.'''
S1=int(input("Enter first side:"))
S2=int(input("Enter second side:"))
S3=int(input("Enter third side:"))

if(S1+S2>S3 and S1+S3>S2 and S2+S3>S1):
    print("Triangle can be formed.")
else:
    print("Triangle can't be formed.")