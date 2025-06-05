import turtle

# Imposta la tartaruga
t = turtle.Turtle()
t.pensize(5)
t.speed(1)

# Funzione per disegnare la lettera E
def draw_E():
    t.pendown()
    t.forward(40)     # linea orizzontale superiore
    t.backward(40)
    t.right(90)
    t.forward(60)     # linea verticale
    t.left(90)
    t.forward(40)     # linea orizzontale inferiore
    t.penup()
    t.backward(40)
    t.right(90)
    t.backward(30)
    t.left(90)
    t.pendown()
    t.forward(30)     # linea orizzontale centrale
    t.penup()

# Funzione per disegnare un punto (.)
def draw_dot():
    t.forward(10)
    t.dot(10)
    t.forward(20)

# Funzione per disegnare la lettera F
def draw_F():
    t.pendown()
    t.left(90)
    t.forward(60)     # linea verticale
    t.right(90)
    t.forward(40)     # linea orizzontale superiore
    t.penup()
    t.backward(40)
    t.right(90)
    t.backward(30)
    t.left(90)
    t.pendown()
    t.forward(30)     # linea orizzontale centrale
    t.penup()

# Posizionamento iniziale
t.penup()
t.goto(-100, 0)
t.setheading(0)

# Disegna E, punto, F, punto
draw_E()
draw_dot()
draw_F()
draw_dot()

# Termina
t.hideturtle()
turtle.done()
