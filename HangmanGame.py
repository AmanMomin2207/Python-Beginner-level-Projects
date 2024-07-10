import random
Characters = ["apple","Aman","Jenny"]
word = random.choice(Characters)
print(word)
live = 6
list = ['_'] * len(word)
print(list)
guess = input("Guess a character:")
flag = 0
for i in range(len(word+1)):
    if word[i] == guess:
        list[i] = guess
        flag +=1
    else:
        pass
if flag == 0:
    if live >=0:
        print("Lose a life")
        live -= 1
    else:
        print("You lose")
        