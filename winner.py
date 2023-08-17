from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()



def findZone (x1,y1,x2,y2):
    zone=None
    dx=x2-x1
    dy=y2-y1

    if abs(dx)>abs(dy):
        if abs(dx)>0 & abs(dy>=0):
            zone=0
        elif abs(dx)<0 & abs(dy>=0):
            zone=3
        elif abs(dx)>0 & abs(dy<=0):
            zone=7
        elif abs(dx)<0 & abs(dy<=0):
            zone=4
    else:
        if abs(dx)>=0 & abs(dy>0):
            zone=1
        elif abs(dx)<=0 & abs(dy>0):
            zone=2
        elif abs(dx)>=0 & abs(dy<0):
            zone=6
        elif abs(dx)<=0 & abs(dy<0):
            zone=5

    return zone

def OriginalZone(X,Y,zone):
    x=X
    y=Y
    if zone==1:
        x=Y
        y=X
    elif zone==2:
        x=-Y
        y=X
    elif zone==3:
        x=-X
        y=Y
    elif zone==4:
        x=-X
        y=-Y
    elif zone==5:
        x=-Y
        y=-X
    elif zone==6:
        x=Y
        y=-X
    elif zone==7:
        x=X
        y=-Y

    return (x,y)

def ConvertToZone0(X,Y,zone):
    x=X
    y=Y
    if zone==1:
        x=Y
        y=X
    elif zone==2:
        x=Y
        y=-X
    elif zone==3:
        x=-X
        y=Y
    elif zone==4:
        x=-X
        y=-Y
    elif zone==5:
        x=-Y
        y=-X
    elif zone==6:
        x=Y
        y=-X
    elif zone==7:
        x=X
        y=-Y

    return (x,y)


def draw_lines (x0,y0,x1,y1):
    zone=findZone(x0,y0,x1,y1)
    x0,y0=ConvertToZone0(x0,y0,zone)
    x1,y1=ConvertToZone0(x1,y1,zone)
    dx=x1-x0
    dy=y1-y0
    d=2*dy - dx
    E=2*dy
    NE=2*(dy-dx)
    x=x0
    y=y0
    X,Y=OriginalZone(x,y,zone)
    draw_points (X,Y)
    while(x<x1):
        if d<=0:
            d=d+E
            x=x+1

        else:
            d=d+NE
            x=x+1
            y=y+1

        X,Y=OriginalZone(x,y,zone)
        draw_points(X,Y)

def winner(d):
    
    y=200
    x=190


    # # above
    # draw_lines(x, y+100, x+50, y+100)

    # # left
    # draw_lines(x, y, x, y+100)
    
    # # right
    # draw_lines(x+50, y, x+50, y+100)

    # # below
    # draw_lines(x, y, x+50, y)

    



    # O

    # draw_lines(x, y, x+50, y)
    # draw_lines(x, y, x, y+100)
    # draw_lines(x+50, y, x+50, y+100)
    # draw_lines(x, y+100, x+50, y+100)

    # I

    # draw_lines(x+50, y, x+50, y+100)

    # U

    # draw_lines(x, y, x+50, y)
    # draw_lines(x, y, x, y+100)
    # draw_lines(x+50, y, x+50, y+100)



    # N

    

    draw_lines(x, y, x, y+100)

    
    draw_lines(x+50, y, x+50, y+100)







def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears the color and depth buffers using glClear
    glLoadIdentity() # loads the identity matrix with glLoadIdentity
    iterate() # sets up the viewport and matrices using iterate
    glColor3f(1.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here
    

    string = 'WINNER'
    
    winner(string)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Student ID : ") #window name
glutDisplayFunc(showScreen)

glutMainLoop()