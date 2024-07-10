import random
computer = random.randint(0,2)
users = int(input("Enter your choice \n 0 for Rock \n 1 for Paper \n 2 for Scissors:"))
print(f"{users} verses {computer}")
if users >= 3 or users < 0:
    print("enter valid choice")
else:
    if users == computer:
        print("Draw")
    elif users == 2 and computer == 0:
        print("Computer Wins")
    elif computer == 2 and users == 0:
        print("Users Wins")
    elif computer < users:
        print("User Wins")
    elif computer > users:
        print("Computer Wins")