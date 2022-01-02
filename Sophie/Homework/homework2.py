import random

questionnumber = 1
score = 0

while questionnumber <= 5:
    
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number3 = random.randint(1, 10)

    guess = input("What is " + str(number1) + " + " + str(number2) + " + " + str(number3) + " ? ")

    answer = number1 + number2 + number3
    guess = int(guess)

    if guess == answer:
        print ("that is the right answer!")
        score += 1 
    else:
        print ("that is the wrong answer")
        
    questionnumber += 1

#print out score
print ("your score is..." + str(score ))

if score == 5:
    print ("top marks!!!")
elif score == 4:
    print ("great job!")
elif score <= 3 and score >= 1:
    print ("good try") 
elif score == 0:
    print ("better luck next time")

