'''Arithmatic operators are used for mathematical operations 
such as addition,substration ,multiplication etc..'''
'''Write a program to show all arithmatic operators'''

'''| **Operator** | **Name**       | **Description**                               | **Example** | **Output** |
| ------------ | -------------- | --------------------------------------------- | ----------- | ---------- |
| `+`          | Addition       | Adds two numbers                              | `10 + 5`    | `15`       |
| `-`          | Subtraction    | Subtracts one number from another             | `10 - 5`    | `5`        |
| `*`          | Multiplication | Multiplies two numbers                        | `10 * 5`    | `50`       |
| `/`          | Division       | Divides and returns a decimal value           | `10 / 5`    | `2.0`      |
| `//`         | Floor Division | Divides and returns the integer (floor) value | `10 // 3`   | `3`        |
| `%`          | Modulus        | Returns the remainder after division          | `10 % 3`    | `1`        |
| `**`         | Exponent       | Raises a number to a power                    | `2 ** 3`    | `8`        |
'''
A=int(input("Enter first number:"))
B=int(input("Enter second number:"))

sum=A+B
diff=A-B
product=A*B
divide=A/B
floor_division=A//B
modulus=A%B
power=A**B 

print("sum of given number:",sum)
print("difference of given number:",diff)
print("Product of given number:",product)
print("division of the given number:",divide)
print("floor division of the given number:",floor_division)
print("modulus of the given number:",modulus)
print("Exponent of the given number",power)
