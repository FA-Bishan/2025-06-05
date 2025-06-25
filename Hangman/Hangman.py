import random as rand

wordToGuess = "aardvark"

gameRunning = True
wordBreakdown  = []
playerGuesses = []
playerLives = 10
for i in wordToGuess:
    wordBreakdown.append(i)
    playerGuesses.append("_")

# print (wordBreakdown)
# print (playerGuesses.count("_"))

while gameRunning:
    

    print ("Welcome to Hangman!")
    print ("This is a game where you guess a word by guessing individual letters.")
    print ("If you get a letter wrong, you lose a life!")
    print ("The game ends when you lose all lives, or you correctly guess the word! whichever comes first.")
    print (f"You have {playerLives} lives, and this word has {playerGuesses.count("_")} letters!")
    print ("Good Luck!")

    letterToGuess = input ("Please guess your a letter")

    if playerLives == 0 or playerGuesses.count("_") == 0:
        gameRunning = False