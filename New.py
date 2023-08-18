from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import keyboard
import time


# Functions for drawing the maze
def draw_points(x, y):
    glPointSize(5)
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


# --------------------------------------END WINNER MESSAGE--------------------------------------------------------------------------------




#  Function of glVertex2f
# def draw_wall(x1, y1, x2, y2, x3, y3, x4, y4):
#     glBegin(GL_QUADS)
#     glVertex2f(x1, y1)
#     glVertex2f(x2, y2)
#     glVertex2f(x3, y3)
#     glVertex2f(x4, y4)
#     glEnd()



#  Function of Mid Point Line
def color_blocks(x1, y1, x2, x4, y4):
    a = x2 - x1
    for i in range(1, a):
        DrawLine(x1+i, y1, x4+i, y4)
    return DrawLine(x1, y1, x4, y4)

def draw_wall(x1, y1, x2, y2, x3, y3, x4, y4):
    color_blocks(x1, y1, x2, x4, y4)

    DrawLine(x1, y1, x2, y2)
    DrawLine(x2, y2, x3, y3)
    DrawLine(x3, y3, x4, y4)
    DrawLine(x4, y4, x1, y1)


#  MAZE
def draw_maze():
    glColor3f(0, 0, 0.2)
    draw_wall(1, 759, 759, 759, 759, 1, 1, 1)

    glColor3f(0.5, 1, 1)
    draw_wall(60, 680, 80, 680, 80, 60, 60, 60)
    draw_wall(80, 80, 660, 80, 660, 60, 80, 60)
    draw_wall(120, 680, 660, 680, 660, 660, 120, 660)
    draw_wall(640, 660, 660, 660, 660, 120, 640, 120)

    draw_wall(120, 660, 140, 660, 140, 600, 120, 600)
    draw_wall(180, 620, 300, 620, 300, 600, 180, 600)
    draw_wall(340, 620, 360, 620, 360, 560, 340, 560)
    draw_wall(400, 620, 640, 620, 640, 600, 400, 600)
    draw_wall(180, 600, 200, 600, 200, 540, 180, 540)
    draw_wall(120, 560, 180, 560, 180, 540, 120, 540)
    draw_wall(120, 540, 140, 540, 140, 480, 120, 480)
    draw_wall(140, 500, 260, 500, 260, 480, 140, 480)
    draw_wall(300, 500, 480, 500, 480, 480, 300, 480)
    draw_wall(460, 480, 480, 480, 480, 280, 460, 280)
    draw_wall(240, 540, 260, 540, 260, 500, 240, 500)
    draw_wall(240, 560, 400, 560, 400, 540, 240, 540)
    draw_wall(440, 560, 540, 560, 540, 540, 440, 540)
    draw_wall(520, 540, 540, 540, 540, 320, 520, 320)
    draw_wall(580, 560, 600, 560, 600, 440, 580, 440)
    draw_wall(540, 460, 580, 460, 580, 440, 540, 440)
    draw_wall(180, 480, 200, 480, 200, 260, 180, 260)
    draw_wall(120, 440, 140, 440, 140, 360, 120, 360)
    draw_wall(240, 440, 420, 440, 420, 420, 240, 420)
    draw_wall(240, 420, 260, 420, 260, 300, 240, 300)
    draw_wall(400, 420, 420, 420, 420, 200, 400, 200)
    draw_wall(300, 380, 360, 380, 360, 360, 300, 360)
    draw_wall(340, 360, 360, 360, 360, 160, 340, 160)
    draw_wall(300, 320, 340, 320, 340, 300, 300, 300)
    draw_wall(580, 400, 600, 400, 600, 280, 580, 280)
    draw_wall(80, 320, 140, 320, 140, 300, 80, 300)
    draw_wall(120, 260, 300, 260, 300, 240, 120, 240)
    draw_wall(420, 280, 480, 280, 480, 260, 420, 260)
    draw_wall(520, 280, 640, 280, 640, 260, 520, 260)
    draw_wall(80, 200, 180, 200, 180, 180, 80, 180)
    draw_wall(220, 200, 300, 200, 300, 180, 220, 180)
    draw_wall(280, 180, 300, 180, 300, 120, 280, 120)
    draw_wall(120, 140, 280, 140, 280, 120, 120, 120)
    draw_wall(340, 100, 480, 100, 480, 80, 340, 80)
    draw_wall(300, 160, 460, 160, 460, 140, 300, 140)
    draw_wall(460, 220, 480, 220, 480, 140, 460, 140)
    draw_wall(480, 220, 600, 220, 600, 200, 480, 200)
    draw_wall(520, 160, 540, 160, 540, 80, 520, 80)
    draw_wall(580, 160, 600, 160, 600, 80, 580, 80)

    glColor3f(0.8, 0, 0)
    draw_wall(640, 120, 680, 120, 680, 80, 640, 80)


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


x = 100
y = 700
radius = 12
point = 0


def handle_key_press(key):
    global x, y, radius, point
    if key == "right" or key == "left" or key == "up" or key == "down":
        temp_x, temp_y = x, y
        x_new, y_new = move(x, y, key)
        pixel = read_pixel_color(int(x_new), int(y_new))  # Ensure integer values for pixel coordinates

        if pixel == b'\x80\xff\xff':
            x, y = temp_x, temp_y  # Restore the previous position
        elif pixel == b'\x00\x003':
            x, y = x_new, y_new  # Update the new position if no collision
        elif pixel == b'\xff\xff\xff':
            x, y = 705, 100
            radius = scale(radius)
            point = 10

            ######add winner function here ######


def winner_lose_message(result):
    #    result_1 = "YOU WIN"

    #    result_2 = "YOU LOST"

    list(result)

    distance = 0

    for i in result:
        output(i, distance)

        distance += 60


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


def showScreen2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0)
    result_2 = "YOU LOST"
    # Draw the ball
    # draw_ball(300, 300, 100)
    winner_lose_message(result_2)

    glutSwapBuffers()


def showScreen3():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    result_1 = "YOU WIN"
    # Draw the ball
    draw_ball(200, 200, 50)
    winner_lose_message(result_1)

    glutSwapBuffers()


# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------


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
end_time = start_time + 2
print("end", end_time)
while True:
    current_time = time.time()
    if point == 10 and current_time < end_time:
        glutDisplayFunc(showScreen3)
        glutPostRedisplay()  # Trigger a redraw to display winner title
        glutMainLoop()
        break
    elif current_time >= end_time:
        print('stop')
        glutDisplayFunc(showScreen2)
        glutPostRedisplay()  # Trigger a redraw to display game over
        glutMainLoop()
        break
    else:
        handle_key_events()
        glutMainLoopEvent()













