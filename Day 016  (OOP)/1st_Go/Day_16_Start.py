
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen ()
print(my_screen.canvheight)
my_screen.exitonclick()

#Timmmy is an object of the class Turtle
#my_screen is an object of the class Screen

#methods are functions that belong to a class
#functions that belong to an object are called methods
#timmy.forward(100) is a method of the class Turtle
#my_screen.exitonclick() is a method of the class Screen

#object.attribute
#timmy.shape
#my_screen.canvheight

#object.method()
#timmy.forward(100)
#my_screen.exitonclick()

