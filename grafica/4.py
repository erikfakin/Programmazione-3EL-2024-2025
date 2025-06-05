from turtle import Turtle
import random

grande = 300
piccolo = 1
quanti = 300

t = Turtle()
t.speed(0)

for i in range(grande, piccolo, -(grande - piccolo) // quanti):
    t.color(random.random(), random.random(), random.random())
    t.teleport(0, -i//2)
    t.begin_fill()
    t.circle(i//2)
    t.end_fill()

t.screen.mainloop()
