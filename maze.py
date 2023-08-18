
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import keyboard
import time


# Functions for drawing the maze

def draw_wall(x1, y1, x2, y2):
    glPointSize(20)
    DrawLine(x1+20,y1,x2+20,y2)
    #DrawLine(x1+20,y1*20+100,x2*20,y2*20+100)


def draw_maze():
    glColor3f(0.5, 1, 1)
    draw_wall(60, 60, 60, 660)    # Left wall
    draw_wall(80, 60, 640, 60)    # Down wall
    draw_wall(640, 120, 640, 660)   # Right wall
    draw_wall(120, 660, 640, 660)   # Up wall

    # Inner maze walls

    # Horizontal Lines
    draw_wall(180, 600, 280, 600)
    draw_wall(340, 600, 340, 560)
    draw_wall(400, 600, 640, 600)
    draw_wall(240, 540, 420, 540)
    draw_wall(480, 540, 520, 540)

    draw_wall(140, 480, 300, 480)
    draw_wall(360, 480, 460, 480)
    draw_wall(480, 320, 500, 320)
    draw_wall(240, 420, 400, 420)
    draw_wall(420, 260, 640, 260)
    draw_wall(120, 540, 180, 540)
    draw_wall(540, 440, 580, 440)
    draw_wall(300, 300, 340, 300)
    draw_wall(300, 360, 340, 360)
    draw_wall(120, 240, 280, 240)
    draw_wall(80, 180, 160, 180)
    draw_wall(220, 180, 280, 180)
    draw_wall(120, 120, 280, 120)
    draw_wall(300, 140, 460, 140)
    draw_wall(340, 80, 460, 80)
    draw_wall(460, 200, 580, 200)
    draw_wall(80, 300, 120, 300)


    # Vertical Lines
    draw_wall(120, 600, 120, 660)
    draw_wall(340, 560, 340, 600)
    draw_wall(180, 540, 180, 580)
    draw_wall(120, 480, 120, 520)
    draw_wall(240, 500, 240, 520)
    draw_wall(180, 260, 180, 460)
    draw_wall(120, 360, 120, 420)
    draw_wall(240, 300, 240, 400)
    draw_wall(400, 200, 400, 400)
    draw_wall(460, 320, 460, 460)
    draw_wall(520, 320, 520, 520)
    draw_wall(580, 280, 580, 380)
    draw_wall(580, 440, 580, 540)
    draw_wall(340, 320, 340, 340)
    draw_wall(340, 160, 340, 280)
    draw_wall(280, 140, 280, 160)
    draw_wall(520, 80, 520, 140)
    draw_wall(580, 80, 580, 140)
    draw_wall(460, 140, 460, 180)


    # finish line
    glColor3f(1, 1, 1)
    draw_wall(640, 80, 640, 100)


# _________________________________________________________________________

# display message
def draw_points(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


# --------------------------------------WINNER MESSAGE--------------------------------------------------------------------------------

def find_zone(dx, dy):
    if dx > -1 and dy > -1:
        if abs(dx) >= abs(dy):
            return 0
        else:
            return 1
    elif dx < 0 and dy > -1:
        if abs(dx) < abs(dy):
            return 2
        else:
            return 3
    elif dx < 0 and dy < 0:
        if abs(dx) >= abs(dy):
            return 4
        else:
            return 5
    else:
        if abs(dx) < abs(dy):
            return 6
        else:
            return 7


def zone0_conversion(x1, y1, x2, y2, zone):
    if zone == 0:
        x1, y1 = x1, y1
        x2, y2 = x2, y2

    elif zone == 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    elif zone == 2:
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2

    elif zone == 3:
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2

    elif zone == 4:
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2

    elif zone == 5:
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2

    elif zone == 6:
        x1, y1 = -y1, x1
        x2, y2 = -y2, x2

    elif zone == 7:
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2
    return x1, y1, x2, y2


def DrawLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = find_zone(dx, dy)
    x1, y1, x2, y2 = zone0_conversion(x1, y1, x2, y2, zone)
    X0 = []
    Y0 = []
    D = []
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    D = D + [d]
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    x = x1
    y = y1

    while x <= x2:
        tempx = x
        tempy = y
        X0 += [x]
        Y0 += [y]
        tempx, tempy = convert_to_origin_zone(tempx, tempy, zone)
        draw_points(tempx, tempy)
        x += 1

        if (d > 0):
            d = d + incNE
            y = y + 1

        else:
            d = d + incE
            D += [d]


def convert_to_origin_zone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


# ===========================================================================


def top(x):
    DrawLine(x + 50, 400, x + 100, 400)


def mid(x):
    DrawLine(x + 50, 350, x + 100, 350)


def bottom(x):
    DrawLine(x + 50, 300, x + 100, 300)


def left_above(x):
    DrawLine(x + 50, 400, x + 50, 350)


def left_bottom(x):
    DrawLine(x + 50, 350, x + 50, 300)


def right_above(x):
    DrawLine(x + 100, 400, x + 100, 350)


def right_bottom(x):
    DrawLine(x + 100, 350, x + 100, 300)


def left_above_right_below(x):
    DrawLine(x + 50, 400, x + 100, 300)


def diagonal_left(x):
    DrawLine(x + 50, 300, x + 75, 400)


def diagonal_right(x):
    DrawLine(x + 100, 300, x + 75, 400)


def diagonal_left_for_Y(x):
    DrawLine(x + 50, 400, x + 75, 350)


def diagonal_right_for_Y(x):
    DrawLine(x + 100, 400, x + 75, 350)


def mid_for_Y(x):
    DrawLine(x + 75, 350, x + 75, 300)


def only_I(x):
    DrawLine(x + 75, 400, x + 75, 300)


# Output

def output(value, x):
    if value == "O":
        top(x)
        right_above(x)
        right_bottom(x)
        left_above(x)
        left_bottom(x)
        bottom(x)

    elif value == "U":
        right_above(x)
        right_bottom(x)
        left_above(x)
        left_bottom(x)
        bottom(x)

    elif value == "I":
        only_I(x)

    elif value == "N":
        left_above(x)
        left_bottom(x)
        left_above_right_below(x)
        right_above(x)
        right_bottom(x)

    elif value == "W":
        right_above(x)
        right_bottom(x)
        diagonal_left(x)
        diagonal_right(x)
        left_above(x)
        left_bottom(x)
    # -----------------------------------------------

    elif value == "Y":
        diagonal_left_for_Y(x)
        diagonal_right_for_Y(x)
        mid_for_Y(x)

    elif value == "S":
        top(x)
        left_above(x)
        mid(x)
        right_bottom(x)
        bottom(x)

    elif value == "L":
        left_above(x)
        left_bottom(x)
        bottom(x)

    elif value == "T":
        top(x)
        only_I(x)


# draw cricle
def drawpoints(x, y):
    glPointSize(1.25)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 0)
    glVertex2f(x, y)
    glEnd()


