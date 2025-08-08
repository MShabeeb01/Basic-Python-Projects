#Step-1: Ask for user details
name = input("Please enter your name:")
from datetime import datetime
dob_str = input("Enter your date of birth in (dd/mm/yyyy) format :")

try :
    dob = datetime.strptime(dob_str,"%d/%m/%Y")
    print("Date of birth accepted:",dob.strftime("%d/%m/%Y"))
except ValueError:
    print("Invalid format! Please enter as (dd/mm/yyyy) format ") 
brand = (input("Please enter the car brand:"))     
car =(input("Which car are you looking for the test drive?"))    

#Step-2: Calculate age 
today = datetime.today()
age = today.year - dob.year - ((today.month,today.date) < (dob.month,dob.date))
print(f"You are {age} years old.")

#Step-3: Calculate live time for greetings
today = datetime.today()
current_hour = today.hour
if (5<= current_hour <12):
    greeting = "Good Morning"
elif(12<= current_hour <16):
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"        

#Step-4: Generate personalised message
print(f"\n----{greeting} {name.title()}!----")
print("I hope you are having a wonderful day.")
print(f"We have recieved your request for a test drive of the {brand.title()} {car.title()} , based on your age we would like to inform that:")
if (age<18):
    print ("You are not eligible for the test drive")
elif(age==18):
    print("You need a guardian to take the test drive")
else:
    print("You are eligible for the test ride ")

    
#LEARNINGS 
#1-Line 3, the datetime class is imported from the datetime moudule which deals with working of dates and time    

#2-Line 6, The try except is used for error handling ,the code inside try is attempted ;if an error occurs,the code in except runs.

#3-Line 7,strptime(): "String parse time"—parses a string into a datetime object using the specified format. datetime.strptime(dob_str, "%d/%m/%Y"): Converts the string dob_str into a datetime object, expecting the format (day/month/year)

#4-Line 8,print("Date of birth accepted:", dob.strftime("%d/%m/%Y")): If parsing is successful, prints a confirmation message , strftime("%d/%m/%Y"): "String format time"—formats the datetime object back into a string in the desired format 

#5-Line 9,except ValueError: If the input does not match the expected format, a ValueError is raised, and the error message is printed

#6-Line 13, it returns the current local date and time 

#7-Line 14, today.year gives the current year , dob.year gives the dob year so 
# age = today.year - dob.year (ex;2025-2005=20) now to check if the birthday has already passed or yet to be passed we check using comparison operator so if 
#((today.month,today.date)<(dob.month,dob.date)) if its true then the bday is not yet happend in true case it will retun 1 so age = 20-1 = 19 years , in case if the birthday has already passed that statement will be false and it will retun false which is 0 so age = 20 -0 = 20 years :