import math
C = 50
H = 30
e_list = []
final = []
user_input = input("Enter the value such as 100,200,180: ")
e_list = user_input.split(',')
e_list = [int(i) for i in e_list]
i=0
t = len(e_list)
while(i<t):
    ele = round(math.sqrt((2 * C * e_list[i]) / H ))
    final.append(ele)
    i+=1
print("output=",final)
