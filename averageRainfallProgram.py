
"""
Program: To calculate the average rainfall over a period of years. Program gets number of years from user and then gets the 
         inches of rainfall per month from user and loops through each individual month per that year. Program then displays 
         the total amount of rainfall, the total number of months, and average monthly rainfall per the entire period. 
"""

'''Declare input variables''' 
months = 12
response =0 #Counter variable to hold the increment of the total amount of inches for rainfall 
time_year = "year"
time_month = "month"
month_counter = 0 #Counter variable to hold the total number of months 
years = int(input("Enter the number of years: "))
rainfall_counter =0 

'''Validate user input''' 
while(years <1 ):
    print(f"The number of years must be at least 1.")
    print(f"Please re-enter the number of years.")
    years = int(input("Enter the number of years: ")) #re-enter input for years

    
'''Nested loop to go through the years and months '''
for i in range(0,years): 
    i+=1
    for x in range(0,months):
        x+=1
        month_counter = x*years #total number of months 
        #get response from user for inches of rainfall
        response = int(input(f"Enter the number of inches of rainfall for {time_month} {x} and {time_year} {i}: "))
        #increment the amount of rainfall 
        rainfall_counter+=response 

        #Validate the user input if a response is negative for inches of rainfall 
        while(response < 0 or response == -0):
            print(f"You can't enter a value less than 0 for the inches of rainfall")
            print(f"Please re-enter the inches of rainfall for that month.")
            response = int(input(f"Enter the number of inches of rainfall for {time_month} {x} and {time_year} {i}: ")) #re-enter user input 
            


#Declare the average monthly rainfall for the entire period 
avg_rainfall = round(rainfall_counter/month_counter,2)

#show output to user 
print(f"***********************************************************************************************")
print(f"The total amount of rainfall is {rainfall_counter} inches.")
print(f"The total number of months is {month_counter} months.")
print(f"The average monthly rainfall for the entire period is {avg_rainfall} inches.")
print(f"***********************************************************************************************")

















