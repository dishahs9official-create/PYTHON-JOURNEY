'''Write a program to take a password as input and check whether it is a strong password based on its length.'''

password=input("Enter password:")
if(len(password)>8):
    print("Strong password")
else:
    print("Week password:")