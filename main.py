# simple maths game
import random
import time


# Function to generate expressions
from typing import List


def generate_expression(no_of_operators):
    operands = []
    operators = []
    operations = ['+', '-', '*', '/']
    expression = []
    operands_count = 0
    operators_count = 0
    for i in range(0, no_of_operators):
        operands.append(random.randint(0, 20))
    for i in range(0, no_of_operators - 1):
        operators.append((random.choice(operations)))
    for i in range(0, len(operators) + len(operands)):
        if i % 2 == 0:
            expression.append(operands[operands_count])
            operands_count += 1
        else:
            expression.append(operators[operators_count])
            operators_count += 1
    expression = ''.join(str(x) for x in expression)
    return expression


# Function to calculate the solution
def result(expression):
    return (int(eval(expression)))


# Function to evaluate if the answer is right
def evaluate(solution, user_solution):
    if solution == user_solution:
        return True
    else:
        return False



# Display Message

print("""Welcome to the maths game !!!
-----------------------------
Test your basic arithematic skills by playing this simple game. With every 5 correct answers, the level increase
increasing the difficulty of the questions.

Remember : 
----------
        1. Write only the integral part of the answer 
        2. Operator precedence applies
        3. You have 3 lives.
        4. Total of 60 seconds will be provided.
        5. The timer starts after the first answer is entered """)
input("Are you ready ?? Press any key to begin ! ")

# Variables on which the game operates
score = 0
level = 1
lives = 3
start = time.time()
finish_time = time.time() + 60  # for the timed mode, 60 seconds are needed

# While loop to drive the game
while lives != 0 and time.time() < finish_time:
    # Increase the level of difficulty every 5 questions.
    if score != 0 and score % 5 == 0:
        level = level + 1
    print("LEVEL : ", level)
    no_of_operands = level + 1
    question_expression = generate_expression(no_of_operands)
    print(question_expression, end='')
    # Checking for any divide by zero or numerical errors that may show up
    correct_answer = 0
    try:
        correct_answer = result(question_expression)
    except:
        print("OOPS ! I messed up ! Lets do it again !")
        continue
    answer = int(input(" = "))

    if evaluate(correct_answer, answer):
        print("CORRECT ! ", end='')
        score = score + 1
        print("SCORE = ", score, "LIVES = ", lives)
    else:
        print("WRONG ! ", end='')
        lives = lives - 1
        print("SCORE = ", score, "LIVES = ", lives)
print("GAME OVER !!!")
print("Maximum Level = ", level, "SCORE = ", score)


