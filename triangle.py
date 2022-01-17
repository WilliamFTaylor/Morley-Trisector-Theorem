import random
import math
import cmath
from graphics import *

rando = [2*math.pi*random.random(), 2*math.pi*random.random(), 2*math.pi*random.random()]

# sort the list
rando.sort()
z1 = cmath.rect(1, rando[0])
z2 = cmath.rect(1, rando[1])
z3 = cmath.rect(1, rando[2])

z31 = z3 - z1
z21 = z2 - z1
z32 = z3 - z2
z12 = z1 - z2
z13 = z1 - z3
z23 = z2 - z3

trisect1 = cmath.rect(1, (rando[2] - rando[1])/6)
trisect2 = cmath.rect(1, (2*math.pi + rando[0] - rando[2])/6)
trisect3 = cmath.rect(1, (rando[1] - rando[0])/6)

#first interior triangle

twist21 = z21*trisect1
twist12 = z12/trisect2

a3 = (-twist12.imag*z21.real + twist12.real*z21.imag)/(-twist21.real*twist12.imag + twist12.real*twist21.imag)
interior3 = z1 + a3*twist21

#second interior triangle
twist32 = z32*trisect2 
twist23 = z23/trisect3

a1 = (-twist23.imag*z32.real + twist23.real*z32.imag)/(-twist32.real*twist23.imag + twist23.real*twist32.imag)
interior1 = z2 + a1*twist32

#third interior triangle
twist13 = z13*trisect3 
twist31 = z31/trisect1

a2 = (-twist31.imag*z13.real + twist31.real*z13.imag)/(-twist13.real*twist31.imag + twist31.real*twist13.imag)
interior2 = z3 + a2*twist13 

def main():

    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

    circen = Point(250, 250)
    circrad = 200
    cir = Circle(circen, circrad)
    cir.setOutline("blue")
    cir.draw(win)
    
    p1x  = 250 + 200*z1.real
    p1y = 250 + 200*z1.imag
    p1 = Point(p1x, p1y)

    p2x = 250 + 200*z2.real
    p2y = 250 + 200*z2.imag
    p2 = Point(p2x, p2y)

    p3x = 250 + 200*z3.real
    p3y = 250 + 200*z3.imag
    p3 = Point(p3x, p3y)

    pp3 = Point(250 + 200*interior3.real, 250 + 200*interior3.imag)
    pp1 = Point(250 + 200*interior1.real, 250 + 200*interior1.imag)
    pp2 = Point(250 + 200*interior2.real, 250 + 200*interior2.imag)

    ln1 = Line(p2, p3)
    ln2 = Line(p1, p3)
    ln3 = Line(p1, p2)




    ln1.setOutline(color_rgb(0, 255, 255))
    ln1.draw(win) 


    ln2.setOutline(color_rgb(0, 255, 255))
    ln2.draw(win)

    ln3.setOutline(color_rgb(0, 255, 255))
    ln3.draw(win)



    ln3a = Line(p1, pp3)
    ln3b = Line(p2, pp3)

    ln3a.setOutline(color_rgb(0, 155, 55))
    ln3a.draw(win)

    ln3b.setOutline(color_rgb(0, 155, 55))
    ln3b.draw(win)
#draw second triangle
    
    ln1a = Line(p2, pp1)
    ln1b = Line(p3, pp1)

    ln1a.setOutline(color_rgb(0, 155, 55))
    ln1a.draw(win)

    ln1b.setOutline(color_rgb(0, 155, 55))
    ln1b.draw(win)

#draw third triangle
    
    ln2a = Line(p3, pp2)
    ln2b = Line(p1, pp2)

    ln2a.setOutline(color_rgb(0, 155, 55))
    ln2a.draw(win)

    ln2b.setOutline(color_rgb(0, 155, 55))
    ln2b.draw(win)

#draw morley triangle
    mln1 = Line(pp3, pp2)
    mln2 = Line(pp1, pp3)
    mln3 = Line(pp2, pp1)

    mln1.setOutline(color_rgb(55, 55, 55))
    mln1.draw(win)
    mln2.setOutline(color_rgb(55, 55, 55))
    mln2.draw(win)
    mln3.setOutline(color_rgb(55, 55, 55))
    mln3.draw(win)

    

    win.getMouse()
    win.close()

main()
