import random




scissors = "✌️"
paper = "✋"
rock = "✊"

game = [ rock , paper , scissors ]

computer = random.randint(0,2)
#print(computer,type(computer))

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n "))
#print(user, type(user))

if   user >= 3 or user < 0:
    print(" You entered invalid number. You lose! chose a right number :) \n ")
    print(" if you want to play again push f5 botten")
else:
    print("you chose: ", game[user])
    print("computer chose: ", game[computer])

    if computer == 2 and user == 0:
        print(" You win!")
        print(" if you want to play again push f5 botten")
    elif computer == 0 and user == 2:
        print(" You lose!")
        print(" if you want to play again push f5 botten")
    elif computer > user:
        print(" You lose!")
        print(" if you want to play again push f5 botten")
    elif computer < user:
        print(" You win!")
        print(" if you want to play again push f5 botten")
    elif user == computer:
        print(" equal choices. It's a draw. \n ")
        print(" if you want to play again push f5 botten")
