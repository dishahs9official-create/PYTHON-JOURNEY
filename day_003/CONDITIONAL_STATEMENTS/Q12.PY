'''Write a program to take a username as input and check whether its length is between 5 and 15 characters.'''

user=input("Enter a username:")
if(len(user)>5 and len(user)<15):
    print("YES")
else:
    print("NO")

    