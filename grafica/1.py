from turtle import Turtle
from random import random

t = Turtle()
t.speed(0)

scale = 1
steps = 1000
l = 100
t.teleport(-scale/2*100, scale/2*100)
for i in range(steps):
    t.fd((l - i*(l/steps))*scale)
    t.right(50)
    t.color((i / steps, 10/255, 5/255))


t.screen.mainloop()
