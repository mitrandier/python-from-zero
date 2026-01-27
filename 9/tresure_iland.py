print("Welcome to tresure Island.")
print("Your mission is to find the treasure.")
direction=input("You are at a crossroad. where do you want to go? type 'left' or 'right': \n")
new_direction = direction.lower()
if new_direction == "left":
    tool = input("You come to a lake. Ther is an island inthe middle of the lake. type 'wait' to wait for a boat or type 'swim' to swim across: \n")
    new_tool= tool.lower()
    if new_tool=="wait":
        door= input("You arived at the island unharmed, there is a house with 3 doors. one red, one yellow and the last one is blue. wich door do you choise? \n")
        new_door= door.lower()
        if new_door == "yellow":
            print("congratulation. You found the tresure box. ")
        elif new_door == "red":
            print("It's a room full of fire. Game over. ")
        elif new_door == "blue":
            print("It's a room full of snakes. Game over. ")
        else:
            print("You chose a door that doesn't exist. Game over. ")
    elif new_tool=="swim":
        print("you choosed a bad option. you got attacked by an angry trout. Game over.")
    else:
        print("You chosed a way that doesn't exist. Game over. ")
elif new_direction == "right":
    print("you chosed a bad direction and you fell into a hole. Game over.")
else:
    print("You chosed a word that doesn't exist. Game over. ")