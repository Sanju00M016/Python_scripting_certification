def withdrawl():
    amount = int(input("Enter the amount for withdrawal:"))
    if amount > 1000:
        print("Insufficicent Fund ! Transaction Declined")
        return withdrawl()
    else:
        print("Please withdrawl and leave the counter aft1er couting the cash of Rs:",amount,"\n Remaining Balance is",1000 - amount)
        return bank()

def cashCredit():
    currentBalance = 0
    amount = int(input("Enter the amount to be Deposit:"))

    if amount > 0:
        currentBalance += amount
        print("The Depoisted Amount is Rs:",amount,"\n The Current Balance",currentBalance)
    if amount == 0:
        print("Please enter the valid amount")
    else:
        print("Thank you for Banking with us!")
        return bank()

def changePasword():
    currentPin = 1234
    newPin = int(input("Enter your OLD pin: "))
    if newPin==currentPin:
        print(int(input("Enter the New Pin: ")))
    if newPin!=currentPin:
        print("you have entered wrong pin!")
        return changePasword()
    else:
        print("Is your new Pin!")
        print( )
        print(bank())

def exit():
    print("Thank you for Banking with us! Have a Nice Day")

def bank():
    print("\nWelcome to Dell Bank\n\nPlease select the your Banking service from the below list:\n\n 1. Cash Withdrawal\n 2. Cash Depoist\n 3. Change Pin\n 4. Exit\n")
    option = int(input("Enter your Choice: "))
    if option == 1:
        print()
        print(withdrawl())
    if option == 2:
        print()
        print(cashCredit())
    if option == 3:
        print()
        print(changePasword())
    if option == 4:
        print(exit())

bank()


