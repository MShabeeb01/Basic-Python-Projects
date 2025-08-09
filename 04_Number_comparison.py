#Number Comparison Tools 

#Step-1: Get user input for 2 numbers 
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

#Step-2: Check the numbers 
print("/n-----Comparison Details-----")
if num1 == num2:
    print(f"Both the numbers are equal:{num1}")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else :
    print(f"{num2} is greater than {num1}")

#Step-3: Check if number is positive , negative or zero.

if num1 < 0 :
    print(f"{num1} is negative")
elif num1 > 0 :
    print(f"{num1} is positive")   
else :
    print("The number is zero")

if num2 < 0:
    print(f"{num2} is negative")
elif num2 > 0:
    print(f"{num2} is positive")
else :
    print ("The number is zero")                 

                
