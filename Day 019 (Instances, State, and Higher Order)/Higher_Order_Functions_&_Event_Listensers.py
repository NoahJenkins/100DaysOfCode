from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key ='space', fun = move_forward)
#When using a method as an arguement, you do not add the () after the method. 

#Higher Order Functions:
#These are functions that can be used in another function. 
#You should use key word arugments rather than positional word arguments. 
screen.exitonclick()