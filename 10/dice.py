import random
n = int(input("please enter the size of your dice between 1 and 12: "))
random1 = random.randint(1,n)
print(random1)

game = input(" do you want to continue the game? enter y for Yes and n for No :")
new_game = game.lower()
if new_game == "y":
    import random
    m = int(input("please enter the size of your dice between 1 and 12: "))
    random1 = random.randint(1,m)
    print(random1)
    game = input(" do you want to continue the game? enter y for Yes and n for No :")
    new_game = game.lower()
    if new_game == "y":
        import random
        m = int(input("please enter the size of your dice between 1 and 12: "))
        random1 = random.randint(1,m)
        print(random1)
        game = input(" do you want to continue the game? enter y for Yes and n for No :")
        new_game = game.lower()
        if new_game == "y":
            import random
            m = int(input("please enter the size of your dice between 1 and 12: "))
            random1 = random.randint(1,m)
            print(random1)
        else:
            print("that was cool, until next round goodbye.")
    else:
        print("that was cool, until next round goodbye.")
else:
    print("that was cool, until next round goodbye.")

