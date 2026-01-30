import random

guess = input("enter your guess letter: ")
guess = guess.lower()
print("your guess= ", guess)

word_list = ["ali" , "mehdi" , "asghar" ]

chosen_word= random.choice(word_list)
print("chosen_word:" ,chosen_word)

for char in chosen_word:
    if char == guess:
        print("right")
    else:
        print("wrong")

