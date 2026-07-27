'''Write a program that:
Takes two numbers as input.
Prints the result of these comparison operators'''
'''| Operator | Name                     | Example    | Result |
| -------- | ------------------------ | ---------- | ------ |
| `==`     | Equal to                 | `5 == 5`   | `True` |
| `!=`     | Not Equal to             | `5 != 3`   | `True` |
| `>`      | Greater Than             | `10 > 5`   | `True` |
| `<`      | Less Than                | `5 < 10`   | `True` |
| `>=`     | Greater Than or Equal To | `10 >= 10` | `True` |
| `<=`     | Less Than or Equal To    | `5 <= 10`  | `True` |

'''
F=int(input("Enter first number:"))
S=int(input("Enter second number:"))

Operator_1=F==S
Operator_2=F!=S
Operator_3=F>S
Operator_4=F<S
Operator_5=F<=S
Operator_6=F>=S

print("Result of equal to operator :",Operator_1)
print("Result of not equal to operator :",Operator_2)
print("Result of Greater than operator :",Operator_3)
print("Result of less than operator :",Operator_4)
print("Result of  Less Than or Equal To operator :",Operator_5)
print("Result of  Greater Than or Equal To operator :",Operator_6)


