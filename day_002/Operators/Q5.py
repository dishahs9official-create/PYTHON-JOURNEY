'''Write a Python program to:

Take the length of a rectangle as input.
Take the breadth of the rectangle as input.
Print:
Area
Perimeter'''
L=int(input("Enter length of the Rectangle:"))
B=int(input("Enter breath of the Rectangle:"))

Area=L*B
Perimeter=2*(L+B)

print("Area of rectangle is:",Area)
print("Perimeter of rectangle is:",Perimeter)