import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list				#import clear
print(logo[0], "\n")
print("Hi welcome to Hangman")
lives = 6
word_list = ["ali" , "asghar" ]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)				#print(f"pssst, the chosen word is: {chosen_word}. ")
display = []
for _ in range(word_lenght):
    display += "_"				#print(display, " \n")
end_of_game = False
while not end_of_game:
    guess = input("enter your guess letter: ")
    guess = guess.lower()				#print("your guess= ", guess)				#clear()
    if guess in display:
        print(f"you've already guessed {guess}")
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter		  #print("match")
    if guess not in chosen_word:				 #print("no matches")
        print(f"you guessed {guess}, that's not in the word. you lose a life.")
        lives -= 1
        print(f"Your chance is:" , lives)
        if lives == 0:
            end_of_game = True
            print("You lose!\n")     
    b = ""
    for i in range (len(display)):
        b += (display[i] + " ")
    print(b)
    if "_" not in display:
        end_of_game = True
        print("you win.\n")   
    print(stages[lives])       
    
    
















