#Basic Math Quiz
import random #Random variable generators

#Step-1: Define the Math question function:
def generate_question():
    num1 = random.randint(1,10) #Return random integer in range [a, b], including both end points
    num2 = random.randint(1,10)
    operator = random.choice(['+','-','*']) #Choose a random element from a non-empty sequence.

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return f"{num1} {operator} {num2}", answer           
    
#Step-2: Define the main game loop
def math_quiz():
    score = 0
    rounds = 5

    print("\n---Welcome to the Math Quiz Game---")
    print("You will be presented with Math Problems,you need to provide the correct answers.")
    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"\n Question {i+1}: {question}")
        user_answer = int(input("Your answer:"))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct Answer is {correct_answer}")

    print("\n---Game Over---")
    print(f"Your final score is {score}/{rounds} ")
    if score == rounds:
        print("Congrats you got all the questions correct")
    elif score >= rounds//2:
        print("Good job! You did well")
    else:
        print("Keep practising! You can do better next time")                           

#Step-3: Run the game
math_quiz()
    
