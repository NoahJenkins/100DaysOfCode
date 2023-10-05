from turtle import Turtle
from turtle import Screen
import random
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('red')


#Challenge 1, make a square with the turtle.
# def square_component():
#     timmy.forward(100)
#     timmy.right(90)
# def make_square():
#     square_component()
#     square_component()
#     square_component()  
#     square_component()

# make_square()

# for num in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# # The exit screen on click has to happen last, so it is at the bottom of the file
# screen = Screen()
# screen.exitonclick()

#Challenge 2:
# timmy = Turtle()
# dash = 15
# skip = 5

# for num in range(20):
#     timmy.pendown()
#     timmy.forward(dash)
#     timmy.penup()
#     timmy.forward(skip)

# screen = Screen()
# screen.exitonclick()

# Challenge 3:

# tim = Turtle()

# # def triangle():
# #     for num in range(3):
# #         timmy.color("red")
# #         timmy.forward(30)
# #         timmy.right(120)

# # def square():
# #     for num in range(4):
# #         timmy.color("green")
# #         timmy.forward(40)
# #         timmy.right(90)

# # def pentagon():
# #     for num in range(5):
# #         timmy.color("blue")
# #         timmy.forward(50)
# #         timmy.right(72)

# # def hexagon():
# #     for num in range(6):
# #         timmy.color("purple")
# #         timmy.forward(60)
# #         timmy.right(60)

# # triangle()
# # square()
# # pentagon()
# # hexagon()

# colors = ['red', "orange", 'green', 'blue', 'pink']

# def draw_shape(num_sides):
#     for num in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)

# for shape_side in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side)

# screen = Screen()
# screen.exitonclick()


# challange 4:

tim = Turtle()
tim.pensize(10)
colors = ['red', "orange", 'green', 'blue', 'pink']
directions = [0, 90, 180, 270]

for num in range(100):
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
    tim.forward(30)

screen = Screen()
screen.exitonclick()
