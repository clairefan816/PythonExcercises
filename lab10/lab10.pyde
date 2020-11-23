size_x = 600
size_y = 600
circle_x = 300
circle_rad = 75
thrust_factor = 0
spaceship_x = 300
spaceship_y = 300
x_vel = 0
y_vel = 0
rotation = 0


def setup():
    size(size_x, size_y)
    strokeWeight(3)
    colorMode(RGB, 1)


def draw():
    global circle_x
    global rotation
    background(0)
    
    circle_x = circle_x + 1
    
    if circle_x > size_x + circle_rad:
        circle_x = circle_x - size_x
    elif circle_x > size_x - circle_rad:
        draw_circle_1(circle_x - size_x)
        draw_circle_2(circle_x - size_x)
        draw_circle_3(circle_x - size_x)
    
    draw_circle_2(circle_x)
    
    pushMatrix()
    draw_spaceship()
    popMatrix()
    
    draw_circle_1(circle_x)
    draw_circle_3(circle_x)
    
    
def keyPressed():
    global rotation
    global thrust_factor
    if (key == CODED):
        if keyCode == UP:
            thrust_factor = 0.5
        if keyCode == RIGHT:
            rotation += 3
        if keyCode == LEFT:
            rotation -= 3


def draw_circle_1(x):
    fill(0.5, 0.5, 0.5)
    stroke(1.0, 1.0, 1.0)
    ellipse(x, 100, circle_rad*2, circle_rad*2)


def draw_circle_2(x):
    fill(0.8, 0.9, 1.0)
    stroke(1.0, 1.0, 1.0)
    ellipse(300, x, circle_rad*2, circle_rad*2)


def draw_circle_3(x):
    fill(0.5, 0.5, 0.5)
    stroke(1.0, 1.0, 1.0)
    ellipse(x, 500, circle_rad*2, circle_rad*2)

def draw_spaceship():
    global spaceship_x
    global spaceship_y
    global x_vel
    global y_vel
    global thrust_factor
    x_vel = (x_vel + sin(radians(rotation))) * thrust_factor
    y_vel = (y_vel - cos(radians(rotation))) * thrust_factor
    
    spaceship_x = spaceship_x + x_vel
    spaceship_y = spaceship_y + y_vel
    translate(spaceship_x, spaceship_y)
    rotate(radians(rotation))
    fill(0)
    stroke(1)
    strokeWeight(3)
    triangle(-16, 10, 0, -30, 16, 10)
