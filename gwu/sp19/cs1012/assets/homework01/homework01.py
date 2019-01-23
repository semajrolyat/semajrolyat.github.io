from turtle import *
from math import sqrt

setup(400,400,200,200)
screensize(400,400)

w=200.0
h=100.0
dw=40.0
dh=2.0*dw
ww=25.0
wh=40.0
wy=40.0
wx=25.0
penup()
forward(w/2)
left(90)
forward(h/2)
pendown()
left(90)
forward(w)
left(90)
forward(h)
left(90)
forward(w)
left(90)
forward(h)

left(45)
forward(sqrt(float(w*w/2.0)))
left(90)
forward(sqrt(float(w*w/2.0)))

left(45)
forward(h)
left(90)
forward((w+dw)/2.0)
left(90)
forward(dh)
left(90)
forward(dw)
left(90)
forward(dh)

left(90)
backward((w-dw)/2.0)
forward(wx)
left(90)
penup()
forward(wy)
pendown()
forward(wh)
right(90)
forward(ww)
right(90)
forward(wh)
right(90)
forward(ww)
left(90)
penup()
forward(wy)
left(90)
backward(wx)
forward(w)
backward(wx)
left(90)
forward(wy)
pendown()
forward(wh)
left(90)
forward(ww)
left(90)
forward(wh)
left(90)
forward(ww)
done()
