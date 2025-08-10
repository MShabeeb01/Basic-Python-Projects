#Step-1: Get user input for countdown start
import time
#Importing this module for time related projects
start = int(input("Enter the number to start the countdown from:"))

#Step-2: Countdown using a while loop
print("\n---Countdown Begins---")
while start > 0:
    print(start)
    time.sleep(1) #Delay execution for a given number of seconds. 
    start -= 1 #Reduce the numbers by 1 second

#Print the final message 
print("---Countdown Completed---")    
