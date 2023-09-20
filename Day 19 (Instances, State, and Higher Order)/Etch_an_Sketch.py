from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.forward(-10)

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

screen.listen()
screen.onkey(key ='w', fun = move_forward)
#When using a method as an arguement, you do not add the () after the method. 
screen.onkey(key = "c", fun = clear_screen)
screen.onkey(key ='s', fun = move_backward)
screen.onkey(key ='a', fun = move_left)
screen.onkey(key ='d', fun = move_right)

#Higher Order Functions:
#These are functions that can be used in another function. 
#You should use key word arugments rather than positional word arguments. 
screen.exitonclick()