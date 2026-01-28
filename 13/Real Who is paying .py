import random

print("Hello, Wellcome to the Game ' Who\'s Paying '")

names_str = input('''Please enter the name of persons that sited around the table
 and seperate their name by using',': ''')

name = names_str.split(",")

random1 = random.randint(0,len(name) - 1)

print(f"Today {name[random1]}is going to buy the meal! ")

#print(name)
#example input names: ali , ahmad , mamad , jeff , ross , jj , mj , joj , vahid , asghar 

