

#1:
Ans : 4

#2:
Ans : dict_keys(['john', 'peter'])



#3
Name = input("Enter your Name:")
password = input("Enter your Password:").split(",")
password_valid = []
spec_char = ["#","@","$"]

for p in password:
    if(len(p) > 12 or len(p) < 6):
        print("Not valid ! Total characters should be between 6 and 12")
        continue


    Special = any(s in spec_char for s in p)
    if(not Special):
        print("Not valid ! It should contain at least one letter in @,#,$")
        continue

    Number = any(t.isdigit() for t in p)
    if(not Number):
        print("Not valid ! It should contain one letter between [1-9]")
        continue

    if(p.islower() or p.isupper()):
        print("Not valid ! It should contain one letter between [A-Z] and [a-z]")
        continue

    password_valid.append(p)
    print(Name)
    print(password_valid)




#4
a=[4,7,3,2,5,9]
for x in range(len(a)):
    print("Index %d=%d,"%(x,a[x]))



#5
inputchars = input("Please enter text to print::")
if inputchars:
    string = ""
    for i in inputchars:
        if inputchars.index(i) % 2 == 0:
            string += str(i)
    print(string)




#6
user_rev = input("Enter the String to reverse:")
for x in user_rev[::-1]:
    print(x,end="")


#7
String = input("Enter your string:")
str = {x:String.count(x) for x in set(String)}
print("%s"%(str))



#8
a= [1,3,6,78,35,55]
s = set(a)
b = [12,24,35,24,88,120,155]
t = set(b)
print(s & t)


#9
set1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
set2 = set(set1)
list1 = list(set2)
print(list1[::-1])



#10
list3 = [12,24,35,24,88,120,155]
set1 = set(list3)
list2 = list(set1)
list2.remove(24)
print(list2)



#11
try1  = [12, 24, 35, 70, 88, 120, 155]
try1 = [t for (i,t) in enumerate(try1) if i not in(0,4,5)]
print(try1)



#12
try2 = [12,24,35,70,88,120,155]
print([i for i in try2 if i % 5 != 0 and i % 7 != 0])



#13
import random
create1 = []
for i in range(1,1001):
    if(i % 5 == 0 and i % 7 == 0):
        create1.append(i)
print(random.sample(create1,5))
#Alternative: print(random.sample([i for i in range(1,1001)if i%5==0 and i%7==0],5))


#14
num = int(input("enter the Number:"))
ans = 0.0
for i in range(1,num+1):
    ans += float(float(i)/(num+1))
print(ans)



