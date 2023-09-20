import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('painting.jpeg', 6)
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
red = rgb[0]
red = rgb.r

from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()

