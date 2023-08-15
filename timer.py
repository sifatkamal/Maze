from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np
import time

def draw_lines(x1, y1, x2, y2):
    glLineWidth(10)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()



def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def rotate(angle):
    a = math.cos(math.radians(angle))
    b = math.sin(math.radians(angle))

    r = np.array([[a, -b, 0],
                  [b, a, 0],
                  [0, 0, 1]])

    v1 = np.array([[0],  # Length of the line
                   [100],    # Initial Y-coordinate (since it's a horizontal line)
                   [1]])

    # Apply rotation transformation
    v11 = np.matmul(r, v1)

    glColor3f(1, 0, 0)
    draw_lines(900, 600, v11[0][0] + 900, v11[1][0] + 600)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    angle = 0
    t = 20





    while t>=0:
        glutSwapBuffers()
        time.sleep(1)
        if t % 5 == 0:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            iterate()
            rotate(-1*angle)
            print(angle,t)
            glutSwapBuffers()
        t -= 1
        angle += 90






glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()