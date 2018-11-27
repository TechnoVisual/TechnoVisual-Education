import random

correct = False
r = random.randint(1,10)
c = 0
while correct == False:
    n = input("Guess my number between 1 and 10: ")
    c = c + 1
    if int(n) == r:
        correct = True
    else:
        if int(n) > r:
            print("Sorry, my number is lower. Try again.")
        else:
            print("Sorry, my number is higher. Try again")
        
print("Well done. The correct answer was " + str(r) + ". You got it in " + str(c) + " tries.")
