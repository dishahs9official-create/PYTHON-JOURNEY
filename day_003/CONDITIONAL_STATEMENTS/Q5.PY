'''WAP to find greatest of 3 number entered by the user.'''

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if(num1>num2 and num1>num3):
    print("the greatest number is",num1)
elif(num2>num3):
    print("the greatest number is",num2)
else:
    print("the greatest number is",num3)


# OTHER APPROACH USING BUILT IN FUNCTION 
'''
num1 = 63
num2 = 96
num3 = -56

largest = max(num1, num2, num3)

print(largest)'''