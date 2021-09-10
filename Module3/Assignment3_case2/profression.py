
import numpy as np
import pandas as pd

#Reading the file
filepath=("C:\\Users\sanjum\\Desktop\\Devops\\venv\\unmv8h36uh\\777_m3_datasets_v1.0\\bank-data.csv")
bank_file = pd.read_csv(filepath)
new_job = bank_file["job"].unique()
profession = str(input("Enter your Profession:"))

if profession in new_job:
    print("You're eligible for marketing campaign")
else:
    print("Sorry! your not eligible")


#Enhancements for code

max_age = bank_file['age'].max()
min_age = bank_file['age'].min()

condition = {"Maximum age for loan":max_age,"Minimun age for loan":min_age}

while True:
    user_input = str(input("Enter the Profession Checking: "))
    x = user_input.lower()
    if x in new_job:
        print("Profession Exist")
    else:
        print("Profession is not available")
    if user_input=="end" or user_input=="END":
        break









