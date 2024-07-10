import random
import question
print("*****************************************************************************")
print("Welcome to My Quiz Game")
print("*****************************************************************************")
def find(score,ques,live):
    no = [1,2,3,4,5]
    while live:
        que = random.choice(no)
        no.remove(que)
        print(question.list1[que])
        ans = input("Enter your answer(A/B/C/D):").upper()
        if ans == question.answer[que]:
            print("Correct Answer")
            score+=1
        else:
            print("Incorrect Answer")
            print(f"The correct answer is: {question.answer[que]}")
        ques +=1
        print(f"Your score is is {score}/{ques}")
        live -=1
    print("Your score is ",(score / 5)*100)
        
score = 0
ques = 0
live = 5
find(score,ques,live)