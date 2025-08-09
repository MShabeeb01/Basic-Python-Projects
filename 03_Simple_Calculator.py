#Simple Calculator

#Step-1: Get user input for two numbers
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

#Step-2: Select the operation
operation = input("Input the operation which you want to perform:(+,-,*,**,/,//,%)")

#Step-3: Perform the operation
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2 
        print(f"Result: {num1} / {num2} = {result}")
    else :
        print("Error: Division by zero is not allowed")    
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "**":
    result = num1 ** num2
    print(f"Result: {num1} ** {num2} = {result}")
elif operation == "//":
    if num2 != 0:    
        result = num1 // num2
        print(f"Result: {num1} // {num2} = {result}")
    else:
        print("Error: Floor Division by zero is not allowed")
elif operation == "%":
    result = num1 % num2
    print(f"Result: {num1} % {num2} = {result}" )                        
else:
    print("Invalid operation selected")
