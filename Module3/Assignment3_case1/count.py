user_input =input("Enter the string: ")
upper=0
lower=0
for x in user_input:
    if x.isupper():
        upper = upper + 1
    if x.islower():
        lower = lower + 1
print("the Number of Upper case:",upper)
print("the Number of lower case:",lower)
