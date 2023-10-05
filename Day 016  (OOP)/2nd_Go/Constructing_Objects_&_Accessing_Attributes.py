# Constructing Objects $ Accessing Attributes

# object = Class()
# car = CarBlueprint()
#Notice the class is in PascalCase (the first letter of earch word is cap)

# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen
# (from turle library imort turle class)

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('green')
timmy.forward(100)

#Accessing Attributes
# object.attribute
#car.speed

my_screen = Screen()
my_screen.canvheight
print(my_screen.canvheight)
my_screen.exitonclick()

# Accesing Methods
# object.method()
# car.stop()