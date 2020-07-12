'''
    Program:
'''
#Import libaries 
import  re

#Declare variables 
withdraw_counter = 0          #variable to hold total amount of withdrawals from account 
deposit_counter = 0           #Variable to hold total amount of deposits from account   
starting_balance = float(input("Please enter the starting balance in the account: "))
num_months = int(input("How many months has it been since the account was open: "))
annualInterestRate = str(input("Please enter the annual interest rate for the account balance: "))

#Parse string to get value for the number entered with percentage annual interest rate 
interest = re.findall(r'\d+',annualInterestRate)
rate = list(map(int,interest))
interestRate = rate[0] #Get the value entered for the interest rate
 

for i in range(0,num_months):
    
    i+=1

    #Get the amount deposited into the account 
    amount = int(input(f"Enter the amount deposited into your account during month {i}: "))
    starting_balance +=amount #increment the amount added 

    #validate user input for amount entered 
    while(amount < 0):
        print(f"You can't enter a negative amount for your account deposit.")
        print(f"Re-enter the amount entered")
        amount = int(input("Enter the amount deposited into your account: "))

    #Get the amount withdrawn from the account 
    amount_withdrawn = int(input(f"Enter the amount withdrawn from your account during month {i}:"))
    starting_balance -=amount_withdrawn #decrement the balance withdrawed 

    #validate user input for amount withdrawn 
    while(amount_withdrawn < 0):
        print(f"You can't enter a negative amount for your amount withdrawn.")
        print(f"Re-enter the amount entered")
        amount_withdrawn = int(input(f"Enter the amount withdrawn from your account during month {i}:"))

    #Increment the total number of withdrawls and deposits for the account
    deposit_counter +=amount
    withdraw_counter +=amount_withdrawn
            
    #Calculate the monthly interest rate 
    monthly_Ir = round((interestRate/12)*starting_balance,2)
 
    #Add monthly interest rate to the balance  
    starting_balance += monthly_Ir

    #If the balance goes below zero during the loop then show user error message and break the loop
    if(starting_balance < 0):
        print(f"Error: you can't have negative account") 
        print(f"The account has been closed")
        break  

#round the balance,deposit amount, and withdrawal amount to 2 decimal places
round(starting_balance,2) 
round(deposit_counter,2)
round(withdraw_counter,2)

#Print output to user if balance is above 0
if(starting_balance > 0):
    print(f"***************************************************************************************************")
    print(f"The ending balance for this account is: ${starting_balance}.")
    print(f"The total amount of deposits is: ${deposit_counter}")
    print(f"The total amount of withdrawls is: ${withdraw_counter}")
    print(f"The total interest earned is ${monthly_Ir}")
    print(f"***************************************************************************************************")






 

 













