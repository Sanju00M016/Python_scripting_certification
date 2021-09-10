def recFact(t):
    if t == 1 or t == 0:
        return t
    else:
        return t * recFact(t-1)

giveInput = int(input("Enter the Number to find the factorial of Number:"))
print("The Factorial of Entered Number is: ",recFact(giveInput))