def midpoint_circle(x1, y1, r):
    d = 1 - r
    x = 0
    y = r
    circlepoints(x, y, x1, y1)
    while (x < y):
        # Choose East
        if d < 0:
            d = d + (2 * x) + 3
            x = x + 1
        else:
            # Choose SE
            d = d + (2 * x) - (2 * y) + 5
            x = x + 1
            y = y - 1
        circlepoints(x, y, x1, y1)


def circlepoints(x, y, x1, y1):
    drawpoints(x + x1, y + y1)
    drawpoints(y + x1, x + y1)
    drawpoints(y + x1, -x + y1)
    drawpoints(x + x1, -y + y1)
    drawpoints(-x + x1, -y + y1)
    drawpoints(-y + x1, -x + y1)
    drawpoints(-y + x1, x + y1)
    drawpoints(-x + x1, y + y1)


def draw_ball(x, y, r):
    for i in range(r):
        midpoint_circle(x, y, i)
    return midpoint_circle(x, y, r)


def read_pixel_color(x, y):
    glReadBuffer(GL_FRONT)  # Set the buffer to be read (front buffer in this case)
    pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)  # Read the pixel color
    return pixel


def move(x, y, direction):
    tx = 0
    ty = 0
    if direction == "up":
        ty = 20
    elif direction == "down":
        ty = -20
    elif direction == "left":
        tx = -20
    else:
        tx = 20

    t = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])

    s = np.array([[x],
                  [y],
                  [1]])

    ts = np.matmul(t, s)

    return ts[0][0], ts[1][0]


def scale(r):
    sc = 2
    s = np.array([[sc, 0],
                  [0, 1]])

    v = np.array([[r],
                  [1]])

    scaled_r = np.matmul(s, v)
    return scaled_r[0][0]


x = 110
y = 710
radius = 10
point = 0


def handle_key_press(key):
    global x, y, radius, point
    if key == "right" or key == "left" or key == "up" or key == "down":
        temp_x, temp_y = x, y
        x_new, y_new = move(x, y, key)
        pixel = read_pixel_color(int(x_new), int(y_new))  # Ensure integer values for pixel coordinates
        print(pixel)
        if pixel == b'\x80\xff\xff':
            x, y = temp_x, temp_y  # Restore the previous position
        elif pixel == b'\x00\x00\x00':
            x, y = x_new, y_new  # Update the new position if no collision
        elif pixel == b'\xff\xff\xff':
            x, y = 705, 100
            radius = scale(radius)
            point = 10

            ######add winner function here ######


def refresh_window(value):
    glutPostRedisplay()
    glutTimerFunc(16, refresh_window, 0)


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_maze()

    # Draw the ball
    draw_ball(x, y, radius)

    glutSwapBuffers()


def handle_key_events():
    try:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            handle_key_press(event.name)
    except:
        pass


def winner_lose_message(result):
    #    result_1 = "YOU WIN"
    #    result_2 = "YOU LOST"
    list(result)
    distance = 0
    glPointSize(5)
    for i in result:
        output(i, distance)
        distance += 60


def showScreen2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0)
    result_2 = "YOU LOST"
    winner_lose_message(result_2)
    glutSwapBuffers()


def showScreen3():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    result_1 = "YOU WIN"
    winner_lose_message(result_1)
    glutSwapBuffers()


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


print("INSTRUCTIONS")
print("You have 20 seconds to reach the finish line")
print("")
print("Press any key to start")
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(735, 735)
glutInitWindowPosition(400, 10)
wind = glutCreateWindow(b"Maze")
glutDisplayFunc(showScreen)
glutTimerFunc(0, refresh_window, 0)  # Start the refresh timer
start_time = time.time()
end_time = start_time + 40

while True:
    current_time = time.time()
    if point == 10 and current_time < end_time:
        time.sleep(1.5)
        glutDisplayFunc(showScreen3)
        glutPostRedisplay()  # Trigger a redraw to display winner title
        glutMainLoop()
        break
    elif current_time >= end_time:

        glutDisplayFunc(showScreen2)
        glutPostRedisplay()  # Trigger a redraw to display game over
        glutMainLoop()
        break
    else:
        handle_key_events()
        glutMainLoopEvent()

