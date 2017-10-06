#simple maths game
import random
import time
#Function to generate expressions
def GEN_EX (NO_OP):
    OPERANDS=[]
    OPERATORS =[]
    OPERATIONS = ['+','-','*','/']
    EXPRESSION =[]
    OPR_CNT = 0
    OPRN_CNT=0
    for i in range (0,NO_OP):
        OPERANDS.append(random.randint(0,20))
    for i in range (0,NO_OP-1):
        OPERATORS.append((random.choice(OPERATIONS)))
    for i in range (0,len(OPERATORS)+len(OPERANDS)):
        if i % 2 == 0:
            EXPRESSION.append(OPERANDS[OPR_CNT])
            OPR_CNT += 1
        else:
            EXPRESSION.append(OPERATORS[OPRN_CNT])
            OPRN_CNT += 1
    EXPRESSION = ''.join(str(x) for x in EXPRESSION)
    return EXPRESSION
#Function to calculate the solution
def RESULT (EXPRESSION):
    return (int(eval(EXPRESSION)))
#Function to evaluate if the answer is right
def EVALUATE(P,Q):
    if P == Q:
        return True
    else:
        return False
# Display Message

print ("""Welcome to the maths game !!!
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




#Variables on which the game operates
SCORE = 0
LEVEL = 1
LIVES = 3
start = time.time()
finish = time.time()+60 # for the timed mode, 60 seconds are needed

#While loop to drive the game
while(LIVES != 0 and time.time()<finish):

    if SCORE != 0 and SCORE % 5 == 0:
        LEVEL = LEVEL + 1
    print("LEVEL : ", LEVEL)
    NO_OPERANDS = LEVEL + 1
    REG_EX = GEN_EX(NO_OPERANDS)
    print(REG_EX,end='')
    ANSWER = int(input( " = " ))

    if(EVALUATE(RESULT(REG_EX),ANSWER)):
        print ("CORRECT ! ",end = '')
        SCORE = SCORE + 1;
        print("SCORE = ", SCORE, "LIVES = ", LIVES)
    else:
        print ("WRONG ! ",end='')
        LIVES = LIVES - 1
        print("SCORE = ", SCORE, "LIVES = ", LIVES)
print ("GAME OVER !!!")
print ("Maximum Level = ",LEVEL,"SCORE = ",SCORE)
