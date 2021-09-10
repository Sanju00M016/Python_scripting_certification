digalpha = input("Enter any sentence:")
Digit = 0
Letter = 0
for i in digalpha:
    if i.isdigit():
        Digit=Digit+1
    elif i.isalpha():
        Letter=Letter+1
    else:
        pass
print("Number of Digit", Digit)
print("Number of Letter", Letter)
