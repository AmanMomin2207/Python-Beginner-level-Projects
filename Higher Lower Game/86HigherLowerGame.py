import database #file in folder
import logo   #file in folder
import random  #built in library
import os   #built in library
score = 0
def higher_lower():
    global score
    print(logo.game_logo)
    choice1 = random.choice(database.data)
    choice2 = random.choice(database.data)
    while True:
        if choice1 == choice2:
            choice2 = random.choice(database.data)
        else:
            break
    print(f"Compare 1: Name : {choice1['Name']}, Description: {choice1['Description']}, Country: {choice1['Country']}")
    print(logo.vs)
    print(f"Compare 2: Name : {choice2['Name']}, Description: {choice2['Description']}, Country: {choice2['Country']}")
    print()
    flag = int(input("Who has more followers ? Type 1 or 2:"))
    if flag == 1:
        if choice1['Followers'] > choice2['Followers']:
            os.system('cls')
            score+=1
            print(f"You are right . Your Score is {score}")
            higher_lower()
        else:
            os.system('cls')
            print(f"You are wrong... Your final score is {score}")
    elif flag == 2:
        if choice2['Followers'] > choice1['Followers']:
            os.system('cls')
            score+=1
            print(f"You are right . Your Score is {score}")
            higher_lower()
        else:
            os.system('cls')
            print(f"You are wrong... Your final score is {score}")

higher_lower()