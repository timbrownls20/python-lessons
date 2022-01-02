#Homework
# print the score
# increse number of questions to 5
# add 3 numbers not 2

#extension
#extra mnesaage
#5 - top marks
#4 Well done
#1-3 Good Try
#0 Oops. Please revise

import random

questionNumber = 1
#score = 0

while questionNumber <= 3:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    guess = input("What is " + str(number1) + " + " + str(number2) + " ? ")

    answer = number1 + number2
    guess = int(guess)

    if guess == answer:
        print ("that is the right answer!")
        #add one to score here 
    else:
        print ("that is the wrong answer")

    questionNumber += 1

#print out the score
