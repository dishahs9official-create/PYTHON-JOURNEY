'''---------------TRAFFIC LIGHT-----------------'''

light=input("Enter the colour of the traffic light:").lower()

if(light=="red"):
    print("Please stop")#INDENTATION IS THE FOUR SPACE THAT U SEE
elif(light=="yellow"):
    print("Please wait till the light turns green.")
elif(light=="green"):
    print("You can go.")
else:
    print("The traffic light is broken.")

print("-------------EXIT OF THE CODE------------")