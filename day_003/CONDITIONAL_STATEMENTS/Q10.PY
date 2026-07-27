'''Write a program to take a single alphabet as input and check whether it is a vowel or a consonant.'''

alpha=input("Enter a alphabet:")
if(len(alpha)==1):
    if(alpha=="a"or alpha=="e" or alpha=="i" or alpha=="o" or alpha=="u" or alpha=="A" or alpha=="E" or alpha=="I" or alpha=="O" or alpha=="U" ):   #== is only for one value not multiple
        print("VOWEL")
    elif(alpha.isalpha()):
        print("You entered a number.")
    else:
        print("consonant")
else:
    print("INVALID INPUT")

