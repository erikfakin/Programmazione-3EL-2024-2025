# Esercizio 1 - quadrato di lato 400 centrato sullo schermo

from turtle import Turtle

t = Turtle()
t.speed=0

def disegna_quadrato(lato):
    t.teleport(-lato//2, -lato//2)

    for i in range(4):  
        t.fd(lato)
        t.lt(90)


for j in range(1,100):
    lato = j * 5
    disegna_quadrato(lato)











t.screen.mainloop()
