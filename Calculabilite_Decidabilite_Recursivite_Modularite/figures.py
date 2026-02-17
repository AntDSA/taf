from turtle import *
from math import *
speed(2)
def rectangle(L, l, c):
    color(c) 
    forward(L)
    left(90)
    forward(l)
    left(90)
    forward(L)
    left(90)
    forward(l)
    penup()
    
    Pr = (L+l)*2
    Ar = L*l
    forward(30)
    pendown()
    write(f"Périmétre :{Pr:.2f}\n Air :{Ar:.2f}", False, "left")

def triangle (t, c): 
    h = t*sqrt(3)/2
    Pt = t*3
    At = (t*h)/2
    color(c)
    forward(t)
    
    penup()
    forward(30)
    pendown()
    write(f"Périmétre :{Pt:.2f}\n Air :{At:.2f}", False, "left")
    penup()
    goto(-80, -105)
    
    pendown()
    left(120)
    forward(t)
    left(120)
    forward(t)
    
def cercle(r, c):
    Pc = 2*pi*r
    Ac = pi*r*r 
    color(c)     
    circle(r)
    penup()
    
    goto(5, 70)
    pendown()
    write(f"Périmétre :{Pc:.2f}\n Air :{Ac:.2f}", False, "left")