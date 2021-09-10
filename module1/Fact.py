ele = int(input("Enter the Number: "))

factorial = 1;

if ele < 0:
    print("Please enter the Number Above 1 and Factorial does not exist for number less than ZERO")
elif ele == 0:
    print("The factorial of the Zero is 1")
else:
    for i in range(ele,1,-1):
        print(i)
        factorial = factorial * i
    print("The factorial of the Element", ele ,"is", factorial)

    if (ele % 2) == 0:
     print("The Input Number is EVEN:", ele)
    else:
       print("The Input Number is ODD:", ele)
