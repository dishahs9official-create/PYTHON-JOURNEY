'''Write a program to take an email address as input and check whether it contains the '@' symbol.'''

'''| Operator | Meaning                                      | Example                       |
| -------- | -------------------------------------------- | ----------------------------- |
| `in`     | Checks if something exists inside a sequence | `"a" in "apple"` → `True`     |
| `not in` | Checks if something does **not** exist       | `"z" not in "apple"` → `True` |
'''
e=input("Enter your email:")
if('@' in e):
    print("Valid Email")
else:
    print("Invalid Email")