import random as rand

wordToGuess = "aardvark"

gameRunning = True
wordBreakdown  = []
playerGuesses = []
playerLives = 10
for i in wordToGuess:
    wordBreakdown.append(i)
    playerGuesses.append("_")

# print (wordBreakdown.)
# print (wordToGuess.find("a"))

print ("Welcome to Hangman!")
print ("This is a game where you guess a word by guessing individual letters.")
print ("If you get a letter wrong, you lose a life!")
print ("The game ends when you lose all lives, or you correctly guess the word! whichever comes first.")
print (f"You have {playerLives} lives, and this word has {playerGuesses.count("_")} letters!")
print ("Good Luck!")

while gameRunning:
    # gameRunning = False



    print (f"Here is the word to guess: {playerGuesses}")

    letterToGuess = input ("Please guess your a letter \n")

    # if wordToGuess.count("letterToGuess", 0, len(wordToGuess)) > 0:
    #     print ("Letter Found")
    #     wordToGuess.find(letterToGuess)
    guessOccurance = 0
    for i in range(len(playerGuesses)):
        if wordBreakdown[i] == letterToGuess:
            playerGuesses[i] = letterToGuess
            guessOccurance += 1

    if guessOccurance == 0:
        playerLives -= 1

    print (f"You guessed the letter {letterToGuess}. it appeared {guessOccurance} times in the word.")
    print (f"Here are your guesses {playerGuesses}")
    print (f"You have {playerLives} left.")

    if playerLives == 0:
        gameRunning = False
        print ("You have lost all lives.")
        print ("The game is over!")
    
    if playerGuesses.count("_") == 0:
        gameRunning = False
        print("You have correctly guessed the word!")
        print ("The game is over!")