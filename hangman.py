#Create variable for word that user is trying to create
word = 'python'
letters_guessed = ""

#Starts from high number and decreases
wrongTurns = 6

#Loops until user has failed 6 times
while wrongTurns > 0:
    #Ask user for a letter
    guess = input('Enter a letter: ')
    
    if guess in word:
        print(f"Correct! The given word has at least one letter {guess}.")
    else:
        wrongTurns -= 1
        print(f"Wrong! The letter {guess} is not in the word. You have {wrongTurns} turn(s) left.")
    #Create a list of all the letters guessed
    letters_guessed = letters_guessed + guess
    wrongLetterCount = 0
    for letter in word:
        if letter in letters_guessed:
            print(f"{letter}", end='')
        else:
            print("*", end='')
            wrongLetterCount += 1
    #Prints a blank line
    print("")
    if wrongLetterCount == 0:
        print(f"Congrats! The secret word was {word}. You won!")
        break
else:
    print("Game Over!!! Try again.")