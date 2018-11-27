import random

WORDLIST = ["orange", "table", "january", "balloon", "mouse", "speaker", "lorry"]
theWord = random.choice(WORDLIST)

def startGuessing():
    triesLeft = 10
    answer = "-" * len(theWord)
    
    while triesLeft > -1 and not answer == theWord:
        print("\n" + answer)
        print(str(triesLeft) + " tries left")
        guess = input("Guess a letter:")
        if len(guess) != 1:
            print("Just guess one letter at a time.")
        elif guess in theWord:
            print("Yes that letter is in the word.")
            answer = updateAnswer(theWord, answer, guess)
        else:
            print("Sorry, that letter is not in the word.")
            triesLeft -= 1
    
    if triesLeft < 0:
        print("Sorry, you have run out of tries. The word was: " + theWord)
    else:
        print("Well done, You guessed right. The word was: " + theWord)

def updateAnswer(word, ans, guess):
    result = ""
    for i in range(len(word)):
        if word[i] == guess:
            result = result + guess
        else:
            result = result + ans[i]
    return result

print("I'm thinking of a word....")
startGuessing()