'''
Write a Python program that:

Takes two numbers as input from the user.
Store them in variables a and b.
Perform the following assignment operations on a:
a += b
a -= b
a *= b
a /= b
a %= b
a //= b
a **= b
Print the value of a after each operation'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a += b
print("After += :", a)

a -= b
print("After -= :", a)

a *= b
print("After *= :", a)

a /= b
print("After /= :", a)

a %= b
print("After %= :", a)

a //= b
print("After //= :", a)

a **= b
print("After **= :", a)
