# simple maths game
import random
import time


# Function to generate expressions
def generate_expression(no_of_operators):
    operations = ['+', '-', '*', '/']
    expression = []

    expression.append(random.randint(0, 20))

    for _ in range(no_of_operators):
        expression.append(random.choice(operations))
        expression.append(random.randint(0, 20))

    expression = ''.join(str(term) for term in expression)
    return expression


# Function to calculate the solution
def result(expression):
    return int(eval(expression))


def main():
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
        print("LEVEL : ", level)
        no_of_operands = level + 1
        question_expression = generate_expression(no_of_operands)
        print(question_expression, end='')
        # Checking for any divide by zero or numerical errors that may show up
        try:
            correct_answer = result(question_expression)
        except:
            print("OOPS ! I messed up ! Lets do it again !")
            continue
        answer = int(input(" = "))
        if correct_answer ==  answer:
            print("CORRECT ! ", end='')
            score = score + 1
            print("SCORE = ", score, "LIVES = ", lives)
            # Increase the level of difficulty every 5 questions.
            if score != 0 and score % 5 == 0:
                level = level + 1
        else:
            print("WRONG ! CORRECT ANSWER WAS ",correct_answer, end='')
            lives = lives - 1
            print("SCORE = ", score, "LIVES = ", lives)
    
    print("GAME OVER !!!")
    print("Maximum Level = ", level, "SCORE = ", score)

if __name__ == "__main__":
    main()






