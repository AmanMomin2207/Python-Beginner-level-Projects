import random
letter = int(input("How many numbers you want in password:"))
listle = ["a","b","c","d","e","f","g","h","i","j","k","l","k","m","n"]
symbol = int(input("How many symbols you want in password:"))
listsy = ["!","@","#","$"]
number = int(input("How many numbers you want in password:"))
listno = [1,2,3,4,5,6,7,8,9]
password = []
size = letter+symbol+number
for i in range(size+1):
    if i < letter:
        char = random.choice(listle)
        password.append(char)
    if i < symbol:
        char = random.choice(listsy)
        password.append(char)
    if i < number:
        char = random.choice(listno)
        password.append(char)
random.shuffle(password)
for i in range(0,len(password)):
    print(password[i],end="")