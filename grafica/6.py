import turtle
import math

# Imposta la tartaruga
t = turtle.Turtle()
t.pensize(5)
t.speed(10)


altezza = 75
larghezza = 50

def disegna_e(x, y):
    t.teleport(x, y)
    t.setheading(0)
    t.forward(larghezza)
    t.teleport(x, y)
    t.setheading(90)
    t.forward(altezza)
    t.teleport(x, y + altezza // 2)
    t.setheading(0)
    t.forward(larghezza)
    t.teleport(x, y + altezza)
    t.forward(larghezza)

def disegna_r(x, y):
    t.teleport(x, y)
    t.setheading(90)
    t.forward(altezza)
    t.setheading(0)
    t.forward(altezza//3)
    t.setheading(180)
    t.circle(larghezza//2.5, -180)
    t.setheading(180)
    t.forward(altezza//3)
    t.penup()
    t.setheading(0)
    t.forward(altezza//3)
    t.pendown()
    t.setheading(-60)
    t.forward(altezza//1.95)

def disegna_i(x, y):
    t.teleport(x,y)
    t.setheading(90)
    t.forward(altezza)

def disegna_k(x, y):
    t.teleport(x, y)
    t.setheading(90)
    t.forward(altezza)
    t.teleport(x, y + altezza//2)
    t.setheading(-45)
    t.forward(math.sqrt((altezza // 2)**2 + larghezza**2) - 10)
    t.teleport(x, y + altezza//2)
    t.setheading(45)
    t.forward(math.sqrt((altezza // 2)**2 + larghezza**2) - 10)
    


disegna_e(0, 0)
disegna_r(75, 0)
disegna_i(145, 0)
disegna_k(170, 0)




