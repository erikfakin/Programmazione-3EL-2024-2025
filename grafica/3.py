from turtle import Turtle
import math

t = Turtle()
t.speed=0
n_cicli=5
for i in range(360):
    t.fd(2)
    t.right(1)
    t.color((math.sin((i/360)*2*math.pi*n_cicli) + 1)/2, 0, 0)


t.screen.mainloop()
