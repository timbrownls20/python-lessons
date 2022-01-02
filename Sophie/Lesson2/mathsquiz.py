import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

guess = input("What is " + str(number1) + " + " + str(number2) + " ? ")

answer = number1 + number2
guess = int(guess)

if guess == answer:
    print ("that is the right answer!")
else:
    print ("that is the wrong answer")
