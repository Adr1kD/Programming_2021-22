# :
from turtle import *
from random import *
from math import *
 
def tree(n, l):
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
 
 
    if n > 0:
        b = random() * 15 + 10 # right branch deflection angle
        c = random() * 15 + 10 # left branch deflection angle
        d = l * (random() * 0.35 + 0.6) # The length of the next branch
                 # Right turn a certain angle, draw the right branch
        right(b)
        tree(n - 1, d)
                 # Left turn a certain angle, draw the left branch
        left(b + c)
        tree(n - 1, d)
 
                 # 
        right(c)
    else:
                 # 
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
 
 
    pu()
 
    Bgcolor(0.5, 0.5, 0.5) # Background color
    Ht() # hide turtle
    Speed(0) # speed, 1-10 progressive, 0 fastest
    tracer(0, 0)
    Left(90) # Left turn 90 degrees
    Pu() # Raise the pen
    Backward(300) # back 300
    Tree(13, 100) # recursive 7th floor
done()
