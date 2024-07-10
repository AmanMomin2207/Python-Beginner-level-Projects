from turtle import *
import random
WIDTH,HEIGHT = 400,400
color_list = ["red","green","pink","dark orange","violet","brown","blue","grey","black"]

def no_of_turtles():
    while True:
        turtles = int(input("How many turtles are you want to participate in race(2-10):"))
        
        if 2<=turtles<=10:
            return turtles
        
        else:
            print("Please select right option")
            
def race():
    max = 0
    win = 0
    is_race_on = 1
    while is_race_on:
        for i in list_turtles:
            distance = random.randrange(10,50)
            i.fd(distance)
            
            x,y = i.pos()
            
            if y >= 100:
                is_race_on = 0
                print(f"Winner is {i.pencolor()} turtle")
                

    

        
turtles = no_of_turtles()
print(turtles)
s1 = Screen()
s1.setup(400,400)

x_paremeter = WIDTH // (turtles + 1)
list_turtles = []

for i in range(1,turtles+1):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-WIDTH//2 + (i * x_paremeter),-HEIGHT//2 + 30)
    list_turtles.append(new_turtle)

race()
s1.exitonclick()