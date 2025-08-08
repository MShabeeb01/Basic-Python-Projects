#Step-1:Ask for user details using input function
name = input("What's your name?")
hobby = input("What's your hobby?")

#Step-2: Generate a personalised welcome message
print("\n--- Welcome to Visual Studio Code---")
print(f"Hello,{name.title()}!")
print("Welcome to the world of Python Programming")
print(f"Its great to know that you love {hobby.capitalize()}.")
print("Get ready to learn something exciting today!!")

#LEARNINGS
#1-title() function is used to capitalize the first letter of all words in the input whereas capitalize() function is used only to capitalize the first letter of first word
