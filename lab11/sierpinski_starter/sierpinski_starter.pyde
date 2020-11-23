add_library('controlP5')
from controlP5 import ControlP5
from controlP5 import Slider
from point import Point

# For setting up the slider
MIN_DEPTH = 0
MAX_DEPTH = 8

# Coords of starting triangle
TOP_X = 200
TOP_Y = 100
LEFT_X = 50
LEFT_Y = 350
RIGHT_X = 350
RIGHT_Y = 350

startLeft = Point(LEFT_X, LEFT_Y)
startRight = Point(RIGHT_X, RIGHT_Y)
startTop = Point(TOP_X, TOP_Y)

# Controls the recursive depth
depth = 0


def setup():
    size(430, 400)
    noStroke()
    setupSlider()


def draw():
    background(0)

    # Draws the initial white triangle
    fill(255)
    triangle(startLeft.getX(), startLeft.getY(),
             startRight.getX(), startRight.getY(),
             startTop.getX(), startTop.getY())
    sierpinksi(startLeft, startRight, startTop, depth)


# This is a recursive function that draws the Sierpinski triangle
def sierpinksi(bottomLeft, bottomRight, top, recursionDepth):
    if recursionDepth == 0:
        return
    a = Point.midPoint(top, bottomRight)
    b = Point.midPoint(top, bottomLeft)
    c = Point.midPoint(bottomLeft, bottomRight)
    fill(0)
    triangle(a.getX(), a.getY(), b.getX(), b.getY(), c.getX(), c.getY())
    recursionDepth -= 1
    sierpinksi(b, a, top, recursionDepth)
    sierpinksi(bottomLeft, c, b, recursionDepth)
    sierpinksi(c, bottomRight, a, recursionDepth)


# The code below sets up the slider and sets a listener callback
# function to respond to the user sliding the slider.
def setupSlider():
    cp5 = ControlP5(this)
    depthSlider = cp5.addSlider("Recursion Depth")\
        .setPosition(20, 20)\
        .setSize(200, 40)\
        .setRange(MIN_DEPTH, MAX_DEPTH)\
        .setNumberOfTickMarks(9)\
        .addListener(listener)


def listener(event):
    global depth
    depth = event.value()
