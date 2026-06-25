"""
Program description: Before the game begins, the computer will randomly choose a word for 
you. The game will then display the mestery word as a series of asterisks("*") and the
player has a certain number of guesses to guess the letter. You win if you guess the 
word before you run out of guesses.
"""
#This function will randomly choose a word and set it as avarieble for convinience of following codes.
import random
words=["high", "school","students","study","hard"]
secret_word=random.choice(words)

# create the mystery word mask
mystery = ["*" for _ in secret_word]
guessed_letters = []

#This nfunction includes if statements to judge player's letter are rather right or wrong.
#The Logic is if it's right print out the position of the letter in word and -1 to the ltters 
#player needs to guess. If wrong then guesses -1.
player_chance=5

def player_guess():
    global player_chance
    player_guess = input("What letter would you like to guess next? : ").lower()
    guessed_letters.append(player_guess)

    index=0
    correct = False
    while index<len(secret_word):
        if secret_word[index].lower()==player_guess :
            mystery[index] = secret_word[index]
            correct = True
        index+=1

    if correct:
        print("CORRECT!!!")
    else:
        print("I'm sorry...")
        player_chance-=1

    print("Here's what you have so far:", "".join(mystery))
    print("You have", player_chance, "guesses left")
    print("Here are the letters you have guessed so far:", " ".join(guessed_letters))

#This code will print off the prologue of the game and lead the player into the game. 
#Explain and introduce the program to them.
print("Welcome to the game of hangman. You will have to guess a meystry word with only 5 chances. If you got a letter wrong you will lose a chance. Good luck!!!")

#This While-loop will continuely repeat the second function until player win/lose the game.
while player_chance >0:
    player_guess()
    if "*" not in mystery:
        break

#This function can break the program when player wins or lose the game
#This code will print off the win/lose line by using if-statement. ANd terminate the program for users.
if "*" not in mystery:
    print("YOU WIN!!! The word was:", secret_word)
else:
    print("You lost... The word was:", secret_word)
