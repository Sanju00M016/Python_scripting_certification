#Problem 1
import math

user_input = input("Enter the Direction and Distance the robot travelled :->")
user_input_list = user_input.split(' ')
x=0
y=0

for i in range(0,len(user_input_list),2):
    a=user_input_list[i]
    b=user_input_list[i+1]
    if a=="up" or a=="UP":
        y += int(b)
    elif a=="down" or a=="DOWN":
        y-= int(b)
    elif a=="left" or a=="LEFT":
        x-=int(b)
    elif a=="right" or a=="RIGHT":
        x+=int(b)
    else:
        pass
user_input_list=round(int(math.sqrt((x*x)+(y*y))))
print("The Distance covered is:",user_input_list)