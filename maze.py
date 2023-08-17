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


def draw_background(x1, y1, x2, y2, x3, y3, x4, y4):
    glColor3f(0, 0, 0.2)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()


def draw_wall(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()


def draw_maze():
    draw_background(1, 759, 759, 759, 759, 1, 1, 1)
    glColor3f(0.5, 1, 1)
    draw_wall(60, 680, 80, 680, 80, 60, 60, 60)
    draw_wall(80, 80, 660, 80, 660, 60, 80, 60)
    draw_wall(120, 680, 660, 680, 660, 660, 120, 660)
    draw_wall(640, 120, 640, 660, 660, 660, 660, 120)
    draw_wall(140, 600, 120, 600, 120, 660, 140, 660)
    draw_wall(180, 620, 300, 620, 300, 600, 180, 600)
    draw_wall(340, 560, 340, 620, 360, 620, 360, 560)
    draw_wall(400, 600, 400, 620, 640, 620, 640, 600)
    draw_wall(200, 540, 180, 540, 180, 600, 200, 600)
    draw_wall(120, 540, 120, 560, 180, 560, 180, 540)
    draw_wall(120, 540, 140, 540, 140, 480, 120, 480)
    draw_wall(140, 480, 140, 500, 480, 500, 480, 480)
    draw_wall(480, 480, 480, 280, 460, 280, 460, 480)
    draw_wall(240, 500, 240, 540, 260, 540, 260, 500)
    draw_wall(240, 540, 240, 560, 540, 560, 540, 540)
    draw_wall(540, 540, 540, 320, 520, 320, 520, 540)
    draw_wall(580, 560, 600, 560, 600, 440, 580, 440)
    draw_wall(540, 460, 580, 460, 580, 440, 540, 440)
    draw_wall(180, 260, 180, 480, 200, 480, 200, 260)
    draw_wall(120, 360, 120, 440, 140, 440, 140, 360)
    draw_wall(240, 420, 240, 440, 420, 440, 420, 420)
    draw_wall(240, 420, 260, 420, 260, 300, 240, 300)
    draw_wall(400, 200, 400, 420, 420, 420, 420, 200)
    draw_wall(300, 360, 300, 380, 360, 380, 360, 360)
    draw_wall(340, 160, 340, 360, 360, 360, 360, 160)
    draw_wall(300, 300, 300, 320, 340, 320, 340, 300)
    draw_wall(580, 280, 580, 400, 600, 400, 600, 280)
    draw_wall(80, 300, 80, 320, 140, 320, 140, 300)
    draw_wall(120, 240, 120, 260, 300, 260, 300, 240)
    draw_wall(420, 260, 420, 280, 640, 280, 640, 260)
    draw_wall(80, 180, 80, 200, 180, 200, 180, 180)
    draw_wall(220, 180, 220, 200, 300, 200, 300, 180)
    draw_wall(280, 120, 280, 180, 300, 180, 300, 120)
    draw_wall(120, 120, 120, 140, 280, 140, 280, 120)
    draw_wall(340, 80, 340, 100, 480, 100, 480, 80)
    draw_wall(300, 140, 300, 160, 460, 160, 460, 140)
    draw_wall(460, 140, 460, 220, 480, 220, 480, 140)
    draw_wall(480, 200, 480, 220, 600, 220, 600, 200)
    draw_wall(520, 80, 520, 160, 540, 160, 540, 80)
    draw_wall(580, 80, 580, 160, 600, 160, 600, 80)

    # finish line
    glColor3f(1, 1, 1)  ### note to Anika.. ekhane checkered finish line banay dio please
    draw_wall(640, 80, 640, 120, 680, 120, 680, 80)


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
point=0

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
            point=10

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


def showScreen2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # Draw the ball
    draw_ball(300, 300, 100)

    glutSwapBuffers()

def showScreen3():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # Draw the ball
    draw_ball(200, 200, 50)

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
end_time = start_time + 20
print("end",end_time)
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






