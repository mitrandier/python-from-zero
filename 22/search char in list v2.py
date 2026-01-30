print("Hi welcome to Hangman")

import random

stages = ['''

    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
_____|___

''','''

    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
_____|___

''','''

    _______
     |/      |
     |      (_)
     |      \|/
     |       
     |     
     |
_____|___

''','''

    _______
     |/      |
     |      (_)
     |       |
     |       
     |     
     |
_____|___

''','''

    _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
_____|___

''','''

    _______
     |/      |
     |      
     |      
     |       
     |       
     |
_____|___

''','''

    _______
     |/      
     |      
     |      
     |       
     |       
     |
_____|___

''']

lives = 6

word_list = ["ali" , "asghar" ]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

#print(f"pssst, the chosen word is: {chosen_word}. ")



display = []
for _ in range(word_lenght):
    display += "_"
#print(display, " \n")

end_of_game = False
while not end_of_game:
    
    guess = input("enter your guess letter: ")
    guess = guess.lower()
    #print("your guess= ", guess)

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            #print("match")
    
    
    if guess not in chosen_word:
        #print("no matches")
        lives -= 1
        print(f"Your chance is:" , lives)
        if lives == 0:
            end_of_game = True
            print("You lose!\n")
            
    print(display , "\n")
    
    if "_" not in display:
        end_of_game = True
        print("you win.\n")
        
    print(stages[lives])       
    
    
















