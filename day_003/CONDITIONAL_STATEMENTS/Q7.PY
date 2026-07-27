'''Write a program to check whether a number entered by the user is divisible by both 5 and 11.'''

a=int(input("Enter a number:"))
if(a%5==0 and a%11==0):
    print("THE NUMBER ENTERED IS DIVISIBLE BY 11 AND 5")
else:
    print("Not divisible")