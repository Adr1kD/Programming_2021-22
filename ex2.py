# Figure II: 
from turtle import *
from random import *
from math import *
 
def tree(n, l):
         Pd() #  
         #shadow effect
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
         Forward(l) # draw branches
 
 
    if n > 0:
                 b = random() * 15 + 10 # right branch deflection angle
                 c = random() * 15 + 10 # left branch deflection angle
                 d = l * (random() * 0.25 + 0.7) # the length of the next branch
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
        pencolor(n, n*0.8, n*0.8)
        circle(3)
        left(90)
 
                 # Add 0.3 times the falling leaves
        if(random() > 0.7):
            pu()
                         # 
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
 
 
                         # 
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
            circle(2)
            left(90)
            pu()
 
                         # 
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
 
    pu()
         Backward(l)# returned
 
 Bgcolor(0.5, 0.5, 0.5) # Background color
 Ht() # hide turtle
 Speed(0) # speed, 1-10 progressive, 0 fastest
tracer(0, 0)
 Pu() # Raise the pen
backward(100)
 Left(90) # Left turn 90 degrees
 Pu() # Raise the pen
 Backward(300) # back 300
 Tree(12, 100) # recursive 7th floor
done()
