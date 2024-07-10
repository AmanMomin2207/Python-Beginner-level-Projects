import random
import guessthenumberlogo
easy_attempt = 10
hard_attempt = 5
def easy(number):
    global easy_attempt
    if easy_attempt > 0:
        print(f"You have {easy_attempt} attemts remaining the guess number!")
        guess_no = int(input("Make a guess:"))
        if guess_no == number:
            print(f"Your guess is right.... The answer was {guess_no}")
            return
        elif guess_no > number:
            print("Your is too high")
            easy_attempt-=1
            easy(number)
        elif guess_no < number:
            print("Your is too low")
            easy_attempt-=1
            easy(number)
    else:
        print("You are out of guesses ... You lose!!")
        return
  
    
def hard(number):
    global hard_attempt
    if hard_attempt > 0:
        print(f"You have {hard_attempt} attemts remaining the guess number!")
        guess_no = int(input("Make a guess:"))
        if guess_no == number:
            print(f"Your guess is right.... The answer was {guess_no}")
            return
        elif guess_no > number:
            print("Your is too high")
            hard_attempt-=1
            hard(number)
        elif guess_no < number:
            print("Your is too low")
            hard_attempt-=1
            hard(number)
    else:
        print("You are out of guesses ... You lose!!")
        return
    
print(guessthenumberlogo.logo)
print("let me think of a number between 1 to 50:")
number = random.randint(1,50)
difficulty_level = input("Choose level of difficulty .... Type 'easy' or 'hard' :").lower()
if difficulty_level == 'easy':
    easy(number)
elif difficulty_level == 'hard':
    hard(number)
else:
    print("Choose right word")
    print("You are out of game")