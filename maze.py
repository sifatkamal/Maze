from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import keyboard
import time


# Function to draw pixels
def draw_points(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


# --------------------------------Midpoint Line-----------------------------------------------------------

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


# ---------------------------------------------------------MAZE------------------------------------------------

# -----------------------------Functions for drawing the maze-------------------------------------------------------
def draw_wall(x1, y1, x2, y2):  # calling midpoint line algorithm
    glPointSize(30)
    DrawLine(x1, y1, x2, y2)# calling draw_wall which in turn calls the midpoint line


def draw_maze():
    glColor3f(0.5, 1, 1)
    draw_wall(60, 60, 60, 660)  # Left wall
    draw_wall(80, 60, 640, 60)  # Down wall
    draw_wall(640, 120, 640, 660)  # Right wall
    draw_wall(60, 660, 640, 660)  # Up wall

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
    glPointSize(35)
    DrawLine(642, 92, 642, 95)


# ------------------------------------ MESSAGE DRAWING FUNCTIONS with midpoint line--------------------------------------------------------------------------------

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


# -------------------------------OUTPUT REPRESENTS THE WIN/LOSE MESSAGE------------------------------------------

def output(value, x): #value=winner or youlost
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


# ---------------------this is used to generate the win/lose message by drawing lines-----------------
def winner_lose_message(result): #called from showscreen
    #    result_1 = "YOU WIN"
    #    result_2 = "YOU LOST"
    list(result)
    distance = 0
    glPointSize(5)
    for i in result:
        output(i, distance) #calls output to show the characters
        distance += 60


# -------------------------------------BALL---------------------------------------------------------
# ------------------initial variables for the ball----------------------------------------

x = 90
y = 630
radius = 12


# -------------------------------ball with midpoint circle-----------------------------------------------------
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


# --------------------loop to color the ball by reducing radius everytime-------------------------------------------------------------
def draw_ball(x, y, r):
    for i in range(r):
        midpoint_circle(x, y, i)
    return midpoint_circle(x, y, r)


# ----------------ball detects pixel color--------------------------------------------

def read_pixel_color(x, y):
    glReadBuffer(GL_FRONT)  # Set the buffer to be read (front buffer in this case)
    pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)  # Read the pixel color
    return pixel


# --------------------------------translation--------------------------------------------
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


# -----------------------------scaling--------------------------------------------
def scale(r):
    sc = 2
    s = np.array([[sc, 0],
                  [0, 1]])

    v = np.array([[r],
                  [1]])

    scaled_r = np.matmul(s, v)
    return scaled_r[0][0]


# --------------------it is used to detect keyboard presses------------------------------------------------
def handle_key_events():
    try:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            handle_key_press(event.name)
    except:
        pass


# -------------function to translate based on keyboard presses and not move by detecting pixel color------------------------------------------------------
point = 0
def handle_key_press(key):
    global x, y, radius, point #circle's x,y,and radius
    if key == "right" or key == "left" or key == "up" or key == "down":
        temp_x, temp_y = x, y
        x_new, y_new = move(x, y, key)
        pixel = read_pixel_color(int(x_new), int(y_new))  # Ensure integer values for pixel coordinates
        if pixel == b'\x80\xff\xff': #wall's color
            x, y = temp_x, temp_y  # Restore the previous position
        elif pixel == b'\x00\x00\x00': #blank space
            x, y = x_new, y_new

        elif pixel == b'\xff\xff\xff': #white finish line
            x, y = 690, 90
            radius = scale(radius) #scaling is done here
            point = 10  # point is updated to 10 upon reaching the finish line


# ----this is used to refresh screen every 16ms to show the animation which is the movement of the ball here------------
# --------glutTimerFunc(milliseconds, callback_function, value):--------------------------
def refresh_window(value):
    glutPostRedisplay()
    glutTimerFunc(5, refresh_window, 0)


# -----------------this is used to show window with the maze and the ball----------------------
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_maze()
    # Draw the ball
    draw_ball(x, y, radius)

    glutSwapBuffers()


# ------------------it is used to show the window with losing message--------------------------------
def showScreen2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0)
    result_2 = "YOU LOST"
    winner_lose_message(result_2)
    glutSwapBuffers()


# ------------------it is used to show the window with winning message--------------------------------
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


# initial instructions for the user---------------------------

print("INSTRUCTIONS")
print(".")
print(".")
print("You have 20 seconds to reach the finish line")
print("")
print("Press any key to start")

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(735, 735)
glutInitWindowPosition(400, 10)
wind = glutCreateWindow(b"Maze")
glutDisplayFunc(showScreen)
glutTimerFunc(0, refresh_window, 0)  # Start the refresh timer to refresh the window
start_time = time.time()  # recording the starting time
end_time = start_time + 20  # calculate the ending time by adding 10s

# ----------------------start the timer------------------------------------------
while True:
    current_time = time.time()
    if point == 10 and current_time < end_time:  # true if ball has reached the finish line before the timer ends
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
    else:  # this means that the game is still ongoing and the player has time left to play.
        handle_key_events()  # This function is called to handle keyboard events. It allows the player to control the ball's movement.
        glutMainLoopEvent()  # This function is called to process any pending events in the GLUT event queue.
    # This is necessary to keep the game loop responsive to user input.