# Draws in the window a star surrounded with a circle

import turtle as t
import math as m

FULL_SEGMENT = 500
HALF_SEGMENT = FULL_SEGMENT / 2
STAR_ANGLE = m.pi / 5
TOP_LEFT_VERTEX_Y = HALF_SEGMENT * m.tan(STAR_ANGLE / 2)
CIRCLE_RADIUS = HALF_SEGMENT / m.cos(STAR_ANGLE / 2)


def draw_circle(top_x, top_y, radius):
    t.penup()
    t.setposition(top_x, top_y)
    t.pendown()
    t.color('cyan')
    t.begin_fill()
    t.circle(-radius)
    t.end_fill()
    t.penup()


def draw_star(topleft_x, topleft_y, segment_len):
    """
    Draw a big star
    full_SEGMENT
    """
    t.penup()
    t.setposition(topleft_x, topleft_y)
    t.pendown()
    t.color('blue', 'yellow')
    t.speed('slow')
    t.begin_fill()
    for _ in range(5):
        t.forward(segment_len)
        t.right(m.degrees(m.pi - STAR_ANGLE))
    t.end_fill()
    t.penup()


def main():
    draw_circle(0, CIRCLE_RADIUS, CIRCLE_RADIUS)
    draw_star(-HALF_SEGMENT, TOP_LEFT_VERTEX_Y, FULL_SEGMENT)
    t.done()


main()
