import os
print("Welcome to the Silent Auction Paper")
members = {}
name = 'str'
while True:
    Name = input("What is your name?:")
    Bid = float(input("What is your bid?:"))
    
    members[Name] = Bid

    Pass = input("Are there any other bidders? Type 'yes' or 'no':")
    Pass.lower()
    if Pass == 'no':
        os.system('cls') 
        break
    elif Pass == 'yes':
       os.system('cls') 
large = 0
for i,j in members.items(): 
    if j >= large:
        large = j
        name = i
print(f"Auction wineer is {name} and it's bid is {large}")