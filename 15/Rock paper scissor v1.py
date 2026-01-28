import random

user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n ")
user = int(user)
#print(user, type(user))
game = ["Rock","paper","scissors"]

computer = random.randint(0,2)
#print(computer,type(computer))s

if   user == 0 and computer == 1:
    print(f" you choosed {game[user]} ✊and computer choosed {game[computer]} ✋\n ")
    print(" You lose, play again and win the computer :) \n ")
    print(" if you want to play again push f5 botten")
elif user == 0 and computer == 2:
    print(f" you choosed {game[user]} ✊and computer choosed {game[computer]} ✌ \n ")
    print(" You Won, winner winner chicken dinner :) \n ")
    print(" if you want to play again push f5 botten")
elif user == 1 and computer == 0:
    print(f" you choosed {game[user]} ✋and computer choosed {game[computer]} ✊ \n ")
    print(" You Won, winner winner chicken dinner :) \n ")
    print(" if you want to play again push f5 botten")
elif user == 1 and computer == 2:
    print(f" you choosed {game[user]} ✋and computer choosed {game[computer]} ✌️ \n ")
    print(" You lose, play again and win the computer :) \n ")
    print(" if you want to play again push f5 botten")
elif user == 2 and computer == 0:
    print(f" you choosed {game[user]} ✌️and computer choosed {game[computer]} ✊ \n ")
    print(" You lose, play again and win the computer :) \n ")
    print(" if you want to play again push f5 botten")
elif user == 2 and computer == 1:
    print(f" you choosed {game[user]} ✌️and computer choosed {game[computer]} ✋ \n ")
    print(" You Won, winner winner chicken dinner :) \n ")
    print(" if you want to play again push f5 botten")
elif user >= 3:
    print(" You entered invalid number. You lose! do it wright. :) \n ")
    print(" if you want to play again push f5 botten")
else:
    print(" equal choices. It's a draw. \n ")
    print(" if you want to play again push f5 botten")

