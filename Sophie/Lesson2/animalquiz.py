def check_guess(guess, answer):
    global score
    if guess.lower() == answer.lower():
        print ("Right answer")
        score = score + 1 

    
score = 0
print ("Hello Human, animal quiz!")

guess1 = input ("which bear lives in the north pole? ")
check_guess(guess1, "polar bear")

guess2 = input ("who's dog is the cutest? ")
check_guess(guess2, "Rosie dog")

guess3 = input ("is the blue whale a mammal? Y/N ")
check_guess(guess3, "yes")

guess4 = input ("how many teeth does an adult dog have? ")
check_guess(guess4, "42")

print ("your score is " + str(score))



  